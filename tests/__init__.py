"""
Ensure that test classes can import pyRACF classes.
"""

import os
import sys

if os.getcwd()[-5:] != "tests":
    os.chdir("tests")

sys.path.append("..")
