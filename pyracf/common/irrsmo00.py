"""Interface to irrsmo00.dll."""
import platform
from typing import Union

try:
    from cpyracf import call_irrsmo00
except ImportError as import_error:
    if platform.system() == "OS/390":
        raise import_error

    # Ignore import of extension on non-z/OS platforms to allow for unit testing off platform.
    def call_irrsmo00() -> None:
        return None


class IRRSMO00:
    """Interface to irrsmo00 callable service through cpyracf Python extension."""

    def __init__(self, response_buffer_size=16384) -> None:
        # Initialize size of the response buffer (16 kilobytes by default)
        self.__response_buffer_size = response_buffer_size
        self.__raw_binary_response = b""

    def get_raw_binary_response(self) -> bytes:
        return bytes(self.__raw_binary_response)

    def clear_raw_binary_response(self) -> None:
        self.__raw_binary_response = b""

    def call_racf(
        self,
        request_xml: bytes,
        precheck: bool = False,
        run_as_userid: Union[str, None] = None,
    ) -> str:
        """Make request to call_irrsmo00 in the cpyracf Python extension."""
        irrsmo00_options = 15 if precheck else 13
        running_userid = b""
        running_userid_length = 0
        if run_as_userid:
            running_userid = run_as_userid.encode("cp1047")
            running_userid_length = len(run_as_userid)
        response = call_irrsmo00(
            request_xml=request_xml,
            request_xml_length=len(request_xml),
            response_buffer_size=self.__response_buffer_size,
            irrsmo00_options=irrsmo00_options,
            running_userid=running_userid,
            running_userid_lngth=running_userid_length,
        )
        if response[0] == b"":
            return list(response[1:4])
        # Preserve raw binary respone just in case we need to create a dump.
        # If the decoded response cannot be parsed with the XML parser,
        # a dump may need to be taken to aid in problem determination.
        # Also note that the response xml returned is a memory view object.
        # We must cast the memoryview object to a bytes object.
        # Python C API 'y*': https://python.readthedocs.io/en/stable/c-api/arg.html
        # Py_buffer: https://docs.python.org/3/c-api/buffer.html#c.Py_buffer
        # memory view objects: https://www.geeksforgeeks.org/memoryview-in-python/
        self.__raw_binary_response = response[0]
        return bytes(response[0]).decode("cp1047")
