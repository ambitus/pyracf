"""
Sample data for testing Connection Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "connection")


# ============================================================================
# Connection Administration Result Sample Data
# ============================================================================

# Add Connection
TEST_ADD_CONNECTION_RESULT_SUCCESS_XML = get_sample("add_connection_result_success.xml")
TEST_ADD_CONNECTION_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_connection_result_success.json"
)
TEST_ADD_CONNECTION_RESULT_ERROR_XML = get_sample("add_connection_result_error.xml")
TEST_ADD_CONNECTION_RESULT_ERROR_DICTIONARY = get_sample(
    "add_connection_result_error.json"
)

# Alter Connection
TEST_ALTER_CONNECTION_RESULT_SUCCESS_XML = get_sample(
    "alter_connection_result_success.xml"
)
TEST_ALTER_CONNECTION_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_connection_result_success.json"
)
TEST_ALTER_CONNECTION_RESULT_ERROR_XML = get_sample("alter_connection_result_error.xml")
TEST_ALTER_CONNECTION_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_connection_result_error.json"
)


# Delete Connection
TEST_DELETE_CONNECTION_RESULT_SUCCESS_XML = get_sample(
    "delete_connection_result_success.xml"
)
TEST_DELETE_CONNECTION_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_connection_result_success.json"
)
TEST_DELETE_CONNECTION_RESULT_ERROR_XML = get_sample(
    "delete_connection_result_error.xml"
)
TEST_DELETE_CONNECTION_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_connection_result_error.json"
)

# ============================================================================
# Connection Administration Request Sample Data
# ============================================================================

# Add Connection
TEST_ADD_CONNECTION_REQUEST_XML = get_sample("add_connection_request.xml")

# Alter Connection
TEST_ALTER_CONNECTION_REQUEST_XML = get_sample("alter_connection_request.xml")
TEST_ALTER_CONNECTION_REQUEST_TRAITS = {
    "base:operator": False,
    "base:special": True,
}

# Delete Connection
TEST_DELETE_CONNECTION_REQUEST_XML = get_sample("delete_connection_request.xml")

# ============================================================================
# Connection Administration Setters Sample Data
# ============================================================================

TEST_CONNECTION_SET_GROUP_SPECIAL = get_sample("connection_set_group_special.xml")
TEST_CONNECTION_DEL_GROUP_SPECIAL = get_sample("connection_del_group_special.xml")
TEST_CONNECTION_SET_GROUP_AUDITOR = get_sample("connection_set_group_auditor.xml")
TEST_CONNECTION_DEL_GROUP_AUDITOR = get_sample("connection_del_group_auditor.xml")
TEST_CONNECTION_SET_GROUP_OPERATIONS = get_sample("connection_set_group_operations.xml")
TEST_CONNECTION_DEL_GROUP_OPERATIONS = get_sample("connection_del_group_operations.xml")
TEST_CONNECTION_SET_GRPACC = get_sample("connection_set_grpacc.xml")
TEST_CONNECTION_DEL_GRPACC = get_sample("connection_del_grpacc.xml")

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ADD_CONNECTION_SUCCESS_LOG = get_sample("add_connection_success.log")
TEST_ADD_CONNECTION_ERROR_LOG = get_sample("add_connection_error.log")
