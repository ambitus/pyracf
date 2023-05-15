"""
Sample data for testing General Resource Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "genprof")


# ============================================================================
# Genprof Administration Result Sample Data
# ============================================================================

# Add Genprof
TEST_ADD_GENPROF_RESULT_SUCCESS_XML = get_sample("add_genprof_result_success.xml")
TEST_ADD_GENPROF_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_genprof_result_success.json"
)
TEST_ADD_GENPROF_RESULT_ERROR_XML = get_sample("add_genprof_result_error.xml")
TEST_ADD_GENPROF_RESULT_ERROR_DICTIONARY = get_sample("add_genprof_result_error.json")

# Alter Genprof
TEST_ALTER_GENPROF_RESULT_SUCCESS_XML = get_sample("alter_genprof_result_success.xml")
TEST_ALTER_GENPROF_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_genprof_result_success.json"
)
TEST_ALTER_GENPROF_RESULT_ERROR_XML = get_sample("alter_genprof_result_error.xml")
TEST_ALTER_GENPROF_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_genprof_result_error.json"
)

# Extract Genprof
TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML = get_sample(
    "extract_genprof_result_base_success.xml"
)
TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_genprof_result_base_success.json"
)
TEST_EXTRACT_GENPROF_RESULT_MULTI_BASE_SUCCESS_XML = get_sample(
    "extract_genprof_result_multi_base_success.xml"
)
TEST_EXTRACT_GENPROF_RESULT_MULTI_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_genprof_result_multi_base_success.json"
)
TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_XML = get_sample(
    "extract_genprof_result_base_error.xml"
)
TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_DICTIONARY = get_sample(
    "extract_genprof_result_base_error.json"
)

# Delete Genprof
TEST_DELETE_GENPROF_RESULT_SUCCESS_XML = get_sample("delete_genprof_result_success.xml")
TEST_DELETE_GENPROF_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_genprof_result_success.json"
)
TEST_DELETE_GENPROF_RESULT_ERROR_XML = get_sample("delete_genprof_result_error.xml")
TEST_DELETE_GENPROF_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_genprof_result_error.json"
)

# ============================================================================
# Genprof Administration Request Sample Data
# ============================================================================

# Add Genprof
TEST_ADD_GENPROF_REQUEST_XML = get_sample("add_genprof_request.xml")
TEST_ADD_GENPROF_REQUEST_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "uacc": "None",
    "owner": "eswift",
}

# Alter Genprof
TEST_ALTER_GENPROF_REQUEST_XML = get_sample("alter_genprof_request.xml")
TEST_ALTER_GENPROF_REQUEST_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "uacc": "Read",
    "owner": "eswift",
}
TEST_ALTER_GENPROF_REQUEST_ERROR_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
    "uacc": "ALL",
    "owner": "eswift",
}

# Extract Genprof
TEST_EXTRACT_GENPROF_REQUEST_BASE_XML = get_sample("extract_genprof_request_base.xml")
TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST",
}
TEST_EXTRACT_GENPROF_REQUEST_MULTI_BASE_TRAITS = {
    "resourcename": "*",
    "classname": "XFACILIT",
}

# Delete Genprof
TEST_DELETE_GENPROF_REQUEST_XML = get_sample("delete_genprof_request.xml")

# ============================================================================
# Genprof Administration Setters Sample Data
# ============================================================================

TEST_GENPROF_SET_UACC_XML = get_sample("genprof_set_uacc.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ADD_GENPROF_SUCCESS_LOG = get_sample("add_genprof_success.log")
TEST_ADD_GENPROF_ERROR_LOG = get_sample("add_genprof_error.log")

TEST_EXTRACT_GENPROF_BASE_SUCCESS_LOG = get_sample(
    "extract_genprof_base_success.log"
)
TEST_EXTRACT_GENPROF_BASE_ERROR_LOG = get_sample("extract_genprof_base_error.log")
