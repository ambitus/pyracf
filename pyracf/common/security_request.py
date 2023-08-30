"""Generic Security Request builder."""

import platform
import xml.etree.ElementTree as XMLBuilder
from typing import Union


class SecurityRequest:
    """Generic Security Request builder."""

    def __init__(self) -> None:
        self.__racf_request = XMLBuilder.Element("securityrequest")
        self.__racf_request.attrib = {
            "xmlns": "http://www.ibm.com/systems/zos/saf",
            "xmlns:racf": "http://www.ibm.com/systems/zos/racf",
        }
        self._security_definition = XMLBuilder.SubElement(
            self.__racf_request, "undefined"
        )

    def _get_volume_and_generic_security_definition_values(
        self, volume: Union[str, None], generic: bool
    ) -> None:
        """Get volid and generic xml values for security definition."""
        security_definition_volume = ""
        security_definition_generic = "no"
        if volume:
            security_definition_volume = volume
        if generic:
            security_definition_generic = "yes"
        return (security_definition_volume, security_definition_generic)

    def _build_segments(
        self,
        segment_traits_dictionary: dict,
        trait_map: dict,
        alter: bool = False,
        extract: bool = False,
    ) -> None:
        """Build XML representation of segments."""
        for segment, segment_traits in segment_traits_dictionary.items():
            self._build_segment(
                segment,
                segment_traits,
                trait_map,
                alter=alter,
                extract=extract,
            )

    def _build_segment(
        self,
        segment_name: str,
        traits: dict,
        trait_map: dict,
        alter: bool = False,
        extract: bool = False,
    ) -> None:
        """Build segment in XML format."""
        if not traits:
            return
        if segment_name:
            segment = XMLBuilder.SubElement(self._security_definition, segment_name)
        else:
            segment = self._security_definition
        if isinstance(traits, bool):
            return
        for trait in traits:
            if isinstance(traits[trait], bool) and not traits[trait] and not alter:
                continue
            trait_element = XMLBuilder.SubElement(segment, trait_map[trait])
            value = traits[trait]["value"]
            operation = traits[trait]["operation"]
            if operation:
                if operation == "delete":
                    operation = "del"
                trait_element.attrib = {"operation": operation}
            if not operation and alter:
                trait_element.attrib = {"operation": "set"}
            if isinstance(value, list):
                trait_element.text = " ".join(value)
                # trait_element.attrib = {"operation": operation}
                continue
            if not isinstance(value, bool):
                trait_element.text = str(value)
        if len(list(segment.iter())) == 1 and not extract:
            self._security_definition.remove(segment)

    def dump_request_xml(self, encoding: str = "cp1047") -> bytes:
        """Dump XML as EBCDIC encoded bytes. (Encoding can be overridden)."""
        if platform.system() != "OS/390" and encoding == "cp1047":
            # If not running on z/OS, EBCDIC is most likely not supported.
            # Force utf-8 if running tests on Linux, Mac, Windows, etc...
            encoding = "utf-8"
        return XMLBuilder.tostring(self.__racf_request, encoding=encoding)
