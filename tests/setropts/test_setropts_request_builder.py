"""Test setropts request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SetroptsAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestSetroptsRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> SetroptsAdmin:
        irrsmo00_init_mock.return_value = None
        return SetroptsAdmin(generate_requests_only=True)

    def test_setropts_admin_build_command_setropts_request(
        self, irrsmo00_init_mock: Mock
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.command(
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestSetroptsConstants.TEST_COMMAND_SETROPTS_REQUEST_XML
        )

    def test_setropts_admin_build_list_setropts_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.list_ropts()
        self.assertEqual(result, TestSetroptsConstants.TEST_LIST_SETROPTS_REQUEST_XML)
