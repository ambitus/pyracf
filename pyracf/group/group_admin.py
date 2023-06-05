"""Group Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin

from .group_request import GroupRequest


class GroupAdmin(SecurityAdmin):
    """Group Administration."""

    def __init__(
        self, debug: bool = False, generate_requests_only: bool = False
    ) -> None:
        super().__init__(
            "group", debug=debug, generate_requests_only=generate_requests_only
        )
        self._valid_segment_traits = {
            "base": {
                "base:connects": "racf:connects",
                "base:gauth": "racf:gauth",
                "base:guserid": "racf:guserid",
                "base:creatdat": "racf:creatdat",
                "base:data": "racf:data",
                "base:model": "racf:model",
                "base:owner": "racf:owner",
                "base:subgroup": "racf:subgroup",
                "base:supgroup": "racf:supgroup",
                "base:termuacc": "racf:termuacc",
                "base:universl": "racf:universl",
            },
            "csdata": {"csdata:custom-keyword": "racf:custom-keyword"},
            "dfp": {
                "dfp:dataappl": "racf:dataappl",
                "dfp:dataclas": "racf:dataclas",
                "dfp:mgmtclas": "racf:mgmtclas",
                "dfp:storclas": "racf:storclas",
            },
            "omvs": {
                "omvs:autogid": "racf:autogid",
                "omvs:gid": "gid",
                "omvs:shared": "racf:shared",
            },
            "ovm": {"ovm:gid": "gid"},
            "tme": {"tme:roles": "racf:roles"},
        }

    def get_group_special(self, group: str, userid: str) -> dict:
        result = self.extract(group)
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        if profile["base"]["users"] is None:
            return False
        connect_profile = [
            user
            for user in profile["base"]["users"]
            if user["userid"].lower() == userid.lower()
        ]
        if connect_profile:
            if "special" in connect_profile[0]["connectattributes"]:
                return True
        return False

    def get_group_operations(self, group: str, userid: str) -> dict:
        result = self.extract(group)
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        if profile["base"]["users"] is None:
            return False
        connect_profile = [
            user
            for user in profile["base"]["users"]
            if user["userid"].lower() == userid.lower()
        ]
        if connect_profile:
            if "operations" in connect_profile[0]["connectattributes"]:
                return True
        return False

    def get_group_auditor(self, group: str, userid: str) -> dict:
        result = self.extract(group)
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        if profile["base"]["users"] is None:
            return False
        connect_profile = [
            user
            for user in profile["base"]["users"]
            if user["userid"].lower() == userid.lower()
        ]
        if connect_profile:
            if "auditor" in connect_profile[0]["connectattributes"]:
                return True
        return False

    def get_grpacc(self, group: str, userid: str) -> dict:
        result = self.extract(group)
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        if profile["base"]["users"] is None:
            return False
        connect_profile = [
            user
            for user in profile["base"]["users"]
            if user["userid"].lower() == userid.lower()
        ]
        if connect_profile:
            if "grpacc" in connect_profile[0]["connectattributes"]:
                return True
        return False

    def get_omvs_gid(self, group: str) -> Union[str, int]:
        """Get a group's GID."""
        result = self.extract(group, {"omvs": True})
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        try:
            return profile["omvs"]["gid"]
        except KeyError:
            return None

    def set_omvs_gid(self, group: str, gid: int) -> dict:
        """Set a group's GID."""
        return self.alter(group, {"omvs:gid": str(gid)})

    def get_ovm_gid(self, group: str) -> Union[str, int]:
        """Get a group's GID."""
        result = self.extract(group, {"ovm": True})
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        try:
            return profile["ovm"]["gid"]
        except KeyError:
            return None

    def set_ovm_gid(self, group: str, gid: int) -> dict:
        """Set a group's GID."""
        return self.alter(group, {"ovm:gid": str(gid)})

    def add(self, group: str, traits: dict = {}) -> dict:
        """Create a new group."""
        self._build_segment_dictionaries(traits)
        group_request = GroupRequest(group, "set")
        self._build_xml_segments(group_request)
        return self._make_request(group_request)

    def alter(self, group: str, traits: dict = {}) -> dict:
        """Alter an existing group."""
        self._build_segment_dictionaries(traits)
        group_request = GroupRequest(group, "set")
        self._build_xml_segments(group_request, alter=True)
        return self._make_request(group_request, irrsmo00_options=3)

    def extract(self, group: str, segments: dict = {}) -> dict:
        """Extract a group's profile."""
        self._build_bool_segment_dictionaries(segments)
        group_request = GroupRequest(group, "listdata")
        self._build_xml_segments(group_request, extract=True)
        return self._extract_and_check_result(group_request)

    def delete(self, group_name: str) -> dict:
        """Delete a group."""
        group_request = GroupRequest(group_name, "del")
        return self._make_request(group_request)

    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["group"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "INFORMATION FOR GROUP " in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            if "subgroup(s)" in profile.keys():
                profile["subgroup(s)"] = profile["subgroups"]
            profiles.append(profile)

        # Post processing
        del result["securityresult"]["group"]["commands"][0]["messages"]
        result["securityresult"]["group"]["commands"][0]["profiles"] = profiles
