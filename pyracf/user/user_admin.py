"""User Administration."""

from typing import List, Union

from pyracf.common.security_admin import SecurityAdmin

from .user_request import UserRequest


class UserAdmin(SecurityAdmin):
    """User Administration."""

    def __init__(
        self, debug: bool = False, generate_requests_only: bool = False
    ) -> None:
        super().__init__(
            "user", debug=debug, generate_requests_only=generate_requests_only
        )
        self._valid_segment_traits = {
            "base": {
                "base:adsp": "racf:adsp",
                "base:auditor": "racf:auditor",
                "base:auth": "racf:auth",
                "base:category": "racf:category",
                "base:clauth": "racf:clauth",
                "base:connects": "racf:connects",
                "base:cadsp": "racf:cadsp",
                "base:cauditor": "racf:cauditor",
                "base:cauthda": "racf:cauthda",
                "base:cgroup": "racf:cgroup",
                "base:cgrpacc": "racf:cgrpacc",
                "base:cinitct": "racf:cinitct",
                "base:cljdate": "racf:cljdate",
                "base:cljtime": "racf:cljtime",
                "base:coper": "racf:coper",
                "base:cowner": "racf:cowner",
                "base:cresume": "racf:cresume",
                "base:crevoke": "racf:crevoke",
                "base:crevokfl": "racf:crevokfl",
                "base:cspecial": "racf:cspecial",
                "base:cuacc": "racf:cuacc",
                "base:creatdat": "racf:creatdat",
                "base:data": "racf:data",
                "base:dfltgrp": "defgroup",
                "base:expired": "racf:expired",
                "base:factorn": "racf:factorn",
                "base:factor": "racf:factor",
                "base:facactv": "racf:facactv",
                "base:factagnn": "racf:factagnn",
                "base:facvalnn": "racf:facvalnn",
                "base:group": "racf:group",
                "base:grpacc": "racf:grpacc",
                "base:hasphras": "racf:hasphras",
                "base:haspwd": "racf:haspwd",
                "base:lastdate": "racf:lastdate",
                "base:lasttime": "racf:lasttime",
                "base:mfaflbk": "racf:mfaflbk",
                "base:mfapolnm": "racf:mfapolnm",
                "base:model": "racf:model",
                "base:name": "name",
                "base:oidcard": "racf:oidcard",
                "base:oper": "racf:oper",
                "base:owner": "racf:owner",
                "base:passdate": "racf:passdate",
                "base:passint": "racf:passint",
                "base:password": "racf:password",
                "base:phrase": "racf:phrase",
                "base:phrdate": "racf:phrdate",
                "base:phrint": "racf:phrint",
                "base:pphenv": "racf:pphenv",
                "base:protectd": "racf:protectd",
                "base:pwdenv": "racf:pwdenv",
                "base:rest": "racf:rest",
                "base:resume": "resumedate",
                "base:revoke": "revokedate",
                "base:revokefl": "racf:revokefl",
                "base:roaudit": "racf:roaudit",
                "base:seclabel": "seclabel",
                "base:seclevel": "racf:seclevel",
                "base:special": "racf:special",
                "base:uacc": "racf:uacc",
                "base:uaudit": "uaudit",
                "base:whendays": "whendays",
                "base:whensrv": "whensrv",
                "base:whentime": "whentime",
            },
            "cics": {
                "cisc:opclass": "racf:opclass",
                "cics:opident": "opident",
                "cics:opprty": "opprty",
                "cics:rslkey": "racf:rslkey",
                "cics:timeout": "timeout",
                "cics:tslkey": "racf:tslkey",
                "cics:xrfsoff": "force",
            },
            "csdata": {"csdata:custom-keyword": "racf:custom-keyword"},
            "dce": {
                "dce:autolog": "autolog",
                "dce:dcename": "dcename",
                "dce:homecell": "homecell",
                "dce:homeuuid": "homeuuid",
                "dce:uuid": "uuid",
            },
            "dfp": {
                "dfp:dataappl": "dataappl",
                "dfp:dataclas": "dataclas",
                "dfp:mgmtclas": "mgmtclass",
                "dfp:storclas": "storclas",
            },
            "eim": {"ldapprof": "racf:ldapprof"},
            "kerb": {
                "dfp:encrypt": "racf:encrypt",
                "dfp:kerbname": "racf:kerbname",
                "dfp:keyfrom": "racf:keyfrom",
                "dfp:keyvers": "racf:keyvers",
                "dfp:maxtktlf": "racf:maxtktlf",
            },
            "language": {"language:primary": "primary", "language:second": "secondary"},
            "lnotes": {"lnotes:sname": "racf:sname"},
            "mfa": {
                "mfa:factor": "racf:factor",
                "mfa:facactv": "racf:facactv",
                "mfa:factags": "racf:factags",
                "mfa:mfaflbk": "racf:mfaflbk",
                "mfa:mfapolnm": "racf:mfapolnm",
            },
            "nds": {"nds:uname": "racf:uname"},
            "netview": {
                "netview:consname": "consid",
                "netview:ctl": "secctl",
                "netview:domains": "nvdomains",
                "netview:ic": "ic",
                "netview:msgrecvr": "msgrec",
                "netview:ngmfadmn": "racf:ngmfadmn",
                "netview:ngmfvspn": "gmfadmin",
                "netview:opclass": "racf:opclass",
            },
            "omvs": {
                "omvs:assize": "assize",
                "omvs:autouid": "racf:autouid",
                "omvs:cputime": "cputime",
                "omvs:fileproc": "filemax",
                "omvs:home": "home",
                "omvs:memlimit": "memlim",
                "omvs:mmaparea": "mmaparea",
                "omvs:procuser": "procmax",
                "omvs:program": "pgm",
                "omvs:shared": "racf:shared",
                "omvs:shmemmax": "shmemmax",
                "omvs:threads": "threads",
                "omvs:uid": "uid",
            },
            "operparm": {
                "operparm:altgrp": "altgrp",
                "operparm:auto": "auto",
                "operparm:cmdsys": "cmdsys",
                "operparm:dom": "dom",
                "operparm:hc": "hc",
                "operparm:intids": "intid",
                "operparm:key": "key",
                "operparm:level": "racf:level",
                "operparm:logcmd": "logcmd",
                "operparm:mform": "mform",
                "operparm:migid": "migid",
                "operparm:monitor": "mon",
                "operparm:mscope": "racf:mscope",
                "operparm:operauth": "auth",
                "operparm:routcode": "routcode",
                "operparm:storage": "storage",
                "operparm:ud": "ud",
                "operparm:unknids": "unkids",
            },
            "ovm": {
                "ovm:fsroot": "racf:fsroot",
                "ovm:vhome": "racf:vhome",
                "ovm:vprogram": "racf:vprogram",
                "ovm:vuid": "racf:vuid",
            },
            "proxy": {
                "proxy:binddn": "racf:binddn",
                "proxy:bindpw": "racf:bindpw",
                "proxy:ldaphost": "racf:ldaphost",
            },
            "tso": {
                "tso:acctnum": "acctnum",
                "tso:command": "command",
                "tso:dest": "dest",
                "tso:hldclass": "holdclass",
                "tso:jobclass": "jobclass",
                "tso:maxsize": "maxsize",
                "tso:msgclass": "msgclass",
                "tso:proc": "proc",
                "tso:seclabel": "seclabel",
                "tso:size": "size",
                "tso:sysoutcl": "sysclass",
                "tso:unit": "unit",
                "tso:userdata": "userdata",
            },
            "workattr": {
                "workattr:waaccnt": "waaccnt",
                "workattr:waaddr1": "waaddr1",
                "workattr:waaddr2": "waaddr2",
                "workattr:waaddr3": "waaddr3",
                "workattr:waaddr4": "waaddr4",
                "workattr:wabldg": "wabldg",
                "workattr:wadept": "wadept",
                "workattr:waname": "waname",
                "workattr:waroom": "waroom",
                "workattr:waemail": "waemail",
            },
        }

    # ============================================================================
    # Special Attribute
    # ============================================================================
    def is_special(self, userid: str) -> bool:
        """Check if a user has RACF special authority."""
        result = self.extract(userid)
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        if "special" in profile["base"]["attributes"]:
            return True
        return False

    def set_special(self, userid: str) -> dict:
        """Give a user RACF special authority."""
        return self.alter(userid, traits={"base:special": True})

    def delete_special(
        self,
        userid: str,
    ) -> dict:
        """Remove a user's RACF special authority."""
        return self.alter(userid, traits={"base:special": False})

    # ============================================================================
    # Auditor Attribute
    # ============================================================================
    def is_auditor(self, userid: str) -> bool:
        """Check if a user has auditor authority"""
        result = self.extract(userid)
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        if "auditor" in profile["base"]["attributes"]:
            return True
        return False

    def set_auditor(self, userid: str) -> dict:
        """Give a user auditor authority."""
        return self.alter(userid, traits={"base:auditor": True})

    def delete_auditor(self, userid: str) -> dict:
        """Remove a user's auditor authority."""
        return self.alter(userid, traits={"base:auditor": False})

    # ============================================================================
    # Operations Attribute
    # ============================================================================
    def is_operations(self, userid: str) -> bool:
        """Check if a user has operations authority."""
        result = self.extract(userid)
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        if "operations" in profile["base"]["attributes"]:
            return True
        return False

    def set_operations(self, userid: str) -> dict:
        """Give a user operations authority."""
        return self.alter(userid, traits={"base:oper": True})

    def delete_operations(self, userid: str) -> dict:
        """Remove a user's operations authority."""
        return self.alter(userid, traits={"base:oper": False})

    # ============================================================================
    # Password
    # ============================================================================
    def set_password(
        self,
        userid: str,
        password: str,
    ) -> dict:
        """Set a user's password."""
        return self.alter(userid, traits={"base:password": password})

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def set_class_authorizations(
        self, userid: str, class_authorizations: List[str]
    ) -> dict:
        """
        Set a user's class authorizations.
        removes the user's current class authorizations and then recreates
        the class authorizations list using the list that the user provides.
        """
        remove_steps = self.delete_all_class_authorizaitons(userid)
        add_steps = self.add_class_authorizations(userid, class_authorizations)
        return self._to_steps_dictionary(
            list(remove_steps.values()) + list(add_steps.values())
        )

    def add_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> dict:
        """Add a class to a user's class authorizations."""
        result = self.alter(userid, traits={"add:base:clauth": class_authorizations})
        return self._to_steps_dictionary([result])

    def remove_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> dict:
        """Remove a class from a user's class authorizations."""
        result = self.alter(userid, traits={"remove:base:clauth": class_authorizations})
        return self._to_steps_dictionary([result])

    def delete_all_class_authorizaitons(self, userid: str) -> dict:
        """Delete all classes from a users class authorizations."""
        current_class_authorizations = self.get_class_authorizations(userid)
        return self.remove_class_authorizations(userid, current_class_authorizations)

    def get_class_authorizations(self, userid: str) -> Union[List[str], None]:
        """Get a user's class authorizations."""
        result = self.extract(userid)
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        try:
            return profile["base"]["classauthorizations"]
        except KeyError:
            return None

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def get_omvs_uid(self, userid: str) -> Union[int, None]:
        """Get a user's OMVS UID."""
        result = self.extract(userid, segments={"omvs": True})
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        try:
            return profile["omvs"]["uid"]
        except KeyError:
            return None

    def set_omvs_uid(
        self,
        userid: str,
        uid: int,
    ) -> dict:
        """Set a user's OMVS UID."""
        return self.alter(userid, traits={"omvs:uid": uid})

    # ============================================================================
    # OMVS Home
    # ============================================================================
    def get_omvs_home(self, userid: str) -> Union[str, None]:
        """Get a user's OMVS home directory."""
        result = self.extract(userid, segments={"omvs": True})
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        try:
            return profile["omvs"]["home"]
        except KeyError:
            return None

    def set_omvs_home(
        self,
        userid: str,
        home_directory: str,
    ) -> dict:
        """Set a user's OMVS home directory."""
        return self.alter(userid, traits={"omvs:home": str(home_directory)})

    # ============================================================================
    # OMVS Program
    # ============================================================================
    def get_omvs_program(self, userid: str) -> Union[str, None]:
        """Get a user's OMVS program."""
        result = self.extract(userid, segments={"omvs": True})
        profile = result["securityresult"]["user"]["commands"][0]["profiles"][0]
        try:
            return profile["omvs"]["home"]
        except KeyError:
            return None

    def set_omvs_program(
        self,
        userid: str,
        program: str,
    ) -> dict:
        """Set a user's OMVS program."""
        return self.alter(userid, traits={"omvs:home": str(program)})

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, userid: str, traits: dict = {}) -> dict:
        """Create a new user."""
        self._build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self._build_xml_segments(user_request)
        return self._make_request(user_request)

    def alter(self, userid: str, traits: dict = {}) -> dict:
        """Alter an existing user."""
        self._build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self._build_xml_segments(user_request, alter=True)
        return self._make_request(user_request, irrsmo00_options=3)

    def extract(self, userid: str, segments: dict = {}) -> dict:
        """Extract a user's profile."""
        self._build_bool_segment_dictionaries(segments)
        user_request = UserRequest(userid, "listdata")
        self._build_xml_segments(user_request, extract=True)
        return self._extract_and_check_result(user_request)

    def delete(self, userid: str) -> dict:
        """Delete a user."""
        user_request = UserRequest(userid, "del")
        return self._make_request(user_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["user"]["commands"][0]["messages"]
        userid = result["securityresult"]["user"]["name"]
        exclude_command_audit_trail_string = f"Command Audit Trail for USER {userid}"
        if exclude_command_audit_trail_string in messages:
            messages = messages[: messages.index(exclude_command_audit_trail_string)]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "USER=" in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            profiles.append(profile)

        # Post processing
        del result["securityresult"]["user"]["commands"][0]["messages"]
        result["securityresult"]["user"]["commands"][0]["profiles"] = profiles
