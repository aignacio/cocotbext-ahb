#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : amba_ahb.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 01.10.2023
# Last Modified Date: 02.10.2023
import cocotb
import enum

from cocotb_bus.drivers import BusDriver
from cocotb.handle import SimHandleBase
from typing import Iterable, Tuple, Any, Optional, Callable

class AHBBurst(enum.IntEnum):
    SINGLE  = 0b000
    INCR    = 0b001
    WRAP4   = 0b010
    INCR4   = 0b011
    WRAP8   = 0b100
    INCR8   = 0b101
    WRAP16  = 0b110
    INCR16  = 0b111

class AHBResp(enum.IntEnum):
    OKAY    = 0b0
    ERROR   = 0b1

class AHBTrans(enum.IntEnum):
    IDLE    = 0b00
    BUSY    = 0b01
    NONSEQ  = 0b10
    SEQ     = 0b11

class AHBWrite(enum.IntEnum):
    WRITE   = 0b0
    READ    = 0b1

class AHBMaster(BusDriver):
    _signals = ["haddr", "hburst", "hsize", "htrans", "hwdata",
                "hrdata", "hwrite", "hready", "hresp"]

    _optionl_signals = ["hmastlock", "hprot", "hnonsec", "hexcl",
                        "hmaster", "hexokay", "hsel"]

    def __init__(self, entity: SimHandleBase, name: str, clock: SimHandleBase,
                 **kwargs: Any):
        BusDriver.__init__(self, entity, name, clock, **kwargs)
            
        # Drive some sensible defaults (setimmediatevalue to avoid x asserts)
        self.bus.haddr.setimmediatevalue(0)
        self.bus.hburst.setimmediatevalue(0)
        self.bus.hsize.setimmediatevalue(0)
        self.bus.htrans.setimmediatevalue(0)
        self.bus.hwdata.setimmediatevalue(0)
        self.bus.hwrite.setimmediatevalue(0)
        # self.hrdata.setimmediatevalue(0)
        # self.hready.setimmediatevalue(0)
        # self.hresp.setimmediatevalue(0)

