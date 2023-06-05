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
                "altvol": "racf:altvol",
                "category": "racf:category",
                "creatdat": "racf:creatdat",
                "data": "racf:data",
                "dsns": "racf:dsns",
                "dstype": "racf:dstype",
                "erase": "racf:erase",
                "fclass": "racf:fclass",
                "fgeneric": "racf:fgeneric",
                "fileseq": "racf:fileseq",
                "from": "racf:from",
                "groupnm": "racf:groupnm",
                "history": "racf:history",
                "id": "racf:id",
                "lchgdat": "racf:lchgdat",
                "level": "racf:level",
                "lrefdat": "racf:lrefdat",
                "model": "racf:model",
                "noracf": "racf:noracf",
                "notify": "racf:notify",
                "owner": "racf:owner",
                "prefix": "racf:prefix",
                "profile": "racf:profile",
                "raudit": "racf:raudit",
                "retpd": "racf:retpd",
                "rgaudit": "racf:rgaudit",
                "seclabel": "racf:seclabel",
                "seclevel": "racf:seclevel",
                "set": "racf:set",
                "setonly": "racf:setonly",
                "stats": "racf:stats",
                "tape": "racf:tape",
                "uacc": "racf:uacc",
                "unit": "racf:unit",
                "volume": "racf:volume",
                "volser": "racf:volser",
                "warning": "racf:warning",
            },
            "csdata": {"custom-keyword": "racf:custom-keyword"},
            "dfp": {"resowner": "racf:resowner", "datakey": "racf:datakey"},
            "tme": {"roles": "racf:roles"},
        }
        self._valid_segment_traits["base"].update(
            self._common_base_traits_dataset_generic
        )
        del self._valid_segment_traits["base"]["generic"]

    def get_uacc(self, data_set: str) -> str:
        """Get UACC associated with a data set profile."""
        result = self.extract(data_set)
        profile = result["securityresult"]["dataset"]["commands"][0]["profiles"][0]
        return profile["base"].get("universal access")

    def set_uacc(self, data_set: str, uacc: str) -> str:
        """Set the UACC for a data set profile."""
        return self.alter(data_set, {"uacc": uacc})

    def get_your_acc(self, data_set: str) -> str:
        """Get the UACC associated with your own data set profile."""
        result = self.extract(data_set)
        profile = result["securityresult"]["dataset"]["commands"][0]["profiles"][0]
        return profile["base"].get("your access")

    def add_category(self, data_set: str, category: str) -> str:
        """Set the category for the Dataset Profile"""
        return self.alter(data_set, {"addcategory": category})

    def del_category(self, data_set: str, category: str) -> str:
        """Delete the category from the Dataset Profile"""
        return self.alter(data_set, {"delcategory": category})

    def set_volume(self, data_set: str, volume: str) -> str:
        """Set the volume for the Dataset Profile"""
        return self.alter(data_set, {"setvolume": volume})

    def add_volume(self, data_set: str, volume: str) -> str:
        """Add a volume to the Dataset Profile"""
        return self.alter(data_set, {"addvolume": volume})

    def del_volume(self, data_set: str, volume: str) -> str:
        """Delete a volume from the Dataset Profile"""
        return self.alter(data_set, {"delvolume": volume})

    def set_role(self, data_set: str, role: str) -> str:
        """Set a role for the Dataset Profile"""
        return self.alter(data_set, {"setroles": role})

    def add_role(self, data_set: str, role: str) -> str:
        """Add a role to the Dataset Profile"""
        return self.alter(data_set, {"addroles": role})

    def del_role(self, data_set: str, role: str) -> str:
        """Delete a role from the Dataset Profile"""
        return self.alter(data_set, {"delroles": role})

    def no_roles(self, data_set: str) -> str:
        """Delete all role(s) from the Dataset Profile"""
        return self.alter(data_set, {"noroles": "N/A"})

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
        self.build_segments(dataset_request)
        return self.make_request(dataset_request)

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
        self.build_segments(dataset_request, alter=True)
        return self.make_request(dataset_request, 3)

    def extract(
        self,
        data_set: str,
        segments: dict = {},
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Extract a data set profile."""
        self._build_bool_segment_dictionaries(segments)
        dataset_request = DatasetRequest(data_set, "listdata", volume, generic)
        self.build_segments(dataset_request, extract=True)
        return self._extract_and_check_result(dataset_request)

    def delete(
        self,
        data_set: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> dict:
        """Delete a data set profile."""
        dataset_request = DatasetRequest(data_set, "del", volume, generic)
        return self.make_request(dataset_request)

    def build_segments(
        self, dataset_request: DatasetRequest, alter=False, extract=False
    ) -> None:
        """Build XML representation of segments."""
        dataset_request.build_segments(
            self._segment_traits, self._trait_map, alter=alter, extract=extract
        )
        # Clear segments for new request
        self._segment_traits = {}

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
