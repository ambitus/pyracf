"""Test password sanitization in connection debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin, SecurityResponseError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestConnectionDebugLogging(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    connection_admin = ConnectionAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Connect Connection
    # ============================================================================
    def test_connect_connection_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.connection_admin.connect(
                "ESWIFT",
                "TESTGRP0",
                traits=TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_TRAITS,
            ),
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestConnectionConstants.TEST_CONNECT_CONNECTION_SUCCESS_LOG
        )

    def test_connect_connection_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.connection_admin.connect(
                    "ESWIFT",
                    "TESTGRP0",
                    traits=TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_TRAITS,
                ),
            except SecurityResponseError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestConnectionConstants.TEST_CONNECT_CONNECTION_ERROR_LOG
        )
