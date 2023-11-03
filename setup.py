from setuptools import setup, find_packages, find_namespace_packages
import codecs
import os
from cocotbext.ahb.version import __version__

DESCRIPTION = "CocotbExt AHB Bus VIP"
LONG_DESCRIPTION = "AHB VIP for Bus interface"

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Setting up
setup(
    name="cocotbext-ahb",
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
    install_requires=["cocotb>=1.8.0", "cocotb-bus>=0.2.1", "cocotb-test>=0.2.4"],
    extras_require={
        "test": [
            "pytest",
            "cocotb-test",
        ],
    },
    keywords=["soc", "vip", "hdl", "verilog", "systemverilog", "ahb"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
)
