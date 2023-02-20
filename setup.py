import os
from subprocess import run

from setuptools import setup
from setuptools.command.build_py import build_py
from typing import List

class Build(build_py):
    def run(self):
        os.chdir(f"{os.path.dirname(__file__)}/pyracf/common")
        command = (
            "pwd && c89 -c -D_XOPEN_SOURCE_EXTENDED "
            + "-Wc,lp64,langlvl\(extended\),STACKPROTECT\(ALL\) "
            + "-I../../safCommon -I irrsmo00.so irrsmo00.c "
            + "&& c89 -Wl,\"DLL,LP64,XPLINK\" -o irrsmo00.dll irrsmo00.o"
        )
        run(
            command,
            shell=True,
            text=True,
            check=True)
        os.chdir(f"{os.path.dirname(__file__)}")
        build_py.run(self)


def get_requirements() -> List[str]:
    with open("requirements.txt", "r") as requirements_file:
        return [line.strip() for line in requirements_file.readlines()]


setup(
    name="pyRACF",
    version=f"1.0",
    description="Python wrapper for zEnterprise Data Compression (zEDC).",
    author="IBM",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console" "Intended Audience :: Developers",
        "Topic :: RACF Administration",
        "License :: IBM Internal For Now...",
        "Operating System :: z/OS",
    ],
    packages=[
        'pyracf.access', 
        'pyracf.common',
        'pyracf.dataset',
        'pyracf.genprof',
        'pyracf.setropts',
        'pyracf.user',
    ],
    package_dir={'': '.'},
    package_data={'pyracf.common': ['zEDC_gzip.c','zEDC_gzip.so', 'zEDC_gzip.x']},
    python_requires=">=3.8",
    license_files=("LICENSE"),
    install_requires=get_requirements(),
    cmdclass = {
        'build_py': Build
    },
)