#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_lite.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
# Date              : 30.09.2023
# Last Modified Date: 01.10.2023
import random
import cocotb
import os
import logging
import pytest
import itertools

from random import randrange
from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import RisingEdge, ClockCycles
from cocotb.regression import TestFactory
from cocotb.clock import Clock
from cocotbext.ahb import AhbBus

async def reset_dut(dut, cycles):
    dut.hresetn.setimmediatevalue(0) 
    await ClockCycles(dut.hclk, cycles) 
    dut.hresetn.setimmediatevalue(1) 

@cocotb.test()
async def run_test(dut):
    cocotb.start_soon(Clock(dut.hclk, *cfg.CLK_100MHz).start())
    await reset_dut(dut, cfg.RST_CYCLES) 
    cnt = 0
    while True:
        await RisingEdge(dut.hclk)
        cnt += 1
        if cnt > 100:
            break

    ander = AhbBus

def test_ahb_lite():
    """
    Test AHB lite

    Test ID: 1
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    SIM_BUILD = os.path.join(cfg.TESTS_DIR, f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}")
    extra_args_sim = cfg.EXTRA_ARGS

    run(
        python_search=[cfg.TESTS_DIR],
        verilog_sources=cfg.VERILOG_SOURCES,
        toplevel=cfg.TOPLEVEL,
        module=module,
        sim_build=SIM_BUILD,
        extra_args=extra_args_sim
    )
