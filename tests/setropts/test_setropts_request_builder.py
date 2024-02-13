"""Test setropts request builder."""

import unittest

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SetroptsAdmin

# Resolves F401
__init__


class TestSetroptsRequestBuilder(unittest.TestCase):
    maxDiff = None
    setropts_admin = SetroptsAdmin(generate_requests_only=True)

    def test_setropts_admin_build_alter_setropts_request(self):
        result = self.setropts_admin.alter(options={"base:raclist": "elijtest"})
        self.assertEqual(result, TestSetroptsConstants.TEST_ALTER_SETROPTS_REQUEST_XML)

    def test_setropts_admin_build_list_setropts_request(self):
        result = self.setropts_admin.list_racf_options()
        self.assertEqual(result, TestSetroptsConstants.TEST_LIST_SETROPTS_REQUEST_XML)
