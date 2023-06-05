"""Test general resource profile getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.genprof.test_genprof_constants as TestGenprofConstants
from pyracf import ResourceAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGenprofGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        return ResourceAdmin()

    # ============================================================================
    # ResourceAdmin.get_uacc(class_name)
    # ============================================================================
    def test_resource_admin_get_uacc_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            resource_admin.get_uacc("TESTING", "ELIJTEST").title() == "Read"
        )

    def test_resource_admin_get_uacc_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        genprof_extract_no_uacc = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        genprof_extract_no_uacc = genprof_extract_no_uacc.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          NONE               READ    NO</message>",
        )
        call_racf_mock.return_value = genprof_extract_no_uacc
        self.assertTrue(resource_admin.get_uacc("TESTING", "ELIJTEST") is None)

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_uacc_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            resource_admin.get_uacc("TESTING", "ELIJTEST")

    # ============================================================================
    # ResourceAdmin.get_your_acc(class_name)
    # ============================================================================
    def test_resource_admin_get_your_acc_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            resource_admin.get_your_acc("TESTING", "ELIJTEST").title() == "Read"
        )

    def test_resource_admin_get_your_acc_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        genprof_extract_no_your_acc = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        genprof_extract_no_your_acc = genprof_extract_no_your_acc.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ               NONE    NO</message>",
        )
        call_racf_mock.return_value = genprof_extract_no_your_acc
        self.assertTrue(resource_admin.get_your_acc("TESTING", "ELIJTEST") is None)

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_your_acc_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            resource_admin.get_your_acc("TESTING", "ELIJTEST")
