"""
Sample data for testing Common functions in pyracf.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "common")


# ============================================================================
# Setup Precheck Sample Data
# ============================================================================

TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_ERROR_XML = get_sample(
    "extract_resource_result_precheck_error.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML = get_sample(
    "extract_resource_result_precheck_success.xml"
)

TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_XML = get_sample(
    "add_resource_result_precheck_uacc_none_success.xml"
)
TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_DICTIONARY = get_sample(
    "add_resource_result_precheck_uacc_none_success.json"
)

TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_ERROR_XML = get_sample(
    "add_resource_result_precheck_uacc_none_error.xml"
)
TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_ERROR_DICTIONARY = get_sample(
    "add_resource_result_precheck_uacc_none_error.json"
)

TEST_SETUP_PRECHECK_VALIDATED_ACCESS_TEXT = (
    "'IRR.IRRSMO00.PRECHECK' is already defined, and you already have 'ALTER' access!\n"
    + "You are ready to start using pyRACF!\n"
    + "Please ensure other users of pyRACF also have at least 'READ' access.\n"
    + "Review our documentation at https://ambitus.github.io/pyracf/ as well!\n"
)

TEST_SETUP_PRECHECK_FOUND_NO_ACCESS_TEXT = (
    "'IRR.IRRSMO00.PRECHECK' is already defined, but you have no access.\n"
    + "Contact your security administrator for 'READ' access before using pyRACF.\n"
    + "Review our documentation at https://ambitus.github.io/pyracf/ as well!\n"
)

TEST_SETUP_PRECHECK_DEFINED_PROFILE_TEXT = (
    "'IRR.IRRSMO00.PRECHECK' is now defined with a 'Universal Access' of 'NONE'.\n"
    + "Contact your security administrator for 'READ' access before using pyRACF.\n"
    + "Other users of pyRACF will also need to have at least 'READ' access.\n"
    + "You may also need to refresh the 'XFACILIT' class.\n"
    + "Review our documentation at https://ambitus.github.io/pyracf/ as well!\n"
)

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

# ============================================================================
# Additional Secrets Redaction
# ============================================================================

TEST_ALTER_USER_REQUEST_TRAITS_INST_DATA = {
    "base:name": "Squidward",
    "base:owner": "leonard",
    "base:special": True,
    "omvs:uid": "2424",
    "omvs:home_directory": "/u/squidwrd",
    "omvs:default_shell": "/bin/sh",
    "base:installation_data": "Test = Value; Other(stuff goes here)'')",
}
TEST_ALTER_USER_RESULT_SUCCESS_UID_SECRET_DICTIONARY = get_sample(
    "alter_user_result_success_uid_secret.json"
)
TEST_ALTER_USER_RESULT_ERROR_UID_SECRET_DICTIONARY = get_sample(
    "alter_user_result_error_uid_secret.json"
)
TEST_ALTER_USER_RESULT_INST_DATA_SUCCESS_XML = get_sample(
    "alter_user_result_success_inst_data.xml"
)
TEST_ALTER_USER_RESULT_SUCCESS_INST_DATA_SECRET_DICTIONARY = get_sample(
    "alter_user_result_success_inst_data_secret.json"
)
TEST_ALTER_USER_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG = get_sample(
    "alter_user_additional_secret_added_success.log"
)
TEST_ALTER_USER_ADDITIONAL_SECRET_ADDED_ERROR_LOG = get_sample(
    "alter_user_additional_secret_added_error.log"
)

TEST_ALTER_DATA_SET_RESULT_SUCCESS_OWNER_SECRET_DICTIONARY = get_sample(
    "alter_data_set_result_success_owner_secret.json"
)
TEST_ALTER_DATA_SET_RESULT_ERROR_UACC_SECRET_DICTIONARY = get_sample(
    "alter_data_set_result_error_uacc_secret.json"
)
TEST_ALTER_DATA_SET_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG = get_sample(
    "alter_data_set_additional_secret_added_success.log"
)
TEST_ALTER_DATA_SET_ADDITIONAL_SECRET_ADDED_ERROR_LOG = get_sample(
    "alter_data_set_additional_secret_added_error.log"
)

TEST_ALTER_GROUP_RESULT_SUCCESS_GID_SECRET_DICTIONARY = get_sample(
    "alter_group_result_success_gid_secret.json"
)
TEST_ALTER_GROUP_RESULT_ERROR_GID_SECRET_DICTIONARY = get_sample(
    "alter_group_result_error_gid_secret.json"
)
TEST_ALTER_GROUP_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG = get_sample(
    "alter_group_additional_secret_added_success.log"
)
TEST_ALTER_GROUP_ADDITIONAL_SECRET_ADDED_ERROR_LOG = get_sample(
    "alter_group_additional_secret_added_error.log"
)

TEST_ALTER_RESOURCE_OVERWRITE_AUDIT_RESULT_SUCCESS_XML = get_sample(
    "alter_resource_overwrite_audit_result_success.xml"
)
TEST_ALTER_RESOURCE_RESULT_SUCCESS_OWNER_SECRET_DICTIONARY = get_sample(
    "alter_resource_result_success_owner_secret.json"
)
TEST_ALTER_RESOURCE_RESULT_SUCCESS_AUDIT_SECRET_DICTIONARY = get_sample(
    "alter_resource_result_success_audit_secret.json"
)
TEST_ALTER_RESOURCE_RESULT_ERROR_UACC_SECRET_DICTIONARY = get_sample(
    "alter_resource_result_error_uacc_secret.json"
)
TEST_ALTER_RESOURCE_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG = get_sample(
    "alter_resource_additional_secret_added_success.log"
)
TEST_ALTER_RESOURCE_ADDITIONAL_SECRET_ADDED_ERROR_LOG = get_sample(
    "alter_resource_additional_secret_added_error.log"
)

# ============================================================================
# Run As UserId
# ============================================================================

TEST_RUNNING_USERID = "eswift"
TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG = get_sample("alter_user_success_as_eswift.log")
TEST_EXTRACT_RESOURCE_PRECHECK_AS_SQUIDWRD_LOG = get_sample(
    "extract_resource_precheck_as_squidwrd.log"
)

# ============================================================================
# Downstream Fatal Error
# ============================================================================

TEST_DOWNSTREAM_FATAL_ERROR_PRECHECK_TEXT = (
    "(DownstreamFatalError) Security request made to IRRSMO00 failed."
    + "\n\nSAF Return Code: 8\nRACF Return Code: 200\nRACF Reason Code: 16"
    + "\n\nCheck to see if the proper RACF permissions are in place.\n"
    + "For 'set' or 'alter' functions, you must have at least 'READ' "
    + "access to 'IRR.IRRSMO00.PRECHECK' in the 'XFACILIT' class."
)

TEST_DOWNSTREAM_FATAL_ERROR_SURROGAT_TEXT = (
    "(DownstreamFatalError) Security request made to IRRSMO00 failed."
    + "\n\nSAF Return Code: 8\nRACF Return Code: 200\nRACF Reason Code: 8"
    + "\n\nCheck to see if the proper RACF permissions are in place.\n"
    + "For the 'run_as_userid' feature, you must have at least 'UPDATE' "
    + "access to 'ESWIFT.IRRSMO00' in the 'SURROGAT' class."
)

TEST_DOWNSTREAM_FATAL_ERROR_GENERIC_TEXT = (
    "(DownstreamFatalError) Security request made to IRRSMO00 failed."
    + "\n\nSAF Return Code: 8\nRACF Return Code: 2000\nRACF Reason Code: 20"
    + "\n\nPlease check the specified return and reason codes against "
    + "the documented IRRSMO00 return and reason codes for more information "
    + "about this error.\n"
    + "https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes"
)

# ============================================================================
# Dump Processing
# ============================================================================

TEST_EXTRACT_USER_SUCCESS_DUMP_MODE_LOG = get_sample(
    "extract_user_success_dump_mode.log"
)

TEST_EXTRACT_USER_FAILURE_DUMP_MODE_LOG = get_sample(
    "extract_user_failure_dump_mode.log"
)

TEST_EXTRACT_USER_SUCCESS_UNEVEN_BYTE_BOUNDARY_LOG = get_sample(
    "extract_user_success_dump_mode_uneven_byte_boundary.log"
)

TEST_EXTRACT_USER_SUCCESS_DUMP_MODE_ALL_BYTES_LOG = get_sample(
    "extract_user_success_dump_mode_all_bytes.log"
)

TEST_ALTER_USER_PASSWORD_DUMP_MODE_LOG = get_sample(
    "alter_user_password_success_dump_mode.log"
)
