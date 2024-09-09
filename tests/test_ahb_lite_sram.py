# -*- coding: utf-8 -*-
# File              : test_ahb_lite_sram.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 09.09.2024

import cocotb
import os
import random
import math
import pytest

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlaveRAM, AHBResp, AHBMonitor
from cocotb.regression import TestFactory

recv_txn = []


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
    # pass
    recv_txn.append(txn)
    print(txn)


@cocotb.test()
async def run_test(dut, bp_fn=None, pip_mode=False):
    mem_size_kib = 16
    N = 1000

    ahb_bus_slave = AHBBus.from_entity(dut)

    data_width = ahb_bus_slave.data_width

    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_mon = AHBMonitor(
        ahb_bus_slave, dut.hclk, dut.hresetn, "ahb_monitor", callback=txn_recv
    )

    # Below is only required bc of flake8 - non-used rule
    type(ahb_lite_mon)

    ahb_lite_sram = AHBLiteSlaveRAM(
        AHBBus.from_entity(dut),
        dut.hclk,
        dut.hresetn,
        bp=bp_fn,
        mem_size=mem_size_kib * 1024,
    )

    # Below is only required bc of flake8 - non-used rule
    type(ahb_lite_sram)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_entity(dut), dut.hclk, dut.hresetn, def_val="Z"
    )

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

    # Perform the writes and reads
    resp = await ahb_lite_master.write(address, value, size, pip=pip_mode)
    resp = await ahb_lite_master.read(address, size, pip=pip_mode)
    print(resp)
    # Compare all txns
    for index, (real, expect) in enumerate(zip(resp, expected)):
        if real != expect:
            print("------ERROR------")
            print(f"Txn ID: {index}")
            print("DUT")
            print(real)
            print("Expected")
            print(expect)
            assert real == expect, "DUT != Expected"

    # Prepare data to compare
    txn = []
    for hwrite in [1, 0]:
        for i_addr, i_value, i_size in zip(address, value, size):
            txn_sent = {}
            txn_sent["haddr"] = i_addr
            txn_sent["value"] = i_value
            txn_sent["size"] = i_size
            txn_sent["hwrite"] = hwrite
            txn.append(txn_sent)

    # Compare all sent txns with the monitor
    print(f"Sent txn {len(txn)} and monitored {len(recv_txn)}")
    # for index, (real, expect) in enumerate(zip( )):
    # if real != expect:
    # print("------ERROR------")
    # print(f"Txn ID: {index}")
    # print("DUT")
    # print(real)
    # print("Expected")
    # print(expect)
    # assert real == expect, "DUT != Expected"


if cocotb.SIM_NAME:
    factory = TestFactory(run_test)
    factory.add_option(
        "bp_fn", [slave_back_pressure_generator(), slave_no_back_pressure_generator()]
    )
    factory.add_option("pip_mode", [False, True])
    factory.generate_tests()


@pytest.mark.parametrize("data_width", [{"DATA_WIDTH": "32"}, {"DATA_WIDTH": "64"}])
def test_ahb_lite_sram(data_width):
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
