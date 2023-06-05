"""Interface to irrsmo00.dll."""

import ctypes
import os


class IRRSMO00:
    """Interface to irrsmo00.dll."""

    def __init__(self) -> None:
        # Use PWD to build path to DLL and load it.
        self.dll = ctypes.CDLL(f"{os.path.dirname(__file__)}/irrsmo00.dll")
        self.buffer_size = 10000

    def call_racf(self, request_xml: bytes, options: int = 1) -> str:
        """Make request to IRRSMO00."""
        # Specify return type and argument types
        self.dll.call_irrsmo00.restype = ctypes.c_char_p
        self.dll.call_irrsmo00.argtypes = [
            ctypes.c_char * self.buffer_size,
            ctypes.c_uint,
            ctypes.c_uint,
        ]
        req_opts = ctypes.c_uint(options)
        req_len = ctypes.c_uint(len(request_xml))
        req_buf = (ctypes.c_char * (self.buffer_size))(*request_xml)
        # Decode result bytes from
        return self.dll.call_irrsmo00(req_buf, req_len, req_opts).decode("cp1047")
