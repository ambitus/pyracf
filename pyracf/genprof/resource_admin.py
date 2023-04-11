"""General Resource Profile Administration."""

from pyracf.common.security_admin import SecurityAdmin
from pyracf.genprof.resource_request import ResourceRequest


class ResourceAdmin(SecurityAdmin):
    """General Resaurce Profile Administration."""

    def __init__(self) -> None:
        super().__init__()
        self.valid_segment_traits = {
            "base": {
                "appldata": "racf:appldata",
                "automatc": "racf:automatc",
                "category": "racf:category",
                "creatdat": "racf:creatdat",
                "data": "racf:data",
                "fclass": "racf:fclass",
                "fgeneric": "racf:fgeneric",
                "fprofile": "racf:fprofile",
                "history": "racf:history",
                "lchgdat": "racf:lchgdat",
                "level": "racf:level",
                "lrefdat": "racf:lrefdat",
                "member": "racf:member",
                "noracf": "racf:noracf",
                "notify": "racf:notify",
                "noyourac": "racf:noyourac",
                "owner": "racf:owner",
                "profile": "racf:profile",
                "raudit": "racf:raudit",
                "resgroup": "racf:resgroup",
                "rgaudit": "racf:rgaudit",
                "seclabel": "racf:seclabel",
                "seclevel": "racf:seclevel",
                "singldsn": "racf:singldsn",
                "stats": "racf:stats",
                "timezone": "racf:timezone",
                "tvtoc": "racf:tvtoc",
                "uacc": "racf:uacc",
                "volume": "racf:volume",
                "warning": "racf:warning",
                "whendays": "racf:whendays",
                "whentime": "racf:whentime",
            },
            "cdtinfo": {
                "cdtcase": "case",
                "cdtdftrc": "defaultrc",
                "cdtfirst": "first",
                "cdtgen": "generic",
                "cdtgenl": "genlist",
                "cdtgroup": "grouping",
                "cdtkeyql": "keyqual",
                "cdtmac": "macprocessing",
                "cdtmaxln": "maxlenx",
                "cdtmaxlx": "maxlength",
                "cdtmembr": "member",
                "cdtoper": "operations",
                "cdtother": "other",
                "cdtposit": "posit",
                "cdtprfal": "profilesallowed",
                "cdtracl": "raclist",
                "cdtsigl": "signal",
                "cdtslreq": "seclabelrequired",
                "cdtuacc": "defaultuacc",
            },
            "cfdef": {
                "cfdtype": "type",
                "cffirst": "first",
                "cfhelp": "help",
                "cflist": "listhead",
                "cfmixed": "mixed",
                "cfmnval": "minvalue",
                "cfmxlen": "maxlength",
                "cfmxval": "other",
                "cfother": "other",
                "cfvalrx": "racf:cfvalrx",
            },
            "csdata": {"custom-keyword": "racf:custom-keyword"},
            "dlfdata": {"jobname": "racf:jobname", "retain": "racf:retain"},
            "eim": {
                "domaindn": "domaindn",
                "kerbreg": "kerberg",
                "localreg": "localreg",
                "options": "options",
                "x509reg": "X509reg",
            },
            "kerb": {
                "chkaddrs": "checkaddrs",
                "deftktlf": "deftktlife",
                "encrypt": "encrypt",
                "kerbname": "kerbname",
                "keyvers": "racf:keyvers",
                "maxtktlf": "maxtktlf",
                "mintktlf": "mintklife",
                "password": "password",
            },
            "icsf": {
                "crtlbls": "symexportcert",
                "export": "symexportable",
                "keylbls": "symexportkey",
                "scpwrap": "symcpacfwrap",
                "scpret": "symcpacfret",
                "usage": "asymusage",
            },
            "ictx": {
                "domap": "domap",
                "mapreq": "mapreq",
                "maptimeo": "maptimeo",
                "usemap": "usemap",
            },
            "idtparms": {
                "sigtoken": "sigtoken",
                "sigseqn": "sigseqnum",
                "sigcat": "sigcat",
                "sigalg": "sigalg",
                "idttimeo": "idttimeout",
                "anyappl": "anyappl",
            },
            "jes": {"keylabel": "racf:keylabel"},
            "mfpolicy": {
                "factors": "racf:factors",
                "timeout": "racf:timeout",
                "reuse": "racf:reuse",
            },
            "proxy": {"binddn": "binddn", "bindpw": "bindpw", "ldaphost": "ldaphost"},
            "session": {
                "convsec": "racf:convsec",
                "interval": "racf:interval",
                "lock": "racf:lock",
                "sesskey": "racf:sesskey",
            },
            "sigver": {
                "failload": "failload",
                "sigaudit": "sigaudit",
                "sigreqd": "sigrequired",
            },
            "ssignon": {
                "keycrypt": "racf:keycrypt",
                "ptkeylab": "ptkeylab",
                "pttype": "pttype",
                "pttimeo": "pttimeo",
                "ptreplay": "ptreplay",
                "keylabel": "racf:keylabel",
                "keymask": "racf:keymask",
            },
            "stdata": {
                "group": "racf:group",
                "privlege": "racf:privlege",
                "trace": "racf:trace",
                "trusted": "racf:trusted",
                "user": "racf:user",
            },
            "svfmr": {"parmname": "racf:parmname", "script": "racf:script"},
            "tme": {
                "children": "racf:children",
                "groups": "racf:groups",
                "parent": "racf:parent",
                "resource": "racf:resource",
                "roles": "racf:roles",
            },
        }
        self.profile_type = "resource"

    def get_uacc(
        self, resource_name: str, class_name: str, generate_request_only=False
    ) -> str:
        """Get UACC associated with a general resource profile."""
        result = self.extract(
            {"resourcename": resource_name, "classname": class_name},
            generate_request_only=generate_request_only,
        )
        profile = result["securityresult"]["resource"]["commands"][0]["profiles"][0]
        return profile["base"].get("universal access")

    def set_uacc(
        self,
        resource_name: str,
        class_name: str,
        uacc: str,
        generate_request_only=False,
    ) -> str:
        """Set the UACC for a general resource profile."""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "uacc": uacc},
            generate_request_only=generate_request_only,
        )

    def get_your_acc(
        self, resource_name: str, class_name: str, generate_request_only=False
    ) -> str:
        """Get the UACC associated with your own general resource profile."""
        result = self.extract(
            {"resourcename": resource_name, "classname": class_name},
            generate_request_only=generate_request_only,
        )
        profile = result["securityresult"]["resource"]["commands"][0]["profiles"][0]
        return profile["base"].get("your access")

    def add_category(
        self, resource_name: str, class_name: str, category_name: str
    ) -> str:
        """Set the category for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addcategory": category_name,
            }
        )

    def del_category(
        self, resource_name: str, class_name: str, category_name: str
    ) -> str:
        """Delete the category from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delcategory": category_name,
            }
        )

    def add_member(self, resource_name: str, class_name: str, member_name: str) -> str:
        """Add a member to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addmember": member_name,
            }
        )

    def del_member(self, resource_name: str, class_name: str, member_name: str) -> str:
        """Delete a member from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delmember": member_name,
            }
        )

    def add_volume(self, resource_name: str, class_name: str, volume_name: str) -> str:
        """Add a volume to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addvolume": volume_name,
            }
        )

    def del_volume(self, resource_name: str, class_name: str, volume_name: str) -> str:
        """Delete a volume from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delvolume": volume_name,
            }
        )

    def set_jobname(
        self, resource_name: str, class_name: str, jobname_name: str
    ) -> str:
        """Set the jobname for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setjobname": jobname_name,
            }
        )

    def add_jobname(
        self, resource_name: str, class_name: str, jobname_name: str
    ) -> str:
        """Add a jobname to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addjobname": jobname_name,
            }
        )

    def del_jobname(
        self, resource_name: str, class_name: str, jobname_name: str
    ) -> str:
        """Delete a jobname from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "deljobname": jobname_name,
            }
        )

    def no_jobnames(self, resource_name: str, class_name: str) -> str:
        """Delete all jobname(s) from the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "nojobname": "N/A"}
        )

    def set_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        """Set the certificate label for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setcrtlbls": crtlbl_name,
            }
        )

    def add_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        """Add a certificate label to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addcrtlbls": crtlbl_name,
            }
        )

    def del_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        """Delete a certificate label from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delcrtlbls": crtlbl_name,
            }
        )

    def no_crtlbls(self, resource_name: str, class_name: str) -> str:
        """Delete all certificate label(s) the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "nocrtlbls": "N/A"}
        )

    def set_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        """Set the key label for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setkeylbls": keylbl_name,
            }
        )

    def add_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        """Add a key label to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addkeylbls": keylbl_name,
            }
        )

    def del_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        """Delete a key label from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delkeylbls": keylbl_name,
            }
        )

    def no_keylbls(self, resource_name: str, class_name: str) -> str:
        """Delete all key label(s) from the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "nokeylbls": "N/A"}
        )

    def set_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        """Set the MFA factor for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setfactors": factor_name,
            }
        )

    def add_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        """Add a MFA factor to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addfactors": factor_name,
            }
        )

    def del_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        """Delete a MFA factor from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delfactors": factor_name,
            }
        )

    def no_factors(self, resource_name: str, class_name: str) -> str:
        """Delete all MFA facor(s) from the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "nofactors": "N/A"}
        )

    def set_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        """Set the child for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setchildren": child_name,
            }
        )

    def add_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        """Add a child to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addchildren": child_name,
            }
        )

    def del_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        """Delete a child from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delchildren": child_name,
            }
        )

    def no_children(self, resource_name: str, class_name: str) -> str:
        """Delete all child(ren) from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "nochildren": "N/A",
            }
        )

    def set_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        """Set the group for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setgroups": group_name,
            }
        )

    def add_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        """Add a group to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addgroups": group_name,
            }
        )

    def del_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        """Delete a group from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delgroups": group_name,
            }
        )

    def no_groups(self, resource_name: str, class_name: str) -> str:
        """Delete all group(s) from the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "nogroups": "N/A"}
        )

    def set_resource(
        self, resource_name: str, class_name: str, tme_resource_name: str
    ) -> str:
        """Set the TME resource for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setresource": tme_resource_name,
            }
        )

    def add_resource(
        self, resource_name: str, class_name: str, tme_resource_name: str
    ) -> str:
        """Add a TME resource to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addresource": tme_resource_name,
            }
        )

    def del_resource(
        self, resource_name: str, class_name: str, tme_resource_name: str
    ) -> str:
        """Delete a TME resource from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delresource": tme_resource_name,
            }
        )

    def no_resources(self, resource_name: str, class_name: str) -> str:
        """Delete all TME resource(s) from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "noresource": "N/A",
            }
        )

    def set_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        """Set a role for the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "setroles": role_name,
            }
        )

    def add_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        """Add a role to the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "addroles": role_name,
            }
        )

    def del_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        """Delete a role from the General Resource Profile"""
        return self.alter(
            {
                "resourcename": resource_name,
                "classname": class_name,
                "delroles": role_name,
            }
        )

    def no_roles(self, resource_name: str, class_name: str) -> str:
        """Delete all role(s) from the General Resource Profile"""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "noroles": "N/A"}
        )

    def add(self, traits: dict, generate_request_only=False) -> dict:
        """Create a new general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request)
        return self.make_request(
            profile_request, generate_request_only=generate_request_only
        )

    def alter(self, traits: dict, generate_request_only=False) -> dict:
        """Alter an existing general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request, alter=True)
        return self.make_request(
            profile_request, 3, generate_request_only=generate_request_only
        )

    def extract(self, traits: dict, generate_request_only=False) -> dict:
        """Extract a general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_bool_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "listdata")
        self.build_segments(profile_request, extract=True)
        return self.extract_and_check_result(
            profile_request, generate_request_only=generate_request_only
        )

    def delete(
        self, resourcename: str, classname: str, generate_request_only=False
    ) -> dict:
        """Delete a general resource profile."""
        profile_request = ResourceRequest(resourcename, classname, "del")
        return self.make_request(
            profile_request, generate_request_only=generate_request_only
        )

    def build_segments(
        self,
        profile_request: ResourceRequest,
        alter=False,
        extract=False,
    ) -> None:
        """Build XML representation of segments."""
        profile_request.build_segments(
            self.segment_traits, self.trait_map, alter=alter, extract=extract
        )
        # Clear segments for new request
        self.segment_traits = {}

    def format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["resource"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "CLASS      NAME" in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self.format_profile_generic(
                messages[indexes[i] : indexes[i + 1]], self.valid_segment_traits, profile_type="generic"
            )
            # Post processing
            if "(g)" in profile["base"].get("name"):
                profile["base"]["generic"] = True
                profile["base"]["name"] = self.cast_from_str(profile["base"].get("name")[0])
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityresult"]["resource"]["commands"][0]["messages"]
        result["securityresult"]["resource"]["commands"][0]["profiles"] = profiles
