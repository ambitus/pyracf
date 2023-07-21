"""PyRACF setup/build configuration."""
import os
from typing import List

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CustomBuildExt(build_ext):
    """Environment staging to build pyracf_call_irrsmo00 extension"""

    def build_extensions(self):
        os.environ["_CC_CCMODE"] = "1"
        os.environ["_CXX_CCMODE"] = "1"
        os.environ["_C89_CCMODE"] = "1"
        os.environ["_CC_EXTRA_ARGS"] = "1"
        os.environ["_CXX_EXTRA_ARGS"] = "1"
        os.environ["_C89_EXTRA_ARGS"] = "1"

        build_ext.build_extensions(self)


def get_requirements() -> List[str]:
    """Get dependencies that must be installed with pyRACF."""
    with open("requirements.txt", "r", encoding="utf-8") as requirements_file:
        return [line.strip() for line in requirements_file.readlines()]


def main():
    """Main function for Setup of Pyracf module and inline commands"""
    os.environ["CC"] = "xlc"
    os.environ["CXX"] = "xlc++"

    setup(
        name="pyRACF",
        version="1.0",
        description="Python interface to RACF using RACF Callable Service IRRSMO00",
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
        ext_modules=[
            Extension(
                "pyracf_call_irrsmo00",
                sources=["pyracf/common/pyracf_call_irrsmo00.c"],
                extra_compile_args=[
                    "-D_XOPEN_SOURCE_EXTENDED",
                    "-Wc,lp64,langlvl(EXTC99),STACKPROTECT(ALL),",
                    "-qcpluscmt",
                ],
                extra_link_args=["-Wl,INFO"],
            )
        ],
        python_requires=">=3.9",
        license_files=("LICENSE"),
        install_requires=get_requirements(),
        cmdclass={"build_ext": CustomBuildExt},
    )


if __name__ == "__main__":
    main()
