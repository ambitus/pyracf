"""PyRACF setup/build configuration."""

import os
import subprocess
from typing import List

from setuptools import setup
from setuptools.command.build_py import build_py


class Build(build_py):
    """Build irrsmo00.dll."""

    def run(self):
        subprocess.Popen("py3 setup.py", cwd = f"{os.path.dirname(__file__)}/pyracf/common")
        build_py.run(self)


def get_requirements() -> List[str]:
    """Get dependencies that must be installed with pyRACF."""
    with open("requirements.txt", "r", encoding="utf-8") as requirements_file:
        return [line.strip() for line in requirements_file.readlines()]


setup(
    name="pyRACF",
    version="1.0",
    description="Python wrapper for zEnterprise Data Compression (zEDC).",
    author="IBM",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: RACF Administration",
        "License :: IBM Internal For Now...",
        "Operating System :: z/OS",
    ],
    packages=[
        "pyracf",
        "pyracf.access",
        "pyracf.common",
        "pyracf.connection",
        "pyracf.data_set",
        "pyracf.group",
        "pyracf.resource",
        "pyracf.setropts",
        "pyracf.user",
    ],
    package_dir={"": "."},
    package_data={"pyracf.common": ["irrsmo00.c", "irrsmo00.x", "irrsmo00.dll"]},
    python_requires=">=3.9",
    license_files=("LICENSE"),
    install_requires=get_requirements(),
    cmdclass={"build_py": Build},
)
