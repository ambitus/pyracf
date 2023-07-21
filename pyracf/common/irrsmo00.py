"""Interface to irrsmo00.dll."""
import platform

try:
    from pyracf_call_irrsmo00 import pyracf_call_irrsmo00
except ImportError as import_error:
    if platform.system() == "OS/390":
        raise import_error

    # Ignore import of extension on non-z/OS platforms to allow for unit testing off platform.
    def pyracf_call_irrsmo00() -> None:
        return None


class IRRSMO00:
    """Interface to irrsmo00.dll."""

    def __init__(self) -> None:
        # Initialize size of output buffer
        self.buffer_size = 100000

    def call_racf(self, request_xml: bytes, options: int = 1) -> str:
        """Make request to IRRSMO00."""

        # Make call to pyobject to call SMO and decode result bytes
        return pyracf_call_irrsmo00(
            xml_str=request_xml, xml_len=len(request_xml), opts=options
        ).decode("cp1047")
