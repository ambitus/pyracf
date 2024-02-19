"""Test general resource profile getter functions."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin, SecurityRequestError, UserIdError

# Resolves F401
__init__


class TestResourceGetters(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    resource_admin = ResourceAdmin()

    # ============================================================================
    # Universal Access
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_universal_access_returns_valid_when_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST"), "read"
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_universal_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_universal_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_universal_access = resource_extract_no_universal_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          NONE               READ    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_universal_access
        self.assertIsNone(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")
        )

    # Error in environment, TESTING already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")

    # ============================================================================
    # Individual Access
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_my_access_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_my_access("TESTING", "ELIJTEST"), "read"
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_my_access_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_your_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_your_access = resource_extract_no_your_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ               NONE    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_your_access
        self.assertIsNone(self.resource_admin.get_my_access("TESTING", "ELIJTEST"))

    # Error in environment, TESTING already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_my_access("TESTING", "ELIJTEST")

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_get_user_access_general_resource(
        self,
        call_racf_mock: Mock,
    ):
        precheck_profile_as_squidwrd = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        precheck_profile_as_squidwrd = precheck_profile_as_squidwrd.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
        )
        resource_admin = ResourceAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.return_value = precheck_profile_as_squidwrd
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            access = resource_admin.get_user_access("TESTING", "ELIJTEST", "squidwrd")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_BASE_AS_SQUIDWRD_SUCCESS_LOG,
        )
        self.assertEqual(access, "alter")

    def test_get_user_access_general_resource_raises_userid_error(self):
        userid = "squidwrdtest"
        resource_admin = ResourceAdmin(debug=True, run_as_userid="ESWIFT")
        with self.assertRaises(UserIdError) as exception:
            resource_admin.get_user_access("TESTING", "ELIJTEST", userid)
        self.assertEqual(
            exception.exception.message,
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length.",
        )

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_audit_rules(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_audit_rules("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_GET_AUDIT_RULES,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_audit_rules_single(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_GENERIC_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_audit_rules("TEST*", "ELIJTEST"),
            TestResourceConstants.TEST_GET_AUDIT_RULES_SINGLE,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_audit_rules_none(
        self,
        call_racf_mock: Mock,
    ):
        profile_with_none_auditing = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        profile_with_none_auditing = profile_with_none_auditing.replace(
            "<message>SUCCESS(UPDATE),FAILURES(READ)</message>",
            "<message>NONE</message>",
        )
        call_racf_mock.return_value = profile_with_none_auditing
        self.assertIsNone(self.resource_admin.get_audit_rules("TESTING", "ELIJTEST"))

    # Error in environment, TESTING already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_get_audit_rules_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_audit_rules("TESTING", "ELIJTEST")
