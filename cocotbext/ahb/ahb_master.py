#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 01.10.2023
# Last Modified Date: 07.10.2023
import cocotb

from .ahb_types import AHBTrans, AHBWrite
from .ahb_bus import AHBBus

from cocotb_bus.drivers import Bus
from cocotb.handle import SimHandleBase
from cocotb.triggers import RisingEdge
from typing import Any, List, Optional, Sequence, Tuple, Union
from cocotb.log import SimLog

class AHBLiteMaster:
    def __init__(self, bus: AHBBus, clock: str, reset: str, **kwargs): 
        self.bus = bus
        for signal in bus._signals:
            if signal not in ["hready", "hresp", "hrdata"]:
                try:
                    default_value = 0
                    getattr(self.bus, signal).setimmediatevalue(default_value)
                except AttributeError:
                    pass
    
    def _convert_size(self, value):
        for hsize in AHBSize:
            if (2**hsize.value) == value:
                return hsize
        raise ValueError(f"No hsize value found for {input_int} number of bytes")

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
        if size is None:
            size = len(self.bus.hwdata) // 8
        else:
            AHBLiteMaster._check_size(size, len(self.bus.hwdata) // 8)
        
        await RisingEdge(self.clock)
        
        # Address phase
        self.bus.haddr.value  = address
        self.bus.htrans.value = AHBTrans(0b10)
        self.bus.hsize.value  = self._convert_size(size) 
        self.bus.hwrite.value = AHBWrite(0b1) 
        await RisingEdge(self.clock)

        # while self.bus.hready.value == 0:
            # await RisingEdge(self.clock)

        # Data phase
        self.bus.hwdata.value = value
        await RisingEdge(self.clock)
