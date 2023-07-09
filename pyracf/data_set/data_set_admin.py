"""RACF Data Set Profile Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin

from .data_set_request import DataSetRequest


class DataSetAdmin(SecurityAdmin):
    """RACF Data Set Profile Administration."""

    _valid_segment_traits = {
        "base": {
            "base:altvol": "racf:altvol",
            "base:category": "racf:category",
            "base:creatdat": "racf:creatdat",
            "base:data": "racf:data",
            "base:dsns": "racf:dsns",
            "base:dstype": "racf:dstype",
            "base:erase": "racf:erase",
            "base:fclass": "racf:fclass",
            "base:fgeneric": "racf:fgeneric",
            "base:fileseq": "racf:fileseq",
            "base:from": "racf:from",
            "base:groupnm": "racf:groupnm",
            "base:history": "racf:history",
            "base:id": "racf:id",
            "base:lchgdat": "racf:lchgdat",
            "base:level": "racf:level",
            "base:lrefdat": "racf:lrefdat",
            "base:model": "racf:model",
            "base:noracf": "racf:noracf",
            "base:notify": "racf:notify",
            "base:owner": "racf:owner",
            "base:prefix": "racf:prefix",
            "base:profile": "racf:profile",
            "base:raudit": "racf:raudit",
            "base:retpd": "racf:retpd",
            "base:rgaudit": "racf:rgaudit",
            "base:seclabel": "racf:seclabel",
            "base:seclevel": "racf:seclevel",
            "base:set": "racf:set",
            "base:setonly": "racf:setonly",
            "base:stats": "racf:stats",
            "base:tape": "racf:tape",
            "base:universal_access": "racf:uacc",
            "base:unit": "racf:unit",
            "base:volume": "racf:volume",
            "base:volser": "racf:volser",
            "base:warning": "racf:warning",
        },
        "dfp": {"dfp:resowner": "racf:resowner", "dfp:datakey": "racf:datakey"},
        "tme": {"tme:roles": "racf:roles"},
    }

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        add_field_data: Union[dict, None] = None,
        overwrite_field_data: Union[dict, None] = None,
    ) -> None:
        super().__init__(
            "dataSet",
            debug=debug,
            generate_requests_only=generate_requests_only,
            add_field_data=add_field_data,
            overwrite_field_data=overwrite_field_data,
        )
        self._valid_segment_traits["base"].update(
            self._common_base_traits_data_set_generic
        )
        del self._valid_segment_traits["base"]["base:generic"]

    # ============================================================================
    # Access
    # ============================================================================
    def get_universal_access(self, data_set: str) -> str:
        """Get universal access for data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return self._get_field(profile, "base", "universalAccess")

    def set_universal_access(self, data_set: str, universal_acccess: str) -> dict:
        """Set the universal access for a data set profile."""
        result = self.alter(data_set, {"base:universal_access": universal_acccess})
        return self._to_steps(result)

    def get_my_access(self, data_set: str) -> str:
        """Get the access associated with your own data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return self._get_field(profile, "base", "yourAccess")

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(
        self,
        data_set: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Create a new data set profile."""
        self._build_segment_dictionaries(traits)
        data_set_request = DataSetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(data_set_request)
        return self._make_request(data_set_request)

    def alter(
        self,
        data_set: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Alter an existing data set profile."""
        self._build_segment_dictionaries(traits)
        data_set_request = DataSetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(data_set_request, alter=True)
        return self._make_request(data_set_request, irrsmo00_options=3)

    def extract(
        self,
        data_set: str,
        segments: dict = {},
        volume: Union[str, None] = None,
        generic: bool = False,
        profile_only: bool = False,
    ) -> dict:
        """Extract a data set profile."""
        self._build_bool_segment_dictionaries(segments)
        data_set_request = DataSetRequest(data_set, "listdata", volume, generic)
        self._build_xml_segments(data_set_request, extract=True)
        result = self._extract_and_check_result(data_set_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(
        self,
        data_set: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Delete a data set profile."""
        self._clear_state()
        data_set_request = DataSetRequest(data_set, "del", volume, generic)
        return self._make_request(data_set_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["dataSet"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "INFORMATION FOR DATASET " in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            # Post processing
            if "(g)" in profile["base"].get("name"):
                profile["base"]["generic"] = True
                profile["base"]["name"] = self._cast_from_str(
                    profile["base"].get("name").split(" ")[0]
                )
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("installationData"):
                profile["base"]["installationData"] = " ".join(
                    profile["base"]["installationData"]
                )
            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityResult"]["dataSet"]["commands"][0]["messages"]
        result["securityResult"]["dataSet"]["commands"][0]["profiles"] = profiles
