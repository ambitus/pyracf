"""Used to drive all unit tests for pyRACF."""

import sys
import unittest

import __init__

from tests.access.test_access_debug_logging import TestAccessDebugLogging
from tests.access.test_access_request_builder import TestAccessRequestBuilder
from tests.access.test_access_result_parser import TestAccessResultParser
from tests.dataset.test_dataset_debug_logging import TestDatasetDebugLogging
from tests.dataset.test_dataset_getters import TestDatasetGetters
from tests.dataset.test_dataset_request_builder import TestDatasetRequestBuilder
from tests.dataset.test_dataset_result_parser import TestDatasetResultParser
from tests.dataset.test_dataset_setters import TestDatasetSetters
from tests.genprof.test_genprof_debug_logging import TestGenprofDebugLogging
from tests.genprof.test_genprof_getters import TestGenprofGetters
from tests.genprof.test_genprof_request_builder import TestGenprofRequestBuilder
from tests.genprof.test_genprof_result_parser import TestGenprofResultParser
from tests.genprof.test_genprof_setters import TestGenprofSetters
from tests.setropts.test_setropts_debug_logging import TestSetroptsDebugLogging
from tests.setropts.test_setropts_getters import TestSetroptsGetters
from tests.setropts.test_setropts_request_builder import TestSetroptsRequestBuilder
from tests.setropts.test_setropts_result_parser import TestSetroptsResultParser
from tests.setropts.test_setropts_setters import TestSetroptsSetters
from tests.user.test_user_debug_logging import TestUserDebugLogging
from tests.user.test_user_getters import TestUserGetters
from tests.user.test_user_request_builder import TestUserRequestBuilder
from tests.user.test_user_result_parser import TestUserResultParser
from tests.user.test_user_setters import TestUserSetters

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
        TestUserDebugLogging,
        TestGenprofResultParser,
        TestGenprofRequestBuilder,
        TestGenprofGetters,
        TestGenprofSetters,
        TestGenprofDebugLogging,
        TestDatasetResultParser,
        TestDatasetRequestBuilder,
        TestDatasetGetters,
        TestDatasetSetters,
        TestDatasetDebugLogging,
        TestAccessResultParser,
        TestAccessRequestBuilder,
        TestAccessDebugLogging,
        TestSetroptsResultParser,
        TestSetroptsRequestBuilder,
        TestSetroptsGetters,
        TestSetroptsSetters,
        TestSetroptsDebugLogging,
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
