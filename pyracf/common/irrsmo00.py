"""Interface to irrsmo00.dll."""

import ctypes
import os


class IRRSMO00:
    """Interface to irrsmo00.dll."""

    def __init__(self) -> None:
        # Use PWD to build path to DLL and load it.
        self.buffer_size = 10000

    def call_racf(self, request_xml: bytes, opts: int = 1) -> str:
        """Make request to IRRSMO00."""
        # Specify return type and argument types

        req_opts = ctypes.c_uint(opts)
        req_len = ctypes.c_uint(len(request_xml))
        req_buf = (ctypes.c_char * (self.buffer_size))(*request_xml)
        print(request_xml)
        return -1
        # Decode result bytes from
        #return self.dll.call_irrsmo00(req_buf, req_len, req_opts).decode("cp1047")
