"""RACF Access Administration."""

from pyracf.access.access_request import AccessRequest
from pyracf.common.security_admin import SecurityAdmin


class AccessAdmin(SecurityAdmin):
    """RACF Access Administration."""

    def __init__(self) -> None:
        super().__init__()
        self.valid_segment_traits = {
            "base": {
                "access": "access",
                "delete": "racf:delete",
                "fclass": "racf:fclass",
                "fprofile": "racf:fprofile",
                "fgeneric": "racf:fgeneric",
                "fvolume": "racf:fvolume",
                "generic": "racf:generic",
                "id": "authid",
                "profile": "racf:profile",
                "reset": "racf:reset",
                "volume": "racf:volume",
                "whenappc": "racf:whenappc",
                "whencons": "racf:whencons",
                "whenjes": "racf:whenjes",
                "whenprog": "racf:whenprog",
                "whenserv": "racf:whenserv",
                "whensms": "racf:whensms",
                "whensqlr": "racf:whensqlr",
                "whensrv": "racf:whensrv",
                "whensys": "racf:whensys",
                "whenterm": "racf:whenterm",
            }
        }

    def add(self, traits: dict) -> dict:
        """Create a new user."""
        self.build_segment_dictionaries(traits)
        if traits["classname"] == "dataset":
            access_request = AccessRequest(traits, "set")
        else:
            access_request = AccessRequest(traits, "set")
        self.build_segments(access_request)
        return self.make_request(access_request)

    def alter(self, traits: dict) -> dict:
        """Alter an existing user."""
        self.build_segment_dictionaries(traits)
        if traits["classname"] == "dataset":
            access_request = AccessRequest(traits, "set")
        else:
            access_request = AccessRequest(traits, "set")
        self.build_segments(access_request, alter=True)
        return self.make_request(access_request, 3)

    def delete(self, traits: dict) -> dict:
        """Delete a user."""
        self.build_segment_dictionaries(traits)
        if traits["classname"] == "dataset":
            access_request = AccessRequest(traits, "del")
        else:
            access_request = AccessRequest(traits, "del")
        self.build_segments(access_request)
        return self.make_request(access_request)

    def build_segments(self, access_request: AccessRequest, alter=False) -> None:
        """Build XML representation of segments."""
        for segment, traits in self.segment_traits.items():
            if segment == "base":
                access_request.build_segment("", traits, self.trait_map, alter=alter)
        # Clear segments for new request
        self.segment_traits = {}
