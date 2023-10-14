#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 14.10.2023

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

    def _convert_size(self, value) -> Union[AHBTrans, LogicArray]:
        """Convert byte size into hsize."""

        if isinstance(value, LogicArray):
            return value

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
            raise ValueError(f"Error -> {size} - Size must"
                             "be a positive power of 2")

    def _addr_phase(self, addr: int, size: int, mode: str):
        """Drive the AHB signals of the address phase."""
        wr = AHBWrite(0b1) if mode == 'write' else AHBWrite(0b0)
        self.bus.haddr.value = addr
        self.bus.htrans.value = AHBTrans(0b10)
        self.bus.hsize.value = self._convert_size(size)
        self.bus.hwrite.value = wr
        if self.bus.hsel_exist:
            self.bus.hsel.value = 1

    def _create_vector(self, vec: Sequence[int],
                       width: int,
                       phase: str,
                       pip: Optional[bool] = False) -> Sequence[int]:
        """Create a list to be driven during address/data phase."""
        vec_out = []
        if pip:
            # Format address/data to send in pipeline
            # Address
            # |   ADDRESS 0  | ADDRESS 1 | ... | default value |
            # Data
            # |  default val |   DATA 0  | ... |    DATA N     |

            if phase == 'address_phase':
                vec_out = vec
                vec_out.append(self._get_def(width, self.def_val))
            elif phase == 'data_phase':
                vec_out = vec
                vec_out.insert(0, self._get_def(width, self.def_val))
        else:
            # Format address/data to send in non-pipeline
            # Address
            # |   ADDRESS 0  | default value |   ADDRESS 1   | default value |
            # Data
            # |  default val |     DATA 0    | default value |    DATA 1     |

            if phase == 'address_phase':
                for i in vec:
                    vec_out.append(i)
                    vec_out.append(self._get_def(width, self.def_val))
            elif phase == 'data_phase':
                for i in vec:
                    vec_out.append(self._get_def(width, self.def_val))
                    vec_out.append(i)
        return vec_out

    @cocotb.coroutine
    async def _send_txn(self, address: Sequence[int],
                        value: Sequence[int],
                        size: Sequence[int],
                        mode: str = 'write') -> Sequence[AHBResp]:
        """Drives the AHB transaction into the bus."""
        response = []
        first_txn = True

        for index, (txn_addr, txn_data, txn_size) in enumerate(zip(address,
                                                                   value,
                                                                   size)):
            if index == len(address) - 1:
                self._init_bus()
            else:
                self._addr_phase(txn_addr, txn_size, mode)
                if txn_addr != self.def_val:
                    if not isinstance(txn_addr, LogicArray):
                        self.log.info(f"AHB write txn:\n"
                                      f"\tADDR = 0x{txn_addr:x}\n"
                                      f"\tDATA = 0x{value[index+1]:x}\n"
                                      f"\tSIZE = {txn_size}")
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

    @cocotb.coroutine
    async def write(self, address: Union[int, Sequence[int]],
                    value: Union[int, Sequence[int]],
                    size: Optional[Union[int, Sequence[int]]] = None,
                    pip: Optional[bool] = False) -> Sequence[AHBResp]:
        """Write data in the AHB bus."""

        if size is None:
            size = [self.bus._data_width // 8 for _ in range(len(address))]
        else:
            for sz in size:
                AHBLiteMaster._check_size(sz, len(self.bus.hwdata) // 8)

        # Convert all inputs into lists, if not already
        if not isinstance(address, list):
            address = [address]
        if not isinstance(value, list):
            value = [value]
        if not isinstance(size, list):
            size = [size]

        # First check if the input sizes are correct
        if len(address) != len(value):
            raise Exception(f'Address length ({len(address)}) is'
                            f'different from data length ({len(value)})')

        if len(address) != len(size):
            raise Exception(f'Address length ({len(address)}) is'
                            f'different from size length ({len(size)})')

        # Need to copy data as we'll have to shift address/value
        t_address = copy.deepcopy(address)
        t_value = copy.deepcopy(value)
        t_size = copy.deepcopy(size)

        width = len(self.bus.haddr)
        t_address = self._create_vector(t_address, width, 'address_phase', pip)
        width = len(self.bus.hwdata)
        t_value = self._create_vector(t_value, width, 'data_phase', pip)
        width = len(self.bus.hsize)
        t_size = self._create_vector(t_size, width, 'address_phase', pip)

        return await self._send_txn(t_address, t_value, t_size, 'write')
