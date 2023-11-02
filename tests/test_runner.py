"""Used to drive all unit tests for pyRACF."""

import sys
import unittest

import __init__

from tests.access.test_access_debug_logging import TestAccessDebugLogging
from tests.access.test_access_request_builder import TestAccessRequestBuilder
from tests.access.test_access_result_parser import TestAccessResultParser
from tests.common.test_logger import TestLogger
from tests.connection.test_connection_debug_logging import TestConnectionDebugLogging
from tests.connection.test_connection_request_builder import (
    TestConnectionRequestBuilder,
)
from tests.connection.test_connection_result_parser import TestConnectionResultParser
from tests.connection.test_connection_setters import TestConnectionSetters
from tests.data_set.test_data_set_debug_logging import TestDataSetDebugLogging
from tests.data_set.test_data_set_getters import TestDataSetGetters
from tests.data_set.test_data_set_request_builder import TestDataSetRequestBuilder
from tests.data_set.test_data_set_result_parser import TestDataSetResultParser
from tests.data_set.test_data_set_setters import TestDataSetSetters
from tests.group.test_group_debug_logging import TestGroupDebugLogging
from tests.group.test_group_getters import TestGroupGetters
from tests.group.test_group_request_builder import TestGroupRequestBuilder
from tests.group.test_group_result_parser import TestGroupResultParser
from tests.group.test_group_setters import TestGroupSetters
from tests.resource.test_resource_debug_logging import TestResourceDebugLogging
from tests.resource.test_resource_getters import TestResourceGetters
from tests.resource.test_resource_request_builder import TestResourceRequestBuilder
from tests.resource.test_resource_result_parser import TestResourceResultParser
from tests.resource.test_resource_setters import TestResourceSetters
from tests.resource.test_resource_sub_function_extracts import (
    TestResourceSubFunctionExtracts,
)
from tests.resource.test_resource_sub_function_requests import (
    TestResourceSubFunctionRequests,
)
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
        TestAccessResultParser,
        TestAccessRequestBuilder,
        TestAccessDebugLogging,
        TestLogger,
        TestConnectionResultParser,
        TestConnectionRequestBuilder,
        TestConnectionSetters,
        TestConnectionDebugLogging,
        TestDataSetResultParser,
        TestDataSetRequestBuilder,
        TestDataSetGetters,
        TestDataSetSetters,
        TestDataSetDebugLogging,
        TestResourceResultParser,
        TestResourceRequestBuilder,
        TestResourceGetters,
        TestResourceSetters,
        TestResourceDebugLogging,
        TestResourceSubFunctionRequests,
        TestResourceSubFunctionExtracts,
        TestGroupResultParser,
        TestGroupRequestBuilder,
        TestGroupGetters,
        TestGroupSetters,
        TestGroupDebugLogging,
        TestSetroptsResultParser,
        TestSetroptsRequestBuilder,
        TestSetroptsGetters,
        TestSetroptsSetters,
        TestSetroptsDebugLogging,
        TestUserResultParser,
        TestUserRequestBuilder,
        TestUserGetters,
        TestUserSetters,
        TestUserDebugLogging,
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
