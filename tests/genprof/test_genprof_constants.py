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
TEST_ADD_GENPROF_RESULT_SUCCESS_DICTIONARY = get_sample("add_genprof_result_success.json")
TEST_ADD_GENPROF_RESULT_ERROR_XML = get_sample("add_genprof_result_error.xml")
TEST_ADD_GENPROF_RESULT_ERROR_DICTIONARY = get_sample("add_genprof_result_error.json")

# Alter Genprof
TEST_ALTER_GENPROF_RESULT_SUCCESS_XML = get_sample("alter_genprof_result_success.xml")
TEST_ALTER_GENPROF_RESULT_SUCCESS_DICTIONARY = get_sample("alter_genprof_result_success.json")
TEST_ALTER_GENPROF_RESULT_ERROR_XML = get_sample("alter_genprof_result_error.xml")
TEST_ALTER_GENPROF_RESULT_ERROR_DICTIONARY = get_sample("alter_genprof_result_error.json")

# Extract Genprof
TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML = get_sample(
    "extract_genprof_result_base_success.xml"
)
TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_genprof_result_base_success.json"
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
TEST_DELETE_GENPROF_RESULT_ERROR_DICTIONARY = get_sample("delete_genprof_result_error.json")

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

# Extract Genprof
TEST_EXTRACT_GENPROF_REQUEST_BASE_OMVS_XML = get_sample(
    "extract_genprof_request_base.xml"
)
TEST_EXTRACT_GENPROF_REQUEST_BASE_OMVS_TRAITS = {
    "resourcename": "TESTING",
    "classname": "ELIJTEST"
}

# Delete Genprof
TEST_DELETE_GENPROF_REQUEST_XML = get_sample("delete_genprof_request.xml")

# ============================================================================
# Genprof Administration Setters Sample Data
# ============================================================================

TEST_GENPROF_SET_UACC_XML = get_sample("genprof_set_uacc.xml")

