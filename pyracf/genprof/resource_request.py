"""General Resource Profile Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class ResourceRequest(SecurityRequest):
    """General Resource Profile Administration Request Builder."""

    def __init__(self, resourcename: str, classname: str, operation: str) -> None:
        super().__init__()
        self._security_definition.tag = "resource"
        self._security_definition.attrib = {
            "name": resourcename,
            "class": classname,
            "operation": operation,
            "requestid": "ResourceRequest",
        }
