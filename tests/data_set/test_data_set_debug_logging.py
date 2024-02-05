"""Test data set administration debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin, SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestDataSetDebugLogging(unittest.TestCase):
    maxDiff = None
    data_set_admin = DataSetAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Alter Data Set
    # ============================================================================
    def test_alter_data_set_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestDataSetConstants.TEST_ALTER_DATA_SET_SUCCESS_LOG
        )

    def test_alter_data_set_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.data_set_admin.alter(
                    "ESWIFT.TEST.T1136242.P3020470",
                    traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestDataSetConstants.TEST_ALTER_DATA_SET_ERROR_LOG)

    # ============================================================================
    # Extract Data Set
    # ============================================================================
    def test_extract_data_set_base_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_BASE_ONLY_SUCCESS_LOG,
        )

    def test_extract_data_set_base_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestDataSetConstants.TEST_EXTRACT_DATA_SET_BASE_ONLY_ERROR_LOG
        )
