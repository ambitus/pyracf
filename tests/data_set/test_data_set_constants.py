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
TEST_EXTRACT_DATA_SET_RESULT_BAD_ATTRIBUTE_ERROR_XML = get_sample(
    "extract_data_set_result_bad_attribute_error.xml"
)
TEST_EXTRACT_DATA_SET_RESULT_BAD_ATTRIBUTE_ERROR_DICTIONARY = get_sample(
    "extract_data_set_result_bad_attribute_error.json"
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
TEST_EXTRACT_DATA_SET_REQUEST_GENRIC_BASE_XML = get_sample(
    "extract_data_set_request_generic_base.xml"
)
TEST_EXTRACT_DATA_SET_REQUEST_GENERIC_BASE_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.*"
}
TEST_EXTRACT_DATA_SET_BASE_ONLY_TEMPLATE_TRAITS = {
    "base:audit_read": "failure",
    "base:level": 0,
    "base:owner": "eswift",
    "base:universal_access": "read",
    "base:warn_on_insufficient_access": None,
    "base:erase_data_sets_on_delete": None,
    "base:notify_userid": None,
    "base:volumes": ["usrat2"],
    "base:installation_data": None,
}

# Delete Data Set
TEST_DELETE_DATA_SET_REQUEST_XML = get_sample("delete_data_set_request.xml")

# ============================================================================
# Data Set Administration Setters Sample Data
# ============================================================================

TEST_DATA_SET_SET_UNIVERSAL_ACCESS_XML = get_sample("data_set_set_universal_access.xml")
# Audit Rules Request Samples
TEST_DATA_SET_REMOVE_ALL_AUDIT_RULES_REQUEST_XML = get_sample(
    "data_set_remove_all_audit_rules.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_attempt.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_attempt_multiple.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_attempt_all.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_attempt_none.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_access_level.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_MULT_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_access_level_multiple.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_ALL_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_access_level_all.xml"
)
TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_NONE_REQUEST_XML = get_sample(
    "data_set_alter_audit_rules_by_access_level_none.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_attempt.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_attempt_multiple.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_attempt_all.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_attempt_none.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_access_level.xml"
)
# The following Test variables break convention to avoid E501 length errors from Flake8
TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_MULT_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_access_level_multiple.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_ALL_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_access_level_all.xml"
)
TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_NONE_REQUEST_XML = get_sample(
    "data_set_overwrite_audit_rules_by_access_level_none.xml"
)


# ============================================================================
# Data Set Administration Getters Result Data
# ============================================================================

TEST_GET_AUDIT_RULES = {"success": "update", "failures": "read"}
TEST_GET_AUDIT_RULES_SINGLE = {"failures": "read"}
TEST_GET_AUDIT_RULES_WITH_ALL = {"success": "update", "all": "read"}

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
TEST_EXTRACT_DATA_SET_BASE_AS_SQUIDWRD_SUCCESS = get_sample(
    "extract_data_set_base_as_squidwrd_success.log"
)
