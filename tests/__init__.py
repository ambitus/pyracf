"""
Ensure that test classes can import pyRACF classes.
"""

import os
import sys

if os.getcwd()[-6:] == "pyRACF":
    os.chdir("tests")

sys.path.append("..")
