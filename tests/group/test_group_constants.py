"""
Sample data for testing Group Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "group")


# ============================================================================
# Group Administration Result Sample Data
# ============================================================================

# Add Group
TEST_ADD_GROUP_RESULT_SUCCESS_XML = get_sample("add_group_result_success.xml")
TEST_ADD_GROUP_RESULT_SUCCESS_DICTIONARY = get_sample("add_group_result_success.json")
TEST_ADD_GROUP_RESULT_ERROR_XML = get_sample("add_group_result_error.xml")
TEST_ADD_GROUP_RESULT_ERROR_DICTIONARY = get_sample("add_group_result_error.json")

# Alter Group
TEST_ALTER_GROUP_RESULT_SUCCESS_XML = get_sample("alter_group_result_success.xml")
TEST_ALTER_GROUP_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_group_result_success.json"
)
TEST_ALTER_GROUP_RESULT_ERROR_XML = get_sample("alter_group_result_error.xml")
TEST_ALTER_GROUP_RESULT_ERROR_DICTIONARY = get_sample("alter_group_result_error.json")

# Extract Group
TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML = get_sample(
    "extract_group_result_base_omvs_success.xml"
)
TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_DICTIONARY = get_sample(
    "extract_group_result_base_omvs_success.json"
)
TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML = get_sample(
    "extract_group_result_base_omvs_error.xml"
)
TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_DICTIONARY = get_sample(
    "extract_group_result_base_omvs_error.json"
)
TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML = get_sample(
    "extract_group_result_base_only_success.xml"
)
TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_JSON = get_sample(
    "extract_group_result_base_only_success.json"
)
TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_ERROR_XML = get_sample(
    "extract_group_result_base_only_error.xml"
)
TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_ERROR_JSON = get_sample(
    "extract_group_result_base_only_error.json"
)
TEST_EXTRACT_GROUP_RESULT_BAD_ATTRIBUTE_ERROR_XML = get_sample(
    "extract_group_result_bad_attribute_error.xml"
)
TEST_EXTRACT_GROUP_RESULT_BAD_ATTRIBUTE_ERROR_DICTIONARY = get_sample(
    "extract_group_result_bad_attribute_error.json"
)

# Delete Group
TEST_DELETE_GROUP_RESULT_SUCCESS_XML = get_sample("delete_group_result_success.xml")
TEST_DELETE_GROUP_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_group_result_success.json"
)
TEST_DELETE_GROUP_RESULT_ERROR_XML = get_sample("delete_group_result_error.xml")
TEST_DELETE_GROUP_RESULT_ERROR_DICTIONARY = get_sample("delete_group_result_error.json")

# ============================================================================
# Group Administration Request Sample Data
# ============================================================================

# Add Group
TEST_ADD_GROUP_REQUEST_XML = get_sample("add_group_request.xml")
TEST_ADD_GROUP_REQUEST_TRAITS = {
    "omvs:gid": "6667",
}

# Alter Group
TEST_ALTER_GROUP_REQUEST_XML = get_sample("alter_group_request.xml")
TEST_ALTER_GROUP_REQUEST_TRAITS = {"omvs:gid": "1234567"}
TEST_ALTER_GROUP_REQUEST_ERROR_TRAITS = {"omvs:gid": "3000000000"}

# Extract Group
TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_XML = get_sample(
    "extract_group_request_base_omvs.xml"
)

# Delete Group
TEST_DELETE_GROUP_REQUEST_XML = get_sample("delete_group_request.xml")

# ============================================================================
# Group Administration Setters Sample Data
# ============================================================================

TEST_GROUP_SET_OMVS_GID_XML = get_sample("group_set_omvs_gid.xml")
TEST_GROUP_SET_OVM_GID_XML = get_sample("group_set_ovm_gid.xml")


# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_GROUP_SUCCESS_LOG = get_sample("alter_group_success.log")
TEST_ALTER_GROUP_ERROR_LOG = get_sample("alter_group_error.log")

TEST_EXTRACT_GROUP_BASE_OMVS_SUCCESS_LOG = get_sample(
    "extract_group_base_omvs_success.log"
)
TEST_EXTRACT_GROUP_BASE_OMVS_ERROR_LOG = get_sample("extract_group_base_omvs_error.log")
