"""Data Set Profile Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class DatasetRequest(SecurityRequest):
    """Data Set Profile Administration Request Builder."""

    def __init__(self, traits: dict, operation: str) -> None:
        super().__init__()
        self.security_definition.tag = "dataset"

        if "generic" not in traits:
            traits["generic"] = "no"
        if "volid" not in traits:
            traits["volid"] = ""

        self.security_definition.attrib = {
            "name": traits["datasetname"],
            "operation": operation,
            "generic": traits["generic"],
            "requestid": "DatasetRequest",
        }
        self.set_volid_and_generic(traits)
