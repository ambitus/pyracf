"""
Sample data for testing Data Set Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "data_set")


# ============================================================================
# Data Set Administration Result Sample Data
# ============================================================================

# Add Data Set
TEST_ADD_DATA_SET_RESULT_SUCCESS_XML = get_sample("add_data_set_result_success.xml")
TEST_ADD_DATA_SET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_data_set_result_success.json"
)
TEST_ADD_DATA_SET_RESULT_ERROR_XML = get_sample("add_data_set_result_error.xml")
TEST_ADD_DATA_SET_RESULT_ERROR_DICTIONARY = get_sample("add_data_set_result_error.json")
TEST_ADD_DATA_SET_RESULT_GENERIC_SUCCESS_XML = get_sample(
    "add_data_set_result_generic_success.xml"
)
TEST_ADD_DATA_SET_RESULT_GENERIC_SUCCESS_DICTIONARY = get_sample(
    "add_data_set_result_generic_success.json"
)

# Alter Data Set
TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML = get_sample("alter_data_set_result_success.xml")
TEST_ALTER_DATA_SET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_data_set_result_success.json"
)
TEST_ALTER_DATA_SET_RESULT_ERROR_XML = get_sample("alter_data_set_result_error.xml")
TEST_ALTER_DATA_SET_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_data_set_result_error.json"
)

# Extract Data Set
TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML = get_sample(
    "extract_data_set_result_base_only_success.xml"
)
TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_DICTIONARY = get_sample(
    "extract_data_set_result_base_only_success.json"
)
TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_XML = get_sample(
    "extract_data_set_result_generic_base_only_success.xml"
)
TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_DICTIONARY = get_sample(
    "extract_data_set_result_generic_base_only_success.json"
)
TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML = get_sample(
    "extract_data_set_result_base_only_error.xml"
)
TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_DICTIONARY = get_sample(
    "extract_data_set_result_base_only_error.json"
)
TEST_EXTRACT_DATA_SET_RESULT_INVALID_ATTRIBUTE_ERROR_XML = get_sample(
    "extract_data_set_result_invalid_attribute_error.xml"
)
TEST_EXTRACT_DATA_SET_RESULT_INVALID_ATTRIBUTE_ERROR_DICTIONARY = get_sample(
    "extract_data_set_result_invalid_attribute_error.json"
)

# Delete Data Set
TEST_DELETE_DATA_SET_RESULT_SUCCESS_XML = get_sample(
    "delete_data_set_result_success.xml"
)
TEST_DELETE_DATA_SET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_data_set_result_success.json"
)
TEST_DELETE_DATA_SET_RESULT_ERROR_XML = get_sample("delete_data_set_result_error.xml")
TEST_DELETE_DATA_SET_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_data_set_result_error.json"
)

# ============================================================================
# Data Set Administration Request Sample Data
# ============================================================================

# Add Data Set
TEST_ADD_DATA_SET_REQUEST_XML = get_sample("add_data_set_request.xml")
TEST_ADD_DATA_SET_REQUEST_TRAITS = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

# Add Data Set Generic
TEST_ADD_DATA_SET_REQUEST_GENERIC_XML = get_sample("add_data_set_request_generic.xml")

# Alter Data Set
TEST_ALTER_DATA_SET_REQUEST_XML = get_sample("alter_data_set_request.xml")
TEST_ALTER_DATA_SET_REQUEST_TRAITS = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}

# Extract Data Set
TEST_EXTRACT_DATA_SET_REQUEST_BASE_XML = get_sample("extract_data_set_request_base.xml")
TEST_EXTRACT_DATA_SET_REQUEST_BASE_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.P3020470"
}
# Extract Data Set
TEST_EXTRACT_DATA_SET_REQUEST_GENRIC_BASE_XML = get_sample(
    "extract_data_set_request_generic_base.xml"
)
TEST_EXTRACT_DATA_SET_REQUEST_GENERIC_BASE_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.*"
}

# Delete Data Set
TEST_DELETE_DATA_SET_REQUEST_XML = get_sample("delete_data_set_request.xml")

# ============================================================================
# Data Set Administration Setters Sample Data
# ============================================================================

TEST_DATA_SET_SET_UNIVERSAL_ACCESS_XML = get_sample("data_set_set_universal_access.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_DATA_SET_SUCCESS_LOG = get_sample("alter_data_set_success.log")
TEST_ALTER_DATA_SET_ERROR_LOG = get_sample("alter_data_set_error.log")

TEST_EXTRACT_DATA_SET_BASE_ONLY_SUCCESS_LOG = get_sample(
    "extract_data_set_base_only_success.log"
)
TEST_EXTRACT_DATA_SET_BASE_ONLY_ERROR_LOG = get_sample(
    "extract_data_set_base_only_error.log"
)
