#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_monitor_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 29.11.2023

import os
import random

import cocotb
from cocotb.clock import Clock
from cocotb.regression import TestFactory
from cocotb.triggers import ClockCycles
from cocotb_tools.runner import get_runner
from const import cfg

from cocotbext.ahb import AHBBus, AHBMonitor, AHBResp, AHBTrans


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


@cocotb.test(expect_fail=True)
async def run_test(dut):  # , msig="hsel"):
    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_mon = AHBMonitor(AHBBus.from_entity(dut), dut.hclk, dut.hresetn)

    type(ahb_mon)

    dut.hsel.value = 1
    dut.haddr.value = 0xDEADBEEF
    dut.hsize.value = 0x2
    dut.htrans.value = AHBTrans.NONSEQ
    dut.hwdata.value = 0xBABEBABE
    dut.hwrite.value = 1
    dut.hready_in.value = 1

    dut.hready.value = 1
    dut.hresp.value = 0
    dut.hrdata.value = 0

    await ClockCycles(dut.hclk, 1)

    dut.hsel.value = 1
    dut.haddr.value = 0xDEADBEEF
    dut.hsize.value = 0x2
    dut.htrans.value = AHBTrans.NONSEQ
    dut.hwdata.value = 0xBABEBABE
    dut.hwrite.value = 1
    dut.hready_in.value = 1

    # Test bad slave - Slave does not throw error correctly
    dut.hready.value = 1
    dut.hresp.value = AHBResp.ERROR
    dut.hrdata.value = 0

    await ClockCycles(dut.hclk, 2)


def test_ahb_monitor_slave():
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
