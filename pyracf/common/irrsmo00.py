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

    def __init__(self, result_buffer_size=16384) -> None:
        # Initialize size of the result buffer (16 kilobytes by default)
        self.__result_buffer_size = result_buffer_size
        self.__raw_result_xml = b""

    def get_raw_result_xml(self) -> bytes:
        """Get the current preserved raw result XML from IRRSMO00."""
        return self.__raw_result_xml

    def clear_raw_result_xml(self) -> None:
        """Clear the current preserved raw result XML from IRRSMO00."""
        self.__raw_result_xml = b""

    def __null_byte_fix(self, result_xml: bytes) -> bytes:
        """
        This function replaces all null bytes that exist before the
        last occurance the '>' (0x6E in IBM-1047) character in the
        result XML with ' ' (0x40 in IBM-1047) characters.
        This is a workaround for an issue where profile data embedded
        in result XML returned by IRROSMO00 sometimes includes null
        bytes instead of properly encoded text, which causes the
        returned xml to be truncated.
        """
        result_xml = bytearray(result_xml)
        last_greater_than = result_xml.rfind(b"\x6e")
        for i in range(last_greater_than):
            if result_xml[i] == 0:
                # 64 is 0x40, which is a space character in IBM-1047 encoding.
                result_xml[i] = 64
        return bytes(result_xml)

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
        result = call_irrsmo00(
            request_xml=request_xml,
            request_xml_length=len(request_xml),
            result_buffer_size=self.__result_buffer_size,
            irrsmo00_options=irrsmo00_options,
            running_userid=running_userid,
            running_userid_length=len(running_userid),
        )
        # Preserve raw result XML just in case we need to create a dump.
        # If the decoded result XML cannot be parsed with the XML parser,
        # a dump may need to be taken to aid in problem determination.
        self.__raw_result_xml = result[0]
        # Replace any null bytes in the result XML with spaces.
        result_xml = self.__null_byte_fix(result[0])
        # 'irrsmo00.c' returns a raw unmodified bytes object containing a copy
        # of the exact contents of the result xml buffer that the IRRSMO00
        # callable service populates.
        #
        # The first occurance of a null byte '0x00' is the end of the IBM-1047
        # encoded result XML and all of the trailing null bytes should be removed
        # from the result XML to ensure that downstream XML parsing is successful.
        result_xml_length = len(result_xml)
        null_terminator_index = result_xml.find(b"\x00")
        if null_terminator_index != -1:
            result_xml_length = null_terminator_index
        # If 'result_xml_length' is 0, this indicates that the IRRSMO00 callable
        # service was unable to process the request. in this case, would should
        # only return the return and reasons codes for error handling downstream.
        if result_xml_length == 0:
            return list(result[1:4])
        return result_xml[:result_xml_length].decode("cp1047")
