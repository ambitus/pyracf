"""Interface to irrsmo00.dll."""

import ctypes
import os

from call_smo import call_smo


class IRRSMO00:
    """Interface to irrsmo00.dll."""

    def __init__(self) -> None:
        # Initialize size of output buffer
        self.buffer_size = 100000

    def call_racf(self, request_xml: bytes, options: int = 1) -> str:
        """Make request to IRRSMO00."""
        # Initialize bytes object for output buffer
        rsp = bytes(10000)
        # Make call to pyobject to call SMO
        rsp = call_smo(xml_str=request_xml, xml_len=len(request_xml), opts=options)

        # Decode result bytes from pyobject
        return rsp.decode("cp1047")
