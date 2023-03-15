"""User Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin
from pyracf.user.user_request import UserRequest


class UserAdmin(SecurityAdmin):
    """User Administration."""

    def __init__(self) -> None:
        super().__init__()
        self.valid_segment_traits = {
            "base": {
                "adsp": "racf:adsp",
                "auditor": "racf:auditor",
                "auth": "racf:auth",
                "category": "racf:category",
                "clauth": "racf:clauth",
                "connects": "racf:connects",
                "cadsp": "racf:cadsp",
                "cauditor": "racf:cauditor",
                "cauthda": "racf:cauthda",
                "cgroup": "racf:cgroup",
                "cgrpacc": "racf:cgrpacc",
                "cinitct": "racf:cinitct",
                "cljdate": "racf:cljdate",
                "cljtime": "racf:cljtime",
                "coper": "racf:coper",
                "cowner": "racf:cowner",
                "cresume": "racf:cresume",
                "crevoke": "racf:crevoke",
                "crevokfl": "racf:crevokfl",
                "cspecial": "racf:cspecial",
                "cuacc": "racf:cuacc",
                "creatdat": "racf:creatdat",
                "data": "racf:data",
                "dfltgrp": "defgroup",
                "expired": "racf:expired",
                "factorn": "racf:factorn",
                "factor": "racf:factor",
                "facactv": "racf:facactv",
                "factagnn": "racf:factagnn",
                "facvalnn": "racf:facvalnn",
                "group": "racf:group",
                "grpacc": "racf:grpacc",
                "hasphras": "racf:hasphras",
                "haspwd": "racf:haspwd",
                "lastdate": "racf:lastdate",
                "lasttime": "racf:lasttime",
                "mfaflbk": "racf:mfaflbk",
                "mfapolnm": "racf:mfapolnm",
                "model": "racf:model",
                "name": "name",
                "oidcard": "racf:oidcard",
                "oper": "racf:oper",
                "owner": "racf:owner",
                "passdate": "racf:passdate",
                "passint": "racf:passint",
                "password": "racf:password",
                "phrase": "racf:phrase",
                "phrdate": "racf:phrdate",
                "phrint": "racf:phrint",
                "pphenv": "racf:pphenv",
                "protectd": "racf:protectd",
                "pwdenv": "racf:pwdenv",
                "rest": "racf:rest",
                "resume": "resumedate",
                "revoke": "revokedate",
                "revokefl": "racf:revokefl",
                "roaudit": "racf:roaudit",
                "seclabel": "seclabel",
                "seclevel": "racf:seclevel",
                "special": "racf:special",
                "uacc": "racf:uacc",
                "uaudit": "uaudit",
                "whendays": "whendays",
                "whensrv": "whensrv",
                "whentime": "whentime",
            },
            "cics": {
                "opclass": "racf:opclass",
                "opident": "opident",
                "opprty": "opprty",
                "rslkey": "racf:rslkey",
                "timeout": "timeout",
                "tslkey": "racf:tslkey",
                "xrfsoff": "force",
            },
            "csdata": {"custom-keyword": "racf:custom-keyword"},
            "dce": {
                "autolog": "autolog",
                "dcename": "dcename",
                "homecell": "homecell",
                "homeuuid": "homeuuid",
                "uuid": "uuid",
            },
            "dfp": {
                "dataappl": "dataappl",
                "dataclas": "dataclas",
                "mgmtclas": "mgmtclass",
                "storclas": "storclas",
            },
            "eim": {"ldapprof": "racf:ldapprof"},
            "kerb": {
                "encrypt": "racf:encrypt",
                "kerbname": "racf:kerbname",
                "keyfrom": "racf:keyfrom",
                "keyvers": "racf:keyvers",
                "maxtktlf": "racf:maxtktlf",
            },
            "language": {"primary": "primary", "second": "secondary"},
            "lnotes": {"sname": "racf:sname"},
            "mfa": {
                "factor": "racf:factor",
                "facactv": "racf:facactv",
                "factags": "racf:factags",
                "mfaflbk": "racf:mfaflbk",
                "mfapolnm": "racf:mfapolnm",
            },
            "nds": {"uname": "racf:uname"},
            "netview": {
                "consname": "consid",
                "ctl": "secctl",
                "domains": "nvdomains",
                "ic": "ic",
                "msgrecvr": "msgrec",
                "ngmfadmn": "racf:ngmfadmn",
                "ngmfvspn": "gmfadmin",
                "opclass": "racf:opclass",
            },
            "omvs": {
                "assize": "assize",
                "autouid": "racf:autouid",
                "cputime": "cputime",
                "fileproc": "filemax",
                "home": "home",
                "memlimit": "memlim",
                "mmaparea": "mmaparea",
                "procuser": "procmax",
                "program": "pgm",
                "shared": "racf:shared",
                "shmemmax": "shmemmax",
                "threads": "threads",
                "uid": "uid",
            },
            "operparm": {
                "altgrp": "altgrp",
                "auto": "auto",
                "cmdsys": "cmdsys",
                "dom": "dom",
                "hc": "hc",
                "intids": "intid",
                "key": "key",
                "level": "racf:level",
                "logcmd": "logcmd",
                "mform": "mform",
                "migid": "migid",
                "monitor": "mon",
                "mscope": "racf:mscope",
                "operauth": "auth",
                "routcode": "routcode",
                "storage": "storage",
                "ud": "ud",
                "unknids": "unkids",
            },
            "ovm": {
                "fsroot": "racf:fsroot",
                "vhome": "racf:vhome",
                "vprogram": "racf:vprogram",
                "vuid": "racf:vuid",
            },
            "proxy": {
                "binddn": "racf:binddn",
                "bindpw": "racf:bindpw",
                "ldaphost": "racf:ldaphost",
            },
            "tso": {
                "acctnum": "acctnum",
                "command": "command",
                "dest": "dest",
                "hldclass": "holdclass",
                "jobclass": "jobclass",
                "maxsize": "maxsize",
                "msgclass": "msgclass",
                "proc": "proc",
                "seclabel": "seclabel",
                "size": "size",
                "sysoutcl": "sysclass",
                "unit": "unit",
                "userdata": "userdata",
            },
            "workattr": {
                "waaccnt": "waaccnt",
                "waaddr1": "waaddr1",
                "waaddr2": "waaddr2",
                "waaddr3": "waaddr3",
                "waaddr4": "waaddr4",
                "wabldg": "wabldg",
                "wadept": "wadept",
                "waname": "waname",
                "waroom": "waroom",
                "waemail": "waemail",
            },
        }
        self.profile_type = "user"

    def is_special(self, userid: str) -> bool:
        """Check if a user has RACF special."""
        result = self.extract({"userid": userid})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        if "special" in profile["base"]["attributes"]:
            return True
        return False

    def set_special(self, userid: str) -> dict:
        """Make user RACF special."""
        return self.alter({"userid": userid, "special": True})

    def del_special(self, userid: str) -> dict:
        """Make user not RACF special."""
        return self.alter({"userid": userid, "special": False})

    def is_auditor(self, userid: str) -> bool:
        """Check if a user is RACF auditor."""
        result = self.extract({"userid": userid})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        if "auditor" in profile["base"]["attributes"]:
            return True
        return False

    def set_auditor(self, userid: str) -> dict:
        """Make user a RACF auditor."""
        return self.alter({"userid": userid, "auditor": True})

    def del_auditor(self, userid: str) -> dict:
        """Make user not a RACF auditor."""
        return self.alter({"userid": userid, "auditor": False})

    def is_operations(self, userid: str) -> bool:
        """Check if a user is RACF operator."""
        result = self.extract({"userid": userid})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        if "operations" in profile["base"]["attributes"]:
            return True
        return False

    def set_operations(self, userid: str) -> dict:
        """Make user a RACF operator."""
        return self.alter({"userid": userid, "oper": True})

    def del_operations(self, userid: str) -> dict:
        """Make user not a RACF operator."""
        return self.alter({"userid": userid, "oper": False})

    def get_uid(self, userid: str) -> Union[str, int]:
        """Get a user's UID."""
        result = self.extract({"userid": userid, "omvs": True})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        return profile["omvs"]["uid"]

    def set_uid(self, userid: str, uid: int) -> dict:
        """Set a user's UID."""
        return self.alter({"userid": userid, "uid": str(uid)})

    def add_category(self, userid: str, category_name: str) -> str:
        """Set the category for the User Profile"""
        return self.alter({"userid": userid, "addcategory": category_name})

    def del_category(self, userid: str, category_name: str) -> str:
        """Delete the category from the User Profile"""
        return self.alter({"userid": userid, "delcategory": category_name})

    def set_clauth(self, userid: str, clauth_name: str) -> str:
        """Set the class authorization for the User Profile"""
        return self.alter({"userid": userid, "setclauth": clauth_name})

    def add_clauth(self, userid: str, clauth_name: str) -> str:
        """Add a class authorization to the User Profile"""
        return self.alter({"userid": userid, "addclauth": clauth_name})

    def del_clauth(self, userid: str, clauth_name: str) -> str:
        """Remove a class authorization from the User Profile"""
        return self.alter({"userid": userid, "delclauth": clauth_name})

    def no_clauth(self, userid: str) -> str:
        """Remove all class authorization(s) from the User Profile"""
        return self.alter({"userid": userid, "noclauth": "N/A"})

    def add_mfapolnm(self, userid: str, mfapolnm_name: str) -> str:
        """Set the MFA Policy Name from the User Profile"""
        return self.alter({"userid": userid, "addmfapolnm": mfapolnm_name})

    def del_mfapolnm(self, userid: str, mfapolnm_name: str) -> str:
        """Remove the MFA Policy Name from the User Profile"""
        return self.alter({"userid": userid, "delmfapolnm": mfapolnm_name})

    def set_cics_opclass(self, userid: str, opclass_name: str) -> str:
        """Set the Operator Class (CICS) for the User Profile"""
        return self.alter({"userid": userid, "cics:setopclass": opclass_name})

    def add_cics_opclass(self, userid: str, opclass_name: str) -> str:
        """Add an Operator Class (CICS) to the User Profile"""
        return self.alter({"userid": userid, "cics:addopclass": opclass_name})

    def del_cics_opclass(self, userid: str, opclass_name: str) -> str:
        """Remove an Operator Class (CICS) from the User Profile"""
        return self.alter({"userid": userid, "cics:delopclass": opclass_name})

    def no_cics_opclass(self, userid: str) -> str:
        """Remove all Operator Class(es) (CICS) from the User Profile"""
        return self.alter({"userid": userid, "cics:noopclass": "N/A"})

    def set_netview_opclass(self, userid: str, opclass_name: str) -> str:
        """Set the Operator Class (Netview) for the User Profile"""
        return self.alter({"userid": userid, "netview:setopclass": opclass_name})

    def add_netview_opclass(self, userid: str, opclass_name: str) -> str:
        """Add an Operator Class (Netview) to the User Profile"""
        return self.alter({"userid": userid, "netview:addopclass": opclass_name})

    def del_netview_opclass(self, userid: str, opclass_name: str) -> str:
        """Remove an Operator Class (Netview) from the User Profile"""
        return self.alter({"userid": userid, "netview:delopclass": opclass_name})

    def no_netview_opclass(self, userid: str) -> str:
        """Remove all Operator Class(es) (Netview) from the User Profile"""
        return self.alter({"userid": userid, "netview:noopclass": "N/A"})

    def set_domain(self, userid: str, domain_name: str) -> str:
        """Set the Domain for the User Profile"""
        return self.alter({"userid": userid, "setdomains": domain_name})

    def add_domain(self, userid: str, domain_name: str) -> str:
        """Add a Domain for the User Profile"""
        return self.alter({"userid": userid, "adddomains": domain_name})

    def del_domain(self, userid: str, domain_name: str) -> str:
        """Delete a Domain from the User Profile"""
        return self.alter({"userid": userid, "deldomains": domain_name})

    def no_domains(self, userid: str) -> str:
        """Delete all Domain(s) from the User Profile"""
        return self.alter({"userid": userid, "nodomains": "N/A"})

    def set_mscope(self, userid: str, mscope_name: str) -> str:
        """Set the Message Scope for the User Profile"""
        return self.alter({"userid": userid, "setmscope": mscope_name})

    def add_mscope(self, userid: str, mscope_name: str) -> str:
        """Add a Message Scope to the User Profile"""
        return self.alter({"userid": userid, "addmscope": mscope_name})

    def del_mscope(self, userid: str, mscope_name: str) -> str:
        """Delete a Message Scope from the User Profile"""
        return self.alter({"userid": userid, "delmscope": mscope_name})

    def no_mscope(self, userid: str) -> str:
        """Delete all Message Scope(s) from the User Profile"""
        return self.alter({"userid": userid, "nomscope": "N/A"})

    def add(self, traits: dict) -> dict:
        """Create a new user."""
        userid = traits["userid"]
        self.build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self.build_segments(user_request)
        return self.make_request(user_request)

    def alter(self, traits: dict) -> dict:
        """Alter an existing user."""
        userid = traits["userid"]
        self.build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self.build_segments(user_request, alter=True)
        return self.make_request(user_request, 3)

    def extract(self, traits: dict) -> dict:
        """Extract a user's profile."""
        userid = traits["userid"]
        self.build_bool_segment_dictionaries(traits)
        user_request = UserRequest(userid, "listdata")
        self.build_segments(user_request, extract=True)
        return self.extract_and_check_result(user_request)

    def delete(self, userid: str) -> dict:
        """Delete a user."""
        user_request = UserRequest(userid, "del")
        return self.make_request(user_request)

    def build_segments(
        self, user_request: UserRequest, alter=False, extract=False
    ) -> None:
        """Build XML representation of segments."""
        user_request.build_segments(
            self.segment_traits, self.trait_map, alter=alter, extract=extract
        )
        # Clear segments for new request
        self.segment_traits = {}

    def format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["user"]["commands"][0]["messages"]
        profile = self.format_profile_generic(
            messages, self.valid_segment_traits, profile_type="user"
        )
        # Post processing
        del result["securityresult"]["user"]["commands"][0]["messages"]
        result["securityresult"]["user"]["commands"][0]["profile"] = profile
