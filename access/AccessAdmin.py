from common.irrsmo00 import IRRSMO00
from access.AccessRequest import AccessRequest
from common.SecurityResult import SecurityResult


class AccessAdmin():
    def __init__(self) -> None:
        self.irrsmo00 = IRRSMO00()
        self.valid_segment_traits = {
            'base': {
                'access': 'access', 
                'delete': 'racf:delete', 
                'fclass': 'racf:fclass', 
                'fprofile': 'racf:fprofile', 
                'fgeneric': 'racf:fgeneric', 
                'fvolume': 'racf:fvolume', 
                'generic': 'racf:generic', 
                'id': 'authid', 
                'profile': 'racf:profile', 
                'reset': 'racf:reset', 
                'volume': 'racf:volume', 
                'whenappc': 'racf:whenappc', 
                'whencons': 'racf:whencons', 
                'whenjes': 'racf:whenjes', 
                'whenprog': 'racf:whenprog', 
                'whenserv': 'racf:whenserv', 
                'whensms': 'racf:whensms', 
                'whensqlr': 'racf:whensqlr', 
                'whensrv': 'racf:whensrv', 
                'whensys': 'racf:whensys', 
                'whenterm': 'racf:whenterm'
            }
        }
        self.segment_traits = {}
        self.trait_map = {}

    def add(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        if classname == "dataset":
            volid = traits["volid"]
            generic = traits["generic"]
            access_request = AccessRequest(resourcename, classname, "set", generic, volid)
        else:
            access_request = AccessRequest(resourcename, classname, "set")
        self.build_segments(access_request)
        return self.make_request(access_request)

    def alter(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        if classname == "dataset":
            volid = traits["volid"]
            generic = traits["generic"]
            access_request = AccessRequest(resourcename, classname, "set", generic, volid)
        else:
            access_request = AccessRequest(resourcename, classname, "set")
        self.build_segments(access_request, alter=True)
        return self.make_request(access_request,3)

    def delete(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        if classname == "dataset":
            volid = traits["volid"]
            generic = traits["generic"]
            access_request = AccessRequest(resourcename, classname, "del", generic, volid)
        else:
            access_request = AccessRequest(resourcename, classname, "del")
        self.build_segments(access_request)
        return self.make_request(access_request)

    def build_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            for segment in self.valid_segment_traits.keys():
                if trait in self.valid_segment_traits[segment].keys():
                    if not segment in self.segment_traits.keys():
                        self.segment_traits[segment] = {}
                    self.segment_traits[segment][trait] = traits[trait]
                    self.trait_map[trait] =  self.valid_segment_traits[segment][trait]

    def build_segments(self, access_request: AccessRequest, alter=False) -> None:
        for segment in self.segment_traits.keys():
            if segment == "base":
                access_request.build_segment("", self.segment_traits[segment], self.trait_map, alter=alter)
        # Clear segments for new request
        self.segment_traits = {}

    def make_request(self, access_request: AccessRequest, opts: int = 1) -> dict:
        result_xml = self.irrsmo00.call_racf(access_request.dump_request_xml(),opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()
