"""
Sample data for testing Common functions in pyracf.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str, function_group: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, function_group)


# ============================================================================
# Install Precheck Sample Data
# ============================================================================

TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_ERROR_XML = get_sample(
    "extract_resource_result_precheck_error.xml", "resource"
)
TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML = get_sample(
    "extract_resource_result_precheck_success.xml", "resource"
)

TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_XML = get_sample(
    "add_resource_result_precheck_uacc_none_success.xml", "resource"
)
TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_DICTIONARY = get_sample(
    "add_resource_result_precheck_uacc_none_success.json", "resource"
)

TEST_INSTALL_PRECHECK_VALIDATED_ACCESS_TEXT = (
    "IRR.IRRSMO00.PRECHECK is already defined, and you already have alter access!"
    + "\nYou are ready to start using pyRACF!"
    + "\nPlease ensure other users of pyRACF also have at least read access."
    + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!\n"
)

TEST_INSTALL_PRECHECK_FOUND_NO_ACCESS_TEXT = (
    "IRR.IRRSMO00.PRECHECK is already defined, but you have no access."
    + "\nContact your security administrator for READ access before using pyRACF."
    + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!\n"
)

TEST_INSTALL_PRECHECK_DEFINED_PROFILE_TEXT = (
    "IRR.IRRSMO00.PRECHECK is now defined with a `Universal Access` of None."
    + "\nContact your security administrator for READ access before using pyRACF."
    + "\nOther users of pyRACF will also need to have at least read access."
    + "\nYou may also need to REFRESH the `XFACILIT` class."
    + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!\n"
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
    "alter_user_request_replace_segments.xml", "user"
)
TEST_ALTER_USER_REQUEST_UPDATE_SEGMENTS_XML = get_sample(
    "alter_user_request_update_segments.xml", "user"
)

# Extract User Results
TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_XML = get_sample(
    "extract_user_result_base_omvs_csdata_success.xml", "user"
)
TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_DICTIONARY = get_sample(
    "extract_user_result_base_omvs_csdata_success.json", "user"
)

# ============================================================================
# Run As UserId
# ============================================================================

TEST_RUNNING_USERID = "ESWIFT"
TEST_ALTER_USER_REQUEST_TRAITS = {
    "base:special": False,
    "omvs:home_directory": "/u/clarinet",
    "omvs:default_shell": False,
}
TEST_ALTER_USER_REQUEST_XML = get_sample("alter_user_request.xml", "user")
TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML = get_sample(
    "extract_user_result_base_only_success.xml", "user"
)
TEST_ALTER_USER_SUCCESS_LOG = get_sample("alter_user_success.log", "user")
TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG = get_sample(
    "alter_user_success_as_eswift.log", "user"
)
TEST_ALTER_USER_RESULT_SUCCESS_XML = get_sample("alter_user_result_success.xml", "user")
TEST_EXTRACT_RESOURCE_PRECHECK_AS_SQUIDWRD_LOG = get_sample(
    "extract_resource_precheck_as_squidwrd.log", "resource"
)

# ============================================================================
# Null Response Error
# ============================================================================

TEST_NULL_RESPONSE_PRECHECK_TEXT = (
    "(NullResponseError) Security request made to IRRSMO00 failed."
    + "\nSAF Return Code: 8 \nRACF Return Code: 200 \nRACF Reason Code: 16"
    + "\n\nCheck to see if the proper RACF permissions are in place.\n"
    + "For `set` or `alter` functions, you must have at least READ "
    + "access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class."
)

TEST_NULL_RESPONSE_SURROGAT_TEXT = (
    "(NullResponseError) Security request made to IRRSMO00 failed."
    + "\nSAF Return Code: 8 \nRACF Return Code: 200 \nRACF Reason Code: 8"
    + "\n\nCheck to see if the proper RACF permissions are in place.\n"
    + "For the `run_as_userid` feature, you must have at least UPDATE"
    + " access to `ESWIFT.IRRSMO00` in the `SURROGAT` class."
)

TEST_NULL_RESPONSE_GENERIC_TEXT = (
    "(NullResponseError) Security request made to IRRSMO00 failed."
    + "\nSAF Return Code: 8 \nRACF Return Code: 2000 \nRACF Reason Code: 20"
    + "\n\nPlease check the specified return and reason codes against"
    + " the IRRSMO00 documented return and reason codes for more information"
    + " about this error.\n"
    + "(https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes)"
)
