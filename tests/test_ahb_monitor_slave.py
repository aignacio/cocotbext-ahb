#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_monitor_slave.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 29.11.2023

import cocotb
import os
import random

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBMonitor, AHBTrans, AHBResp
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
