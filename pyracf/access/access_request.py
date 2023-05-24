"""Access Request Builder."""

from typing import Union

from pyracf.common.security_request import SecurityRequest


class AccessRequest(SecurityRequest):
    """Access Request Builder."""

    def __init__(
        self,
        resource: str,
        class_name: str,
        operation: str,
        volume: Union[str, bool],
        generic: bool,
    ) -> None:
        super().__init__()
        self.security_definition.tag = "permission"
        (volume, generic) = self.get_volume_and_generic_security_definition_values(
            volume, generic
        )
        self.security_definition.attrib.update(
            {
                "name": resource,
                "class": class_name,
                "operation": operation,
                "generic": generic,
                "volume": volume,
                "requestid": "AccessRequest",
            }
        )
        if volume == "":
            del self.security_definition.attrib["volume"]
        if generic == "no":
            del self.security_definition.attrib["generic"]
