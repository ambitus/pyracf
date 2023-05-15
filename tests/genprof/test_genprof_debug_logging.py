"""Test password sanitization in genprof debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.genprof.test_genprof_constants as TestGenprofConstants
from pyracf import ResourceAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGenprofDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return ResourceAdmin(debug=True)

    # ============================================================================
    # Add Genprof
    # ============================================================================
    def test_add_genprof_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        genprof_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestGenprofConstants.TEST_ADD_GENPROF_RESULT_SUCCESS_XML
        with contextlib.redirect_stdout(self.stdout):
            genprof_admin.add(TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_TRAITS)
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestGenprofConstants.TEST_ADD_GENPROF_SUCCESS_LOG)

    def test_add_genprof_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        genprof_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestGenprofConstants.TEST_ADD_GENPROF_RESULT_ERROR_XML
        with contextlib.redirect_stdout(self.stdout):
            try:
                genprof_admin.add(TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_ERROR_TRAITS)
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestGenprofConstants.TEST_ADD_GENPROF_ERROR_LOG)

    # ============================================================================
    # Extract Genprof
    # ============================================================================
    def test_extract_genprof_base_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        genprof_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            genprof_admin.extract(TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS)
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestGenprofConstants.TEST_EXTRACT_GENPROF_BASE_SUCCESS_LOG
        )

    def test_extract_genprof_base_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        genprof_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                genprof_admin.extract(TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS)
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestGenprofConstants.TEST_EXTRACT_GENPROF_BASE_ERROR_LOG
        )
