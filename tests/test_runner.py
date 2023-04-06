"""Used to drive all unit tests for pyRACF."""

import sys
import unittest

import __init__

from tests.user.test_user_getters import TestUserGetters
from tests.user.test_user_request_builder import TestUserRequestBuilder
from tests.user.test_user_result_parser import TestUserResultParser
from tests.user.test_user_setters import TestUserSetters

from tests.genprof.test_genprof_getters import TestGenprofGetters
from tests.genprof.test_genprof_request_builder import TestGenprofRequestBuilder
from tests.genprof.test_genprof_result_parser import TestGenprofResultParser
from tests.genprof.test_genprof_setters import TestGenprofSetters

# Resolves F401
__init__


def __test_suite() -> unittest.TestSuite:
    """Load and run each unit test class."""
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_classes = [
        TestUserResultParser,
        TestUserRequestBuilder,
        TestUserGetters,
        TestUserSetters,
        TestGenprofResultParser,
        TestGenprofRequestBuilder,
        TestGenprofGetters,
        TestGenprofSetters,
    ]
    for test_class in test_classes:
        tests = test_loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    return test_suite


def main():
    """Test runner entrypoint."""
    test_runner = unittest.TextTestRunner(verbosity=2, failfast=True, buffer=True)
    result = not test_runner.run(__test_suite()).wasSuccessful()
    sys.exit(result)


if __name__ == "__main__":
    main()
