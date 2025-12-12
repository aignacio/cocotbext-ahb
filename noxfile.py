#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : noxfile.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 24.10.2024

import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12"], reuse_venv=True)
def run(session):
    session.env["DUT"] = "ahb_template"
    session.env["SIM"] = "icarus"
    # session.env["COCOTB_LOG_LEVEL"] = "debug"
    # session.env['SIM'] = "verilator"
    session.env["TIMEPREC"] = "1ps"
    session.env["TIMEUNIT"] = "1ns"
    session.install(
        "pytest",
        "pytest-xdist",
        "pytest-sugar",
        "pytest-cov",
        "pytest-split",
    )
    session.install("-e", ".[test]")
    session.run(
        "pytest",
        "--cov=cocotbext",
        "--cov-branch",
        "--cov-report=xml",
        # "-rf",
        "-rP",
        "-n",
        "auto",
        *session.posargs,
    )


@nox.session(python=["3.9", "3.10", "3.11", "3.12"], reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8")
