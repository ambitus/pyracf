import unittest
from unittest.mock import Mock, patch

import ebcdic

from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
ebcdic
IRRSMO00


# @patch.object(IRRSMO00, "_IRRSMO00__call_irrsmo00_wrapper")
@patch("pyracf.common.irrsmo00.call_irrsmo00")
class TestIRRSMO00Interface(unittest.TestCase):
    maxDiff = None
    irrsmo00 = IRRSMO00()
    # deactivate black temporarily
    # fmt: off
    good_xml = bytes([
        76, 163, 129, 135, 241, 110, 76, 163, 129, 135,
        242, 110, 210, 197, 232, 241, 64, 126, 64, 229,
        193, 211, 228, 197, 241, 76, 97, 163, 129, 135,
        242, 110, 76, 163, 129, 135, 243, 110, 210, 197,
        232, 242, 64, 126, 64, 64, 64, 64, 64, 76,
        97, 163, 129, 135, 243, 110, 76, 97, 163, 129,
        135, 241, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
    ])
    # fmt: on
    good_xml_null_terminator_index = good_xml.find(b"\x00")

    # ============================================================================
    # Test IRRSMO00 Result XML Post Processing
    # ============================================================================
    def test_irrsmo00_null_byte_fix(
        self,
        call_irrsmo00_wrapper_mock: Mock,
    ):
        # deactivate black temporarily
        # fmt: off
        xml_containing_null_bytes = bytes([
            76, 163, 129, 135, 241, 110, 76, 163, 129, 135,
            242, 110, 210, 197, 232, 241, 64, 126, 64, 229,
            193, 211, 228, 197, 241, 76, 97, 163, 129, 135,
            242, 110, 76, 163, 129, 135, 243, 110, 210, 197,
            232, 242, 64, 126, 64, 0, 0, 0, 0, 76,
            97, 163, 129, 135, 243, 110, 76, 97, 163, 129,
            135, 241, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
        ])
        # fmt: on
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": xml_containing_null_bytes,
            "returnCodes": [0, 0, 0],
        }
        self.assertEqual(
            self.irrsmo00.call_racf(b""),
            self.good_xml.decode("cp1047")[: self.good_xml_null_terminator_index],
        )

    def test_irrsmo00_empty_result(
        self,
        call_irrsmo00_wrapper_mock: Mock,
    ):
        # Simulate failure due to incomplete 'IRR.IRRSMO00.PRECHECK' setup
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": bytes([0 for i in range(256)]),
            "returnCodes": [8, 200, 16],
        }
        self.assertEqual(self.irrsmo00.call_racf(b""), [8, 200, 16])

    def test_irrsmo00_result_buffer_full_failure(
        self,
        call_irrsmo00_wrapper_mock: Mock,
    ):
        # Simulate scenario where result buffer is too small.
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml[:32],
            "returnCodes": [8, 4000, 100000000],
        }
        self.assertEqual(
            self.irrsmo00.call_racf(b""), self.good_xml.decode("cp1047")[:32]
        )

    # def test_irrsmo00_result_buffer_full_redrive(
    #     self,
    #     call_irrsmo00_wrapper_mock: Mock,
    # ):
    #     # Simulate scenario where result buffer is too small.
    #     call_irrsmo00_wrapper_mock.side_effect = [
    #     {
    #         "resultBuffer": self.good_xml[:32],
    #         "returnCodes": [8, 4000, 32],
    #     },
    #     {
    #         "resultBuffer": self.good_xml[32:],
    #         "returnCodes": [0, 0, 0],
    #     },
    #     ]
    #     self.assertEqual(
    #         self.irrsmo00.call_racf(b""), self.good_xml.decode("cp1047")
    #     )

    def test_irrsmo00_result_buffer_full_success(
        self,
        call_irrsmo00_wrapper_mock: Mock,
    ):
        # Simulate scenario where result buffer is exactly the right size.
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml[: self.good_xml_null_terminator_index],
            "returnCodes": [0, 0, 0],
        }
        self.assertEqual(
            self.irrsmo00.call_racf(b""),
            self.good_xml.decode("cp1047")[: self.good_xml_null_terminator_index],
        )

    def test_irrsmo00_normal_result(self, call_irrsmo00_wrapper_mock: Mock):
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml,
            "returnCodes": [0, 0, 0],
        }
        self.assertEqual(
            self.irrsmo00.call_racf(b""),
            self.good_xml.decode("cp1047")[: self.good_xml_null_terminator_index],
        )

    # ============================================================================
    # Test IRRSMO00 Argument Construction
    # ============================================================================
    def test_irrsmo00_minimum_arguments(self, call_irrsmo00_wrapper_mock: Mock):
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml,
            "returnCodes": [0, 0, 0],
        }
        self.irrsmo00.call_racf(b"some bytes")
        call_irrsmo00_wrapper_mock.assert_called_with(
            request_xml=b"some bytes",
            request_xml_len=10,
            result_buffer_size=16384,
            irrsmo00_options=13,
            running_userid=b"",
            running_userid_len=0,
        )

    def test_irrsmo00_with_precheck_set_to_true(self, call_irrsmo00_wrapper_mock: Mock):
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml,
            "returnCodes": [0, 0, 0],
        }
        self.irrsmo00.call_racf(b"some bytes", precheck=True)
        call_irrsmo00_wrapper_mock.assert_called_with(
            request_xml=b"some bytes",
            request_xml_len=10,
            result_buffer_size=16384,
            irrsmo00_options=15,
            running_userid=b"",
            running_userid_len=0,
        )

    def test_irrsmo00_with_run_as_userid_set(self, call_irrsmo00_wrapper_mock: Mock):
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml,
            "returnCodes": [0, 0, 0],
        }
        self.irrsmo00.call_racf(b"some bytes", run_as_userid="KRABS")
        call_irrsmo00_wrapper_mock.assert_called_with(
            request_xml=b"some bytes",
            request_xml_len=10,
            result_buffer_size=16384,
            irrsmo00_options=13,
            running_userid=b"\xd2\xd9\xc1\xc2\xe2",
            running_userid_len=5,
        )

    def test_irrsmo00_with_custom_result_buffer_size(
        self, call_irrsmo00_wrapper_mock: Mock
    ):
        call_irrsmo00_wrapper_mock.return_value = {
            "resultBuffer": self.good_xml,
            "returnCodes": [0, 0, 0],
        }
        irrsmo00 = IRRSMO00(result_buffer_size=32768)
        irrsmo00.call_racf(b"some bytes")
        call_irrsmo00_wrapper_mock.assert_called_with(
            request_xml=b"some bytes",
            request_xml_len=10,
            result_buffer_size=32768,
            irrsmo00_options=13,
            running_userid=b"",
            running_userid_len=0,
        )
