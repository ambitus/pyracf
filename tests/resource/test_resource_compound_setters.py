"""Test general resource profile compound setter functions."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin, SecurityRequestError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestResourceCompoundSetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    def test_resource_admin_clear_audit_failures_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.clear_audit_by_attempt(
                "TESTING", "ELIJTEST", "failures"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_FAILURES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_clear_audit_failures_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.clear_audit_by_attempt(
                    "TESTING", "ELIJTEST", "failures"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_FAILURES_ERROR_LOG,
        )

    def test_resource_admin_clear_audit_successes_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.clear_audit_by_attempt("TESTING", "ELIJTEST", "success")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_clear_audit_successes_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.clear_audit_by_attempt(
                    "TESTING", "ELIJTEST", "success"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_ERROR_LOG,
        )

    def test_resource_admin_clear_audit_both_successes_and_failures_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_audit_all_read_success_control = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_audit_all_read_success_control = (
            resource_extract_audit_all_read_success_control.replace(
                "<message>SUCCESS(UPDATE),FAILURES(READ)</message>",
                "<message>ALL(READ),SUCCESS(CONTROL)</message>",
            )
        )
        call_racf_mock.side_effect = [
            resource_extract_audit_all_read_success_control,
            resource_extract_audit_all_read_success_control,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_AND_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.clear_audit_by_attempt("TESTING", "ELIJTEST", "all")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_AND_FAILURES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_clear_audit_both_successes_and_failures_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_AND_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.clear_audit_by_attempt("TESTING", "ELIJTEST", "all")
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_CLEAR_AUDIT_SUCCESSES_AND_FAILURES_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_failures_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", failure="control"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_failures_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_attempt(
                    "TESTING", "ELIJTEST", failure="control"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_FAILURES_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_successes_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", success="control"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_successes_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_attempt(
                    "TESTING", "ELIJTEST", success="control"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_both_successes_and_failures_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_audit_all_read_success_control = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_audit_all_read_success_control = (
            resource_extract_audit_all_read_success_control.replace(
                "<message>SUCCESS(UPDATE),FAILURES(READ)</message>",
                "<message>ALL(READ),SUCCESS(CONTROL)</message>",
            )
        )
        call_racf_mock.side_effect = [
            resource_extract_audit_all_read_success_control,
            resource_extract_audit_all_read_success_control,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", all="update"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_both_successes_and_failures_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_XML,
        ]
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.clear_audit_by_attempt("TESTING", "ELIJTEST", "all")
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_attempt(
                    "TESTING", "ELIJTEST", all="update"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_SUCCESSES_AND_FAILURES_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_audit_alter_access_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", alter="success"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_audit_alter_access_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_access_level(
                    "TESTING", "ELIJTEST", alter="success"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_ALTER_ACCESS_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_audit_control_access_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", control="success"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_audit_control_access_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_access_level(
                    "TESTING", "ELIJTEST", control="success"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_CONTROL_ACCESS_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_audit_read_access_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", read="success"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_audit_read_access_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_access_level(
                    "TESTING", "ELIJTEST", read="success"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_READ_ACCESS_ERROR_LOG,
        )

    def test_resource_admin_alter_audit_by_audit_update_access_logs_correctly_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", update="failure"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_SUCCESS_LOG,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_alter_audit_by_audit_update_access_logs_correctly_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.resource_admin.alter_audit_by_access_level(
                    "TESTING", "ELIJTEST", update="success"
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log,
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_AUDIT_UPDATE_ACCESS_ERROR_LOG,
        )
