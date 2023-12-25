# -*- coding: utf-8 -*-
# File              : test_ahb_lite_sram_all_sizes.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 25.12.2023

import cocotb
import os
import random
import math
import pytest

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import (
    AHBBus,
    AHBLiteMaster,
    AHBLiteSlaveRAM,
    AHBResp,
    AHBMonitor,
    AHBSize,
)
from cocotb.regression import TestFactory


def get_rnd_addr(mem_size_kib: int = 0):
    return random.randint(0, ((mem_size_kib - 1) * 1024) - 1) & 0xFFFF_FFF8


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


@cocotb.test()
async def run_test(dut, bp_fn=None, pip_mode=False):
    mem_size_kib = 16

    ahb_bus_slave = AHBBus.from_entity(dut)

    data_width = ahb_bus_slave.data_width
    n_bytes = data_width // 8

    ahb_lite_sram = AHBLiteSlaveRAM(
        AHBBus.from_entity(dut),
        dut.hclk,
        dut.hresetn,
        def_val=0,
        bp=bp_fn,
        mem_size=mem_size_kib * 1024,
    )

    # Below is only required bc of flake8 - non-used rule
    type(ahb_lite_sram)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, def_val="Z"
    )

    await setup_dut(dut, cfg.RST_CYCLES)

    seq_ops = [1, 2, 4] if data_width == 32 else [1, 2, 4, 8]
    mask = [0xFF, 0xFFFF, 0xFFFF_FFFF, 0xFFFF_FFFF_FFFF_FFFF]

    for index, byte_mode in enumerate(seq_ops):
        address_dw_aligned = get_rnd_addr(mem_size_kib)
        addr = [address_dw_aligned + i for i in range(0, n_bytes, byte_mode)]
        data = [rnd_val(data_width, False) for i in range(len(addr))]
        size = [byte_mode for i in range(len(addr))]
        resp_wr = await ahb_lite_master.write(addr, data, size, pip=pip_mode)
        print(resp_wr)
        expect = sum(
            (data[i // byte_mode] & mask[index]) << (8 * i)
            for i in range(0, n_bytes, byte_mode)
        )
        resp_rd = await ahb_lite_master.read(address_dw_aligned, pip=pip_mode)
        assert (
            hex(expect) == resp_rd[0]["data"]
        ), f"Mismatch between WR/RD {hex(expect)} != {resp_rd[0]['data']}"


if cocotb.SIM_NAME:
    factory = TestFactory(run_test)
    factory.add_option(
        "bp_fn", [slave_back_pressure_generator(), slave_no_back_pressure_generator()]
    )
    factory.add_option("pip_mode", [False, True])
    factory.generate_tests()


@pytest.mark.parametrize("data_width", [{"DATA_WIDTH": "32"}, {"DATA_WIDTH": "64"}])
def test_ahb_lite_sram_all_sizes(data_width):
    """
    Test AHB lite SRAM

    Test ID: 3
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    SIM_BUILD = os.path.join(
        cfg.TESTS_DIR,
        f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}_data_width_{data_width['DATA_WIDTH']}_bits",
    )
    extra_args_sim = cfg.EXTRA_ARGS

    run(
        python_search=[cfg.TESTS_DIR],
        verilog_sources=cfg.VERILOG_SOURCES,
        toplevel=cfg.TOPLEVEL,
        module=module,
        parameters=data_width,
        sim_build=SIM_BUILD,
        extra_args=extra_args_sim,
        extra_env=cfg.EXTRA_ENV,
        timescale=cfg.TIMESCALE,
        waves=1,
    )
