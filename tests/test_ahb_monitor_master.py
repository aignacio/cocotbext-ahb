#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_monitor_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 10.06.2024

import os
import random

import cocotb
from cocotb.clock import Clock
from cocotb.regression import TestFactory
from cocotb.triggers import ClockCycles, Event
from cocotb_tools.runner import get_runner
from const import cfg

from cocotbext.ahb import AHBBus, AHBMonitor, AHBTrans


def rnd_val(bit: int = 0, zero: bool = True):
    if zero is True:
        return random.randint(0, (2**bit) - 1)
    else:
        return random.randint(1, (2**bit) - 1)


def pick_random_value(input_list):
    if input_list:
        return random.choice(input_list)
    else:
        return None  # Return None if the list is empty


async def setup_dut(dut, cycles):
    cocotb.start_soon(Clock(dut.hclk, *cfg.CLK_100MHz).start())
    dut.hresetn.value = 0
    await ClockCycles(dut.hclk, cycles)
    dut.hresetn.value = 1


def recv_txn(txn):
    print(txn)


@cocotb.test(expect_fail=True)
async def run_test(dut):  # , msig="hsel"):
    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_mon = AHBMonitor(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn
    )  # , callback=recv_txn, event=fn)

    type(ahb_mon)

    msig = pick_random_value(["hsel", "haddr", "hsize", "htrans", "hwrite"])

    dut.hsel.value = 1
    dut.haddr.value = 0xDEADBEEF
    dut.hsize.value = 0x2
    dut.htrans.value = AHBTrans.NONSEQ
    dut.hwdata.value = 0xBABEBABE
    dut.hwrite.value = 1
    dut.hready_in.value = 1

    dut.hready.value = 0
    dut.hresp.value = 0
    dut.hrdata.value = 0

    await ClockCycles(dut.hclk, 1)

    # Test bad master - Master changes address phase qualifiers
    dut.hsel.value = 1 if msig != "hsel" else 0
    dut.haddr.value = 0xDEADBEEF if msig != "haddr" else 0
    dut.hsize.value = 0x2 if msig != "hsize" else 0
    dut.htrans.value = AHBTrans.NONSEQ if msig != "htrans" else 0
    dut.hwdata.value = 0xBABEBABE
    dut.hwrite.value = 1 if msig != "hwrite" else 0
    dut.hready_in.value = 1

    dut.hready.value = 0
    dut.hresp.value = 0
    dut.hrdata.value = 0

    await ClockCycles(dut.hclk, 2)


def test_ahb_monitor_master():
    """
    Test AHB monitor

    Test ID: 4
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    sim_build = os.path.join(
        cfg.TESTS_DIR, f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}"
    )

    runner = get_runner(cfg.SIMULATOR)

    runner.build(
        sources=cfg.VERILOG_SOURCES,
        hdl_toplevel=cfg.TOPLEVEL,
        build_dir=sim_build,
        timescale=cfg.TIMESCALE,
        build_args=cfg.EXTRA_ARGS,
        waves=True,
    )

    runner.test(
        test_module=module,
        hdl_toplevel=cfg.TOPLEVEL,
        waves=True,
        extra_env=cfg.EXTRA_ENV,
        log_file=sim_build + "_run.log",
    )
