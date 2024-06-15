#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_lite.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 14.06.2024

import cocotb
import os
import random

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlave, AHBMonitor
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


def txn_recv(txn):
    print(txn)


@cocotb.test()
async def run_test(dut, bp_fn=None, pip_mode=False):
    N = 1000

    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_mon = AHBMonitor(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, "ahb_monitor", callback=txn_recv
    )

    # Below is only required bc of flake8 - non-used rule
    type(ahb_lite_mon)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, def_val="Z"
    )

    ahb_lite_slave = AHBLiteSlave(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, def_val=0, bp=bp_fn
    )

    type(ahb_lite_slave)

    address = [rnd_val(32) for _ in range(N)]
    value = [rnd_val(32) for _ in range(N)]
    size = [pick_random_value([1, 2, 4]) for _ in range(N)]

    resp = await ahb_lite_master.write(address, value, pip=pip_mode)
    resp = await ahb_lite_master.write(address, value, pip=not pip_mode)
    resp = await ahb_lite_master.write(address, value, pip=pip_mode)

    resp = await ahb_lite_master.read(address, size, pip=pip_mode)
    resp = await ahb_lite_master.read(address, size, pip=not pip_mode)
    resp = await ahb_lite_master.read(address, size, pip=pip_mode)

    address = [rnd_val(32) for _ in range(N)]
    value = [rnd_val(32) for _ in range(N)]
    size = [pick_random_value([1, 2, 4]) for _ in range(N)]

    print(resp)

    txn_type = [pick_random_value([1, 0]) for _ in range(N)]

    resp = await ahb_lite_master.custom(address, value, txn_type, size, pip_mode)


if cocotb.SIM_NAME:
    factory = TestFactory(run_test)
    factory.add_option(
        "bp_fn", [slave_back_pressure_generator(), slave_no_back_pressure_generator()]
    )
    factory.add_option("pip_mode", [False, True])
    factory.generate_tests()


def test_ahb_lite():
    """
    Test AHB lite

    Test ID: 1
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
