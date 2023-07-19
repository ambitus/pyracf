"""Interface to irrsmo00.dll."""
import platform

try:
    from call_irrsmo import call_irrsmo
except ImportError as import_error:
    if platform.system() == "OS/390":
        raise import_error

    def call_irrsmo(xml_str, xml_len, opts):
        return "SERIOUS ERROR".encode("cp1047")


class IRRSMO00:
    """Interface to irrsmo00.dll."""

    def __init__(self) -> None:
        # Initialize size of output buffer
        self.buffer_size = 100000

    def call_racf(self, request_xml: bytes, options: int = 1) -> str:
        """Make request to IRRSMO00."""
        # Make call to pyobject to call SMO and decode result bytes
        rsp = call_irrsmo(
            xml_str=request_xml, xml_len=len(request_xml), opts=options
        ).decode("cp1047")

        # Return the decoded string
        return rsp
