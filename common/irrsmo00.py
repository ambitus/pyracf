import ctypes
import os


class IRRSMO00:
    def __init__(self) -> None:
        # Use PWD to build path to DLL and load it.
        self.dll = ctypes.CDLL(f"{os.path.dirname(__file__)}/irrsmo00.dll")
        self.buffer_size = 10000

    def call_racf(self, request_xml: bytes, opts: int = 1) -> bytes:
        # Specify return type and argument types
        self.dll.call_irrsmo00.restype = ctypes.c_char_p
        self.dll.call_irrsmo00.argtypes = [ctypes.c_char * self.buffer_size, ctypes.c_uint, ctypes.c_uint]
        req_opts = ctypes.c_uint(opts)
        req_len = ctypes.c_uint (len(request_xml))
        req_buf = (ctypes.c_char * (self.buffer_size))(*request_xml)
        # Decode result bytes from 
        return self.dll.call_irrsmo00(req_buf,req_len,req_opts).decode("cp1047")
