"""Interface to irrsmo00.dll."""

import platform
from typing import Tuple, Union

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
        self.__raw_response = b""

    def get_raw_response(self) -> bytes:
        """Get the current preserved raw response from IRRSMO00."""
        return self.__raw_response

    def clear_raw_response(self) -> None:
        """Clear the current preserved raw response from IRRSMO00."""
        self.__raw_response = b""

    def __null_byte_fix(self, response: bytes) -> bytes:
        """
        This function replaces all null bytes that exist before the
        last occurance the '>' (0x6E in IBM-1047) character in the
        response ' ' (0x40 in IBM-1047) characters.
        This is a workaround for an issue where profile data embedded
        in response xml returned by IRROSMO00 sometimes includes null
        bytes instead of properly encoded text, which causes the
        returned xml to be truncated.
        """
        response = bytearray(response)
        last_greater_than = response.rfind(b"\x6e")
        for i in range(last_greater_than):
            if response[i] == 0:
                # 64 is 0x40, which is a space character in IBM-1047 encoding.
                response[i] = 64
        return bytes(response)

    def call_racf(
        self,
        request_xml: bytes,
        precheck: bool = False,
        run_as_userid: Union[str, None] = None,
    ) -> str:
        """Make request to call_irrsmo00 in the cpyracf Python extension."""
        irrsmo00_options = 15 if precheck else 13
        running_userid = b""
        if run_as_userid:
            running_userid = run_as_userid.encode("cp1047")
        response = self.__call_irrsmo00_wrapper(
            request_xml,
            len(request_xml),
            irrsmo00_options,
            running_userid,
            len(running_userid),
        )
        # Preserve raw binary respone just in case we need to create a dump.
        # If the decoded response cannot be parsed with the XML parser,
        # a dump may need to be taken to aid in problem determination.
        self.__raw_response = response[0]
        # Replace any null bytes in the XML response with spaces.
        response_xml = self.__null_byte_fix(response[0])
        # 'irrsmo00.c' returns a raw unmodified bytes object containing a copy
        # of the exact contents of the response xml buffer that the IRRSMO00
        # callable service populates.
        #
        # The first occurance of a null byte '0x00' is the end of the IBM-1047
        # encoded XML response and all of the trailing null bytes should be removed
        # from the XML response to ensure that downstream XML parsing is successful.
        response_length = len(response_xml)
        null_terminator_index = response_xml.find(b"\x00")
        if null_terminator_index != -1:
            response_length = null_terminator_index
        # If 'response_length' is 0, this indicates that the IRRSMO00 callable
        # service was unable to process the request. in this case, would should
        # only return the return and reasons codes for error handling downstream.
        if response_length == 0:
            return list(response[1:4])
        return response_xml[:response_length].decode("cp1047")

    def __call_irrsmo00_wrapper(
        self,
        request_xml: bytes,
        request_xml_length: int,
        irrsmo00_options: int,
        running_userid: bytes,
        running_userid_length: int,
    ) -> Tuple[bytes, int, int, int]:
        return call_irrsmo00(
            request_xml=request_xml,
            request_xml_length=request_xml_length,
            response_buffer_size=self.__response_buffer_size,
            irrsmo00_options=irrsmo00_options,
            running_userid=running_userid,
            running_userid_length=running_userid_length,
        )
