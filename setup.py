"""Build python extension for pyRACF."""
import os

from setuptools import Extension, setup


def main():
    """Entrypoint for pyRACF python extension build process."""
    setup_args = {
        "ext_modules": [
            Extension(
                "cpyracf",
                sources=["pyracf/common/irrsmo00.c"],
                extra_compile_args=[
                    "-D_XOPEN_SOURCE_EXTENDED",
                    "-Wc,lp64,langlvl(EXTC99),STACKPROTECT(ALL),",
                    "-qcpluscmt",
                ]
            )
        ]
    }
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
