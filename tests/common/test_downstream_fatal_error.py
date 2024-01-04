"""Test downstream fatal error."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
from pyracf import DownstreamFatalError, UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestDownstreamFatalError(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    user_admin = UserAdmin()

    def test_donwstream_fatal_error_thrown_on_precheck_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = [8, 200, 16]
        with self.assertRaises(DownstreamFatalError) as exception:
            self.user_admin.set_password("TESTUSER", "Testpass")
        self.assertEqual(
            exception.exception.message,
            TestCommonConstants.TEST_DOWNSTREAM_FATAL_ERROR_PRECHECK_TEXT,
        )

    def test_donwstream_fatal_error_thrown_on_surrogat_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = [8, 200, 8]
        self.user_admin.set_running_userid("ESWIFT")
        with self.assertRaises(DownstreamFatalError) as exception:
            self.user_admin.add("squidwrd")
        self.assertEqual(
            exception.exception.message,
            TestCommonConstants.TEST_DOWNSTREAM_FATAL_ERROR_SURROGAT_TEXT,
        )

    def test_donwstream_fatal_error_thrown_on_miscellaneous_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = [8, 2000, 20]
        with self.assertRaises(DownstreamFatalError) as exception:
            self.user_admin.add("squidwrd")
        self.assertEqual(
            exception.exception.message,
            TestCommonConstants.TEST_DOWNSTREAM_FATAL_ERROR_GENERIC_TEXT,
        )
