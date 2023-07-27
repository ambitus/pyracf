"""General Resource Profile Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin

from .resource_request import ResourceRequest


class ResourceAdmin(SecurityAdmin):
    """General Resaurce Profile Administration."""

    _valid_segment_traits = {
        "base": {
            "base:appldata": "racf:appldata",
            "base:automatc": "racf:automatc",
            "base:category": "racf:category",
            "base:creatdat": "racf:creatdat",
            "base:data": "racf:data",
            "base:fclass": "racf:fclass",
            "base:fgeneric": "racf:fgeneric",
            "base:fprofile": "racf:fprofile",
            "base:history": "racf:history",
            "base:lchgdat": "racf:lchgdat",
            "base:level": "racf:level",
            "base:lrefdat": "racf:lrefdat",
            "base:member": "racf:member",
            "base:noracf": "racf:noracf",
            "base:notify": "racf:notify",
            "base:noyourac": "racf:noyourac",
            "base:owner": "racf:owner",
            "base:profile": "racf:profile",
            "base:raudit": "racf:raudit",
            "base:resgroup": "racf:resgroup",
            "base:rgaudit": "racf:rgaudit",
            "base:seclabel": "racf:seclabel",
            "base:seclevel": "racf:seclevel",
            "base:singldsn": "racf:singldsn",
            "base:stats": "racf:stats",
            "base:timezone": "racf:timezone",
            "base:tvtoc": "racf:tvtoc",
            "base:universal_access": "racf:uacc",
            "base:volume": "racf:volume",
            "base:warning": "racf:warning",
            "base:whendays": "racf:whendays",
            "base:whentime": "racf:whentime",
        },
        "cdtinfo": {
            "cdtinfo:cdtcase": "case",
            "cdtinfo:cdtdftrc": "defaultrc",
            "cdtinfo:cdtfirst": "first",
            "cdtinfo:cdtgen": "generic",
            "cdtinfo:cdtgenl": "genlist",
            "cdtinfo:cdtgroup": "grouping",
            "cdtinfo:cdtkeyql": "keyqual",
            "cdtinfo:cdtmac": "macprocessing",
            "cdtinfo:cdtmaxln": "maxlenx",
            "cdtinfo:cdtmaxlx": "maxlength",
            "cdtinfo:cdtmembr": "member",
            "cdtinfo:cdtoper": "operations",
            "cdtinfo:cdtother": "other",
            "cdtinfo:cdtposit": "posit",
            "cdtinfo:cdtprfal": "profilesallowed",
            "cdtinfo:cdtracl": "raclist",
            "cdtinfo:cdtsigl": "signal",
            "cdtinfo:cdtslreq": "seclabelrequired",
            "cdtinfo:cdtuacc": "defaultuacc",
        },
        "cfdef": {
            "cfdef:cfdtype": "type",
            "cfdef:cffirst": "first",
            "cfdef:cfhelp": "help",
            "cfdef:cflist": "listhead",
            "cfdef:cfmixed": "mixed",
            "cfdef:cfmnval": "minvalue",
            "cfdef:cfmxlen": "maxlength",
            "cfdef:cfmxval": "other",
            "cfdef:cfother": "other",
            "cfdef:cfvalrx": "racf:cfvalrx",
        },
        "dlfdata": {
            "dlfdata:jobname": "racf:jobname",
            "dlfdata:retain": "racf:retain",
        },
        "eim": {
            "eim:domaindn": "domaindn",
            "eim:kerbreg": "kerberg",
            "eim:localreg": "localreg",
            "eim:options": "options",
            "eim:x509reg": "X509reg",
        },
        "kerb": {
            "kerb:chkaddrs": "checkaddrs",
            "kerb:deftktlf": "deftktlife",
            "kerb:encrypt": "encrypt",
            "kerb:kerbname": "kerbname",
            "kerb:keyvers": "racf:keyvers",
            "kerb:maxtktlf": "maxtktlf",
            "kerb:mintktlf": "mintklife",
            "kerb:password": "password",
        },
        "icsf": {
            "icsf:crtlbls": "symexportcert",
            "icsf:export": "symexportable",
            "icsf:keylbls": "symexportkey",
            "icsf:scpwrap": "symcpacfwrap",
            "icsf:scpret": "symcpacfret",
            "icsf:usage": "asymusage",
        },
        "ictx": {
            "ictx:domap": "domap",
            "ictx:mapreq": "mapreq",
            "ictx:maptimeo": "maptimeo",
            "ictx:usemap": "usemap",
        },
        "idtparms": {
            "idtpamrs:sigtoken": "sigtoken",
            "idtparms:sigseqn": "sigseqnum",
            "idtparms:sigcat": "sigcat",
            "idtparms:sigalg": "sigalg",
            "idtparms:idttimeo": "idttimeout",
            "idtpamrs:anyappl": "anyappl",
        },
        "jes": {"jes:keylabel": "racf:keylabel"},
        "mfpolicy": {
            "mfpolicy:factors": "racf:factors",
            "mfpolicy:timeout": "racf:timeout",
            "mfpolicy:reuse": "racf:reuse",
        },
        "proxy": {
            "proxy:binddn": "binddn",
            "proxy:bindpw": "bindpw",
            "proxy:ldaphost": "ldaphost",
        },
        "session": {
            "session:convsec": "racf:convsec",
            "session:interval": "racf:interval",
            "session:lock": "racf:lock",
            "session:sesskey": "racf:sesskey",
        },
        "sigver": {
            "sigver:failload": "failload",
            "sigver:sigaudit": "sigaudit",
            "sigver:sigreqd": "sigrequired",
        },
        "ssignon": {
            "ssigon:keycrypt": "racf:keycrypt",
            "ssigon:ptkeylab": "ptkeylab",
            "ssigon:pttype": "pttype",
            "ssigon:pttimeo": "pttimeo",
            "ssigon:ptreplay": "ptreplay",
            "ssigon:keylabel": "racf:keylabel",
            "ssigno:keymask": "racf:keymask",
        },
        "stdata": {
            "ssigon:group": "racf:group",
            "ssigon:privlege": "racf:privlege",
            "ssigon:trace": "racf:trace",
            "ssigon:trusted": "racf:trusted",
            "ssigon:user": "racf:user",
        },
        "svfmr": {"svfmr:parmname": "racf:parmname", "svfmr:script": "racf:script"},
        "tme": {
            "tme:children": "racf:children",
            "tme:groups": "racf:groups",
            "tme:parent": "racf:parent",
            "tme:resource": "racf:resource",
            "tme:roles": "racf:roles",
        },
    }

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        add_field_data: Union[dict, None] = None,
        overwrite_field_data: Union[dict, None] = None,
    ) -> None:
        super().__init__(
            "resource",
            debug=debug,
            generate_requests_only=generate_requests_only,
            add_field_data=add_field_data,
            overwrite_field_data=overwrite_field_data,
        )

    # ============================================================================
    # Universal Access
    # ============================================================================
    def get_universal_access(
        self, resource: str, class_name: str
    ) -> Union[str, bytes, None]:
        """Get the universal access for general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "universalAccess")

    def set_universal_access(
        self,
        resource: str,
        class_name: str,
        universal_access: str,
    ) -> Union[dict, bytes]:
        """Set the universal access for a general resource profile."""
        result = self.alter(
            resource, class_name, {"base:universal_access": universal_access}
        )
        return self._to_steps(result)

    def get_my_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
        """Get the access associated with your own general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "yourAccess")

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(
        self, resource: str, class_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new general resource profile."""
        self._build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self._build_xml_segments(profile_request)
        return self._make_request(profile_request)

    def alter(
        self, resource: str, class_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing general resource profile."""
        self._build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self._build_xml_segments(profile_request, alter=True)
        return self._make_request(profile_request, irrsmo00_options=3)

    def extract(
        self, resource: str, class_name: str, segments={}, profile_only: bool = False
    ) -> Union[dict, bytes]:
        """Extract a general resource profile."""
        self._build_bool_segment_dictionaries(segments)
        resource_request = ResourceRequest(resource, class_name, "listdata")
        self._build_xml_segments(resource_request, extract=True)
        result = self._extract_and_check_result(resource_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(self, resource: str, class_name: str) -> Union[dict, bytes]:
        """Delete a general resource profile."""
        self._clear_state()
        profile_request = ResourceRequest(resource, class_name, "del")
        return self._make_request(profile_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["resource"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "CLASS      NAME" in messages[i]
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
                    profile["base"].get("name")[0]
                )
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityResult"]["resource"]["commands"][0]["messages"]
        result["securityResult"]["resource"]["commands"][0]["profiles"] = profiles
