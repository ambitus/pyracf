"""Generic Security Request builder."""

import xml.etree.ElementTree as XMLBuilder


class SecurityRequest:
    """Generic Security Request builder."""

    def __init__(self) -> None:
        self.racf_request = XMLBuilder.Element("securityrequest")
        self.racf_request.attrib = {
            "xmlns": "http://www.ibm.com/systems/zos/saf",
            "xmlns:racf": "http://www.ibm.com/systems/zos/racf",
        }
        self.security_definition = XMLBuilder.SubElement(self.racf_request, "undefined")

    def set_volid_and_generic(self, traits) -> None:
        """Set volid and generic as attributes for security definition based on traits."""
        if "volid" in traits:
            if traits["volid"]:
                self.security_definition.attrib["volid"] = traits["volid"]
        if "generic" in traits:
            if traits["generic"]:
                self.security_definition.attrib["generic"] = traits["generic"]

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
        for trait in segment:
            print(trait.tag, trait.attrib)

    def dump_request_xml(self) -> bytes:
        """Dump XML as EBCDIC encoded bytes."""
        return XMLBuilder.tostring(self.racf_request, encoding="cp1047")
