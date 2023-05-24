"""Generic Security Request builder."""

import platform
import xml.etree.ElementTree as XMLBuilder
from typing import Union


class SecurityRequest:
    """Generic Security Request builder."""

    def __init__(self) -> None:
        self.racf_request = XMLBuilder.Element("securityrequest")
        self.racf_request.attrib = {
            "xmlns": "http://www.ibm.com/systems/zos/saf",
            "xmlns:racf": "http://www.ibm.com/systems/zos/racf",
        }
        self.security_definition = XMLBuilder.SubElement(self.racf_request, "undefined")

    def get_volume_and_generic_security_definition_values(
        self, volume: Union[str, None], generic: bool
    ) -> None:
        """Get volid and generic xml values for security definition"""
        security_definition_volume = ""
        security_definition_generic = "no"
        if volume:
            security_definition_volume = volume
        if generic:
            security_definition_generic = "yes"
        return (security_definition_volume, security_definition_generic)

    def build_segments(
        self,
        segment_traits_dictionary: dict,
        trait_map: dict,
        alter=False,
        extract=False,
    ) -> None:
        """Build XML representation of segments."""
        for segment, segment_traits in segment_traits_dictionary.items():
            self.build_segment(
                segment,
                segment_traits,
                trait_map,
                alter=alter,
                extract=extract,
            )

    def build_segment(
        self,
        segment_name: str,
        traits: dict,
        trait_map: dict,
        alter=False,
        extract=False,
    ) -> None:
        """Build segment in XML format."""
        if not traits:
            return
        if segment_name:
            segment = XMLBuilder.SubElement(self.security_definition, segment_name)
        else:
            segment = self.security_definition
        if isinstance(traits, bool):
            return
        for trait in traits:
            if isinstance(traits[trait], bool) and not traits[trait] and not alter:
                continue
            trait_element = XMLBuilder.SubElement(segment, trait_map[trait])
            if isinstance(traits[trait], list):
                trait_element.text = traits[trait][0]
                trait_element.attrib = {"operation": traits[trait][1]}
                continue
            if not isinstance(traits[trait], bool):
                trait_element.text = str(traits[trait])
            if not alter:
                continue
            if isinstance(traits[trait], bool) and not traits[trait]:
                trait_element.attrib = {"operation": "del"}
            else:
                trait_element.attrib = {"operation": "set"}
        if len(list(segment.iter())) == 1 and not extract:
            self.security_definition.remove(segment)

    def dump_request_xml(self, encoding="cp1047") -> bytes:
        """Dump XML as EBCDIC encoded bytes. (Encoding can be overridden)."""
        if platform.system() != "OS/390" and encoding == "cp1047":
            # If not running on z/OS EBCDIC is most likely not supported.
            # Force utf-8 if running tests on Linux, Mac, Windows, etc...
            encoding = "utf-8"
        return XMLBuilder.tostring(self.racf_request, encoding=encoding)
