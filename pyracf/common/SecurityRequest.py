import xml.etree.ElementTree as XMLBuilder


class SecurityRequest:
    def __init__(self) -> None:
        self.racf_request = XMLBuilder.Element("securityrequest")
        self.racf_request.attrib = {
            "xmlns": "http://www.ibm.com/systems/zos/saf",
            "xmlns:racf": "http://www.ibm.com/systems/zos/racf",
        }
        self.security_definition = XMLBuilder.SubElement(self.racf_request, "undefined")

    def build_segment(
        self,
        segment_name: str,
        traits: dict,
        trait_map: dict,
        alter=False,
        extract=False,
    ) -> None:
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

    def dump_request_xml(self) -> bytes:
        return XMLBuilder.tostring(self.racf_request, encoding="cp1047")
