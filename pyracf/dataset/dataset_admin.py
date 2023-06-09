"""RACF Data Set Profile Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin

from .dataset_request import DatasetRequest


class DatasetAdmin(SecurityAdmin):
    """RACF DataSet Profile Administration."""

    def __init__(self, debug=False, generate_requests_only=False) -> None:
        super().__init__(
            "dataset", debug=debug, generate_requests_only=generate_requests_only
        )
        self._valid_segment_traits = {
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
                "base:universal-access": "racf:uacc",
                "base:unit": "racf:unit",
                "base:volume": "racf:volume",
                "base:volser": "racf:volser",
                "base:warning": "racf:warning",
            },
            "csdata": {"csdata:custom-keyword": "racf:custom-keyword"},
            "dfp": {"dfp:resowner": "racf:resowner", "dfp:datakey": "racf:datakey"},
            "tme": {"tme:roles": "racf:roles"},
        }
        self._valid_segment_traits["base"].update(
            self._common_base_traits_dataset_generic
        )
        del self._valid_segment_traits["base"]["generic"]

    # ============================================================================
    # Access
    # ============================================================================
    def get_universal_access(self, data_set: str) -> str:
        """Get universal access for data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return profile["base"]["universal access"]

    def set_universal_access(self, data_set: str, universal_acccess: str) -> dict:
        """Set the universal access for a data set profile."""
        result = self.alter(data_set, {"base:universal-access": universal_acccess})
        return self._to_steps(result)

    def get_my_access(self, data_set: str) -> str:
        """Get the access associated with your own data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return profile["base"]["your access"]

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
        dataset_request = DatasetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(dataset_request)
        return self._make_request(dataset_request)

    def alter(
        self,
        data_set: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Alter an existing data set profile."""
        self._build_segment_dictionaries(traits)
        dataset_request = DatasetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(dataset_request, alter=True)
        return self._make_request(dataset_request, irrsmo00_options=3)

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
        dataset_request = DatasetRequest(data_set, "listdata", volume, generic)
        self._build_xml_segments(dataset_request, extract=True)
        result = self._extract_and_check_result(dataset_request)
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
        dataset_request = DatasetRequest(data_set, "del", volume, generic)
        return self._make_request(dataset_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["dataset"]["commands"][0]["messages"]
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

            if profile["base"].get("installation data"):
                profile["base"]["installation data"] = " ".join(
                    profile["base"]["installation data"]
                )
            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityresult"]["dataset"]["commands"][0]["messages"]
        result["securityresult"]["dataset"]["commands"][0]["profiles"] = profiles
