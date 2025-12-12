#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_ahb_lite_log.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 24.10.2024

import os
import random

import cocotb
import pytest
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb_tools.runner import get_runner
from const import cfg

from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlave


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
@cocotb.parametrize(
    bp_fn=[slave_back_pressure_generator(), slave_no_back_pressure_generator()],
    pip_mode=[False, True],
)
async def run_test(dut, bp_fn=None, pip_mode=False):
    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, def_val=0
    )

    ahb_lite_slave = AHBLiteSlave(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, bp=bp_fn
    )

    type(ahb_lite_slave)

    address = [0x00, 0x04, 0x08]
    value = [rnd_val(32) for _ in range(3)]
    size = [pick_random_value([1, 2, 4]) for _ in range(3)]
    mode = [pick_random_value([1, 0]) for _ in range(3)]

    resp = await ahb_lite_master.write(address, value, pip=pip_mode)
    resp = await ahb_lite_master.read(address, size, pip=pip_mode)
    resp = await ahb_lite_master.custom(address, value, mode, size, pip_mode)

    type(resp)

    # ----------------------
    #  AMBA format test
    # ----------------------
    if ahb_lite_master.bus.data_width == 32:
        # Byte access
        address = [0x00, 0x01, 0x02, 0x3]
        value = [rnd_val(32) for _ in range(4)]
        size = [1 for _ in range(4)]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )

        # Half-word access
        address = [0x00, 0x02]
        value = [rnd_val(32) for _ in range(2)]
        size = [2 for _ in range(2)]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )

        # Word access
        address = [0x00]
        value = [rnd_val(32)]
        size = [4]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )
    else:
        # Byte access
        address = [0x00, 0x01, 0x02, 0x3, 0x4, 0x5, 0x6, 0x7]
        value = [rnd_val(32) for _ in range(8)]
        size = [1 for _ in range(8)]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )

        # Half-word access
        address = [0x00, 0x02, 0x4, 0x6]
        value = [rnd_val(32) for _ in range(4)]
        size = [2 for _ in range(4)]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )

        # Word access
        address = [0x00, 0x04]
        rd = rnd_val(32)
        value = [rd, rd]
        size = [4 for _ in range(2)]
        resp = await ahb_lite_master.write(
            address, value, size, format_amba=True, verbose=True
        )


@pytest.mark.parametrize("data_width", [{"DATA_WIDTH": "32"}, {"DATA_WIDTH": "64"}])
def test_ahb_lite_log(data_width):
    """
    Test AHB lite log messages

    Test ID: 1
    """
    module = os.path.splitext(os.path.basename(__file__))[0]
    sim_build = os.path.join(
        cfg.TESTS_DIR,
        f"../run_dir/sim_build_{cfg.SIMULATOR}_{module}_data_width_{data_width['DATA_WIDTH']}_bits",
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
