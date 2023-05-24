"""General Resource Profile Administration."""

from pyracf.common.security_admin import SecurityAdmin

from .resource_request import ResourceRequest


class ResourceAdmin(SecurityAdmin):
    """General Resaurce Profile Administration."""

    def __init__(self, debug=False, generate_requests_only=False) -> None:
        super().__init__(debug=debug, generate_requests_only=generate_requests_only)
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

    def get_uacc(self, resource: str, class_name: str) -> str:
        """Get UACC associated with a general resource profile."""
        result = self.extract(resource, class_name)
        profile = result["securityresult"]["resource"]["commands"][0]["profiles"][0]
        return profile["base"].get("universal access")

    def set_uacc(
        self,
        resource: str,
        class_name: str,
        uacc: str,
    ) -> str:
        """Set the UACC for a general resource profile."""
        return self.alter(resource, class_name, {"uacc": uacc})

    def get_your_acc(self, resource: str, class_name: str) -> str:
        """Get the UACC associated with your own general resource profile."""
        result = self.extract(resource, class_name)
        profile = result["securityresult"]["resource"]["commands"][0]["profiles"][0]
        return profile["base"].get("your access")

    def add_category(self, resource: str, class_name: str, category: str) -> str:
        """Set the category for the General Resource Profile"""
        return self.alter(resource, class_name, {"addcategory": category})

    def del_category(self, resource: str, class_name: str, category: str) -> str:
        """Delete the category from the General Resource Profile"""
        return self.alter(resource, class_name, {"delcategory": category})

    def add_member(self, resource: str, class_name: str, member: str) -> str:
        """Add a member to the General Resource Profile"""
        return self.alter(resource, class_name, {"addmember": member})

    def del_member(self, resource: str, class_name: str, member: str) -> str:
        """Delete a member from the General Resource Profile"""
        return self.alter(resource, class_name, {"delmember": member})

    def add_volume(self, resource: str, class_name: str, volume: str) -> str:
        """Add a volume to the General Resource Profile"""
        return self.alter(resource, class_name, {"addvolume": volume})

    def del_volume(self, resource: str, class_name: str, volume: str) -> str:
        """Delete a volume from the General Resource Profile"""
        return self.alter(resource, class_name, {"delvolume": volume})

    def set_jobname(self, resource: str, class_name: str, jobname: str) -> str:
        """Set the jobname for the General Resource Profile"""
        return self.alter(resource, class_name, {"setjobname": jobname})

    def add_jobname(self, resource: str, class_name: str, jobname: str) -> str:
        """Add a jobname to the General Resource Profile"""
        return self.alter(resource, class_name, {"addjobname": jobname})

    def del_jobname(self, resource: str, class_name: str, jobname: str) -> str:
        """Delete a jobname from the General Resource Profile"""
        return self.alter(resource, class_name, {"deljobname": jobname})

    def no_jobnames(self, resource: str, class_name: str) -> str:
        """Delete all jobname(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"nojobname": "N/A"})

    def set_crtlbl(self, resource: str, class_name: str, crtlbl: str) -> str:
        """Set the certificate label for the General Resource Profile"""
        return self.alter(resource, class_name, {"setcrtlbls": crtlbl})

    def add_crtlbl(self, resource: str, class_name: str, crtlbl: str) -> str:
        """Add a certificate label to the General Resource Profile"""
        return self.alter(resource, class_name, {"addcrtlbls": crtlbl})

    def del_crtlbl(self, resource: str, class_name: str, crtlbl: str) -> str:
        """Delete a certificate label from the General Resource Profile"""
        return self.alter(resource, class_name, {"delcrtlbls": crtlbl})

    def no_crtlbls(self, resource: str, class_name: str) -> str:
        """Delete all certificate label(s) the General Resource Profile"""
        return self.alter(resource, class_name, {"nocrtlbls": "N/A"})

    def set_keylbl(self, resource: str, class_name: str, keylbl: str) -> str:
        """Set the key label for the General Resource Profile"""
        return self.alter(resource, class_name, {"setkeylbls": keylbl})

    def add_keylbl(self, resource: str, class_name: str, keylbl: str) -> str:
        """Add a key label to the General Resource Profile"""
        return self.alter(resource, class_name, {"addkeylbls": keylbl})

    def del_keylbl(self, resource: str, class_name: str, keylbl: str) -> str:
        """Delete a key label from the General Resource Profile"""
        return self.alter(resource, class_name, {"delkeylbls": keylbl})

    def no_keylbls(self, resource: str, class_name: str) -> str:
        """Delete all key label(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"nokeylbls": "N/A"})

    def set_factor(self, resource: str, class_name: str, factor: str) -> str:
        """Set the MFA factor for the General Resource Profile"""
        return self.alter(resource, class_name, {"setfactors": factor})

    def add_factor(self, resource: str, class_name: str, factor: str) -> str:
        """Add a MFA factor to the General Resource Profile"""
        return self.alter(resource, class_name, {"addfactors": factor})

    def del_factor(self, resource: str, class_name: str, factor: str) -> str:
        """Delete a MFA factor from the General Resource Profile"""
        return self.alter(resource, class_name, {"delfactors": factor})

    def no_factors(self, resource: str, class_name: str) -> str:
        """Delete all MFA facor(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"nofactors": "N/A"})

    def set_child(self, resource: str, class_name: str, child: str) -> str:
        """Set the child for the General Resource Profile"""
        return self.alter(resource, class_name, {"setchildren": child})

    def add_child(self, resource: str, class_name: str, child: str) -> str:
        """Add a child to the General Resource Profile"""
        return self.alter(resource, class_name, {"addchildren": child})

    def del_child(self, resource: str, class_name: str, child: str) -> str:
        """Delete a child from the General Resource Profile"""
        return self.alter(resource, class_name, {"delchildren": child})

    def no_children(self, resource: str, class_name: str) -> str:
        """Delete all child(ren) from the General Resource Profile"""
        return self.alter(resource, class_name, {"nochildren": "N/A"})

    def set_group(self, resource: str, class_name: str, group: str) -> str:
        """Set the group for the General Resource Profile"""
        return self.alter(resource, class_name, {"setgroups": group})

    def add_group(self, resource: str, class_name: str, group: str) -> str:
        """Add a group to the General Resource Profile"""
        return self.alter(resource, class_name, {"addgroups": group})

    def del_group(self, resource: str, class_name: str, group: str) -> str:
        """Delete a group from the General Resource Profile"""
        return self.alter(resource, class_name, {"delgroups": group})

    def no_groups(self, resource: str, class_name: str) -> str:
        """Delete all group(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"nogroups": "N/A"})

    def set_resource(self, resource: str, class_name: str, tme_resource: str) -> str:
        """Set the TME resource for the General Resource Profile"""
        return self.alter(resource, class_name, {"setresource": tme_resource})

    def add_resource(self, resource: str, class_name: str, tme_resource: str) -> str:
        """Add a TME resource to the General Resource Profile"""
        return self.alter(resource, class_name, {"addresource": tme_resource})

    def del_resource(self, resource: str, class_name: str, tme_resource: str) -> str:
        """Delete a TME resource from the General Resource Profile"""
        return self.alter(resource, class_name, {"delresource": tme_resource})

    def no_resources(self, resource: str, class_name: str) -> str:
        """Delete all TME resource(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"noresource": "N/A"})

    def set_role(self, resource: str, class_name: str, role: str) -> str:
        """Set a role for the General Resource Profile"""
        return self.alter(resource, class_name, {"setroles": role})

    def add_role(self, resource: str, class_name: str, role: str) -> str:
        """Add a role to the General Resource Profile"""
        return self.alter(resource, class_name, {"addroles": role})

    def del_role(self, resource: str, class_name: str, role: str) -> str:
        """Delete a role from the General Resource Profile"""
        return self.alter(resource, class_name, {"delroles": role})

    def no_roles(self, resource: str, class_name: str) -> str:
        """Delete all role(s) from the General Resource Profile"""
        return self.alter(resource, class_name, {"noroles": "N/A"})

    def add(self, resource: str, class_name: str, traits: dict) -> dict:
        """Create a new general resource profile."""
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self.build_segments(profile_request)
        return self.make_request(profile_request)

    def alter(self, resource: str, class_name: str, traits: dict) -> dict:
        """Alter an existing general resource profile."""
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self.build_segments(profile_request, alter=True)
        return self.make_request(profile_request, 3)

    def extract(self, resource: str, class_name: str, segments={}) -> dict:
        """Extract a general resource profile."""
        self.build_bool_segment_dictionaries(segments)
        profile_request = ResourceRequest(resource, class_name, "listdata")
        self.build_segments(profile_request, extract=True)
        return self.extract_and_check_result(profile_request)

    def delete(self, resource: str, class_name: str) -> dict:
        """Delete a general resource profile."""
        profile_request = ResourceRequest(resource, class_name, "del")
        return self.make_request(profile_request)

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
                messages[indexes[i] : indexes[i + 1]],
                self.valid_segment_traits,
                profile_type="generic",
            )
            # Post processing
            if "(g)" in profile["base"].get("name"):
                profile["base"]["generic"] = True
                profile["base"]["name"] = self.cast_from_str(
                    profile["base"].get("name")[0]
                )
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityresult"]["resource"]["commands"][0]["messages"]
        result["securityresult"]["resource"]["commands"][0]["profiles"] = profiles
