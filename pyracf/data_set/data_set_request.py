"""Data Set Profile Administration Request Builder."""

from typing import Union

from pyracf.common.security_request import SecurityRequest


class DataSetRequest(SecurityRequest):
    """Data Set Profile Administration Request Builder."""

    def __init__(
        self, data_set: str, operation: str, volume: Union[str, bool], generic: bool
    ) -> None:
        super().__init__()
        self._security_definition.tag = "dataset"
        (volume, generic) = self._get_volume_and_generic_security_definition_values(
            volume, generic
        )
        self._security_definition.attrib.update(
            {
                "name": data_set,
                "operation": operation,
                "generic": generic,
                "volume": volume,
                "requestid": "DatasetRequest",
            }
        )
        if volume == "":
            del self._security_definition.attrib["volume"]
