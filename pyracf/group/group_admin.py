"""Group Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin

from .group_request import GroupRequest


class GroupAdmin(SecurityAdmin):
    """Group Administration."""

    def __init__(self, debug=False) -> None:
        super().__init__(debug=debug)
        self.valid_segment_traits = {
            'base': {
                'connects': 'racf:connects', 
                'gauth': 'racf:gauth', 
                'guserid': 'racf:guserid', 
                'creatdat': 'racf:creatdat', 
                'data': 'racf:data', 
                'model': 'racf:model', 
                'owner': 'racf:owner', 
                'subgroup': 'racf:subgroup', 
                'supgroup': 'racf:supgroup', 
                'termuacc': 'racf:termuacc', 
                'universl': 'racf:universl'
            }, 
            'csdata': {'custom-keyword': 'racf:custom-keyword'}, 
            'dfp': {
                'dataappl': 'racf:dataappl', 
                'dataclas': 'racf:dataclas', 
                'mgmtclas': 'racf:mgmtclas', 
                'storclas': 'racf:storclas'
            }, 
            'omvs': {
                'autogid': 'racf:autogid', 
                'gid': 'gid', 
                'shared': 'racf:shared'
            }, 
            'ovm': {'gid': 'gid'}, 
            'tme': {'roles': 'racf:roles'}
        }
        self.profile_type = "group"

    def get_omvs_gid(self, group_name: str) -> Union[str, int]:
        """Get a group's GID."""
        result = self.extract({"groupname": group_name, "omvs": True})
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        try:
            return profile["omvs"]["gid"]
        except KeyError:
            return None

    def set_omvs_gid(
        self,
        group_name: str,
        gid: int,
        generate_request_only=False,
    ) -> dict:
        """Set a group's GID."""
        return self.alter(
            {"groupid": group_name, "omvs:gid": str(gid)},
            generate_request_only=generate_request_only,
        )

    def get_ovm_gid(self, group_name: str) -> Union[str, int]:
        """Get a group's GID."""
        result = self.extract({"groupname": group_name, "ovm": True})
        profile = result["securityresult"]["group"]["commands"][0]["profiles"][0]
        try:
            return profile["ovm"]["gid"]
        except KeyError:
            return None

    def set_ovm_gid(
        self,
        group_name: str,
        gid: int,
        generate_request_only=False,
    ) -> dict:
        """Set a group's GID."""
        return self.alter(
            {"groupid": group_name, "ovm:gid": str(gid)},
            generate_request_only=generate_request_only,
        )

    def add(self, traits: dict, generate_request_only=False) -> dict:
        """Create a new group."""
        group_name = traits["groupname"]
        self.build_segment_dictionaries(traits)
        group_request = GroupRequest(group_name, "set")
        self.build_segments(group_request)
        return self.make_request(
            group_request, generate_request_only=generate_request_only
        )

    def alter(self, traits: dict, generate_request_only=False) -> dict:
        """Alter an existing group."""
        group_name = traits["groupname"]
        self.build_segment_dictionaries(traits)
        group_request = GroupRequest(group_name, "set")
        self.build_segments(group_request, alter=True)
        return self.make_request(
            group_request, 3, generate_request_only=generate_request_only
        )

    def extract(self, traits: dict, generate_request_only=False) -> dict:
        """Extract a group's profile."""
        group_name = traits["groupname"]
        self.build_bool_segment_dictionaries(traits)
        group_request = GroupRequest(group_name, "listdata")
        self.build_segments(group_request, extract=True)
        return self.extract_and_check_result(
            group_request, generate_request_only=generate_request_only
        )

    def delete(self, group_name: str, generate_request_only=False) -> dict:
        """Delete a group."""
        group_request = GroupRequest(group_name, "del")
        return self.make_request(
            group_request, generate_request_only=generate_request_only
        )

    def build_segments(
        self, group_request: GroupRequest, alter=False, extract=False
    ) -> None:
        """Build XML representation of segments."""
        group_request.build_segments(
            self.segment_traits, self.trait_map, alter=alter, extract=extract
        )
        # Clear segments for new request
        self.segment_traits = {}

    def format_profile(self, result: dict) -> None:
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
            profile = self.format_profile_generic(
                messages[indexes[i] : indexes[i + 1]],
                self.valid_segment_traits,
                profile_type="group",
            )
            if "subgroup(s)" in profile.keys():
                profile["subgroup(s)"] = profile["subgroups"]
            profiles.append(profile)

        # Post processing
        del result["securityresult"]["group"]["commands"][0]["messages"]
        result["securityresult"]["group"]["commands"][0]["profiles"] = profiles
