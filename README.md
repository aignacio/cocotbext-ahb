# Cocotb AHB bus driver

[![Lint](https://github.com/aignacio/cocotbext-ahb/actions/workflows/lint.yaml/badge.svg)](https://github.com/aignacio/cocotbext-ahb/actions/workflows/lint.yaml) 
[![Regression Tests](https://github.com/aignacio/cocotbext-ahb/actions/workflows/test.yaml/badge.svg)](https://github.com/aignacio/cocotbext-ahb/actions/workflows/test.yaml) [![codecov](https://codecov.io/gh/aignacio/cocotbext-ahb/graph/badge.svg?token=RHYCK6SSCC)](https://codecov.io/gh/aignacio/cocotbext-ahb) 
[![Downloads](https://static.pepy.tech/badge/cocotbext-ahb)](https://pepy.tech/project/cocotbext-ahb)

## Introduction

This repository contains AHB drivers (AHB and AHB Lite) and a monitor for [cocotb](https://github.com/cocotb/cocotb).

## Installation

Installation from pip (release version, stable):
```bash
$ pip install cocotbext-ahb
```
Installation for active development:
```bash
$ git clone https://github.com/aignacio/cocotbext-ahb
```
The repository contains a small script that starts a container fetched from Docker Hub, equipped with all the required development tools.
```bash
$ cd cocotbext-ahb/
$ ./ship.sh
```
Once the container is up and running, to run the tests through [nox](https://nox.thea.codes/en/stable/) and [pytest](https://docs.pytest.org/), run the following:
```bash
$ nox -l # See the available build options
$ nox -s run-3.xx # Replace xx by a python version you want to test
```
The command above will take some time to complete (depends on your machine cfg) because it will run all the tests and its variants, generating waveforms in each `run_dir/*` folder. If you want to run a specific test, to the following:
```bash
$ nox -s run-3.10 -- -k "test_ahb_monitor_slave" # Runs on python 3.10, the test_ahb_monitor_slave
```
For the list of test, please check the [`tests/`](tests/) directory.

## Documentation and usage examples

The AHB extension is composed by master and slaves, essentially, the following available classes are:

* **AHB Master** - WIP for burst support, base class AHB Lite Master
* **AHB Lite Master** - Perform AHB transactions in non-/pipeline mode
* **AHB Slave** - WIP for burst support, base class AHB Lite Slave
* **AHB Lite Slave** - Support any type of AHB transaction but burst with back-pressure option and configurable default value 

All the different master/slaves and also the monitor requires an **AHBBus** object to be passed to their constructors. This AHBBus defines the pin interface with the dut, some IOs are mandatory but others are optional. In order to create an AHBBus object, here are the two ways.

With a prefix:
```python
# In case your DUT has some prefix for the AHB I/F
# For instance if all AHB signals are following this convention:
# - slave_haddr
# - slave_hsel
# - ...
AHBBus.from_prefix(dut, "slave")
```

Without a prefix:
```python
# In case your DUT has no prefix for the AHB I/F
# For instance if all AHB signals are following this convention:
# - haddr
# - hsel
# - ...
AHBBus.from_entity(dut)
```

For reference, down below is the class header of AHB Bus. More arguments cani also be passed as this extends from cocotb-bus base class.
```python
class AHBBus(Bus):
    _signals = ["haddr", "hsize", "htrans", "hwdata",
                "hrdata", "hwrite", "hready", "hresp"]

    _optional_signals = ["hburst", "hmastlock", "hprot", "hnonsec",
                         "hexcl", "hmaster", "hexokay", "hsel", "hready_in"]
```

### Mandatory vs optional AHB signals

1. AHB Master signals

#### Mandatory:

* haddr - Indicates AHB txn address 
* hsize - Indicates AHB txn size
* htrans - Indicates AHB txn type
* hwdata - Indicates AHB data to be written
* hwrite - Indicates type of AHB txn

#### Optional

* hburst
* hmastlock
* hprot
* hnonsec
* hexcl
* hmaster
* hexokay
* hsel 
* hready_in

2. AHB Slave signals 

#### Mandatory:

* hresp - Indicates AHB txn response type
* hrdata - Indicates AHB txn read data
* hready - Indicates AHB slave availability

The basic example of its usage is demonstrated below within the tests that are available.
