#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_monitor_master.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 10.06.2024

import cocotb
import os
import random

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles, Event
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBMonitor, AHBTrans
from cocotb.regression import TestFactory


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


def slave_back_pressure_generator():
    while True:
        yield pick_random_value([False, True])


def slave_no_back_pressure_generator():
    while True:
        yield True


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


# if cocotb.SIM_NAME:
# factory = TestFactory(run_test)
# factory.add_option("msig", ["hsel", "haddr", "hsize", "htrans", "hwrite"])
# factory.generate_tests()


def test_ahb_monitor_master():
    """
    Test AHB monitor

    Test ID: 4
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    SIM_BUILD = os.path.join(
        cfg.TESTS_DIR, f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}"
    )
    extra_args_sim = cfg.EXTRA_ARGS

    run(
        python_search=[cfg.TESTS_DIR],
        verilog_sources=cfg.VERILOG_SOURCES,
        toplevel=cfg.TOPLEVEL,
        module=module,
        sim_build=SIM_BUILD,
        extra_args=extra_args_sim,
        extra_env=cfg.EXTRA_ENV,
        timescale=cfg.TIMESCALE,
        waves=1,
    )
