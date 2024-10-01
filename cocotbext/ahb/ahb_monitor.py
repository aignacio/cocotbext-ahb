#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_monitor.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 27.10.2023
# Last Modified Date: 01.10.2024
import cocotb
import logging
import random
import copy
import struct
import datetime

from .ahb_types import AHBTrans, AHBWrite, AHBSize, AHBResp
from .ahb_bus import AHBBus
from .version import __version__

from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.handle import SimHandleBase
from cocotb.types import LogicArray
from cocotb_bus.monitors import Monitor
from typing import Optional, Union, Generator, List, Any
from .memory import Memory


class AHBMonitor(Monitor):
    def __init__(
        self, bus: AHBBus, clock: str, reset: str, prefix: str = None, **kwargs: Any
    ) -> None:
        self.name = prefix if prefix is not None else bus.entity._name + "_ahb_monitor"
        self.clk = clock
        self.rst = reset
        self.bus = bus

        # We extend from Monitor base class because we don't need to recreate
        # the internal bus property as it already exists from AHBBus
        Monitor.__init__(self, **kwargs)

        self.log.info(f"AHB ({self.name}) Monitor")
        self.log.info("cocotbext-ahb version %s", __version__)
        self.log.info(
            f"Copyright (c) {datetime.datetime.now().year} Anderson Ignacio da Silva"
        )
        self.log.info("https://github.com/aignacio/cocotbext-ahb")

    async def _monitor_recv(self):
        """Watch the pins and reconstruct transactions."""

        slave_error_prev = 0
        first_txn = {}
        first_st = {}
        first_st["phase"] = "none"
        first_st["write_first_cycle"] = True

        second_txn = {}
        second_st = {}
        second_st["phase"] = "none"
        second_st["write_first_cycle"] = True

        while True:
            await FallingEdge(self.clk)

            # Check that address phase signals of the second txn are stable while slave is not available
            if (second_st["phase"] == "addr") and (self.bus.hready.value == 0):
                self._check_signals(second_txn)

            if first_st["phase"] == "data":
                # Previous cycle we started a txn and slave was ready, but now if it is a write lets
                # check the hwdata whether it is stable or not as the slave is not available anymore
                if self.bus.hready.value == 0:
                    # Copy the latest hresp to ensure slave follow 2-cycle response
                    slave_error_prev = copy.deepcopy(self.bus.hresp.value)

                    if (first_txn["hwrite"] == 1) and (
                        first_st["write_first_cycle"] is True
                    ):
                        first_txn["hwdata"] = copy.deepcopy(self.bus.hwdata.value)
                        first_st["write_first_cycle"] = False
                    elif (first_txn["hwrite"] == 1) and (
                        first_st["write_first_cycle"] is False
                    ):
                        if self.bus.hwdata.value == first_txn["hwdata"]:
                            pass
                        else:
                            raise AssertionError(
                                f"[{self.bus.name}/{self.name}] AHB PROTOCOL VIOLATION: Master.hwdata signal should not change before slave.hready == 1"
                            )

                # Previous cycle we started a txn and slave was ready, and now it is still ready
                # As address and data phase were both completed, push the txn to the next method
                elif self.bus.hready.value == 1:
                    # Check whether the slave response follow the AMBA AHB spec
                    # with 2-cycle delay
                    if (self.bus.hresp.value != AHBResp.OKAY) and (
                        slave_error_prev == 0
                    ):
                        raise AssertionError(
                            f"[{self.bus.name}/{self.name}] AHB PROTOCOL VIOLATION: Slave is not following the 2-cyle error response \
                                    - ARM IHI 0033B.b (ID102715) - Section 5.1.3"
                        )

                    first_txn["response"] = copy.deepcopy(self.bus.hresp.value)
                    first_txn["hrdata"] = copy.deepcopy(self.bus.hrdata.value)
                    first_txn["hwdata"] = copy.deepcopy(self.bus.hwdata.value)

                    txn = AHBTxn(
                        int(first_txn["haddr"]),
                        AHBSize(first_txn["hsize"]),
                        AHBWrite(first_txn["hwrite"]),
                        AHBResp(first_txn["response"]),
                        int(first_txn["hwdata"]),
                        int(first_txn["hrdata"]),
                    )

                    self._recv(txn)
                    # exp_data = int(first_txn["hrdata"]) # struct.pack("I",int(first_txn['hrdata']))
                    # self._recv(exp_data)

                    # Restart the txn status
                    first_st["phase"] = "none"
                    first_st["write_first_cycle"] = True
                    slave_error_prev = 0

                    # Clean second txn
                    second_st["phase"] = "none"
                    second_st["write_first_cycle"] = True

            if (self._check_valid_txn() is True) and (first_st["phase"] == "none"):
                first_st["phase"] = "data" if self.bus.hready.value == 1 else "addr"

                first_txn["hsel"] = (
                    copy.deepcopy(self.bus.hsel.value) if self.bus.hsel_exist else 0
                )
                first_txn["haddr"] = copy.deepcopy(self.bus.haddr.value)
                first_txn["htrans"] = copy.deepcopy(self.bus.htrans.value)
                first_txn["hsize"] = copy.deepcopy(self.bus.hsize.value)
                first_txn["hwrite"] = copy.deepcopy(self.bus.hwrite.value)
            # We only enter in the if below if the last txn did not complete and the master issued a new txn
            elif (self._check_valid_txn() is True) and (first_st["phase"] == "data"):
                second_st["phase"] = "addr"

                second_txn["hsel"] = (
                    copy.deepcopy(self.bus.hsel.value) if self.bus.hsel_exist else 0
                )
                second_txn["haddr"] = copy.deepcopy(self.bus.haddr.value)
                second_txn["htrans"] = copy.deepcopy(self.bus.htrans.value)
                second_txn["hsize"] = copy.deepcopy(self.bus.hsize.value)
                second_txn["hwrite"] = copy.deepcopy(self.bus.hwrite.value)

            if first_st["phase"] == "addr":
                self._check_signals(first_txn)

                if self.bus.hready.value == 0:
                    raise AssertionError(
                        f"[{self.bus.name}/{self.name}] AHB PROTOCOL VIOLATION:"
                        "A slave cannot request that the address phase is extended"
                        "and therefore all slaves must be capable of sampling the address during this time"
                        " - ARM IHI 0033B.b (ID102715) - Section 1.3"
                    )
                else:
                    first_st["phase"] = "data"

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
        if self._check_inputs():
            htrans_st = (AHBTrans(self.bus.htrans.value) != AHBTrans.IDLE) and (
                AHBTrans(self.bus.htrans.value) != AHBTrans.BUSY
            )

            if self.bus.hsel_exist:  # Decoder to slave
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
                if htrans_st:  # In this case it is just a master
                    return True
                else:
                    return False
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
                        f"[{self.bus.name}/{self.name}] AHB PROTOCOL VIOLATION: Master.{signal} signal should not change before slave.hready == 1"
                    )


class AHBTxn:
    def __init__(
        self,
        addr: int = 0x00,
        size: AHBSize = AHBSize.BYTE,
        mode: AHBWrite = AHBWrite.READ,
        resp: AHBResp = AHBResp.OKAY,
        wdata: int = 0x00,
        rdata: int = 0x00,
    ):
        self.addr = addr
        self.size = size
        self.mode = mode
        self.resp = resp
        self.wdata = wdata
        self.rdata = rdata

    def __str__(self):
        return (
            f"AHB Txn Details:\n"
            f"  Address: 0x{self.addr:08X}\n"
            f"  Size: {2**self.size} bytes (0x{self.size:03X})\n"
            f"  Mode: {'Write' if self.mode == 1 else 'Read'} (0x{self.mode:01X})\n"
            f"  Response: {'OKAY' if self.resp == 0 else 'ERROR'} (0x{self.resp:02X})\n"
            f"  Write Data: 0x{self.wdata:08X}\n"
            f"  Read Data: 0x{self.rdata:08X}\n"
        )

    def __eq__(self, other):
        # We have to override the default python comparison method for this class
        # because the Scoreboard class will compare the txns
        if isinstance(other, AHBTxn):
            return (
                self.addr == other.addr
                and self.size == other.size
                and self.mode == other.mode
                and self.resp == other.resp
                and self.wdata == other.wdata
                and self.rdata == other.rdata
            )
        return False
