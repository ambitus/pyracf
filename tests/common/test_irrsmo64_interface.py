import unittest

import ebcdic

import tests.common.test_common_constants as TestCommonConstants
import tests.resource.test_resource_constants as TestResourceConstants
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
ebcdic


class TestIRRSMO64Interface(unittest.TestCase):
    maxDiff = None
    running_userid = b""
    buffer_size = 1500
    irrsmo00 = IRRSMO00(result_buffer_size=1500)

    # ============================================================================
    # Test IRRSMO64 Result Responses in cpyracf
    # ============================================================================
    def test_irrsmo64_basic_call(
        self,
    ):
        request_xml = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_REQUEST_BASE_XML.decode(
                "utf-8"
            ).encode("cp1047")
        )
        result = self.irrsmo00.call_racf(request_xml)
        self.assertEqual(
            result, TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )

    def test_irrsmo64_redrive_call(self):
        request_xml = TestCommonConstants.TEST_EXTRACT_RESOURCE_REQUEST_ALL_XFACILIT_XML
        result = self.irrsmo00.call_racf(request_xml)
        self.assertEqual(
            result,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_XML,
        )

    def test_irrsmo64_too_big_call(self):
        request_xml = TestCommonConstants.TEST_EXTRACT_RESOURCE_REQUEST_ALL_FACILITY_XML
        result = self.irrsmo00.call_racf(request_xml)
        self.assertEqual(result, [8, 4000, 100000000])
