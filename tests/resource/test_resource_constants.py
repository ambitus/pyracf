"""
Sample data for testing General Resource Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "resource")


# ============================================================================
# Resource Administration Result Sample Data
# ============================================================================

# Add Resource
TEST_ADD_RESOURCE_RESULT_SUCCESS_XML = get_sample("add_resource_result_success.xml")
TEST_ADD_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_resource_result_success.json"
)
TEST_ADD_RESOURCE_RESULT_ERROR_XML = get_sample("add_resource_result_error.xml")
TEST_ADD_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample("add_resource_result_error.json")

# Alter Resource
TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML = get_sample("alter_resource_result_success.xml")
TEST_ALTER_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_resource_result_success.json"
)
TEST_ALTER_RESOURCE_RESULT_ERROR_XML = get_sample("alter_resource_result_error.xml")
TEST_ALTER_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_resource_result_error.json"
)

# Extract Resource
TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML = get_sample(
    "extract_resource_result_base_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_resource_result_base_success.json"
)
TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_XML = get_sample(
    "extract_resource_result_multi_base_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_resource_result_multi_base_success.json"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML = get_sample(
    "extract_resource_result_base_error.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_DICTIONARY = get_sample(
    "extract_resource_result_base_error.json"
)
TEST_EXTRACT_RESOURCE_RESULT_INVALID_CLASS_ERROR_XML = get_sample(
    "extract_resource_result_invalid_class_error.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_INVALID_CLASS_ERROR_DICTIONARY = get_sample(
    "extract_resource_result_invalid_class_error.json"
)

# Delete Resource
TEST_DELETE_RESOURCE_RESULT_SUCCESS_XML = get_sample(
    "delete_resource_result_success.xml"
)
TEST_DELETE_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_resource_result_success.json"
)
TEST_DELETE_RESOURCE_RESULT_ERROR_XML = get_sample("delete_resource_result_error.xml")
TEST_DELETE_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_resource_result_error.json"
)

# ============================================================================
# Resource Administration Request Sample Data
# ============================================================================

# Add Resource
TEST_ADD_RESOURCE_REQUEST_XML = get_sample("add_resource_request.xml")
TEST_ADD_RESOURCE_REQUEST_TRAITS = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}
TEST_ADD_RESOURCE_REQUEST_ERROR_TRAITS = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

# Alter Resource
TEST_ALTER_RESOURCE_REQUEST_XML = get_sample("alter_resource_request.xml")
TEST_ALTER_RESOURCE_REQUEST_TRAITS = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}
TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS = {
    "base:universal_access": "ALL",
    "base:owner": "eswift",
}

# Extract Resource
TEST_EXTRACT_RESOURCE_REQUEST_BASE_XML = get_sample("extract_resource_request_base.xml")

# Delete Resource
TEST_DELETE_RESOURCE_REQUEST_XML = get_sample("delete_resource_request.xml")

# ============================================================================
# Resource Administration Setters Sample Data
# ============================================================================

TEST_RESOURCE_SET_UNIVERSAL_ACCESS_XML = get_sample("resource_set_universal_access.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_RESOURCE_SUCCESS_LOG = get_sample("alter_resource_success.log")
TEST_ALTER_RESOURCE_ERROR_LOG = get_sample("alter_resource_error.log")

TEST_EXTRACT_RESOURCE_BASE_SUCCESS_LOG = get_sample("extract_resource_base_success.log")
TEST_EXTRACT_RESOURCE_BASE_ERROR_LOG = get_sample("extract_resource_base_error.log")
