#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_lite.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 16.10.2023

import cocotb
import os
import random

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBMaster


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


@cocotb.coroutine
async def setup_dut(dut, cycles):
    cocotb.start_soon(Clock(dut.hclk, *cfg.CLK_100MHz).start())
    dut.hresetn.value = 0
    await ClockCycles(dut.hclk, cycles)
    dut.hresetn.value = 1


@cocotb.test()
async def run_test(dut):
    ahb_lite_master = AHBLiteMaster(AHBBus.from_prefix(dut, "slave"),
                                    dut.hclk,
                                    dut.hresetn,
                                    def_val='Z')
    await setup_dut(dut, cfg.RST_CYCLES)
    dut.master_hready.value = 1
    dut.master_hresp.value = 0
    dut.master_hrdata.value = 0

    address = [rnd_val(32) for _ in range(200)]
    value = [rnd_val(32) for _ in range(200)]
    size = [pick_random_value([1, 2, 4]) for _ in range(200)]

    resp = await ahb_lite_master.write(address, value, pip=True)
    resp = await ahb_lite_master.write(address, value, pip=False)
    resp = await ahb_lite_master.write(address, value, pip=True)
    resp = await ahb_lite_master.write(address, value, pip=False)

    resp = await ahb_lite_master.write(address, value, size, pip=False)
    resp = await ahb_lite_master.write(address, value, size, pip=False)
    resp = await ahb_lite_master.write(address, value, size, pip=True)
    resp = await ahb_lite_master.write(address, value, size, pip=True)

    resp = await ahb_lite_master.read(address, pip=True)

    print(resp)


def test_ahb_lite():
    """
    Test AHB lite

    Test ID: 1
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    SIM_BUILD = os.path.join(cfg.TESTS_DIR,
                             f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}")
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
        waves=1
    )
