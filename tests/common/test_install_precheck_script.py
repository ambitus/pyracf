"""Test included script to initialize and evaluate precheck permissions."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
from pyracf import setup_precheck
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestInstallPrecheckScript(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def test_install_precheck_works_when_no_setup_done(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_ERROR_XML,
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_ERROR_XML,
            TestCommonConstants.TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            precheck_log, TestCommonConstants.TEST_INSTALL_PRECHECK_DEFINED_PROFILE_TEXT
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ADD_RESOURCE_PRECHECK_UACC_NONE_SUCCESS_DICTIONARY,
        )

    def test_install_precheck_works_when_alter_access_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            precheck_log,
            TestCommonConstants.TEST_INSTALL_PRECHECK_VALIDATED_ACCESS_TEXT,
        )
        self.assertEqual(result, True)

    def test_install_precheck_works_when_control_access_exists(
        self,
        call_racf_mock: Mock,
    ):
        extract_with_control_access = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        extract_with_control_access = extract_with_control_access.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ             CONTROL   NO</message>",
        )
        call_racf_mock.return_value = extract_with_control_access
        validated_control_access = (
            TestCommonConstants.TEST_INSTALL_PRECHECK_VALIDATED_ACCESS_TEXT
        )
        validated_control_access = validated_control_access.replace(
            "you already have alter access!", "you already have control access!"
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(precheck_log, validated_control_access)
        self.assertEqual(result, True)

    def test_install_precheck_works_when_read_access_exists(
        self,
        call_racf_mock: Mock,
    ):
        extract_with_read_access = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        extract_with_read_access = extract_with_read_access.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ              READ     NO</message>",
        )
        call_racf_mock.return_value = extract_with_read_access
        validated_read_access = (
            TestCommonConstants.TEST_INSTALL_PRECHECK_VALIDATED_ACCESS_TEXT
        )
        validated_read_access = validated_read_access.replace(
            "you already have alter access!", "you already have read access!"
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(precheck_log, validated_read_access)
        self.assertEqual(result, True)

    def test_install_precheck_works_when_update_access_exists(
        self,
        call_racf_mock: Mock,
    ):
        extract_with_update_access = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        extract_with_update_access = extract_with_update_access.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ             UPDATE    NO</message>",
        )
        call_racf_mock.return_value = extract_with_update_access
        validated_update_access = (
            TestCommonConstants.TEST_INSTALL_PRECHECK_VALIDATED_ACCESS_TEXT
        )
        validated_update_access = validated_update_access.replace(
            "you already have alter access!", "you already have update access!"
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(precheck_log, validated_update_access)
        self.assertEqual(result, True)

    def test_install_precheck_works_when_none_access_exists(
        self,
        call_racf_mock: Mock,
    ):
        extract_with_none_access = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        extract_with_none_access = extract_with_none_access.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ              NONE     NO</message>",
        )
        call_racf_mock.return_value = extract_with_none_access
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = setup_precheck()
        precheck_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            precheck_log, TestCommonConstants.TEST_INSTALL_PRECHECK_FOUND_NO_ACCESS_TEXT
        )
        self.assertEqual(result, False)
