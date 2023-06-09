"""Test password sanitization in resource debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestResourceDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return ResourceAdmin(debug=True)

    # ============================================================================
    # Add Resource
    # ============================================================================
    def test_add_resource_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            resource_admin.add(
                "TESTING",
                "ELIJTEST",
                TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestResourceConstants.TEST_ADD_RESOURCE_SUCCESS_LOG
        )

    def test_add_resource_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                resource_admin.add(
                    "TESTING",
                    "ELIXTEST",
                    TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_ERROR_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestResourceConstants.TEST_ADD_RESOURCE_ERROR_LOG)

    # ============================================================================
    # Extract Resource
    # ============================================================================
    def test_extract_resource_base_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            resource_admin.extract("TESTING", "ELIJTEST")
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestResourceConstants.TEST_EXTRACT_RESOURCE_BASE_SUCCESS_LOG
        )

    def test_extract_resource_base_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                resource_admin.extract("TESTING", "ELIJTEST")
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestResourceConstants.TEST_EXTRACT_RESOURCE_BASE_ERROR_LOG
        )
