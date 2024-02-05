import contextlib
import io
import os
import platform
import re
import shutil
import unittest
import xml.etree.ElementTree
from unittest.mock import Mock, call, patch

import __init__
import ebcdic

import tests.common.test_common_constants as TestCommonConstants
import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin
from pyracf.common.utilities.dumper import Dumper

# Resolves F401
__init__
ebcdic


class TestDumpProcessing(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    dumper = Dumper()
    mock_home_directory = os.path.join(os.getcwd(), "common", "sandbox")
    os.path.expanduser = Mock(return_value=mock_home_directory)
    dot_pyracf_directory = os.path.join(mock_home_directory, ".pyracf")
    dump_directory = os.path.join(dot_pyracf_directory, "dump")
    timestamp = "20240108-131054"
    dump_file_name = f"pyracf.{timestamp}.e2c865db4162bed963bfaa9ef6ac18f0.dump"
    dump_file_path = os.path.join(dump_directory, dump_file_name)
    dump_bytes = bytes([i for i in range(256)])
    path_separator = "/"
    if platform.platform().split("-")[0] == "Windows":
        path_separator = "\\"

    @classmethod
    def setUpClass(self):
        os.makedirs(self.mock_home_directory)

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(self.mock_home_directory)

    def tearDown(self):
        shutil.rmtree(self.dot_pyracf_directory)

    # ============================================================================
    # Directories and Dump File Creation
    # ============================================================================
    @patch.object(Dumper, "_Dumper__get_timestamp")
    def test_create_pyracf_folder_dump_folder_and_dump_file(
        self, get_timestamp_mock: Mock
    ):
        get_timestamp_mock.return_value = self.timestamp
        # asume '.pyracf' directory does NOT exist.
        dump_file_path_actual = self.dumper.raw_dump(self.dump_bytes)
        # dump file path
        self.assertEqual(dump_file_path_actual, self.dump_file_path)
        # permission bits
        if platform.platform().split("-")[0] != "Windows":
            # Skip these tests on Windows because setting the
            # permissions bits on things does not work on Windows.
            self.assertEqual(
                oct(os.stat(self.dot_pyracf_directory).st_mode)[-3:], "700"
            )
            self.assertEqual(oct(os.stat(self.dump_directory).st_mode)[-3:], "700")
            self.assertEqual(oct(os.stat(self.dump_file_path).st_mode)[-3:], "600")
        # dump file contents
        with open(self.dump_file_path, "rb") as dump_file:
            self.assertEqual(dump_file.read(), self.dump_bytes)

    @patch.object(Dumper, "_Dumper__get_timestamp")
    def test_create_dump_folder_and_dump_file(self, get_timestamp_mock: Mock):
        get_timestamp_mock.return_value = self.timestamp
        # asumme '.pyracf' directory already exists
        os.makedirs(self.dot_pyracf_directory, mode=0o700)
        dump_file_path_actual = self.dumper.raw_dump(self.dump_bytes)
        # dump file path
        self.assertEqual(dump_file_path_actual, self.dump_file_path)
        # permission bits
        if platform.platform().split("-")[0] != "Windows":
            # Skip these tests on Windows because setting the
            # permissions bits on things does not work on Windows.
            self.assertEqual(
                oct(os.stat(self.dot_pyracf_directory).st_mode)[-3:], "700"
            )
            self.assertEqual(oct(os.stat(self.dump_directory).st_mode)[-3:], "700")
            self.assertEqual(oct(os.stat(self.dump_file_path).st_mode)[-3:], "600")
        # dump file contents
        with open(self.dump_file_path, "rb") as dump_file:
            self.assertEqual(dump_file.read(), self.dump_bytes)

    @patch.object(Dumper, "_Dumper__get_timestamp")
    def test_create_dump_file(self, get_timestamp_mock: Mock):
        get_timestamp_mock.return_value = self.timestamp
        # asumme '.pyracf' directory and dump directory already exist
        os.makedirs(self.dump_directory, mode=0o700)
        dump_file_path_actual = self.dumper.raw_dump(self.dump_bytes)
        # dump file path
        self.assertEqual(dump_file_path_actual, self.dump_file_path)
        # permission bits
        if platform.platform().split("-")[0] != "Windows":
            # Skip these tests on Windows because setting the
            # permissions bits on things does not work on Windows.
            self.assertEqual(
                oct(os.stat(self.dot_pyracf_directory).st_mode)[-3:], "700"
            )
            self.assertEqual(oct(os.stat(self.dump_directory).st_mode)[-3:], "700")
            self.assertEqual(oct(os.stat(self.dump_file_path).st_mode)[-3:], "600")
        # dump file contents
        with open(self.dump_file_path, "rb") as dump_file:
            self.assertEqual(dump_file.read(), self.dump_bytes)

    # ============================================================================
    # Debug Logging
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.clear_raw_response")
    @patch.object(Dumper, "_Dumper__get_timestamp")
    @patch("pyracf.common.irrsmo00.IRRSMO00.get_raw_response")
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_debug_and_dump_mode(
        self,
        call_racf_mock: Mock,
        get_raw_response_mock: Mock,
        get_timestamp_mock: Mock,
        clear_raw_response_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, dump_mode=True)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        get_raw_response_mock.return_value = bytes(
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            "cp1047",
        ).ljust(2048, b"\00")
        get_timestamp_mock.return_value = self.timestamp
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.extract("squidwrd")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        success_log = success_log.replace(
            f"{self.dump_directory}{self.path_separator}", "/u/testuser/.pyracf/dump/"
        )
        self.assertEqual(
            success_log, TestCommonConstants.TEST_EXTRACT_USER_SUCCESS_DUMP_MODE_LOG
        )
        get_raw_response_mock.assert_called_once()
        clear_raw_response_mock.assert_called_once()

    @patch("pyracf.common.irrsmo00.IRRSMO00.clear_raw_response")
    @patch.object(Dumper, "_Dumper__get_timestamp")
    @patch("pyracf.common.irrsmo00.IRRSMO00.get_raw_response")
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_debug_and_dump_mode_uneven_byte_boundary(
        self,
        call_racf_mock: Mock,
        get_raw_response_mock: Mock,
        get_timestamp_mock: Mock,
        clear_raw_response_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, dump_mode=True)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        get_raw_response_mock.return_value = bytes(
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            "cp1047",
        ).ljust(2007, b"\00")
        get_timestamp_mock.return_value = self.timestamp
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.extract("squidwrd")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        success_log = success_log.replace(
            f"{self.dump_directory}{self.path_separator}", "/u/testuser/.pyracf/dump/"
        )
        self.assertEqual(
            success_log,
            TestCommonConstants.TEST_EXTRACT_USER_SUCCESS_UNEVEN_BYTE_BOUNDARY_LOG,
        )
        get_raw_response_mock.assert_called_once()
        clear_raw_response_mock.assert_called_once()

    @patch("pyracf.common.irrsmo00.IRRSMO00.clear_raw_response")
    @patch.object(Dumper, "_Dumper__get_timestamp")
    @patch("pyracf.common.irrsmo00.IRRSMO00.get_raw_response")
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_debug_and_dump_mode_all_bytes(
        self,
        call_racf_mock: Mock,
        get_raw_response_mock: Mock,
        get_timestamp_mock: Mock,
        clear_raw_response_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, dump_mode=True)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        get_raw_response_mock.return_value = bytes(
            bytearray([i for i in range(256)])
        ).ljust(512, b"\00")
        get_timestamp_mock.return_value = self.timestamp
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.extract("squidwrd")
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        success_log = success_log.replace(
            f"{self.dump_directory}{self.path_separator}", "/u/testuser/.pyracf/dump/"
        )
        self.assertEqual(
            success_log,
            TestCommonConstants.TEST_EXTRACT_USER_SUCCESS_DUMP_MODE_ALL_BYTES_LOG,
        )
        get_raw_response_mock.assert_called_once()
        clear_raw_response_mock.assert_called_once()

    @patch("pyracf.common.irrsmo00.IRRSMO00.clear_raw_response")
    @patch.object(Dumper, "_Dumper__get_timestamp")
    @patch("pyracf.common.irrsmo00.IRRSMO00.get_raw_response")
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_debug_and_dump_mode_secrets_redaction(
        self,
        call_racf_mock: Mock,
        get_raw_response_mock: Mock,
        get_timestamp_mock: Mock,
        clear_raw_response_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, dump_mode=True)
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_PASSWORD_RESULT_SUCCESS_XML,
        ]
        get_raw_response_mock.return_value = bytes(
            TestUserConstants.TEST_ALTER_USER_PASSWORD_RESULT_SUCCESS_XML,
            "cp1047",
        ).ljust(1024, b"\00")
        get_timestamp_mock.return_value = self.timestamp
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        success_log = success_log.replace(
            f"{self.dump_directory}{self.path_separator}", "/u/testuser/.pyracf/dump/"
        )
        self.assertEqual(
            success_log, TestCommonConstants.TEST_ALTER_USER_PASSWORD_DUMP_MODE_LOG
        )
        get_raw_response_mock.assert_has_calls([call(), call()])
        clear_raw_response_mock.assert_has_calls([call(), call()])

    @patch("pyracf.common.irrsmo00.IRRSMO00.clear_raw_response")
    @patch.object(Dumper, "_Dumper__get_timestamp")
    @patch("pyracf.common.irrsmo00.IRRSMO00.get_raw_response")
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_debug_and_dump_mode_xml_parsing_failure(
        self,
        call_racf_mock: Mock,
        get_raw_response_mock: Mock,
        get_timestamp_mock: Mock,
        clear_raw_response_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, dump_mode=True)
        # Intentionally introduce XML syntax error.
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML[:-3]
        )
        get_raw_response_mock.return_value = bytes(
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML[:-3],
            "cp1047",
        ).ljust(2048, b"\00")
        get_timestamp_mock.return_value = self.timestamp
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                user_admin.extract("squidwrd")
            except xml.etree.ElementTree.ParseError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        error_log = error_log.replace(
            f"{self.dump_directory}{self.path_separator}", "/u/testuser/.pyracf/dump/"
        )
        self.assertEqual(
            error_log, TestCommonConstants.TEST_EXTRACT_USER_FAILURE_DUMP_MODE_LOG
        )
        get_raw_response_mock.assert_called_once()
        clear_raw_response_mock.assert_called_once()
