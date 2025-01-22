#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 16.10.2023
# Last Modified Date: 26.12.2024

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
        def clog2(x):
            import math

            return math.ceil(math.log2(x))

        def calc_addr_mask(addr_width: int, data_width: int) -> int:
            return ((1 << addr_width) - 1) - ((1 << clog2(data_width / 8)) - 1)

        return calc_addr_mask(self.bus._addr_width, self.bus._data_width) & addr

    def _rd(self, addr: int, size: AHBSize) -> int:
        rd_bytes_num = 1 << size
        rd_bits_num = rd_bytes_num * 8

        # Check that HSIZE is less than or equal to the data with
        if self.bus._data_width < rd_bits_num:
            raise AssertionError("HSIZE is larger than the data width")

        # Check that the address is aligned to HSIZE
        if (addr % rd_bytes_num) != 0:
            raise AssertionError("All transfers must be aligned to the address boundary equal to the size of the transfer (HSIZE)")

        # Get the addr aligned to data bus width
        addr_aligned = self._get_addr_aligned(addr)

        # Get data bus width in bytes
        bus_bytes_width = int(self.bus._data_width / 8)

        # Get the data from memory
        mem_data = self.memory.read(addr_aligned, bus_bytes_width)
        mem_data = int.from_bytes(mem_data, byteorder="little")

        # Get mask by hsize
        data_mask = (1 << rd_bits_num) - 1

        # Get the offset in the transaction
        byte_offset = addr & (bus_bytes_width - 1)

        # Get data shifted by offset
        data = (data_mask << (byte_offset * 8)) & mem_data
        return data

    def _wr(self, addr: int, size: AHBSize, value: LogicArray) -> int:
        wr_bytes_num = 1 << size
        wr_bits_num = wr_bytes_num * 8

        # Check that HSIZE is less than or equal to the data with
        if self.bus._data_width < wr_bits_num:
            raise AssertionError("HSIZE is larger than the data width")

        # Check that the address is aligned to HSIZE
        if (addr % wr_bytes_num) != 0:
            raise AssertionError("All transfers must be aligned to the address boundary equal to the size of the transfer (HSIZE)")

        # Get the transfer size aligned addr
        addr_aligned = self._get_addr_aligned(addr)

        # Get data width in bytes
        bus_bytes_width = int(self.bus._data_width / 8)

        # Get the offset in the transaction
        byte_offset = addr & (bus_bytes_width - 1)

        # Get mask by hsize
        data_mask = (1 << wr_bits_num) - 1

        data = (value.integer >> (byte_offset * 8)) & data_mask

        # Get the (d)word data from memory
        mem_data = self.memory.read(addr_aligned, bus_bytes_width)
        mem_data = int.from_bytes(mem_data, byteorder="little")

        # Zero out the section that is being written to
        mem_data = ~(data_mask << (byte_offset * 8)) & mem_data
        # put the data there
        mem_data = (data << (byte_offset * 8)) | mem_data

        # Convert into data width bit long integer byte array
        ba_data = mem_data.to_bytes(bus_bytes_width, byteorder="little")

        # Write the data back to memory
        self.memory.write(addr_aligned, ba_data)
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
