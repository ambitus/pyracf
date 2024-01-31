import unittest
from unittest.mock import Mock, patch

import ebcdic

from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
ebcdic


class TestIRRSMO00Interface(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)

    @patch.object(IRRSMO00, "_IRRSMO00__call_irrsmo00_wrapper")
    def test_null_byte_fix(
        self,
        call_irrsmo00_wrapper_mock: Mock,
    ):
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
        good_xml_null_terminator_index = good_xml.find(b"\x00")
        call_irrsmo00_wrapper_mock.return_value = [xml_containing_null_bytes, 0, 0, 0]
        self.assertEqual(
            irrsmo00.call_racf(b""),
            good_xml.decode("cp1047")[:good_xml_null_terminator_index],
        )

    def test_null_response(self):
        pass
