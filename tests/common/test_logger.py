"""Test the pyRACF logger."""

import unittest

import __init__

from pyracf.common.logger import Logger

# Resolves F401
__init__


class TestLogger(unittest.TestCase):
    logger = Logger()

    def test_logger_can_redact_secrets_from_result_xml(self):
        secret_traits = {"segment:trait": "namespace:secret"}
        unredacted_xml = "<a><b>text</b><c><d>SECRET (secret)</d></c></a>"
        redacted_xml_expected = "<a><b>text</b><c><d>SECRET (********)</d></c></a>"
        redacted_xml_actual = self.logger.redact_result_xml(
            unredacted_xml, secret_traits
        )
        self.assertEqual(redacted_xml_actual, redacted_xml_expected)

    def test_logger_can_redact_secrets_from_result_xml_trailing_space(self):
        secret_traits = {"segment:trait": "namespace:secret"}
        unredacted_xml = "<a><b>text</b><c><d>SECRET (secret) </d></c></a>"
        redacted_xml_expected = "<a><b>text</b><c><d>SECRET (********) </d></c></a>"
        redacted_xml_actual = self.logger.redact_result_xml(
            unredacted_xml, secret_traits
        )
        self.assertEqual(redacted_xml_actual, redacted_xml_expected)
