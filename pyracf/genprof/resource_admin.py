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

    def get_uacc(self, resource_name: str, class_name: str) -> str:
        """Get UACC associated with a general resource profile."""
        result = self.extract({"resourcename": resource_name, "classname": class_name})
        profile = result["securityresult"]["resource"]["commands"][0]["profile"]
        return profile["base"].get("universal access")

    def set_uacc(self, resource_name: str, class_name: str, uacc: str) -> str:
        """Set the UACC for a general resource profile."""
        return self.alter(
            {"resourcename": resource_name, "classname": class_name, "uacc": uacc}
        )

    def get_your_acc(self, resource_name: str, class_name: str) -> str:
        """Get the UACC associated with your own general resource profile."""
        result = self.extract({"resourcename": resource_name, "classname": class_name})
        profile = result["securityresult"]["resource"]["commands"][0]["profile"]
        return profile["base"].get("your access")

    def add(self, traits: dict) -> dict:
        """Create a new general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request)
        return self.make_request(profile_request)

    def alter(self, traits: dict) -> dict:
        """Alter an existing general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request, alter=True)
        return self.make_request(profile_request, 3)

    def extract(self, traits: dict) -> dict:
        """Extract a general resource profile."""
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_bool_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "listdata")
        self.build_segments(profile_request, extract=True)
        return self.extract_and_check_result(profile_request)

    def delete(self, resourcename: str, classname: str) -> dict:
        """Delete a general resource profile."""
        profile_request = ResourceRequest(resourcename, classname, "del")
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
        profile = self.format_profile_generic(
            messages, self.valid_segment_traits, profile_type="generic"
        )
        # Post processing
        if "(g)" in profile["base"].get("name"):
            profile["base"]["generic"] = True
            profile["base"]["name"] = self.__cast_value(profile["base"].get("name")[0])
        else:
            profile["base"]["generic"] = False

        if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
            profile["base"]["notify"] = None

        del result["securityresult"]["resource"]["commands"][0]["messages"]
        result["securityresult"]["resource"]["commands"][0]["profile"] = profile
