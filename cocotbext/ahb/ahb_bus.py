#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ahb_bus.py
# License           : MIT license <Check LICENSE>
# Author            : Anderson I. da Silva (aignacio) <anderson@aignacio.com>
# Date              : 08.10.2023
# Last Modified Date: 12.11.2023

from cocotb_bus.drivers import Bus
from cocotb.handle import SimHandleBase
from typing import Any


class AHBBus(Bus):
    _signals = [
        "haddr",
        "hsize",
        "htrans",
        "hwdata",
        "hrdata",
        "hwrite",
        "hready",
        "hresp",
    ]

    _optional_signals = [
        "hburst",
        "hmastlock",
        "hprot",
        "hnonsec",
        "hexcl",
        "hmaster",
        "hexokay",
        "hsel",
        "hready_in",
    ]

    def __init__(
        self, entity: SimHandleBase = None, prefix: str = None, **kwargs: Any
    ) -> None:
        name = prefix if prefix is not None else entity._name + "_ahb_bus"

        # Handle default signals or signals overrided at an upper level
        if "signals" not in kwargs:
            kwargs["signals"] = self._signals
        else:
            entity._log.info(f"AHB ({name}) master use provided signals mapping")

        # Handle default optional_signals or optional_signals overrided at an upper level
        if "optional_signals" not in kwargs:
            kwargs["optional_signals"] = self._optional_signals
        else:
            entity._log.info(
                f"AHB ({name}) master use provided optional_signals mapping"
            )

        super().__init__(entity, prefix, **kwargs)
        self.entity = entity
        self.name = name
        self._data_width = len(self.hwdata)
        self._addr_width = len(self.haddr)

    @property
    def data_width(self):
        return self._data_width

    @property
    def addr_width(self):
        return self._addr_width

    @property
    def hsel_exist(self):
        return True if "hsel" in self._signals else False

    @property
    def hready_in_exist(self):
        return True if "hready_in" in self._signals else False

    @property
    def hburst_exist(self):
        return True if "hburst" in self._signals else False

    @classmethod
    def from_entity(cls, entity, **kwargs):
        return cls(entity, **kwargs)

    @classmethod
    def from_prefix(cls, entity, prefix, **kwargs):
        return cls(entity, prefix, **kwargs)
