"""
Ensure that test classes can import pyRACF classes.
"""

import os
import platform
import sys

if os.getcwd()[-5:] != "tests":
    os.chdir("tests")

sys.path.append("..")

# Allow unit testing to be done on z/OS.
if platform.system() == "OS/390":
    platform.system = lambda: ""
