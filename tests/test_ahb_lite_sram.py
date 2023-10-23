# -*- coding: utf-8 -*-
# File              : test_ahb_lite_sram.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 23.10.2023

import cocotb
import os
import random

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlaveRAM


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


def slave_back_pressure_generator(boolean_sequence):
    while True:
        for value in boolean_sequence:
            if isinstance(value, bool):
                yield value
            else:
                raise ValueError("Input sequence should contain" "only boolean values")


@cocotb.coroutine
async def setup_dut(dut, cycles):
    cocotb.start_soon(Clock(dut.hclk, *cfg.CLK_100MHz).start())
    dut.hresetn.value = 0
    await ClockCycles(dut.hclk, cycles)
    dut.hresetn.value = 1


@cocotb.test()
async def run_test(dut):
    N = 10

    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_prefix(dut, "slave"), dut.hclk, dut.hresetn, def_val="Z"
    )

    ahb_lite_sram = AHBLiteSlaveRAM(
        AHBBus.from_prefix(dut, "master"),
        dut.hclk,
        dut.hresetn,
        def_val=0,
        mem_size=1024,
    )
    type(ahb_lite_sram)

    address = [rnd_val(10) & 0xFFFFFFFC for _ in range(N)]
    value = [rnd_val(10) for _ in range(N)]
    size = [pick_random_value([1, 2, 4]) for _ in range(N)]

    resp = await ahb_lite_master.write(address, value, size, pip=True)
    resp = await ahb_lite_master.read(address, pip=True)
    print(resp)

    resp = await ahb_lite_master.write(0x4000, 0xDEADBEEF, pip=True)
    print(resp)


def test_ahb_lite_sram():
    """
    Test AHB lite SRAM

    Test ID: 2
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
