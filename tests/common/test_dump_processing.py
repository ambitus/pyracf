import os
import platform
import shutil
import unittest
from unittest.mock import Mock, patch

import __init__

from pyracf.common.irrsmo00 import IRRSMO00
from pyracf.common.logger import Logger

# Resolves F401
__init__


class TestDumpProcessing(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    logger = Logger()
    mock_home_directory = os.path.join(os.getcwd(), "common", "sandbox")
    os.path.expanduser = Mock(return_value=mock_home_directory)
    dot_pyracf_directory = os.path.join(mock_home_directory, ".pyracf")
    dump_directory = os.path.join(dot_pyracf_directory, "dump")
    timestamp = "20240108-131054"
    dump_file_name = f"pyracf.{timestamp}.e2c865db4162bed963bfaa9ef6ac18f0.dump"
    dump_file_path = os.path.join(dump_directory, dump_file_name)
    dump_bytes = bytes([i for i in range(256)])

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
    @patch("pyracf.common.logger.Logger.get_timestamp")
    def test_create_pyracf_folder_dump_folder_and_dump_file(
        self, get_timestamp_mock: Mock
    ):
        get_timestamp_mock.return_value = self.timestamp
        dump_file_path_actual = self.logger.binary_dump(self.dump_bytes)
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

    @patch("pyracf.common.logger.Logger.get_timestamp")
    def test_create_dump_folder_and_dump_file(self, get_timestamp_mock: Mock):
        get_timestamp_mock.return_value = self.timestamp
        # asumme .pyracf directory already exists
        os.makedirs(self.dot_pyracf_directory, mode=0o700)
        dump_file_path_actual = self.logger.binary_dump(self.dump_bytes)
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

    @patch("pyracf.common.logger.Logger.get_timestamp")
    def test_create_dump_file(self, get_timestamp_mock: Mock):
        get_timestamp_mock.return_value = self.timestamp
        # asumme .pyracf directory and dump directory already exist
        os.makedirs(self.dump_directory, mode=0o700)
        dump_file_path_actual = self.logger.binary_dump(self.dump_bytes)
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
