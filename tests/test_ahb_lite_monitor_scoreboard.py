# -*- coding: utf-8 -*-
# File              : test_ahb_lite_monitor_scoreboard.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 15.06.2024

import cocotb
import os
import random
import math
import pytest
import struct

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlaveRAM, AHBMonitor
from cocotbext.ahb import AHBTxn, AHBTrans, AHBWrite, AHBSize, AHBResp
from cocotb.regression import TestFactory
from cocotb_bus.scoreboard import Scoreboard


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


def get_random_txn(mem_size_kib, data_width, N):
    # Generate a list of unique addresses with the double of memory size
    # to create error responses
    address = random.sample(range(0, 2 * mem_size_kib * 1024, 8), N)
    # Generate a list of random 32-bit values
    value = [rnd_val(data_width) for _ in range(N)]
    # Generate a list of random sizes
    if data_width == 32:
        size = [pick_random_value([1, 2, 4]) for _ in range(N)]
    else:
        size = [pick_random_value([1, 2, 4, 8]) for _ in range(N)]

    # Create the comparison list with expected results
    expected = []
    for addr, val, sz in zip(address, value, size):
        resp, data = 0, 0
        if addr >= mem_size_kib * 1024:
            resp = AHBResp.ERROR
        else:
            resp = AHBResp.OKAY
            if sz == 1:
                data = val & 0xFF
            elif sz == 2:
                data = val & 0xFFFF
            elif sz == 4:
                data = val & 0xFFFFFFFF
            elif sz == 8:
                data = val & 0xFFFFFFFFFFFFFFFF
        expected.append({"resp": resp, "data": hex(data)})

    def _convert_size(value) -> AHBTrans:
        """Convert byte size into hsize."""
        for hsize in AHBSize:
            if (2**hsize.value) == value:
                return hsize

    write_txn = []
    read_txn = []

    for mode in [AHBWrite.READ, AHBWrite.WRITE]:
        if mode == AHBWrite.WRITE:
            for addr, sz, val, ex in zip(address, size, value, expected):
                txn = AHBTxn(
                    int(addr),
                    AHBSize(_convert_size(sz)),
                    mode,
                    ex["resp"],
                    int(val),
                    0,
                )

                write_txn.append(txn)
        else:
            for addr, sz, val, ex in zip(address, size, value, expected):
                txn = AHBTxn(
                    int(addr),
                    AHBSize(_convert_size(sz)),
                    mode,
                    ex["resp"],
                    0,
                    int(ex["data"], 16),
                )

                read_txn.append(txn)

    return address, value, size, expected, write_txn, read_txn


@cocotb.test()
async def run_test(dut, bp_fn=None, pip_mode=False):
    mem_size_kib = 16
    N = 100
    expected_output = []

    ahb_bus_slave = AHBBus.from_entity(dut)

    data_width = ahb_bus_slave.data_width

    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_mon = AHBMonitor(
        ahb_bus_slave, dut.hclk, dut.hresetn, "ahb_monitor"  # , callback=txn_recv
    )

    scoreboard = Scoreboard(dut, fail_immediately=True)

    scoreboard.add_interface(ahb_lite_mon, expected_output)

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

    # Generate random transactions and its results to compare in the scoreboard
    address, value, size, expected, wr_txn, rd_txn = get_random_txn(
        mem_size_kib, data_width, N
    )

    for mode in [AHBWrite.WRITE, AHBWrite.READ]:
        if mode == AHBWrite.WRITE:
            for addr, val, sz, tx in zip(address, value, size, wr_txn):
                expected_output.append(tx)
                await ahb_lite_master.write(addr, val, sz, pip=pip_mode)
        else:
            for addr, val, sz, tx in zip(address, value, size, rd_txn):
                expected_output.append(tx)
                await ahb_lite_master.read(addr, sz, pip=pip_mode)

    raise scoreboard.result


if cocotb.SIM_NAME:
    factory = TestFactory(run_test)
    factory.add_option(
        "bp_fn", [slave_back_pressure_generator(), slave_no_back_pressure_generator()]
    )
    factory.add_option("pip_mode", [False, True])
    factory.generate_tests()


@pytest.mark.parametrize("data_width", [{"DATA_WIDTH": "32"}, {"DATA_WIDTH": "64"}])
def test_ahb_lite_sram_monitor_scoreboard(data_width):
    """
    Test AHB lite SRAM to check monitor txns, using a scoreboard to compare both

    Test ID: 8
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
