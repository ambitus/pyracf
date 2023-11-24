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
        running_userid: Union[str, bool] = False,
    ) -> str:
        """Make request to call_irrsmo00 in the cpyracf Python extension."""
        options = 15 if precheck else 13
        if not running_userid:
            return call_irrsmo00(
                xml_str=request_xml,
                xml_len=len(request_xml),
                opts=options,
                userid="".encode("cp1047"),
                userid_len=0,
            ).decode("cp1047")
        return call_irrsmo00(
            xml_str=request_xml,
            xml_len=len(request_xml),
            opts=options,
            userid=running_userid.encode("cp1047"),
            userid_len=len(running_userid),
        ).decode("cp1047")
