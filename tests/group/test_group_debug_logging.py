"""Test password sanitization in group debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGroupDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> GroupAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return GroupAdmin(debug=True)

    # ============================================================================
    # Add Group
    # ============================================================================
    def test_add_group_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML
        with contextlib.redirect_stdout(self.stdout):
            group_admin.add(TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS)
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestGroupConstants.TEST_ADD_GROUP_SUCCESS_LOG)
        self.assertNotIn(self.test_password, success_log)

    def test_add_group_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestGroupConstants.TEST_ADD_GROUP_RESULT_ERROR_XML
        with contextlib.redirect_stdout(self.stdout):
            try:
                group_admin.add(TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS)
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestGroupConstants.TEST_ADD_GROUP_ERROR_LOG)
        self.assertNotIn(self.test_password, error_log)

    # ============================================================================
    # Extract Group
    # ============================================================================
    def test_extract_group_base_omvs_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            group_admin.extract(TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_TRAITS)
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestGroupConstants.TEST_EXTRACT_GROUP_BASE_OMVS_SUCCESS_LOG
        )

    def test_extract_group_base_omvs_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                group_admin.extract(TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_TRAITS)
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestGroupConstants.TEST_EXTRACT_GROUP_BASE_OMVS_ERROR_LOG
        )
