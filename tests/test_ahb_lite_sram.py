# -*- coding: utf-8 -*-
# File              : test_ahb_lite_sram.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 25.10.2023

import cocotb
import os
import random
import math

from const import cfg
from cocotb_test.simulator import run
from cocotb.triggers import ClockCycles
from cocotb.clock import Clock
from cocotbext.ahb import AHBBus, AHBLiteMaster, AHBLiteSlaveRAM, AHBResp


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


@cocotb.coroutine
async def setup_dut(dut, cycles):
    cocotb.start_soon(Clock(dut.hclk, *cfg.CLK_100MHz).start())
    dut.hresetn.value = 0
    await ClockCycles(dut.hclk, cycles)
    dut.hresetn.value = 1


@cocotb.test()
async def run_test(dut):
    data_width = 32
    mem_size_kib = 16
    N = 5000

    await setup_dut(dut, cfg.RST_CYCLES)

    ahb_lite_master = AHBLiteMaster(
        AHBBus.from_prefix(dut, "slave"), dut.hclk, dut.hresetn, def_val="Z"
    )

    ahb_lite_sram = AHBLiteSlaveRAM(
        AHBBus.from_prefix(dut, "master"),
        dut.hclk,
        dut.hresetn,
        def_val=0,
        bp=slave_back_pressure_generator(),
        mem_size=mem_size_kib * 1024,
    )

    type(ahb_lite_sram)

    # Generate a list of unique addresses with the double of memory size
    # to create error responses
    address = random.sample(range(0, 2 * mem_size_kib * 1024, 4), N)
    # Generate a list of random 32-bit values
    value = [rnd_val(data_width) for _ in range(N)]
    # Generate a list of random sizes
    size = [pick_random_value([1, 2, 4]) for _ in range(N)]

    # Create the comparison list
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
    resp = await ahb_lite_master.write(address, value, size, pip=True)
    resp = await ahb_lite_master.read(address, size, pip=True)
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
