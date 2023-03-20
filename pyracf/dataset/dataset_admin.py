"""RACF Data Set Profile Administration."""

from pyracf.common.security_admin import SecurityAdmin
from pyracf.dataset.dataset_request import DatasetRequest


class DatasetAdmin(SecurityAdmin):
    """RACF DataSet Profile Administration."""

    def __init__(self) -> None:
        super().__init__()
        self.valid_segment_traits = {
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
            "dfp": {"resowner": "racf:resowner", "datakey": "racf:datakey"},
            "tme": {"roles": "racf:roles"},
        }
        self.valid_segment_traits["base"].update(
            self.common_base_traits_dataset_generic
        )
        self.segment_traits = {}
        self.trait_map = {}
        self.profile_type = "dataset"

    def get_uacc(self, dataset_name: str) -> str:
        """Get UACC associated with a data set profile."""
        result = self.extract({"datasetname": dataset_name})
        profile = result["securityresult"]["dataset"]["commands"][0]["profile"]
        return profile["base"].get("universal access")

    def set_uacc(self, dataset_name: str, uacc: str) -> str:
        """Set the UACC for a data set profile."""
        return self.alter({"datasetname": dataset_name, "uacc": uacc})

    def get_your_acc(self, dataset_name: str) -> str:
        """Get the UACC associated with your own data set profile."""
        result = self.extract({"datasetname": dataset_name})
        profile = result["securityresult"]["dataset"]["commands"][0]["profile"]
        return profile["base"].get("your access")

    def add_category(self, dataset_name: str, category_name: str) -> str:
        """Set the category for the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "addcategory": category_name})

    def del_category(self, dataset_name: str, category_name: str) -> str:
        """Delete the category from the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "delcategory": category_name})

    def set_volume(self, dataset_name: str, volume_name: str) -> str:
        """Set the volume for the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "setvolume": volume_name})

    def add_volume(self, dataset_name: str, volume_name: str) -> str:
        """Add a volume to the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "addvolume": volume_name})

    def del_volume(self, dataset_name: str, volume_name: str) -> str:
        """Delete a volume from the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "delvolume": volume_name})

    def set_role(self, dataset_name: str, role_name: str) -> str:
        """Set a role for the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "setroles": role_name})

    def add_role(self, dataset_name: str, role_name: str) -> str:
        """Add a role to the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "addroles": role_name})

    def del_role(self, dataset_name: str, role_name: str) -> str:
        """Delete a role from the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "delroles": role_name})

    def no_roles(self, dataset_name: str) -> str:
        """Delete all role(s) from the Dataset Profile"""
        return self.alter({"datasetname": dataset_name, "noroles": "N/A"})

    def add(self, traits: dict) -> dict:
        """Create a new data set profile."""
        self.build_segment_dictionaries(traits)
        dataset_request = DatasetRequest(traits, "set")
        self.build_segments(dataset_request)
        return self.make_request(dataset_request)

    def alter(self, traits: dict) -> dict:
        """Alter an existing data set profile."""
        self.build_segment_dictionaries(traits)
        dataset_request = DatasetRequest(traits, "set")
        self.build_segments(dataset_request, alter=True)
        return self.make_request(dataset_request, 3)

    def extract(self, traits: dict) -> dict:
        """Extract a data set profile."""
        self.build_bool_segment_dictionaries(traits)
        dataset_request = DatasetRequest(traits, "listdata")
        self.build_segments(dataset_request, extract=True)
        return self.extract_and_check_result(dataset_request)

    def delete(self, datasetname: str, generic: str = "no", volid: str = "") -> dict:
        """Delete a data set profile."""
        traits = {"datasetname": datasetname, "generic": generic, "volid": volid}
        dataset_request = DatasetRequest(traits, "del")
        return self.make_request(dataset_request)

    def build_segments(
        self, dataset_request: DatasetRequest, alter=False, extract=False
    ) -> None:
        """Build XML representation of segments."""
        dataset_request.build_segments(
            self.segment_traits, self.trait_map, alter=alter, extract=extract
        )
        # Clear segments for new request
        self.segment_traits = {}

    def format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["dataset"]["commands"][0]["messages"]
        profile = self.format_profile_generic(
            messages, self.valid_segment_traits, profile_type="dataset"
        )
        # Post processing
        if profile["base"].get("installation data"):
            profile["base"]["installation data"] = " ".join(
                profile["base"]["installation data"]
            )
        if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
            profile["base"]["notify"] = None

        del result["securityresult"]["dataset"]["commands"][0]["messages"]
        result["securityresult"]["dataset"]["commands"][0]["profile"] = profile
