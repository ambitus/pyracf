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
        return self.__raw_binary_response

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
            running_userid_length=running_userid_length,
        )
        # Preserve raw binary respone just in case we need to create a dump.
        # If the decoded response cannot be parsed with the XML parser,
        # a dump may need to be taken to aid in problem determination.
        self.__raw_binary_response = response[0]
        # 'irrsmo00.c' returns a raw unmodified bytes object containing a copy
        # of the exact contents of the response xml buffer that the IRRSMO00
        # callable service populates.
        #
        # The first occurance of a null byte '0x00' is the end of the IBM-1047
        # encoded XML response and all of the trailing null bytes should be removed
        # from the XML response to ensure that downstream XML parsing is successful.
        response_length = len(response[0])
        null_terminator_index = response[0].find(b"\x00")
        if null_terminator_index != -1:
            response_length = null_terminator_index
        # If 'response_length' is 0, this indicates that the IRRSMO00 callable
        # service was unable to process the request. in this case, would should
        # only return the return and reasons codes for error handling downstream.
        if response_length == 0:
            return list(response[1:4])
        return response[0][:response_length].decode("cp1047")
