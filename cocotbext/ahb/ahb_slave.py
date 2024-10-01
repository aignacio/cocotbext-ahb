#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 16.10.2023
# Last Modified Date: 01.10.2024

import cocotb
import logging
import random
import copy
import datetime

from .ahb_types import AHBTrans, AHBWrite, AHBSize, AHBResp
from .ahb_bus import AHBBus
from .version import __version__

from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray
from typing import Optional, Union, Generator, List
from .memory import Memory


class AHBLiteSlave:
    def __init__(
        self,
        bus: AHBBus,
        clock: str,
        reset: str,
        bp: Generator[int, None, None] = None,
        name: str = "ahb_lite",
        reset_act_low: bool = True,
        **kwargs,
    ):
        self.bus = bus
        self.clk = clock
        self.rst = reset
        self.rst_act_low = reset_act_low
        self.bp = bp
        self.log = logging.getLogger(
            f"cocotb.{name}.{bus._name}." f"{bus._entity._name}"
        )
        self._init_bus()
        self.log.info(f"AHB ({name}) slave")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info(
            f"Copyright (c) {datetime.datetime.now().year} Anderson Ignacio da Silva"
        )
        self.log.info("https://github.com/aignacio/cocotbext-ahb")

        cocotb.start_soon(self._proc_txn())

    def _init_bus(self) -> None:
        """Initialize the bus with default value."""
        self.bus.hready.setimmediatevalue(1)
        self.bus.hresp.setimmediatevalue(AHBResp.OKAY)
        self.bus.hrdata.setimmediatevalue(0)

    def _get_def(self, width: int = 1) -> LogicArray:
        """Return a handle obj with the default value"""
        return LogicArray([self.def_val for _ in range(width)])

    async def _proc_txn(self):
        """Process any incoming txns"""

        wr_start = False
        rd_start = False
        error = False
        txn_addr = 0
        txn_size = AHBSize.WORD
        txn_type = AHBWrite.READ

        self.bus.hrdata.value = 0

        while True:
            if self.rst.value.is_resolvable:
                if self.rst_act_low:
                    if self.rst.value == 0:  # Active 0
                        self.log.warn("Slave AHB reset issued")
                        self._init_bus()
                else:
                    if self.rst.value == 1:  # Active 1
                        self.log.warn("Slave AHB reset issued")
                        self._init_bus()

            # Wait for a txn
            await RisingEdge(self.clk)

            if self.bus.hready_in_exist:
                cur_hready_in = copy.deepcopy(self.bus.hready_in.value)
            else:
                cur_hready_in = 1
            cur_hready = copy.deepcopy(self.bus.hready.value)
            cur_hresp = copy.deepcopy(self.bus.hresp.value)

            # Default values in case there is no txn
            self.bus.hready.value = 1
            self.bus.hresp.value = AHBResp.OKAY

            if error and (cur_hresp == AHBResp.OKAY):  # First cycle of error response
                self.bus.hready.value = 0
                self.bus.hresp.value = AHBResp.ERROR
            elif error and (
                cur_hresp == AHBResp.ERROR
            ):  # Second cycle of error response
                self.bus.hready.value = 1
                self.bus.hresp.value = AHBResp.ERROR
                error = False
            else:
                if rd_start and cur_hready and cur_hready_in:
                    rd_start = False
                    self.bus.hrdata.value = 0

                if wr_start and cur_hready and cur_hready_in:
                    wr_start = False
                    if txn_type == AHBWrite.WRITE:
                        wr = self._wr(txn_addr, txn_size, self.bus.hwdata.value)
                        self.bus.hrdata.value = wr
                        self.bus.hresp.value = AHBResp.OKAY

            # Check for new txn
            if cur_hready and self._check_inputs() and self._check_valid_txn():
                txn_addr = self.bus.haddr.value
                txn_size = AHBSize(self.bus.hsize.value)
                txn_type = AHBWrite(self.bus.hwrite.value)
                self._check_size(2**txn_size, self.bus.data_width)

                if txn_type == AHBWrite.WRITE:
                    if not self._chk_wr(txn_addr, txn_size):
                        self.bus.hready.value = 0
                        self.bus.hrdata.value = 0
                        error = True
                        wr_start = False
                    else:
                        wr_start = True
                        self.bus.hresp.value = AHBResp.OKAY

                if txn_type == AHBWrite.READ:
                    if not self._chk_rd(txn_addr, txn_size):
                        self.bus.hready.value = 0
                        error = True
                    else:
                        rd_start = True
                        self.bus.hrdata.value = self._rd(txn_addr, txn_size)
                        self.bus.hresp.value = AHBResp.OKAY

            if error is False:
                if self.bp is not None:
                    if rd_start is True or wr_start is True:
                        ready = next(self.bp)
                    else:
                        ready = True  # slave cannot bp on address phase
                else:
                    ready = True

                if ready:
                    self.bus.hready.value = 1
                else:
                    self.bus.hready.value = 0

    @staticmethod
    def _check_size(size: int, data_bus_width: int) -> None:
        """Check that the provided transfer size is valid."""
        if size > data_bus_width:
            raise ValueError(
                "Size of the transfer ({} B)"
                " provided is larger than the bus width "
                "({} B)".format(size, data_bus_width)
            )
        elif size <= 0 or (size & (size - 1)) != 0:
            raise ValueError(f"Error -> {size} - Size must" f"be a positive power of 2")

    def _check_inputs(self) -> bool:
        """Check any of the master signals are resolvable (i.e not 'z')"""
        signals = {
            "htrans": self.bus.htrans,
            "hwrite": self.bus.hwrite,
            "haddr": self.bus.haddr,
            "hsize": self.bus.hsize,
        }

        for var, val in signals.items():
            if val.value.is_resolvable is False:
                # self.log.warn(f"{var} is not resolvable")
                return False
        return True

    def _check_valid_txn(self) -> bool:
        htrans_st = (AHBTrans(self.bus.htrans.value) != AHBTrans.IDLE) and (
            AHBTrans(self.bus.htrans.value) != AHBTrans.BUSY
        )

        if self.bus.hsel_exist:
            if self.bus.hready_in_exist:
                if (
                    (self.bus.hsel.value == 1)
                    and (self.bus.hready_in.value == 1)
                    and htrans_st
                ):
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

    def _default_generator(self) -> Generator[bool, None, None]:
        while True:
            yield True

    def _chk_rd(self, addr: int, size: AHBSize) -> bool:
        return True

    def _chk_wr(self, addr: int, size: AHBSize) -> bool:
        return True

    def _rd(self, addr: int, size: AHBSize) -> int:
        # Return some random data when read
        return 0

    def _wr(self, addr: int, size: AHBSize, value: int) -> int:
        # Return some zero data when write
        return 0


class AHBLiteSlaveRAM(AHBLiteSlave):
    def __init__(
        self,
        bus: AHBBus,
        clock: str,
        reset: str,
        bp: Generator[int, None, None] = None,
        name: str = "ahb_lite_ram",
        mem_size: int = 1024,
        **kwargs,
    ):
        super().__init__(bus, clock, reset, bp, name, **kwargs)
        self.memory = Memory(size=mem_size)

    def _chk_rd(self, addr: int, size: AHBSize) -> bool:
        if addr + (2**size) > self.memory.size:
            return False
        return True

    def _chk_wr(self, addr: int, size: AHBSize) -> bool:
        if addr + (2**size) > self.memory.size:
            return False
        return True

    def _get_addr_aligned(self, addr: int) -> int:
        if self.bus._data_width == 32:
            if self.bus._addr_width == 32:
                return addr & 0xFFFF_FFFC
            elif self.bus._addr_width == 64:
                return addr & 0xFFFF_FFFF_FFFF_FFFC
        elif self.bus._data_width == 64:
            if self.bus._addr_width == 32:
                return addr & 0xFFFF_FFF8
            elif self.bus._addr_width == 64:
                return addr & 0xFFFF_FFFF_FFFF_FFF8

    def _rd(self, addr: int, size: AHBSize) -> int:
        data = self.memory.read(addr, 2**size)
        data = int.from_bytes(data, byteorder="little")
        return data

    def _wr(self, addr: int, size: AHBSize, value: LogicArray) -> int:
        if size == AHBSize.BYTE:
            # Mask the data to a single byte
            data = value.integer & 0xFF

            # Get the byte offset
            if self.bus._data_width == 32:
                byte_sel = addr & 0x3
            elif self.bus._data_width == 64:
                byte_sel = addr & 0x7

            # Get the (d)word aligned addr
            addr_aligned = self._get_addr_aligned(addr)

            # Get the (d)word data from the memory
            if self.bus._data_width == 32:
                mem_data = self.memory.read(addr_aligned, 4)
            elif self.bus._data_width == 64:
                mem_data = self.memory.read(addr_aligned, 8)

            mem_data = int.from_bytes(mem_data, byteorder="little")

            # Zero the N-th byte
            mem_data = ~(0xFF << (byte_sel * 8)) & mem_data

            # OR with the new value
            mem_data = (data << (byte_sel * 8)) | mem_data

            # Convert into 32/64-bit int byte array
            if self.bus._data_width == 32:
                ba_data = mem_data.to_bytes(4, byteorder="little")
            elif self.bus._data_width == 64:
                ba_data = mem_data.to_bytes(8, byteorder="little")

            # Write the data back to the memory
            self.memory.write(addr_aligned, ba_data)
        elif size == AHBSize.HWORD:
            # Mask the data to a half-word
            data = value.integer & 0xFFFF

            # Get the half-word offset
            if self.bus._data_width == 32:
                hword_sel = addr & 0x3
            elif self.bus._data_width == 64:
                hword_sel = addr & 0x7

            if (hword_sel & 0x1) != 0x0:
                raise AssertionError("Half-word write addr LSB has to be 0x0")

            # Get the (d)word aligned addr
            addr_aligned = self._get_addr_aligned(addr)

            # Get the (d)word data from the memory
            if self.bus._data_width == 32:
                mem_data = self.memory.read(addr_aligned, 4)
            elif self.bus._data_width == 64:
                mem_data = self.memory.read(addr_aligned, 8)

            mem_data = int.from_bytes(mem_data, byteorder="little")

            # Zero the N-th h-word
            mem_data = ~(0xFFFF << (hword_sel * 8)) & mem_data

            # OR with the new value
            mem_data = (data << (hword_sel * 8)) | mem_data

            # Convert into 32-bit int byte array
            if self.bus._data_width == 32:
                ba_data = mem_data.to_bytes(4, byteorder="little")
            elif self.bus._data_width == 64:
                ba_data = mem_data.to_bytes(8, byteorder="little")

            # Write the data back to the memory
            self.memory.write(addr_aligned, ba_data)
        elif size == AHBSize.WORD:
            if self.bus._data_width == 32:
                lsbs = addr & 0x3
                if lsbs != 0x0:
                    raise AssertionError("Word write addr LSB needs to be 0x0")
                ba_data = value.integer.to_bytes(4, byteorder="little")
                self.memory.write(addr, ba_data)

            elif self.bus._data_width == 64:
                # Mask the data to a half-word
                data = value.integer & 0xFFFF_FFFF

                # Get the word offset
                word_sel = addr & 0x7

                if (word_sel & 0x3) != 0x0:
                    raise AssertionError("Word write addr LSBs have to be 0x0")

                # Get the (d)word aligned addr
                addr_aligned = self._get_addr_aligned(addr)

                # Get the (d)word data from the memory
                mem_data = self.memory.read(addr_aligned, 8)

                mem_data = int.from_bytes(mem_data, byteorder="little")

                # Zero the N-th word
                mem_data = ~(0xFFFF_FFFF << (word_sel * 8)) & mem_data

                # OR with the new value
                mem_data = (data << (word_sel * 8)) | mem_data

                # Convert into 32-bit int byte array
                ba_data = mem_data.to_bytes(8, byteorder="little")

                # Write the data back to the memory
                self.memory.write(addr_aligned, ba_data)
        elif size == AHBSize.DWORD:
            lsbs = addr & 0x7
            if lsbs != 0x0:
                raise AssertionError("Dword write addr LSB needs to be 0x0")
            ba_data = value.integer.to_bytes(8, byteorder="little")
            self.memory.write(addr, ba_data)

        return 0


class AHBSlave(AHBLiteSlave):
    def __init__(
        self,
        bus: AHBBus,
        clock: str,
        reset: str,
        bp: Generator[int, None, None] = None,
        name: str = "ahb_slave",
        **kwargs,
    ):
        super().__init__(bus, clock, reset, bp, name, **kwargs)
