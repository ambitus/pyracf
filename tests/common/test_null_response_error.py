"""Test general resource profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

from pyracf import NullResponseError, UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestNullResponseError(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    user_admin = UserAdmin()

    def test_null_response_error_thrown_on_null_response(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = ""
        with self.assertRaises(NullResponseError) as exception:
            self.user_admin.set_password("TESTUSER", "Testpass")
        self.assertEqual(
            exception.exception.message,
            "(NullResponseError) Security request made to IRRSMO00 failed."
            + "\n\nCheck to see if proper RACF permissions are in place.\n"
            + "For `set` or `alter` functions, you must have at least READ "
            + "access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class.",
        )
