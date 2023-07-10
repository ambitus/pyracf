import os

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class custom_build_ext(build_ext):
    def build_extensions(self):
        os.environ["_CC_CCMODE"] = "1"
        os.environ["_CXX_CCMODE"] = "1"
        os.environ["_C89_CCMODE"] = "1"
        os.environ["_CC_EXTRA_ARGS"] = "1"
        os.environ["_CXX_EXTRA_ARGS"] = "1"
        os.environ["_C89_EXTRA_ARGS"] = "1"

        build_ext.build_extensions(self)


setup(
    name="call_smo",
    version="1.0",
    ext_modules=[
        Extension(
            "call_smo",
            sources=["call_smo.c"],
            extra_compile_args=[
                "-D_XOPEN_SOURCE_EXTENDED",
                "-Wc,lp64,langlvl(EXTC99),STACKPROTECT(ALL)," + "INFO(ALL),NOOPT",
                "-qcpluscmt",
            ],
            extra_link_args=["-Wl,INFO"],
        )
    ],
    cmdclass={"build_ext": custom_build_ext},
)
