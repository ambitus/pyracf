"""
Sample data for testing Access Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "access")


# ============================================================================
# Access Administration Result Sample Data
# ============================================================================

# Alter Access
TEST_PERMIT_ACCESS_RESULT_SUCCESS_XML = get_sample("permit_access_result_success.xml")
TEST_PERMIT_ACCESS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "permit_access_result_success.json"
)
TEST_PERMIT_ACCESS_RESULT_ERROR_XML = get_sample("permit_access_result_error.xml")
TEST_PERMIT_ACCESS_RESULT_ERROR_DICTIONARY = get_sample(
    "permit_access_result_error.json"
)


# Delete Access
TEST_DELETE_ACCESS_RESULT_SUCCESS_XML = get_sample("delete_access_result_success.xml")
TEST_DELETE_ACCESS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_access_result_success.json"
)
TEST_DELETE_ACCESS_RESULT_ERROR_XML = get_sample("delete_access_result_error.xml")
TEST_DELETE_ACCESS_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_access_result_error.json"
)

# ============================================================================
# Access Administration Request Sample Data
# ============================================================================

# Alter Access
TEST_PERMIT_ACCESS_REQUEST_XML = get_sample("permit_access_request.xml")

# Delete Access
TEST_DELETE_ACCESS_REQUEST_XML = get_sample("delete_access_request.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_PERMIT_ACCESS_SUCCESS_LOG = get_sample("permit_access_success.log")
TEST_PERMIT_ACCESS_ERROR_LOG = get_sample("permit_access_error.log")
