"""User Administration."""

from typing import List, Union

from pyracf.common.security_admin import SecurityAdmin

from .user_request import UserRequest


class UserAdmin(SecurityAdmin):
    """User Administration."""

    _valid_segment_traits = {
        "base": {
            "base:adsp": "racf:adsp",
            "base:auditor": "racf:auditor",
            "base:auth": "racf:auth",
            "base:category": "racf:category",
            "base:class_authorizations": "racf:clauth",
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
            "base:operations": "racf:oper",
            "base:owner": "racf:owner",
            "base:passdate": "racf:passdate",
            "base:passint": "racf:passint",
            "base:password": "racf:password",
            "base:passphrase": "racf:phrase",
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

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        add_field_data: Union[dict, None] = None,
        overwrite_field_data: Union[dict, None] = None,
        add_more_secrets: Union[dict, None] = None,
    ) -> None:
        super().__init__(
            "user",
            debug=debug,
            generate_requests_only=generate_requests_only,
            add_field_data=add_field_data,
            overwrite_field_data=overwrite_field_data,
            add_more_secrets=add_more_secrets,
        )

    # ============================================================================
    # Special Authority
    # ============================================================================
    def has_special_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has RACF special authority."""
        profile = self.extract(userid, profile_only=True)
        return "special" in profile["base"]["attributes"]

    def give_special_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user RACF special authority."""
        result = self.alter(userid, traits={"base:special": True})
        return self._to_steps(result)

    def take_away_special_authority(
        self,
        userid: str,
    ) -> Union[dict, bytes]:
        """Remove a user's RACF special authority."""
        result = self.alter(userid, traits={"base:special": False})
        return self._to_steps(result)

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def has_operations_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has operations authority."""
        profile = self.extract(userid, profile_only=True)
        return "operations" in profile["base"]["attributes"]

    def give_operations_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user operations authority."""
        result = self.alter(userid, traits={"base:operations": True})
        return self._to_steps(result)

    def take_away_operations_authority(self, userid: str) -> Union[dict, bytes]:
        """Remove a user's operations authority."""
        result = self.alter(userid, traits={"base:operations": False})
        return self._to_steps(result)

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def has_auditor_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has auditor authority"""
        profile = self.extract(userid, profile_only=True)
        return "auditor" in profile["base"]["attributes"]

    def give_auditor_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user auditor authority."""
        result = self.alter(userid, traits={"base:auditor": True})
        return self._to_steps(result)

    def take_away_auditor_authority(self, userid: str) -> Union[dict, bytes]:
        """Remove a user's auditor authority."""
        result = self.alter(userid, traits={"base:auditor": False})
        return self._to_steps(result)

    # ============================================================================
    # Password
    # ============================================================================
    def set_password(
        self,
        userid: str,
        password: str,
    ) -> Union[dict, bytes]:
        """Set a user's password."""
        result = self.alter(userid, traits={"base:password": password})
        return self._to_steps(result)

    # ============================================================================
    # Passphrase
    # ============================================================================
    def set_passphrase(
        self,
        userid: str,
        passphrase: str,
    ) -> Union[dict, bytes]:
        """Set a user's passphrase."""
        result = self.alter(userid, traits={"base:passphrase": passphrase})
        return self._to_steps(result)

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def get_class_authorizations(self, userid: str) -> Union[List[str], bytes]:
        """Get a user's class authorizations."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "classAuthorizations")

    def set_class_authorizations(
        self, userid: str, class_authorizations: List[str]
    ) -> Union[dict, bytes]:
        """
        Set a user's class authorizations.
        removes the user's current class authorizations and then recreates
        the class authorizations list using the list that the user provides.
        """
        delete_result = self.delete_all_class_authorizations(userid)
        add_result = self.add_class_authorizations(userid, class_authorizations)
        return self._to_steps([delete_result, add_result])

    def add_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> Union[dict, bytes]:
        """Add a class to a user's class authorizations."""
        result = self.alter(
            userid, traits={"add:base:class_authorizations": class_authorizations}
        )
        return self._to_steps(result)

    def remove_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> Union[dict, bytes]:
        """Remove a class from a user's class authorizations."""
        result = self.alter(
            userid, traits={"remove:base:class_authorizations": class_authorizations}
        )
        return self._to_steps(result)

    def delete_all_class_authorizations(self, userid: str) -> Union[dict, False, bytes]:
        """Delete all classes from a users class authorizations."""
        current_class_authorizations = self.get_class_authorizations(userid)
        if not current_class_authorizations:
            return False
        return self.remove_class_authorizations(userid, current_class_authorizations)

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def get_omvs_uid(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS UID."""
        profile = self.extract(userid, segments={"omvs": True}, profile_only=True)
        return self._get_field(profile, "omvs", "uid")

    def set_omvs_uid(self, userid: str, uid: int) -> Union[dict, bytes]:
        """Set a user's OMVS UID."""
        result = self.alter(userid, traits={"omvs:uid": uid})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Home
    # ============================================================================
    def get_omvs_home(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS home directory."""
        profile = self.extract(userid, segments={"omvs": True}, profile_only=True)
        return self._get_field(profile, "omvs", "home")

    def set_omvs_home(
        self,
        userid: str,
        home_directory: str,
    ) -> Union[dict, bytes]:
        """Set a user's OMVS home directory."""
        result = self.alter(userid, traits={"omvs:home": home_directory})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Program
    # ============================================================================
    def get_omvs_program(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS program."""
        profile = self.extract(userid, segments={"omvs": True}, profile_only=True)
        return self._get_field(profile, "omvs", "program")

    def set_omvs_program(
        self,
        userid: str,
        program: str,
    ) -> Union[dict, bytes]:
        """Set a user's OMVS program."""
        result = self.alter(userid, traits={"omvs:program": program})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, userid: str, traits: dict = {}) -> Union[dict, bytes]:
        """Create a new user."""
        self._build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self._build_xml_segments(user_request)
        return self._make_request(user_request)

    def alter(self, userid: str, traits: dict = {}) -> Union[dict, bytes]:
        """Alter an existing user."""
        self._build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self._build_xml_segments(user_request, alter=True)
        return self._make_request(user_request, irrsmo00_options=11)

    def extract(
        self, userid: str, segments: dict = {}, profile_only: bool = False
    ) -> Union[dict, bytes]:
        """Extract a user's profile."""
        self._build_bool_segment_dictionaries(segments)
        user_request = UserRequest(userid, "listdata")
        self._build_xml_segments(user_request, extract=True)
        result = self._extract_and_check_result(user_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(self, userid: str) -> Union[dict, bytes]:
        """Delete a user."""
        self._clear_state()
        user_request = UserRequest(userid, "del")
        return self._make_request(user_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["user"]["commands"][0]["messages"]
        userid = result["securityResult"]["user"]["name"]
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
        del result["securityResult"]["user"]["commands"][0]["messages"]
        result["securityResult"]["user"]["commands"][0]["profiles"] = profiles
