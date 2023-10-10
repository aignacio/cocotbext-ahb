#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 10.10.2023

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


class AHBLiteMaster:
    def __init__(self, bus: AHBBus, clock: str, reset: str,
                 timeout: int = 100, def_val: Union[int, str] = 'Z', **kwargs):
        self.bus = bus
        self.clk = clock
        self.rst = reset
        self.timeout = timeout
        self.def_val = def_val
        self.log = logging.getLogger(f"cocotb.ahb_lite.{bus._name}."
                                     f"{bus._entity._name}")
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

    def _addr_phase(self, addr, size):
        self.bus.haddr.value = addr
        self.bus.htrans.value = AHBTrans(0b10)
        self.bus.hsize.value = self._convert_size(size)
        self.bus.hwrite.value = AHBWrite(0b1)
        if self.bus.hsel_exist:
            self.bus.hsel.value = 1

    @cocotb.coroutine
    async def write(self, address: Union[int, Sequence[int]],
                    value: Union[int, Sequence[int]],
                    size: Optional[int] = None,
                    pip: Optional[bool] = False) -> Sequence[AHBResp]:
        """Write data in the AHB bus."""

        # Convert all inputs into lists, if not already
        if not isinstance(address, list):
            address = [address]
        if not isinstance(value, list):
            value = [value]

        if size is None:
            size = self.bus._data_width // 8
        else:
            AHBLiteMaster._check_size(size, len(self.bus.hwdata) // 8)

        # First check if the input sizes are correct
        if len(address) != len(value):
            raise Exception(f'Address length ({len(address)}) is'
                            f'different from data length ({len(value)})')

        response = []
        if not pip:
            for txn_addr, txn_data in zip(address, value):
                self.log.info(f"AHB write txn:\n"
                              f"\tADDR = 0x{txn_addr:x}\n"
                              f"\tDATA = 0x{txn_data:x}\n"
                              f"\tSIZE = {size}")

                self._addr_phase(txn_addr, size)
                await RisingEdge(self.clk)

                # Address phase
                timeout_counter = 0
                while self.bus.hready.value != 1:
                    timeout_counter += 1
                    if timeout_counter == self.timeout:
                        raise Exception(f'Timeout value of {timeout_counter}'
                                        f' clock cycles has been reached!')
                    await RisingEdge(self.clk)

                self._init_bus()

                # Data phase
                self.bus.hwdata.value = txn_data
                await RisingEdge(self.clk)
                timeout_counter = 0
                while self.bus.hready.value != 1:
                    timeout_counter += 1
                    if timeout_counter == self.timeout:
                        raise Exception(f'Timeout value of {timeout_counter}'
                                        f' clock cycles has been reached!')
                    await RisingEdge(self.clk)
                response += [{'resp': AHBResp(int(self.bus.hresp.value)),
                              'data': self.bus.hrdata.value}]
                self._init_bus()
        else:
            # Need to copy data as we'll have to shift address/value
            t_address = copy.deepcopy(address)
            t_value = copy.deepcopy(value)

            t_address.append(self._get_def(len(self.bus.haddr),
                                           self.def_val))
            t_value.insert(0, self._get_def(len(self.bus.hwdata),
                                            self.def_val))
            first_txn = True
            # for txn_addr, txn_data in zip(address, value):
            for index, (txn_addr, txn_data) in enumerate(zip(t_address,
                                                             t_value)):
                if index == len(t_address) - 1:
                    self._init_bus()
                else:
                    self._addr_phase(txn_addr, size)
                    self.log.info(f"AHB write txn:\n"
                                  f"\tADDR = 0x{txn_addr:x}\n"
                                  f"\tDATA = 0x{t_value[index+1]:x}\n"
                                  f"\tSIZE = {size}")
                self.bus.hwdata.value = txn_data
                await RisingEdge(self.clk)
                timeout_counter = 0
                while self.bus.hready.value != 1:
                    timeout_counter += 1
                    if timeout_counter == self.timeout:
                        raise Exception(f'Timeout value of {timeout_counter}'
                                        f' clock cycles has been reached!')
                    await RisingEdge(self.clk)

                if first_txn:
                    first_txn = False
                else:
                    response += [{'resp': AHBResp(int(self.bus.hresp.value)),
                                  'data': self.bus.hrdata.value}]
            self._init_bus()
        return response
