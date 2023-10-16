#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 16.10.2023
# Last Modified Date: 16.10.2023

import cocotb
import logging
import copy

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
        self.log.info(f"AHB ({name}) master")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info("Copyright (c) 2023 Anderson Ignacio da Silva")
        self.log.info("https://github.com/aignacio/cocotbext-ahb")

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
