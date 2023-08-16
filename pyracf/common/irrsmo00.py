"""Interface to irrsmo00.dll."""
import platform

try:
    from cpyracf import call_irrsmo00
except ImportError as import_error:
    if platform.system() == "OS/390":
        raise import_error

    # Ignore import of extension on non-z/OS platforms to allow for unit testing off platform.
    def call_irrsmo00() -> None:
        return None


class IRRSMO00:
    """Interface to irrsmo00 callable service through cpyracf Python extension"""

    def __init__(self) -> None:
        # Initialize size of output buffer
        self.buffer_size = 100000

    def call_racf(self, request_xml: bytes, precheck: bool = False) -> str:
        """Make request to call_irrsmo00 in the cpyracf Python extension."""
        options = 11 if precheck else 9
        return call_irrsmo00(
            xml_str=request_xml, xml_len=len(request_xml), opts=options
        ).decode("cp1047")
