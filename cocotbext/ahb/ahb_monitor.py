#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_monitor.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 27.10.2023
# Last Modified Date: 10.06.2024
import cocotb
import logging
import random
import copy
import datetime

from .ahb_types import AHBTrans, AHBWrite, AHBSize, AHBResp
from .ahb_bus import AHBBus
from .version import __version__

from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.handle import SimHandleBase
from cocotb.types import LogicArray
from cocotb.binary import BinaryValue
from cocotb_bus.monitors import BusMonitor
from typing import Optional, Union, Generator, List, Any
from .memory import Memory


class AHBMonitor(BusMonitor):
    def __init__(
            self, bus: AHBBus, clock: str, reset: str,
            prefix: str = None, **kwargs: Any
    ) -> None:
        name = prefix if prefix is not None else bus.entity._name + "_ahb_monitor"

        self.clk = clock
        self.rst = reset

        BusMonitor.__init__(self, bus.entity, name, clock, reset, **kwargs)
        self.bus = bus
        self.log.info(f"AHB ({name}) Monitor")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info(f"Copyright (c) {datetime.datetime.now().year} Anderson Ignacio da Silva")
        self.log.info("https://github.com/aignacio/cocotbext-ahb")


    async def _monitor_recv(self):
        """Watch the pins and reconstruct transactions."""

        pending = False
        stable_signals = {}

        while True:
            await FallingEdge(self.clk)

            # print(f"pending: {pending}")
            # Ensure master does not change its qualifiers before hready
            if (pending is True) and (self.bus.hready.value == 0):
                self._check_signals(stable_signals)
            elif (pending is True) and (self.bus.hready.value == 1):
                self._check_signals(stable_signals)
                pending = False
                self._recv(stable_signals)

            # Check for new txn
            # print(f"hready: {self.bus.hready.value}")
            # print(f"check inputs: {self._check_inputs()}")
            # print(f"check valid_tx: {self._check_valid_txn()}")
            if (
                self.bus.hready.value == 0
                and self._check_inputs()
                and self._check_valid_txn()
            ):
                pending = True
                stable_signals = {
                    "htrans": copy.deepcopy(self.bus.htrans.value),
                    "hwrite": copy.deepcopy(self.bus.hwrite.value),
                    "haddr": copy.deepcopy(self.bus.haddr.value),
                    "hsize": copy.deepcopy(self.bus.hsize.value),
                }
                if self.bus.hsel_exist:
                    stable_signals["hsel"] = copy.deepcopy(self.bus.hsel.value)
            else:
                pending = False
 
    def _check_inputs(self) -> bool:
        """Check any of the master signals are resolvable (i.e not 'z')"""
        signals = {
            "htrans": self.bus.htrans,
            "hwrite": self.bus.hwrite,
            "haddr": self.bus.haddr,
            "hsize": self.bus.hsize,
        }

        if self.bus.hsel_exist:
            signals["hsel"] = self.bus.hsel

        if self.bus.hready_in_exist:
            signals["hready_in"] = self.bus.hready_in

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

    def _check_signals(self, stable):
        """Check any of the master signals are resolvable (i.e not 'z')"""
        if self.bus.hsel_exist:
            current = {
                "hsel": self.bus.hsel,
                "htrans": self.bus.htrans,
                "hwrite": self.bus.hwrite,
                "haddr": self.bus.haddr,
                "hsize": self.bus.hsize,
            }
        else:
            current = {
                "htrans": self.bus.htrans,
                "hwrite": self.bus.hwrite,
                "haddr": self.bus.haddr,
                "hsize": self.bus.hsize,
            }

        for signal in current:
            if current[signal].value.is_resolvable is not True:
                raise AssertionError(f"Signal master.{signal} is not resolvable!")
            if current[signal].value != stable[signal]:
                if (signal == "htrans") and (self.bus.hresp.value == AHBResp.ERROR):
                    pass
                else:
                    raise AssertionError(
                        f"AHB PROTOCOL VIOLATION: Master.{signal} signal should not change before slave.hready == 1"
                    )
