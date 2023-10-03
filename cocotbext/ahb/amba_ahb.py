#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : amba_ahb.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 01.10.2023
# Last Modified Date: 03.10.2023
import cocotb
import enum
import collections.abc

#from cocotb_bus.drivers import BusDriver
# from cocotb_bus.bus import Bus
from cocotb_bus.drivers import BusDriver
from cocotb.handle import SimHandleBase
from cocotb.triggers import RisingEdge
from typing import Any, List, Optional, Sequence, Tuple, Union

class AHBSize(enum.IntEnum):
    BYTE    = 0b000
    HWORD   = 0b001
    WORD    = 0b010
    DWORD   = 0b011
    FWORD   = 0b100
    EWORD   = 0b101

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

class AHBLiteMaster(BusDriver):
    _signals = ["haddr", "hsize", "htrans", "hwdata",
                "hrdata", "hwrite", "hready", "hresp"]

    _optional_signals = ["hburst","hmastlock", "hprot", "hnonsec",
                         "hexcl", "hmaster", "hexokay", "hsel"]

    def __init__(self, entity, name, clock, **kwargs):
        BusDriver.__init__(self, entity, name, clock)
        self.clock = clock
        for signal in self._signals + self._optional_signals:
            if signal not in ["hready", "hresp", "hrdata"]:
                try:
                    default_value = 1
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
