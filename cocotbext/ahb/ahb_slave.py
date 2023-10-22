#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 16.10.2023
# Last Modified Date: 22.10.2023

import cocotb
import logging
import copy
import random

from .ahb_types import AHBTrans, AHBWrite, AHBSize, AHBResp
from .ahb_bus import AHBBus
from .version import __version__

from cocotb.triggers import RisingEdge
from typing import Optional, Sequence, Union
from cocotb.types import LogicArray
from cocotb.binary import BinaryValue


class AHBLiteSlave:
    def __init__(self, bus: AHBBus, clock: str, reset: str,
                 def_val: Union[int, str] = 'Z',
                 name: str = 'ahb_lite', **kwargs):
        self.bus = bus
        self.clk = clock
        self.rst = reset
        self.def_val = def_val
        self.log = logging.getLogger(f"cocotb.{name}.{bus._name}."
                                     f"{bus._entity._name}")
        self._init_bus()
        self.log.info(f"AHB ({name}) slave")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info("Copyright (c) 2023 Anderson Ignacio da Silva")
        self.log.info("https://github.com/aignacio/cocotbext-ahb")
        cocotb.start_soon(self._proc_txn())

    def _init_bus(self) -> None:
        """Initialize the bus with default value."""
        for signal in self.bus._signals:
            if signal in ["hready", "hresp", "hrdata"]:
                sig = getattr(self.bus, signal)
                try:
                    default_value = self._get_def(len(sig))
                    sig.setimmediatevalue(default_value)
                except AttributeError:
                    pass

    def _get_def(self, width: int = 1) -> BinaryValue:
        """Return a handle obj with the default value"""
        return LogicArray([self.def_val for _ in range(width)])

    def _rnd_val(self, bit: int = 0, zero: Optional[bool] = True) -> int:
        if zero is True:
            return random.randint(0, (2**bit) - 1)
        else:
            return random.randint(1, (2**bit) - 1)

    async def _proc_txn(self):
        """Process any incoming txns"""
        while True:
            # Wait for a txn
            await RisingEdge(self.clk)
            # Default values in case there is no txn
            self.bus.hready.value = self._get_def(1)
            self.bus.hrdata.value = self._get_def(len(self.bus.hrdata))
            self.bus.hresp.value = AHBResp.OKAY

            if self._check_inputs():
                if self._check_valid_txn():
                    self.bus.hready.value = 1
                    self.bus.hrdata.value = self._rnd_val(self.bus.data_width)
                    self.bus.hresp.value = AHBResp.OKAY
                else:
                    self.bus.hready.value = 1
                    self.bus.hrdata.value = self._rnd_val(self.bus.data_width)
                    self.bus.hresp.value = AHBResp.OKAY

    def _check_inputs(self) -> bool:
        """Check any of the master signals are resolvable (i.e not 'z')"""
        signals = {'htrans': self.bus.htrans}

        for var, val in signals.items():
            if val.value.is_resolvable is False:
                self.log.warn(f"{var} is not resolvable")
                return False
        return True

    def _check_valid_txn(self) -> bool:
        htrans_st = ((AHBTrans(self.bus.htrans.value) != AHBTrans.IDLE) and
                     (AHBTrans(self.bus.htrans.value) != AHBTrans.BUSY))

        if self.bus.hsel_exist:
            if self.bus.hready_in_exist:
                if ((self.bus.hsel.value == 1) and
                   (self.bus.hready_in.value == 1) and htrans_st):
                    return True
                else:
                    return False
            else:
                if (self.bus.hsel.value == 1) and htrans_st:
                    return True
                else:
                    return False
        else:
            if htrans_st:
                return True
            else:
                return False


class AHBSlave(AHBLiteSlave):
    def __init__(self, bus: AHBBus, clock: str, reset: str,
                 timeout: int = 100, def_val: Union[int, str] = 'Z', **kwargs):
        super().__init__(bus, clock, reset, timeout,
                         def_val, 'ahb_full', **kwargs)
