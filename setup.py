import codecs
import os

from setuptools import find_namespace_packages, find_packages, setup

from cocotbext.ahb.version import __version__

DESCRIPTION = "CocotbExt AHB Bus VIP"
LONG_DESCRIPTION = "AHB VIP for Bus interface"

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Setting up
setup(
    name="cocotbext_ahb",
    packages=find_namespace_packages(include=["cocotbext.*"]),
    version=__version__,
    author="aignacio (Anderson Ignacio)",
    author_email="<anderson@aignacio.com>",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/aignacio/cocotbext-ahb",
    project_urls={
        "Bug Tracker": "https://github.com/aignacio/cocotbext-ahb/issues",
        "Source Code": "https://github.com/aignacio/cocotbext-ahb",
    },
    include_package_data=False,
    python_requires=">=3.6",
    install_requires=["cocotb>=1.8", "cocotb-bus"],
    extras_require={
        "test": [
            "pytest",
            "cocotb>=2.0.0",  # We require >=2.0.0 because of new testing features only avail at this version and onwards
        ],
    },
    keywords=["soc", "vip", "hdl", "verilog", "systemverilog", "ahb"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: cocotb",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
)
