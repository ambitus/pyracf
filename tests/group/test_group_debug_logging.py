"""Test password sanitization in group debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin, SecurityRequestError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestGroupDebugLogging(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    group_admin = GroupAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Add Group
    # ============================================================================
    def test_add_group_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.group_admin.add(
                "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(success_log, TestGroupConstants.TEST_ADD_GROUP_SUCCESS_LOG)

    def test_add_group_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = TestGroupConstants.TEST_ADD_GROUP_RESULT_ERROR_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.group_admin.add(
                    "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestGroupConstants.TEST_ADD_GROUP_ERROR_LOG)

    # ============================================================================
    # Extract Group
    # ============================================================================
    def test_extract_group_base_omvs_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.group_admin.extract("TESTGRP0", segments={"omvs": True})
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestGroupConstants.TEST_EXTRACT_GROUP_BASE_OMVS_SUCCESS_LOG
        )

    def test_extract_group_base_omvs_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.group_admin.extract("TESTGRP0", segments={"omvs": True})
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestGroupConstants.TEST_EXTRACT_GROUP_BASE_OMVS_ERROR_LOG
        )
