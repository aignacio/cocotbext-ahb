#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_types.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 22.10.2023

import enum


class AHBSize(enum.IntEnum):
    BYTE = 0b000
    HWORD = 0b001
    WORD = 0b010
    DWORD = 0b011
    FWORD = 0b100
    EWORD = 0b101


class AHBBurst(enum.IntEnum):
    SINGLE = 0b000
    INCR = 0b001
    WRAP4 = 0b010
    INCR4 = 0b011
    WRAP8 = 0b100
    INCR8 = 0b101
    WRAP16 = 0b110
    INCR16 = 0b111


class AHBResp(enum.IntEnum):
    OKAY = 0b00
    ERROR = 0b01
    UNKNOWN = 0b10


class AHBTrans(enum.IntEnum):
    IDLE = 0b00
    BUSY = 0b01
    NONSEQ = 0b10
    SEQ = 0b11


class AHBWrite(enum.IntEnum):
    READ = 0b0
    WRITE = 0b1
