"""Test data set administration debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDataSetDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DataSetAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return DataSetAdmin(debug=True)

    # ============================================================================
    # Add Data Set
    # ============================================================================
    def test_add_data_set_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            data_set_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestDataSetConstants.TEST_ADD_DATA_SET_SUCCESS_LOG
        )

    def test_add_data_set_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                data_set_admin.add(
                    "ESWIFF.TEST.T1136242.P3020470",
                    TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestDataSetConstants.TEST_ADD_DATA_SET_ERROR_LOG)

    # ============================================================================
    # Extract Data Set
    # ============================================================================
    def test_extract_data_set_base_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestDataSetConstants.TEST_EXTRACT_DATA_SET_BASE_SUCCESS_LOG
        )

    def test_extract_data_set_base_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestDataSetConstants.TEST_EXTRACT_DATA_SET_BASE_ERROR_LOG
        )
