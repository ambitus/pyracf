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

    def __init__(self) -> None:
        # Initialize size of output buffer
        self.buffer_size = 100000

    def call_racf(
        self,
        request_xml: bytes,
        precheck: bool = False,
        run_as_userid: Union[str, None] = None,
    ) -> str:
        """Make request to call_irrsmo00 in the cpyracf Python extension."""
        options = 15 if precheck else 13
        userid = b""
        userid_length = 0
        if run_as_userid:
            userid = run_as_userid.encode("cp1047")
            userid_length = len(run_as_userid)
        response = call_irrsmo00(
            xml_str=request_xml,
            xml_len=len(request_xml),
            opts=options,
            userid=userid,
            userid_len=userid_length,
        )
        if response[0] == b"":
            return list(response[1:4])
        return response[0].decode("cp1047")
