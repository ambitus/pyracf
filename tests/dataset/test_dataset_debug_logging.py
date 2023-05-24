"""Test password sanitization in dataset debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.dataset.test_dataset_constants as TestDatasetConstants
from pyracf import DatasetAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDatasetDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DatasetAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return DatasetAdmin(debug=True)

    # ============================================================================
    # Add Dataset
    # ============================================================================
    def test_add_dataset_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            dataset_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestDatasetConstants.TEST_ADD_DATASET_SUCCESS_LOG)

    def test_add_dataset_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                dataset_admin.add(
                    "ESWIFF.TEST.T1136242.P3020470",
                    TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestDatasetConstants.TEST_ADD_DATASET_ERROR_LOG)

    # ============================================================================
    # Extract Dataset
    # ============================================================================
    def test_extract_dataset_base_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestDatasetConstants.TEST_EXTRACT_DATASET_BASE_SUCCESS_LOG
        )

    def test_extract_dataset_base_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470")
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestDatasetConstants.TEST_EXTRACT_DATASET_BASE_ERROR_LOG
        )
