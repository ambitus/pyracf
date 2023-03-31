"""Access Request Builder."""

from pyracf.common.security_request import SecurityRequest


class AccessRequest(SecurityRequest):
    """Access Request Builder."""

    def __init__(
        self,
        traits: dict,
        operation: str,
    ) -> None:
        super().__init__()
        self.security_definition.tag = "permission"
        self.set_volid_and_generic(traits)
        self.security_definition.attrib.update(
            {
                "name": traits["resourcename"],
                "class": traits["classname"],
                "operation": operation,
                "requestid": "AccessRequest",
            }
        )
