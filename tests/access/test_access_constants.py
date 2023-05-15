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

# Add Access
TEST_ADD_ACCESS_RESULT_SUCCESS_XML = get_sample("add_access_result_success.xml")
TEST_ADD_ACCESS_RESULT_SUCCESS_DICTIONARY = get_sample("add_access_result_success.json")
TEST_ADD_ACCESS_RESULT_ERROR_XML = get_sample("add_access_result_error.xml")
TEST_ADD_ACCESS_RESULT_ERROR_DICTIONARY = get_sample("add_access_result_error.json")

# Alter Access
TEST_ALTER_ACCESS_RESULT_SUCCESS_XML = get_sample("alter_access_result_success.xml")
TEST_ALTER_ACCESS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_access_result_success.json"
)
TEST_ALTER_ACCESS_RESULT_ERROR_XML = get_sample("alter_access_result_error.xml")
TEST_ALTER_ACCESS_RESULT_ERROR_DICTIONARY = get_sample("alter_access_result_error.json")


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

# Add Access
TEST_ADD_ACCESS_REQUEST_XML = get_sample("add_access_request.xml")
TEST_ADD_ACCESS_REQUEST_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "access": "READ",
    "id": "ESWIFT",
}

# Alter Access
TEST_ALTER_ACCESS_REQUEST_XML = get_sample("alter_access_request.xml")
TEST_ALTER_ACCESS_REQUEST_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "access": "NONE",
    "id": "ESWIFT",
}
TEST_ALTER_ACCESS_REQUEST_ERROR_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "access": "NONE",
    "id": "MCGINLEY",
}
# Delete Access
TEST_DELETE_ACCESS_REQUEST_XML = get_sample("delete_access_request.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ADD_ACCESS_SUCCESS_LOG = get_sample("add_access_success.log")
TEST_ADD_ACCESS_ERROR_LOG = get_sample("add_access_error.log")

