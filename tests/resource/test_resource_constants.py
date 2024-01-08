"""
Sample data for testing General Resource Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "resource")


# ============================================================================
# Resource Administration Result Sample Data
# ============================================================================

# Add Resource
TEST_ADD_RESOURCE_RESULT_SUCCESS_XML = get_sample("add_resource_result_success.xml")
TEST_ADD_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_resource_result_success.json"
)
TEST_ADD_RESOURCE_RESULT_ERROR_XML = get_sample("add_resource_result_error.xml")
TEST_ADD_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample("add_resource_result_error.json")

# Alter Resource
TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML = get_sample("alter_resource_result_success.xml")
TEST_ALTER_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_resource_result_success.json"
)
TEST_ALTER_RESOURCE_RESULT_ERROR_XML = get_sample("alter_resource_result_error.xml")
TEST_ALTER_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_resource_result_error.json"
)

# Extract Resource
TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML = get_sample(
    "extract_resource_result_base_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_resource_result_base_success.json"
)
TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_XML = get_sample(
    "extract_resource_result_multi_base_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_resource_result_multi_base_success.json"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML = get_sample(
    "extract_resource_result_base_error.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_DICTIONARY = get_sample(
    "extract_resource_result_base_error.json"
)
TEST_EXTRACT_RESOURCE_RESULT_BAD_CLASS_ERROR_XML = get_sample(
    "extract_resource_result_bad_class_error.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BAD_CLASS_ERROR_DICTIONARY = get_sample(
    "extract_resource_result_bad_class_error.json"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_GENERIC_SUCCESS_XML = get_sample(
    "extract_resource_result_base_generic_success.xml"
)

# Delete Resource
TEST_DELETE_RESOURCE_RESULT_SUCCESS_XML = get_sample(
    "delete_resource_result_success.xml"
)
TEST_DELETE_RESOURCE_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_resource_result_success.json"
)
TEST_DELETE_RESOURCE_RESULT_ERROR_XML = get_sample("delete_resource_result_error.xml")
TEST_DELETE_RESOURCE_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_resource_result_error.json"
)

# ============================================================================
# Resource Administration Request Sample Data
# ============================================================================

# Add Resource
TEST_ADD_RESOURCE_REQUEST_XML = get_sample("add_resource_request.xml")
TEST_ADD_RESOURCE_REQUEST_TRAITS = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}
TEST_ADD_RESOURCE_REQUEST_ERROR_TRAITS = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

# Alter Resource
TEST_ALTER_RESOURCE_REQUEST_XML = get_sample("alter_resource_request.xml")
TEST_ALTER_RESOURCE_REQUEST_TRAITS = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}
TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS = {
    "base:universal_access": "ALL",
    "base:owner": "eswift",
}

# Extract Resource
TEST_EXTRACT_RESOURCE_REQUEST_BASE_XML = get_sample("extract_resource_request_base.xml")

# Delete Resource
TEST_DELETE_RESOURCE_REQUEST_XML = get_sample("delete_resource_request.xml")

# ============================================================================
# Resource Administration Setters Sample Data
# ============================================================================

TEST_RESOURCE_SET_UNIVERSAL_ACCESS_XML = get_sample("resource_set_universal_access.xml")
TEST_RESOURCE_CLEAR_ALL_AUDIT_RULES_XML = get_sample(
    "resource_clear_all_audit_rules.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_ALTER_ACCESS_XML = get_sample(
    "resource_overwrite_audit_by_audit_alter_access.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_CONTROL_ACCESS_XML = get_sample(
    "resource_overwrite_audit_by_audit_control_access.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_UPDATE_ACCESS_XML = get_sample(
    "resource_overwrite_audit_by_audit_update_access.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_READ_ACCESS_XML = get_sample(
    "resource_overwrite_audit_by_audit_read_access.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_SUCCESSES_XML = get_sample(
    "resource_overwrite_audit_by_successes.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_FAILURES_XML = get_sample(
    "resource_overwrite_audit_by_failures.xml"
)
TEST_RESOURCE_OVERWRITE_AUDIT_BY_BOTH_SUCCESSES_AND_FAILURES_XML = get_sample(
    "resource_overwrite_audit_by_both_successes_and_failures.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_XML = get_sample(
    "alter_resource_result_alter_audit_by_failures.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_failures_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_failures_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_XML = get_sample(
    "alter_resource_result_alter_audit_by_successes.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_successes_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_successes_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_XML = get_sample(
    "alter_resource_result_alter_audit_by_both_successes_and_failures.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_both_successes_and_failures_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_both_successes_and_failures_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_XML = get_sample(
    "alter_resource_result_alter_audit_by_audit_alter_access.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_alter_access_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_alter_access_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_XML = get_sample(
    "alter_resource_result_alter_audit_by_audit_control_access.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_control_access_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_control_access_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_XML = get_sample(
    "alter_resource_result_alter_audit_by_audit_read_access.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_read_access_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_read_access_error.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_XML = get_sample(
    "alter_resource_result_alter_audit_by_audit_update_access.xml"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_SUCCESS_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_update_access_success.log"
)
TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_ERROR_LOG = get_sample(
    "alter_resource_alter_audit_by_audit_update_access_error.log"
)

# ============================================================================
# Resource Administration Getters Result Data
# ============================================================================

TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES = {"success": "update", "failures": "read"}

# ============================================================================
# Debug Logging
# ============================================================================

TEST_ALTER_RESOURCE_SUCCESS_LOG = get_sample("alter_resource_success.log")
TEST_ALTER_RESOURCE_ERROR_LOG = get_sample("alter_resource_error.log")

TEST_EXTRACT_RESOURCE_BASE_SUCCESS_LOG = get_sample("extract_resource_base_success.log")
TEST_EXTRACT_RESOURCE_BASE_ERROR_LOG = get_sample("extract_resource_base_error.log")

# ============================================================================
# Class Administration
# ============================================================================

TEST_ADD_RESOURCE_CLASS_REQUEST_XML = get_sample("add_resource_class_request.xml")
TEST_ALTER_RESOURCE_CLASS_REQUEST_XML = get_sample("alter_resource_class_request.xml")
TEST_DELETE_RESOURCE_CLASS_REQUEST_XML = get_sample("delete_resource_class_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_CDTINFO_SUCCESS_XML = get_sample(
    "extract_resource_result_base_cdtinfo_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_CDTINFO_ERROR_XML = get_sample(
    "extract_resource_result_base_cdtinfo_error.xml"
)

TEST_EXTRACT_RESOURCE_CLASS_PROFILE = {
    "caseAllowed": "upper",
    "defaultRacrouteReturnCode": 8,
    "defaultUniversalAccess": None,
    "validFirstCharacters": "alpha",
    "genericProfileSharing": "disallowed",
    "genericProfileChecking": "allowed",
    "groupingClassName": None,
    "keyQualifiers": 0,
    "manditoryAccessControlProcessing": "normal",
    "maxLength": 246,
    "maxLengthEntityx": 246,
    "memberClassName": None,
    "operations": None,
    "validOtherCharacters": ["alpha", "numeric"],
    "positNumber": 200,
    "profilesAllowed": "yes",
    "raclistAllowed": "allowed",
    "securityLabelsRequired": None,
    "sendEnfSignalOnProfileCreation": None,
}


TEST_ADD_RESOURCE_CLASS_REQUEST_TRAITS = {
    "cdtinfo:case_allowed": "UPPER",
    "cdtinfo:valid_first_characters": "ALPHA",
    "cdtinfo:valid_other_characters": ["ALPHA", "NUMERIC"],
    "cdtinfo:max_length": 246,
    "cdtinfo:max_length_entityx": 246,
    "cdtinfo:key_qualifiers": 0,
    "cdtinfo:profiles_allowed": "YES",
    "cdtinfo:posit_number": 200,
    "cdtinfo:default_racroute_return_code": 8,
    "cdtinfo:default_universal_access": "NONE",
    "cdtinfo:raclist_allowed": "ALLOWED",
}

TEST_ALTER_RESOURCE_CLASS_REQUEST_TRAITS = {
    "cdtinfo:valid_first_characters": ["ALPHA", "NUMERIC"],
    "cdtinfo:valid_other_characters": ["ALPHA"],
    "cdtinfo:profiles_allowed": "NO",
    "cdtinfo:default_racroute_return_code": 4,
    "cdtinfo:default_universal_access": "READ",
}

# ============================================================================
# Custom Field Administration
# ============================================================================

TEST_ADD_CUSTOM_FIELD_REQUEST_XML = get_sample("add_custom_field_request.xml")
TEST_ALTER_CUSTOM_FIELD_REQUEST_XML = get_sample("alter_custom_field_request.xml")
TEST_DELETE_CUSTOM_FIELD_REQUEST_XML = get_sample("delete_custom_field_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_CFDEF_SUCCESS_XML = get_sample(
    "extract_resource_result_base_cfdef_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_CFDEF_ERROR_XML = get_sample(
    "extract_resource_result_base_cfdef_error.xml"
)

TEST_EXTRACT_CUSTOM_FIELD_PROFILE = {
    "customFieldDataType": "char",
    "maxlength": None,
    "maxNumericValue": None,
    "minNumericValue": None,
    "validFirstCharacters": "alpha",
    "validOtherCharacters": "alpha",
    "mixedCaseAllowed": None,
    "helpText": ["favorite", "tv", "show"],
}

TEST_ALTER_CUSTOM_FIELD_REQUEST_TRAITS = {
    "cfdef:help_text": "Favorite TV Show",
    "cfdef:valid_first_characters": "ALPHA",
    "cfdef:valid_other_characters": "ALPHA",
}

# ============================================================================
# Started Task Administration
# ============================================================================

TEST_ADD_STARTED_TASK_REQUEST_XML = get_sample("add_started_task_request.xml")
TEST_ALTER_STARTED_TASK_REQUEST_XML = get_sample("alter_started_task_request.xml")
TEST_DELETE_STARTED_TASK_REQUEST_XML = get_sample("delete_started_task_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_STDATA_SUCCESS_XML = get_sample(
    "extract_resource_result_base_stdata_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_STDATA_ERROR_XML = get_sample(
    "extract_resource_result_base_stdata_error.xml"
)

TEST_EXTRACT_STARTED_TASK_PROFILE = {
    "user": None,
    "group": None,
    "trusted": "yes",
    "privileged": None,
    "trace": None,
}

# ============================================================================
# Kerberos Realm Administration
# ============================================================================

TEST_ADD_KERBEROS_REALM_REQUEST_XML = get_sample("add_kerberos_realm_request.xml")
TEST_ALTER_KERBEROS_REALM_REQUEST_XML = get_sample("alter_kerberos_realm_request.xml")
TEST_DELETE_KERBEROS_REALM_REQUEST_XML = get_sample("delete_kerberos_realm_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_KERB_SUCCESS_XML = get_sample(
    "extract_resource_result_base_kerb_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_KERB_ERROR_XML = get_sample(
    "extract_resource_result_base_kerb_error.xml"
)

TEST_EXTRACT_KERBEROS_REALM_PROFILE = {
    "keyEncryptionType": [
        "des",
        "des3",
        "desd",
        "aes128",
        "aes256",
        "aes128sha2",
        "aes256sha2",
    ],
    "checkAddresses": None,
}

# ============================================================================
# Signed Program Administration
# ============================================================================

TEST_ADD_SIGNED_PROGRAM_REQUEST_XML = get_sample("add_signed_program_request.xml")
TEST_ALTER_SIGNED_PROGRAM_REQUEST_XML = get_sample("alter_signed_program_request.xml")
TEST_DELETE_SIGNED_PROGRAM_REQUEST_XML = get_sample("delete_signed_program_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_SIGVER_SUCCESS_XML = get_sample(
    "extract_resource_result_base_sigver_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_SIGVER_ERROR_XML = get_sample(
    "extract_resource_result_base_sigver_error.xml"
)

TEST_EXTRACT_SIGNED_PROGRAM_PROFILE = {
    "signatureRequired": None,
    "failProgramLoadCondition": "never",
    "logSignatureVerificationEvents": "success",
    "library": None,
}

# ============================================================================
# APPC Session Administration
# ============================================================================

TEST_ADD_APPC_SESSION_REQUEST_XML = get_sample("add_appc_session_request.xml")
TEST_ALTER_APPC_SESSION_REQUEST_XML = get_sample("alter_appc_session_request.xml")
TEST_DELETE_APPC_SESSION_REQUEST_XML = get_sample("delete_appc_session_request.xml")

TEST_EXTRACT_RESOURCE_RESULT_BASE_SESSION_SUCCESS_XML = get_sample(
    "extract_resource_result_base_session_success.xml"
)
TEST_EXTRACT_RESOURCE_RESULT_BASE_SESSION_ERROR_XML = get_sample(
    "extract_resource_result_base_session_error.xml"
)

# This segment requires additional logic that is not currently implemented.
# This will not be documented and the rest marked experimental
TEST_EXTRACT_APPC_SESSION_PROFILE = {
    "sessionKeyInterval": 5,
    "locked": True,
    "sessionKey": "e3c5e2e3d2c5e800",
    "securityCheckingLevel": "conv",
}
