"""PyRACF setup/build configuration."""
import os

from setuptools import Extension, setup

setup_args = dict(
    ext_modules = [
        Extension(
            "cpyracf",
            sources=["pyracf/common/irrsmo00.c"],
            extra_compile_args=[
                "-D_XOPEN_SOURCE_EXTENDED",
                "-Wc,lp64,langlvl(EXTC99),STACKPROTECT(ALL),",
                "-qcpluscmt",
            ],
            extra_link_args=["-Wl,INFO"],
        )
    ]   
)

def main():
    """Entrypoint for pyRACF package setup."""
    os.environ["_CC_CCMODE"] = "1"
    os.environ["_CXX_CCMODE"] = "1"
    os.environ["_C89_CCMODE"] = "1"
    os.environ["_CC_EXTRA_ARGS"] = "1"
    os.environ["_CXX_EXTRA_ARGS"] = "1"
    os.environ["_C89_EXTRA_ARGS"] = "1"
    os.environ["CC"] = "xlc"
    os.environ["CXX"] = "xlc++"
    setup(**setup_args)


if __name__ == "__main__":
    main()
