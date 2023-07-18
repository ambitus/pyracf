"""PyRACF setup/build configuration."""
import subprocess
from typing import List

from setuptools import setup
from setuptools.command.install import install


class InstallSMOPackage(install):
    """Install irrsmo00 python package"""

    def run(self):
        command = "python -m pip install ./pyracf/common"
        subprocess.run(command, shell=True, text=True, check=True)
        install.run(self)


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
    package_data={"pyracf.common": ["call_smo.c", "irrsmo00.x", "irrsmo00.dll"]},
    python_requires=">=3.9",
    license_files=("LICENSE"),
    install_requires=get_requirements(),
    cmdclass={"install": InstallSMOPackage},
)
