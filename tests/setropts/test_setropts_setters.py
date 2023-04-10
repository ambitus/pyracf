"""Test setropts setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf.setropts.setropts_admin import SetroptsAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestSetroptsSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> SetroptsAdmin:
        irrsmo00_init_mock.return_value = None
        return SetroptsAdmin()

    def test_setropts_admin_build_audit_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.audit_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_AUDIT_ADD_XML)

    def test_setropts_admin_build_classact_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.classact_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_CLASSACT_ADD_XML)

    def test_setropts_admin_build_classtat_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.classstat_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_CLASSTAT_ADD_XML)

    def test_setropts_admin_build_gencmd_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.gencmd_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENCMD_ADD_XML)

    def test_setropts_admin_build_generic_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.generic_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENERIC_ADD_XML)

    def test_setropts_admin_build_genlist_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.genlist_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENLIST_ADD_XML)

    def test_setropts_admin_build_global_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.global_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GLOBAL_ADD_XML)

    def test_setropts_admin_build_raclist_add_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.raclist_add("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_RACLIST_ADD_XML)

    def test_setropts_admin_build_audit_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.audit_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_AUDIT_DEL_XML)

    def test_setropts_admin_build_classact_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.classact_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_CLASSACT_DEL_XML)

    def test_setropts_admin_build_classtat_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.classstat_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_CLASSTAT_DEL_XML)

    def test_setropts_admin_build_gencmd_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.gencmd_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENCMD_DEL_XML)

    def test_setropts_admin_build_generic_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.generic_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENERIC_DEL_XML)

    def test_setropts_admin_build_genlist_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.genlist_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GENLIST_DEL_XML)

    def test_setropts_admin_build_global_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.global_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_GLOBAL_DEL_XML)

    def test_setropts_admin_build_raclist_del_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.raclist_del("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_RACLIST_DEL_XML)

    def test_setropts_admin_build_refresh_request(self, irrsmo00_init_mock: Mock):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        result = setropts_admin.refresh("ELIJTEST", generate_request_only=True)
        self.assertEqual(result, TestSetroptsConstants.TEST_SETROPTS_REFRESH_CLASS_XML)
