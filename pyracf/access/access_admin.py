"""RACF Access Administration."""

from typing import List, Union

from pyracf.access.access_request import AccessRequest
from pyracf.common.security_admin import SecurityAdmin


class AccessAdmin(SecurityAdmin):
    """RACF Access Administration."""

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:access": "access",
                "base:delete": "racf:delete",
                "base:model_profile_class": "racf:fclass",
                "base:model_profile": "racf:fprofile",
                "base:model_profile_generic": "racf:fgeneric",
                "base:model_profile_volume": "racf:fvolume",
                "base:id": "authid",
                "base:profile": "racf:profile",  # Not documented?
                "base:reset": "racf:reset",
                "base:volume": "racf:volume",
                "base:when_partner_lu_name": "racf:whenappc",
                "base:when_console": "racf:whencons",
                "base:when_jes": "racf:whenjes",
                "base:when_program": "racf:whenprog",
                "base:when_servauth": "racf:whenserv",
                "base:when_sms": "racf:whensms",
                "base:when_db2_role": "racf:whensqlr",
                "base:when_service": "racf:whensrv",
                "base:when_system": "racf:whensys",
                "base:when_terminal": "racf:whenterm",
            }
        }
        super().__init__(
            "permission",
            debug=debug,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            replace_existing_segment_traits=replace_existing_segment_traits,
            additional_secret_traits=additional_secret_traits,
        )

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Create a new permission."""
        traits["base:id"] = auth_id
        self._build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "set", volume, generic)
        self._add_traits_directly_to_request_xml_with_no_segments(access_request)
        return self._make_request(access_request)

    def alter(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Alter an existing permission."""
        traits["base:id"] = auth_id
        self._build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "set", volume, generic)
        self._add_traits_directly_to_request_xml_with_no_segments(
            access_request, alter=True
        )
        return self._make_request(access_request)

    def delete(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Delete a permission."""
        traits = {"base:id": auth_id}
        self._build_segment_dictionaries(traits)
        access_request = AccessRequest(resource, class_name, "del", volume, generic)
        self._add_traits_directly_to_request_xml_with_no_segments(access_request)
        return self._make_request(access_request)
