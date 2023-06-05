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

    def test_setropts_admin_build_alter_setropts_request(
        self, irrsmo00_init_mock: Mock
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.alter(options={"base:raclist": "elijtest"})
        self.assertEqual(result, TestSetroptsConstants.TEST_ALTER_SETROPTS_REQUEST_XML)

    def test_setropts_admin_build_list_setropts_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.list_racf_options()
        self.assertEqual(result, TestSetroptsConstants.TEST_LIST_SETROPTS_REQUEST_XML)
