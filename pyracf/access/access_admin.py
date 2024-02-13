"""RACF Access Administration."""

from typing import List, Union

from pyracf.common.security_admin import SecurityAdmin

from .access_request import AccessRequest


class AccessAdmin(SecurityAdmin):
    """RACF Access Administration."""

    def __init__(
        self,
        irrsmo00_result_buffer_size: Union[int, None] = None,
        debug: bool = False,
        dump_mode: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
        run_as_userid: Union[str, None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:access": "access",
                "base:delete": "racf:delete",
                "base:model_profile_class": "racf:fclass",
                "base:model_profile": "racf:fprofile",
                "base:model_profile_generic": "racf:fgeneric",
                "base:model_profile_volume": "racf:fvolume",
                "base:auth_id": "authid",
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
            irrsmo00_result_buffer_size=irrsmo00_result_buffer_size,
            debug=debug,
            dump_mode=dump_mode,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            replace_existing_segment_traits=replace_existing_segment_traits,
            additional_secret_traits=additional_secret_traits,
            run_as_userid=run_as_userid,
        )

    # ============================================================================
    # Base Functions
    # ============================================================================
    def permit(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Create or change a permission"""
        traits["base:auth_id"] = auth_id
        self._build_segment_trait_dictionary(traits)
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
        traits = {"base:auth_id": auth_id}
        self._build_segment_trait_dictionary(traits)
        access_request = AccessRequest(resource, class_name, "del", volume, generic)
        self._add_traits_directly_to_request_xml_with_no_segments(access_request)
        return self._make_request(access_request)
