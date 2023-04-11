"""
Sample data for testing Setropts Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "setropts")


# ============================================================================
# Setropts Administration Result Sample Data
# ============================================================================

# Setropts Command
TEST_COMMAND_SETROPTS_RESULT_SUCCESS_XML = get_sample(
    "command_setropts_result_success.xml"
)
TEST_COMMAND_SETROPTS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "command_setropts_result_success.json"
)
TEST_COMMAND_SETROPTS_RESULT_ERROR_XML = get_sample("command_setropts_result_error.xml")
TEST_COMMAND_SETROPTS_RESULT_ERROR_DICTIONARY = get_sample(
    "command_setropts_result_error.json"
)

# List Setropts
TEST_LIST_SETROPTS_RESULT_SUCCESS_XML = get_sample("list_setropts_result_success.xml")
TEST_LIST_SETROPTS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "list_setropts_result_success.json"
)

# ============================================================================
# Setropts Administration Request Sample Data
# ============================================================================

# Command Setropts
TEST_COMMAND_SETROPTS_REQUEST_XML = get_sample("command_setropts_request.xml")
TEST_COMMAND_SETROPTS_REQUEST_TRAITS = {"raclist": "elijtest"}

# List Setropts
TEST_LIST_SETROPTS_REQUEST_XML = get_sample("list_setropts_request.xml")

# ============================================================================
# Setropts Administration Setters Sample Data
# ============================================================================

TEST_SETROPTS_AUDIT_ADD_XML = get_sample("setropts_audit_add.xml")
TEST_SETROPTS_AUDIT_DEL_XML = get_sample("setropts_audit_del.xml")
TEST_SETROPTS_CLASSACT_ADD_XML = get_sample("setropts_classact_add.xml")
TEST_SETROPTS_CLASSACT_DEL_XML = get_sample("setropts_classact_del.xml")
TEST_SETROPTS_CLASSTAT_ADD_XML = get_sample("setropts_classstat_add.xml")
TEST_SETROPTS_CLASSTAT_DEL_XML = get_sample("setropts_classstat_del.xml")
TEST_SETROPTS_GENCMD_ADD_XML = get_sample("setropts_gencmd_add.xml")
TEST_SETROPTS_GENCMD_DEL_XML = get_sample("setropts_gencmd_del.xml")
TEST_SETROPTS_GENERIC_ADD_XML = get_sample("setropts_generic_add.xml")
TEST_SETROPTS_GENERIC_DEL_XML = get_sample("setropts_generic_del.xml")
TEST_SETROPTS_GENLIST_ADD_XML = get_sample("setropts_genlist_add.xml")
TEST_SETROPTS_GENLIST_DEL_XML = get_sample("setropts_genlist_del.xml")
TEST_SETROPTS_GLOBAL_ADD_XML = get_sample("setropts_global_add.xml")
TEST_SETROPTS_GLOBAL_DEL_XML = get_sample("setropts_global_del.xml")
TEST_SETROPTS_RACLIST_ADD_XML = get_sample("setropts_raclist_add.xml")
TEST_SETROPTS_RACLIST_DEL_XML = get_sample("setropts_raclist_del.xml")
TEST_SETROPTS_REFRESH_CLASS_XML = get_sample("setropts_refresh_class.xml")

# ============================================================================
# Setropts Administration Getters Comparison Data
# ============================================================================

TEST_SETROPTS_PASSWORD_RULES = [
    {"minlength": 4, "maxlength": 8, "content": "********", "legend": {"*": "ANYTHING"}}
]
TEST_SETROPTS_CLASS_ATTRIBUTES = [
    "active",
    "generic profile",
    "generic command",
    "setr raclist",
]
