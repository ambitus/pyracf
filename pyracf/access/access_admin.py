"""RACF Access Administration."""

from typing import Union

from pyracf.access.access_request import AccessRequest
from pyracf.common.security_admin import SecurityAdmin


class AccessAdmin(SecurityAdmin):
    """RACF Access Administration."""

    def __init__(self, debug=False, generate_requests_only=False) -> None:
        super().__init__(debug=debug, generate_requests_only=generate_requests_only)
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

        del self.valid_segment_traits["base"]["generic"]

    def add(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Create a new permission."""
        traits["id"] = auth_id
        self.build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "set", volume, generic)
        self.build_segments(access_request)
        return self.make_request(access_request)

    def alter(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Alter an existing permission."""
        traits["id"] = auth_id
        self.build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "set", volume, generic)
        self.build_segments(access_request, alter=True)
        return self.make_request(access_request)

    def delete(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Delete a permission."""
        traits = {"id": auth_id}
        self.build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "del", volume, generic)
        self.build_segments(access_request)
        return self.make_request(access_request)

    def build_segments(self, access_request: AccessRequest, alter=False) -> None:
        """Build XML representation of segments."""
        for segment, traits in self.segment_traits.items():
            if segment == "base":
                access_request.build_segment("", traits, self.trait_map, alter=alter)
        # Clear segments for new request
        self.segment_traits = {}
