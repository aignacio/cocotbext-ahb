#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 08.10.2023

import cocotb
import logging

from .ahb_types import AHBTrans, AHBWrite, AHBSize
from .ahb_bus import AHBBus
from .version import __version__

from cocotb.triggers import RisingEdge
from typing import Optional, Sequence, Union
from cocotb.types import LogicArray
from cocotb.binary import BinaryValue


class AHBLiteMaster:
    def __init__(self, bus: AHBBus, clock: str, reset: str,
                 timeout: int = 100, def_val: Union[int, str] = 'Z', **kwargs):
        self.bus = bus
        self.clk = clock
        self.rst = reset
        self.def_val = def_val
        self.log = logging.getLogger(f"cocotb.{bus._name}.{bus._entity._name}")
        self._init_bus()
        self.log.info("AHB lite master")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info("Copyright (c) 2023 Anderson Ignacio da Silva")
        self.log.info("https://github.com/aignacio/cocotbext-ahb")

    def _init_bus(self) -> None:
        """Initialize the bus with default value."""
        for signal in self.bus._signals:
            if signal not in ["hready", "hresp", "hrdata"]:
                sig = getattr(self.bus, signal)
                try:
                    default_value = self._get_def(len(sig), self.def_val)
                    sig.setimmediatevalue(default_value)
                except AttributeError:
                    pass

    def _get_def(self, width: int = 1,
                 val: Union[int, str] = 'Z') -> BinaryValue:
        """Return a handle obj with the default value"""
        return LogicArray([val for _ in range(width)])

    def _convert_size(self, value) -> AHBTrans:
        """Convert byte size into hsize."""
        for hsize in AHBSize:
            if (2**hsize.value) == value:
                return hsize
        raise ValueError(f"No hsize value found for {value} number of bytes")

    @staticmethod
    def _check_size(size: int, data_bus_width: int) -> None:
        """Check that the provided transfer size is valid."""
        if size > data_bus_width:
            raise ValueError("Size of the transfer ({} B)"
                             " provided is larger than the bus width "
                             "({} B)".format(size, data_bus_width))
        elif size <= 0 or (size & (size - 1)) != 0:
            raise ValueError("Size must be a positive power of 2")

    @cocotb.coroutine
    async def write(self, address: int, value: Union[int, Sequence[int]],
                    size: Optional[int] = None) -> None:
        """Write data in the AHB bus."""
        if size is None:
            size = self.bus._data_width//8
        else:
            AHBLiteMaster._check_size(size, len(self.bus.hwdata) // 8)

        await RisingEdge(self.clk)

        # Address phase
        self.bus.haddr.value = address
        self.bus.htrans.value = AHBTrans(0b10)
        self.bus.hsize.value = self._convert_size(size)
        self.bus.hwrite.value = AHBWrite(0b1)
        await RisingEdge(self.clk)
        # Address phase
        self._init_bus()
        # while self.bus.hready.value == 0:
        #   await RisingEdge(self.clock)

        # Data phase
        self.bus.hwdata.value = value
        await RisingEdge(self.clk)
        self._init_bus()
