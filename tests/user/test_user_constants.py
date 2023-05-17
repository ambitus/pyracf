"""
Sample data for testing User Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "user")


# ============================================================================
# User Administration Result Sample Data
# ============================================================================

# Add User
TEST_ADD_USER_RESULT_SUCCESS_XML = get_sample("add_user_result_success.xml")
TEST_ADD_USER_RESULT_SUCCESS_DICTIONARY = get_sample("add_user_result_success.json")
TEST_ADD_USER_RESULT_ERROR_XML = get_sample("add_user_result_error.xml")
TEST_ADD_USER_RESULT_ERROR_DICTIONARY = get_sample("add_user_result_error.json")

# Alter User
TEST_ALTER_USER_RESULT_SUCCESS_XML = get_sample("alter_user_result_success.xml")
TEST_ALTER_USER_RESULT_SUCCESS_DICTIONARY = get_sample("alter_user_result_success.json")
TEST_ALTER_USER_RESULT_ERROR_XML = get_sample("alter_user_result_error.xml")
TEST_ALTER_USER_RESULT_ERROR_DICTIONARY = get_sample("alter_user_result_error.json")

# Extract User
TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML = get_sample(
    "extract_user_result_base_omvs_success.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_DICTIONARY = get_sample(
    "extract_user_result_base_omvs_success.json"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML = get_sample(
    "extract_user_result_base_omvs_error.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_DICTIONARY = get_sample(
    "extract_user_result_base_omvs_error.json"
)
TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML = get_sample(
    "extract_user_result_base_only_no_omvs_success.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_JSON = get_sample(
    "extract_user_result_base_only_no_omvs_success.json"
)

# Delete User
TEST_DELETE_USER_RESULT_SUCCESS_XML = get_sample("delete_user_result_success.xml")
TEST_DELETE_USER_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_user_result_success.json"
)
TEST_DELETE_USER_RESULT_ERROR_XML = get_sample("delete_user_result_error.xml")
TEST_DELETE_USER_RESULT_ERROR_DICTIONARY = get_sample("delete_user_result_error.json")

# ============================================================================
# User Administration Request Sample Data
# ============================================================================

# Add User
TEST_ADD_USER_REQUEST_XML = get_sample("add_user_request.xml")
TEST_ADD_USER_REQUEST_TRAITS = {
    "name": "Squidward",
    "userid": "squidwrd",
    "password": "GIyTTqdF",
    "owner": "leonard",
    "special": True,
    "operator": False,
    "uid": "2424",
    "home": "/u/squidwrd",
    "program": "/bin/sh",
}

# Alter User
TEST_ALTER_USER_REQUEST_XML = get_sample("alter_user_request.xml")
TEST_ALTER_USER_REQUEST_TRAITS = {
    "userid": "squidwrd",
    "special": False,
    "operator": True,
    "home": "/u/clarinet",
    "program": False,
}

# Extract User
TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML = get_sample(
    "extract_user_request_base_omvs.xml"
)
TEST_EXTRACT_USER_REQUEST_BASE_OMVS_TRAITS = {
    "userid": "squidwrd",
    "omvs": True,
    "mfa": False,
}

# Delete User
TEST_DELETE_USER_REQUEST_XML = get_sample("delete_user_request.xml")

# ============================================================================
# User Administration Setters Sample Data
# ============================================================================

TEST_USER_SET_SPECIAL_XML = get_sample("user_set_special.xml")
TEST_USER_DEL_SPECIAL_XML = get_sample("user_del_special.xml")
TEST_USER_SET_AUDITOR_XML = get_sample("user_set_auditor.xml")
TEST_USER_DEL_AUDITOR_XML = get_sample("user_del_auditor.xml")
TEST_USER_SET_OPER_XML = get_sample("user_set_operations.xml")
TEST_USER_DEL_OPER_XML = get_sample("user_del_operations.xml")
TEST_USER_SET_UID_XML = get_sample("user_set_uid.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ADD_USER_SUCCESS_LOG = get_sample("add_user_success.log")
TEST_ADD_USER_ERROR_LOG = get_sample("add_user_error.log")

TEST_EXTRACT_USER_BASE_OMVS_SUCCESS_LOG = get_sample(
    "extract_user_base_omvs_success.log"
)
TEST_EXTRACT_USER_BASE_OMVS_ERROR_LOG = get_sample("extract_user_base_omvs_error.log")
