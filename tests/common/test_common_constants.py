"""
Sample data for testing General Resource Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "resource")


# ============================================================================
# Install Precheck Sample Data
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
