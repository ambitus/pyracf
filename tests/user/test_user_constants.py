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
TEST_ALTER_USER_PASSWORD_RESULT_SUCCESS_XML = get_sample(
    "alter_user_result_password_success.xml"
)
TEST_ALTER_USER_PASSWORD_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_user_result_password_success.json"
)
TEST_ALTER_USER_PASSWORD_RESULT_ERROR_XML = get_sample(
    "alter_user_result_password_error.xml"
)
TEST_ALTER_USER_PASSWORD_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_user_result_password_error.json"
)
TEST_ALTER_USER_PASSPHRASE_RESULT_SUCCESS_XML = get_sample(
    "alter_user_result_passphrase_success.xml"
)
TEST_ALTER_USER_PASSPHRASE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_user_result_passphrase_success.json"
)
TEST_ALTER_USER_PASSPHRASE_RESULT_ERROR_XML = get_sample(
    "alter_user_result_passphrase_error.xml"
)
TEST_ALTER_USER_PASSPHRASE_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_user_result_passphrase_error.json"
)
TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_RESULT_SUCCESS_XML = get_sample(
    "alter_user_result_passphrase_and_password_success.xml"
)
TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_user_result_passphrase_and_password_success.json"
)
TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_RESULT_ERROR_XML = get_sample(
    "alter_user_result_passphrase_and_password_error.xml"
)
TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_user_result_passphrase_and_password_error.json"
)
TEST_ALTER_USER_RESULT_EXTENDED_SUCCESS_XML = get_sample(
    "alter_user_result_extended_success.xml"
)
TEST_ALTER_USER_RESULT_EXTENDED_SUCCESS_DICTIONARY = get_sample(
    "alter_user_result_extended_success.json"
)
TEST_ALTER_USER_RESULT_ERROR_UID_SECRET_DICTIONARY = get_sample(
    "alter_user_result_error_uid_secret.json"
)

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
TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML = get_sample(
    "extract_user_result_base_only_success.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_JSON = get_sample(
    "extract_user_result_base_only_success.json"
)
TEST_EXTRACT_USER_RESULT_BASE_ONLY_ERROR_XML = get_sample(
    "extract_user_result_base_only_error.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_ONLY_ERROR_JSON = get_sample(
    "extract_user_result_base_only_error.json"
)
TEST_EXTRACT_USER_RESULT_WITH_CLASS_AUTHORIZATIONS = get_sample(
    "extract_user_result_with_class_authorizations.xml"
)
TEST_EXTRACT_USER_RESULT_WITH_COMMAND_AUDIT_TRAIL_XML = get_sample(
    "extract_user_result_with_command_audit_trail.xml"
)
TEST_EXTRACT_USER_RESULT_BAD_ATTRIBUTE_XML = get_sample(
    "extract_user_result_bad_attribute_error.xml"
)
TEST_EXTRACT_USER_RESULT_BAD_ATTRIBUTE_JSON = get_sample(
    "extract_user_result_bad_attribute_error.json"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML = get_sample(
    "extract_user_result_base_omvs_tso_revoke_resume.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_DICTIONARY = get_sample(
    "extract_user_result_base_omvs_tso_revoke_resume.json"
)
TEST_EXTRACT_USER_RESULT_EXTRA_MESSAGES_SUCCESS_XML = get_sample(
    "extract_user_result_extra_messages_success.xml"
)
TEST_EXTRACT_USER_RESULT_EXTRA_MESSAGES_SUCCESS_DICTIONARY = get_sample(
    "extract_user_result_extra_messages_success.json"
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
TEST_ADD_USER_BASE_OMVS_TSO_REVOKE_RESUME_REQUEST_XML = get_sample(
    "add_user_request_base_omvs_tso_revoke_resume.xml"
)
TEST_ADD_USER_REQUEST_PASSWORD_XML = get_sample("add_user_request_password.xml")
TEST_ADD_USER_REQUEST_PASSPHRASE_XML = get_sample("add_user_request_passphrase.xml")
TEST_ADD_USER_REQUEST_PASSPHRASE_AND_PASSWORD_XML = get_sample(
    "add_user_request_passphrase_and_password.xml"
)
TEST_ADD_USER_REQUEST_TRAITS = {
    "base:name": "Squidward",
    "base:owner": "leonard",
    "base:special": True,
    "omvs:uid": "2424",
    "omvs:home_directory": "/u/squidwrd",
    "omvs:default_shell": "/bin/sh",
}
TEST_ADD_USER_BASE_OMVS_TSO_REVOKE_RESUME_REQUEST_TRAITS = {
    "base:name": "Squidward",
    "base:password": "PASSWORD",
    "base:owner": "LEONARD",
    "base:revoke_date": "10/22/23",
    "base:resume_date": "11/2/23",
    "omvs:max_address_space_size": 10485760,
    "omvs:max_cpu_time": 1500,
    "omvs:max_files_per_process": 50,
    "omvs:max_non_shared_memory": "4g",
    "omvs:max_file_mapping_pages": 350,
    "omvs:max_processes": 128,
    "omvs:shared": True,
    "omvs:max_shared_memory": "2g",
    "omvs:max_threads": 48,
    "omvs:uid": 1919,
    "omvs:home_directory": "/u/squidward",
    "omvs:default_shell": "/bin/sh",
    "tso:account_number": "SB29",
    "tso:logon_command": "ISPF",
    "tso:hold_class": "A",
    "tso:max_region_size": 2048,
    "tso:message_class": "B",
    "tso:logon_procedure": "PROC",
    "tso:default_region_size": 1024,
    "tso:sysout_class": "O",
    "tso:user_data": "ABCD",
    "tso:data_set_allocation_unit": "SYSDA",
}
TEST_ADD_USER_REQUEST_BAD_TRAITS = dict(TEST_ADD_USER_REQUEST_TRAITS)
TEST_ADD_USER_REQUEST_BAD_TRAITS["omvs:bad_trait"] = "TESTING VALUE"

# Alter User
TEST_ALTER_USER_REQUEST_XML = get_sample("alter_user_request.xml")
TEST_ALTER_USER_REQUEST_TRAITS = {
    "base:special": False,
    "omvs:home_directory": "/u/clarinet",
    "omvs:default_shell": False,
}
TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED = {
    "base:name": "Squidward",
    "base:owner": "leonard",
    "base:special": True,
    "omvs:uid": "2424",
    "omvs:home_directory": "/u/squidwrd",
    "omvs:default_shell": "/bin/sh",
}
TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD = dict(TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED)
TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD["base:password"] = "GIyTTqdF"
TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD_SIMPLE = dict(
    TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED
)
TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD_SIMPLE["base:password"] = "PASSWORD"
TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE = dict(
    TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED
)
TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE["base:passphrase"] = "PassPhrasesAreCool!"
TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD = dict(
    TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED
)
TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD["base:password"] = "GIyTTqdF"
TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD[
    "base:passphrase"
] = "PassPhrasesAreCool!"
TEST_ALTER_USER_REQUEST_TRAITS_UID_ERROR = dict(TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED)
TEST_ALTER_USER_REQUEST_TRAITS_UID_ERROR["omvs:uid"] = 90000000000

# Extract User
TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML = get_sample(
    "extract_user_request_base_omvs.xml"
)

# Delete User
TEST_DELETE_USER_REQUEST_XML = get_sample("delete_user_request.xml")

# ============================================================================
# User Administration Setters Sample Data
# ============================================================================

# Base Segment
TEST_USER_GIVE_SPECIAL_AUTHORITY_XML = get_sample(
    "user_give_special_authority_request.xml"
)
TEST_USER_REMOVE_SPECIAL_AUTHORITY_XML = get_sample(
    "user_remove_special_authority_request.xml"
)
TEST_USER_GIVE_AUDITOR_AUTHORITY_XML = get_sample(
    "user_give_auditor_authority_request.xml"
)
TEST_USER_REMOVE_AUDITOR_AUTHORITY_XML = get_sample(
    "user_remove_auditory_authority_request.xml"
)
TEST_USER_GIVE_OPERATIONS_AUTHORITY_XML = get_sample(
    "user_give_operations_authority_request.xml"
)
TEST_USER_REMOVE_OPERATIONS_AUTHORITY_XML = get_sample(
    "user_remove_operations_authority_request.xml"
)
TEST_USER_SET_PASSWORD_XML = get_sample("user_set_password_request.xml")
TEST_USER_SET_PASSWORD_NOEXPIRED_XML = get_sample(
    "user_set_password_noexpired_request.xml"
)
TEST_USER_SET_PASSWORD_DELETE_XML = get_sample("user_set_password_delete_request.xml")
TEST_USER_SET_PASSPHRASE_XML = get_sample("user_set_passphrase_request.xml")
TEST_USER_SET_PASSPHRASE_NOEXPIRED_XML = get_sample(
    "user_set_passphrase_noexpired_request.xml"
)
TEST_USER_SET_PASSPHRASE_DELETE_XML = get_sample(
    "user_set_passphrase_delete_request.xml"
)
TEST_USER_ADD_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML = get_sample(
    "user_add_class_authorizations_single_class_request.xml"
)
TEST_USER_ADD_CLASS_AUTHORIZATIONS_MULTIPLE_CLASSES_XML = get_sample(
    "user_add_class_authorizations_multiple_classes_request.xml"
)
TEST_USER_REMOVE_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML = get_sample(
    "user_remove_class_authorizations_single_class_request.xml"
)
TEST_USER_REMOVE_CLASS_AUTHORIZATIONS_MULTIPLE_CLASSES_XML = get_sample(
    "user_remove_class_authorizations_multiple_classes_request.xml"
)
TEST_USER_REMOVE_ALL_CLASS_AUTHORIZATIONS_XML = get_sample(
    "user_remove_all_class_authorizations_request.xml"
)
TEST_USER_SET_CLASS_AUTHORIZATIONS_XML = get_sample(
    "user_set_class_authorizations_request.xml"
)
TEST_USER_SET_REVOKE_DATE_XML = get_sample("user_set_revoke_date_request.xml")
TEST_USER_SET_REVOKE_DATE_DELETE_XML = get_sample(
    "user_set_revoke_date_delete_request.xml"
)
TEST_USER_SET_RESUME_DATE_XML = get_sample("user_set_resume_date_request.xml")
TEST_USER_SET_RESUME_DATE_DELETE_XML = get_sample(
    "user_set_resume_date_delete_request.xml"
)
TEST_USER_SET_OWNER_XML = get_sample("user_set_owner_request.xml")
TEST_USER_SET_NAME_XML = get_sample("user_set_name_request.xml")
TEST_USER_SET_NAME_DELETE_XML = get_sample("user_set_name_delete_request.xml")

# OMVS Segment
TEST_USER_SET_OMVS_UID_XML = get_sample("user_set_omvs_uid_request.xml")
TEST_USER_SET_OMVS_UID_DELETE_XML = get_sample("user_set_omvs_uid_delete_request.xml")
TEST_USER_SET_OMVS_MAX_ADDRESS_SPACE_SIZE_XML = get_sample(
    "user_set_omvs_max_address_space_size_request.xml"
)
TEST_USER_SET_OMVS_MAX_ADDRESS_SPACE_SIZE_DELETE_XML = get_sample(
    "user_set_omvs_max_address_space_size_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_CPU_TIME_XML = get_sample(
    "user_set_omvs_max_cpu_time_request.xml"
)
TEST_USER_SET_OMVS_MAX_CPU_TIME_DELETE_XML = get_sample(
    "user_set_omvs_max_cpu_time_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_FILES_PER_PROCESS_XML = get_sample(
    "user_set_omvs_max_files_per_process_request.xml"
)
TEST_USER_SET_OMVS_MAX_FILES_PER_PROCESS_DELETE_XML = get_sample(
    "user_set_omvs_max_files_per_process_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_NON_SHARED_MEMORY_XML = get_sample(
    "user_set_omvs_max_non_shared_memory_request.xml"
)
TEST_USER_SET_OMVS_MAX_NON_SHARED_MEMORY_DELETE_XML = get_sample(
    "user_set_omvs_max_non_shared_memory_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_FILE_MAPPING_PAGES_XML = get_sample(
    "user_set_omvs_max_file_mapping_pages_request.xml"
)
TEST_USER_SET_OMVS_MAX_FILE_MAPPING_PAGES_DELETE_XML = get_sample(
    "user_set_omvs_max_file_mapping_pages_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_PROCESSES_XML = get_sample(
    "user_set_omvs_max_processes_request.xml"
)
TEST_USER_SET_OMVS_MAX_PROCESSES_DELETE_XML = get_sample(
    "user_set_omvs_max_processes_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_SHARED_MEMORY_XML = get_sample(
    "user_set_omvs_max_shared_memory_request.xml"
)
TEST_USER_SET_OMVS_MAX_SHARED_MEMORY_DELETE_XML = get_sample(
    "user_set_omvs_max_shared_memory_delete_request.xml"
)
TEST_USER_SET_OMVS_MAX_THREADS_XML = get_sample("user_set_omvs_max_threads_request.xml")
TEST_USER_SET_OMVS_MAX_THREADS_DELETE_XML = get_sample(
    "user_set_omvs_max_threads_delete_request.xml"
)
TEST_USER_SET_OMVS_HOME_DIRECTORY_XML = get_sample(
    "user_set_omvs_home_directory_request.xml"
)
TEST_USER_SET_OMVS_HOME_DIRECTORY_DELETE_XML = get_sample(
    "user_set_omvs_home_directory_delete_request.xml"
)
TEST_USER_SET_OMVS_DEFAULT_SHELL_XML = get_sample(
    "user_set_omvs_default_shell_request.xml"
)
TEST_USER_SET_OMVS_DEFAULT_SHELL_DELETE_XML = get_sample(
    "user_set_omvs_default_shell_delete_request.xml"
)

# TSO Segment
TEST_USER_SET_TSO_ACCOUNT_NUMBER_XML = get_sample(
    "user_set_tso_account_number_request.xml"
)
TEST_USER_SET_TSO_ACCOUNT_NUMBER_DELETE_XML = get_sample(
    "user_set_tso_account_number_delete_request.xml"
)
TEST_USER_SET_TSO_LOGON_COMMAND_XML = get_sample(
    "user_set_tso_logon_command_request.xml"
)
TEST_USER_SET_TSO_LOGON_COMMAND_DELETE_XML = get_sample(
    "user_set_tso_logon_command_delete_request.xml"
)
TEST_USER_SET_TSO_HOLD_CLASS_XML = get_sample("user_set_tso_hold_class_request.xml")
TEST_USER_SET_TSO_HOLD_CLASS_DELETE_XML = get_sample(
    "user_set_tso_hold_class_delete_request.xml"
)
TEST_USER_SET_TSO_MAX_REGION_SIZE_XML = get_sample(
    "user_set_tso_max_region_size_request.xml"
)
TEST_USER_SET_TSO_MAX_REGION_SIZE_DELETE_XML = get_sample(
    "user_set_tso_max_region_size_delete_request.xml"
)
TEST_USER_SET_TSO_MESSAGE_CLASS_XML = get_sample(
    "user_set_tso_message_class_request.xml"
)
TEST_USER_SET_TSO_MESSAGE_CLASS_DELETE_XML = get_sample(
    "user_set_tso_message_class_delete_request.xml"
)
TEST_USER_SET_TSO_LOGON_PROCEDURE_XML = get_sample(
    "user_set_tso_logon_procedure_request.xml"
)
TEST_USER_SET_TSO_LOGON_PROCEDURE_DELETE_XML = get_sample(
    "user_set_tso_logon_procedure_delete_request.xml"
)
TEST_USER_SET_TSO_DEFAULT_REGION_SIZE_XML = get_sample(
    "user_set_tso_default_region_size_request.xml"
)
TEST_USER_SET_TSO_DEFAULT_REGION_SIZE_DELETE_XML = get_sample(
    "user_set_tso_default_region_size_delete_request.xml"
)
TEST_USER_SET_TSO_SYSOUT_CLASS_XML = get_sample("user_set_tso_sysout_class_request.xml")
TEST_USER_SET_TSO_SYSOUT_CLASS_DELETE_XML = get_sample(
    "user_set_tso_sysout_class_delete_request.xml"
)
TEST_USER_SET_TSO_USER_DATA_XML = get_sample("user_set_tso_user_data_request.xml")
TEST_USER_SET_TSO_USER_DATA_DELETE_XML = get_sample(
    "user_set_tso_user_data_delete_request.xml"
)
TEST_USER_SET_TSO_DATA_SET_ALLOCATION_UNIT_XML = get_sample(
    "user_set_tso_data_set_allocation_unit_request.xml"
)
TEST_USER_SET_TSO_DATA_SET_ALLOCATION_UNIT_DELETE_XML = get_sample(
    "user_set_tso_data_set_allocation_unit_delete_request.xml"
)

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_USER_SUCCESS_LOG = get_sample("alter_user_success.log")
TEST_ALTER_USER_ERROR_LOG = get_sample("alter_user_error.log")

TEST_ALTER_USER_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG = get_sample(
    "alter_user_additional_secret_added_success.log"
)
TEST_ALTER_USER_ADDITIONAL_SECRET_ADDED_ERROR_LOG = get_sample(
    "alter_user_additional_secret_added_error.log"
)

TEST_ALTER_USER_PASSWORD_SUCCESS_LOG = get_sample("alter_user_password_success.log")
TEST_ALTER_USER_PASSWORD_ERROR_LOG = get_sample("alter_user_password_error.log")

TEST_ALTER_USER_PASSPHRASE_SUCCESS_LOG = get_sample("alter_user_passphrase_success.log")
TEST_ALTER_USER_PASSPHRASE_ERROR_LOG = get_sample("alter_user_passphrase_error.log")

TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_SUCCESS_LOG = get_sample(
    "alter_user_passphrase_and_password_success.log"
)
TEST_ALTER_USER_PASSPHRASE_AND_PASSWORD_ERROR_LOG = get_sample(
    "alter_user_passphrase_and_password_error.log"
)

TEST_EXTRACT_USER_BASE_OMVS_SUCCESS_LOG = get_sample(
    "extract_user_base_omvs_success.log"
)
TEST_EXTRACT_USER_BASE_OMVS_ERROR_LOG = get_sample("extract_user_base_omvs_error.log")

# ============================================================================
# Customize Segment Traits
# ============================================================================

# Alter User Traits
TEST_ALTER_USER_CSDATA_AND_OMVS_REQUEST_TRAITS = {
    "base:special": False,
    "omvs:home_directory": "/u/clarinet",
    "omvs:default_shell": False,
    "csdata:tstcsfld": "testval",
}
TEST_ALTER_USER_CSDATA_REQUEST_TRAITS = {
    "base:special": False,
    "csdata:tstcsfld": "testval",
}

# Valid Segment Traits Updates
TEST_USER_REPLACE_SEGMENT_TRAITS = {
    "base": {"base:special": "alt:special"},
    "csdata": {"csdata:tstcsfld": "tstcsfld"},
}

TEST_USER_ADDITIONAL_SEGMENT_TRAITS = {"csdata": {"csdata:tstcsfld": "tstcsfld"}}

# Alter User Requests
TEST_ALTER_USER_REQUEST_REPLACE_SEGMENTS_XML = get_sample(
    "alter_user_request_replace_segments.xml"
)
TEST_ALTER_USER_REQUEST_UPDATE_SEGMENTS_XML = get_sample(
    "alter_user_request_update_segments.xml"
)

# Extract User Results
TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_XML = get_sample(
    "extract_user_result_base_omvs_csdata_success.xml"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_DICTIONARY = get_sample(
    "extract_user_result_base_omvs_csdata_success.json"
)
