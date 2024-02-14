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

# Setropts Alter
TEST_ALTER_SETROPTS_RESULT_SUCCESS_XML = get_sample("alter_setropts_result_success.xml")
TEST_ALTER_SETROPTS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_setropts_result_success.json"
)
TEST_ALTER_SETROPTS_RESULT_ERROR_XML = get_sample("alter_setropts_result_error.xml")
TEST_ALTER_SETROPTS_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_setropts_result_error.json"
)

# List Setropts
TEST_LIST_SETROPTS_RESULT_SUCCESS_XML = get_sample("list_setropts_result_success.xml")
TEST_LIST_SETROPTS_RESULT_SUCCESS_DICTIONARY = get_sample(
    "list_setropts_result_success.json"
)
TEST_LIST_SETROPTS_RESULT_SUCCESS_2_XML = get_sample(
    "list_setropts_result_success_2.xml"
)
TEST_LIST_SETROPTS_RESULT_SUCCESS_2_DICTIONARY = get_sample(
    "list_setropts_result_success_2.json"
)
TEST_LIST_SETROPTS_RESULT_SUCCESS_3_XML = get_sample(
    "list_setropts_result_success_3.xml"
)
TEST_LIST_SETROPTS_RESULT_SUCCESS_3_DICTIONARY = get_sample(
    "list_setropts_result_success_3.json"
)

# ============================================================================
# Setropts Administration Request Sample Data
# ============================================================================

# Setropts Alter
TEST_ALTER_SETROPTS_REQUEST_XML = get_sample("alter_setropts_request.xml")

# List Setropts
TEST_LIST_SETROPTS_REQUEST_XML = get_sample("list_setropts_request.xml")

# ============================================================================
# Setropts Administration Setters Sample Data
# ============================================================================

TEST_SETROPTS_ADD_AUDIT_CLASS_XML = get_sample("setropts_add_audit_class.xml")
TEST_SETROPTS_REMOVE_AUDIT_CLASS_XML = get_sample("setropts_remove_audit_class.xml")
TEST_SETROPTS_ADD_ACTIVE_CLASS_XML = get_sample("setropts_add_active_class.xml")
TEST_SETROPTS_REMOVE_ACTIVE_CLASS_XML = get_sample("setropts_remove_active_class.xml")
TEST_SETROPTS_ADD_STATISTICS_CLASS_XML = get_sample("setropts_add_statistics_class.xml")
TEST_SETROPTS_REMOVE_STATISTICS_CLASS_XML = get_sample(
    "setropts_remove_statistics_class.xml"
)
TEST_SETROPTS_ADD_GENERIC_COMMAND_PROCESSING_CLASS_XML = get_sample(
    "setropts_add_generic_command_processing_class.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_COMMAND_PROCESSING_CLASS_XML = get_sample(
    "setropts_remove_generic_command_processing_class.xml"
)
TEST_SETROPTS_ADD_GENERIC_PROFILE_CHECKING_CLASS_XML = get_sample(
    "setropts_add_generic_profile_checking_class.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_PROFILE_CHECKING_CLASS_XML = get_sample(
    "setropts_remove_generic_profile_checking_class.xml"
)
TEST_SETROPTS_ADD_GENERIC_PROFILE_SHARING_CLASS_XML = get_sample(
    "setropts_add_generic_profile_sharing_class.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_PROFILE_SHARING_CLASS_XML = get_sample(
    "setropts_remove_generic_profile_sharing_class.xml"
)
TEST_SETROPTS_ADD_GLOBAL_ACCESS_CLASS_XML = get_sample(
    "setropts_add_global_access_class.xml"
)
TEST_SETROPTS_REMOVE_GLOBAL_ACCESS_CLASS_XML = get_sample(
    "setropts_remove_global_access_class.xml"
)
TEST_SETROPTS_ADD_RACLIST_CLASS_XML = get_sample("setropts_add_raclist_class.xml")
TEST_SETROPTS_REMOVE_RACLIST_CLASS_XML = get_sample("setropts_remove_raclist_class.xml")
TEST_SETROPTS_ADD_AUDIT_CLASSES_XML = get_sample("setropts_add_audit_classes.xml")
TEST_SETROPTS_REMOVE_AUDIT_CLASSES_XML = get_sample("setropts_remove_audit_classes.xml")
TEST_SETROPTS_ADD_ACTIVE_CLASSES_XML = get_sample("setropts_add_active_classes.xml")
TEST_SETROPTS_REMOVE_ACTIVE_CLASSES_XML = get_sample(
    "setropts_remove_active_classes.xml"
)
TEST_SETROPTS_ADD_STATISTICS_CLASSES_XML = get_sample(
    "setropts_add_statistics_classes.xml"
)
TEST_SETROPTS_REMOVE_STATISTICS_CLASSES_XML = get_sample(
    "setropts_remove_statistics_classes.xml"
)
TEST_SETROPTS_ADD_GENERIC_COMMAND_PROCESSING_CLASSES_XML = get_sample(
    "setropts_add_generic_command_processing_classes.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_COMMAND_PROCESSING_CLASSES_XML = get_sample(
    "setropts_remove_generic_command_processing_classes.xml"
)
TEST_SETROPTS_ADD_GENERIC_PROFILE_CHECKING_CLASSES_XML = get_sample(
    "setropts_add_generic_profile_checking_classes.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_PROFILE_CHECKING_CLASSES_XML = get_sample(
    "setropts_remove_generic_profile_checking_classes.xml"
)
TEST_SETROPTS_ADD_GENERIC_PROFILE_SHARING_CLASSES_XML = get_sample(
    "setropts_add_generic_profile_sharing_classes.xml"
)
TEST_SETROPTS_REMOVE_GENERIC_PROFILE_SHARING_CLASSES_XML = get_sample(
    "setropts_remove_generic_profile_sharing_classes.xml"
)
TEST_SETROPTS_ADD_GLOBAL_ACCESS_CLASSES_XML = get_sample(
    "setropts_add_global_access_classes.xml"
)
TEST_SETROPTS_REMOVE_GLOBAL_ACCESS_CLASSES_XML = get_sample(
    "setropts_remove_global_access_classes.xml"
)
TEST_SETROPTS_ADD_RACLIST_CLASSES_XML = get_sample("setropts_add_raclist_classes.xml")
TEST_SETROPTS_REMOVE_RACLIST_CLASSES_XML = get_sample(
    "setropts_remove_raclist_classes.xml"
)
TEST_SETROPTS_REFRESH_RACLIST_XML = get_sample("setropts_refresh_raclist.xml")
TEST_SETROPTS_REFRESH_RACLIST_MULTIPLE_XML = get_sample(
    "setropts_refresh_raclist_multiple.xml"
)
TEST_SETROPTS_REFRESH_GENERIC_XML = get_sample("setropts_refresh_generic.xml")
TEST_SETROPTS_REFRESH_GENERIC_MULTIPLE_XML = get_sample(
    "setropts_refresh_generic_multiple.xml"
)
TEST_SETROPTS_REFRESH_GLOBAL_XML = get_sample("setropts_refresh_global.xml")
TEST_SETROPTS_REFRESH_GLOBAL_MULTIPLE_XML = get_sample(
    "setropts_refresh_global_multiple.xml"
)

# ============================================================================
# Setropts Administration Getters Comparison Data
# ============================================================================

TEST_SETROPTS_PASSWORD_RULES = {
    "rules": [{"minLength": 4, "maxLength": 8, "content": "********"}],
    "legend": {
        "A": "alpha",
        "C": "consonant",
        "L": "alphanumeric",
        "N": "numeric",
        "V": "vowel",
        "W": "no vowel",
        "*": "anything",
        "c": "mixed consonant",
        "m": "mixed numeric",
        "v": "mixed vowel",
        "$": "national",
        "s": "special",
        "x": "mixed all",
    },
}
TEST_SETROPTS_CLASS_ATTRIBUTES = [
    "active",
    "genericProfile",
    "genericCommand",
    "raclist",
]

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_SETROPTS_SUCCESS_LOG = get_sample("alter_setropts_success.log")
TEST_ALTER_SETROPTS_ERROR_LOG = get_sample("alter_setropts_error.log")

TEST_LIST_SETROPTS_SUCCESS_LOG = get_sample("list_setropts_success.log")
TEST_LIST_SETROPTS_SUCCESS_2_LOG = get_sample("list_setropts_success_2.log")
TEST_LIST_SETROPTS_SUCCESS_3_LOG = get_sample("list_setropts_success_3.log")
