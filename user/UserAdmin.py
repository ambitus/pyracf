from common.irrsmo00 import IRRSMO00
from user.UserRequest import UserRequest
from common.SecurityResult import SecurityResult
from common.SecurityRequestError import SecurityRequestError
from typing import Union, List


class UserAdmin():
    def __init__(self) -> None:
        self.irrsmo00 = IRRSMO00()
        self.valid_segment_traits = {
            'base': {
                'adsp': 'racf:adsp',
                'auditor': 'racf:auditor',
                'auth': 'racf:auth',
                'category': 'racf:category',
                'clauth': 'racf:clauth',
                'connects': 'racf:connects',
                'cadsp': 'racf:cadsp',
                'cauditor': 'racf:cauditor',
                'cauthda': 'racf:cauthda',
                'cgroup': 'racf:cgroup',
                'cgrpacc': 'racf:cgrpacc',
                'cinitct': 'racf:cinitct',
                'cljdate': 'racf:cljdate',
                'cljtime': 'racf:cljtime',
                'coper': 'racf:coper',
                'cowner': 'racf:cowner',
                'cresume': 'racf:cresume',
                'crevoke': 'racf:crevoke',
                'crevokfl': 'racf:crevokfl',
                'cspecial': 'racf:cspecial',
                'cuacc': 'racf:cuacc',
                'creatdat': 'racf:creatdat',
                'data': 'racf:data',
                'dfltgrp': 'defgroup',
                'expired': 'racf:expired',
                'factorn': 'racf:factorn',
                'factor': 'racf:factor',
                'facactv': 'racf:facactv',
                'factagnn': 'racf:factagnn',
                'facvalnn': 'racf:facvalnn',
                'group': 'racf:group',
                'grpacc': 'racf:grpacc',
                'hasphras': 'racf:hasphras',
                'haspwd': 'racf:haspwd',
                'lastdate': 'racf:lastdate',
                'lasttime': 'racf:lasttime',
                'mfaflbk': 'racf:mfaflbk',
                'mfapolnm': 'racf:mfapolnm',
                'model': 'racf:model',
                'name': 'name',
                'oidcard': 'racf:oidcard',
                'oper': 'racf:oper',
                'owner': 'racf:owner',
                'passdate': 'racf:passdate',
                'passint': 'racf:passint',
                'password': 'racf:password',
                'phrase': 'racf:phrase',
                'phrdate': 'racf:phrdate',
                'phrint': 'racf:phrint',
                'pphenv': 'racf:pphenv',
                'protectd': 'racf:protectd',
                'pwdenv': 'racf:pwdenv',
                'rest': 'racf:rest',
                'resume': 'resumedate',
                'revoke': 'revokedate',
                'revokefl': 'racf:revokefl',
                'roaudit': 'racf:roaudit',
                'seclabel': 'seclabel',
                'seclevel': 'racf:seclevel',
                'special': 'racf:special',
                'uacc': 'racf:uacc',
                'uaudit': 'uaudit',
                'whendays': 'whendays',
                'whensrv': 'whensrv',
                'whentime': 'whentime'
            },
            'cics': {
                'opclass': 'racf:opclass',
                'opident': 'opident',
                'opprty': 'opprty',
                'rslkey': 'racf:rslkey',
                'timeout': 'timeout',
                'tslkey': 'racf:tslkey',
                'xrfsoff': 'force'
            },
            'csdata': {
                'custom-keyword': 'racf:custom-keyword'
            },
            'dce': {
                'autolog': 'autolog',
                'dcename': 'dcename',
                'homecell': 'homecell',
                'homeuuid': 'homeuuid',
                'uuid': 'uuid'
            },
            'dfp': {
                'dataappl': 'dataappl',
                'dataclas': 'dataclas',
                'mgmtclas': 'mgmtclass',
                'storclas': 'storclas'
            },
            'eim': {
                'ldapprof': 'racf:ldapprof'
            },
            'kerb': {
                'encrypt': 'racf:encrypt',
                'kerbname': 'racf:kerbname',
                'keyfrom': 'racf:keyfrom',
                'keyvers': 'racf:keyvers',
                'maxtktlf': 'racf:maxtktlf'
            },
            'language': {
                'primary': 'primary',
                'second': 'secondary'
            },
            'lnotes': {
                'sname': 'racf:sname'
            },
            'mfa': {
                'factor': 'racf:factor',
                'facactv': 'racf:facactv',
                'factags': 'racf:factags',
                'mfaflbk': 'racf:mfaflbk',
                'mfapolnm': 'racf:mfapolnm'
            },
            'nds': {
                'uname': 'racf:uname'
            },
            'netview': {
                'consname': 'consid',
                'ctl': 'secctl',
                'domains': 'nvdomains',
                'ic': 'ic',
                'msgrecvr': 'msgrec',
                'ngmfadmn': 'racf:ngmfadmn',
                'ngmfvspn': 'gmfadmin',
                'opclass': 'racf:opclass'
            },
            'omvs': {
                'assize': 'assize',
                'autouid': 'racf:autouid',
                'cputime': 'cputime',
                'fileproc': 'filemax',
                'home': 'home',
                'memlimit': 'memlim',
                'mmaparea': 'mmaparea',
                'procuser': 'procmax',
                'program': 'pgm',
                'shared': 'racf:shared',
                'shmemmax': 'shmemmax',
                'threads': 'threads',
                'uid': 'uid'
            },
            'operparm': {
                'altgrp': 'altgrp',
                'auto': 'auto',
                'cmdsys': 'cmdsys',
                'dom': 'dom',
                'hc': 'hc',
                'intids': 'intid',
                'key': 'key',
                'level': 'racf:level',
                'logcmd': 'logcmd',
                'mform': 'mform',
                'migid': 'migid',
                'monitor': 'mon',
                'mscope': 'racf:mscope',
                'operauth': 'auth',
                'routcode': 'routcode',
                'storage': 'storage',
                'ud': 'ud',
                'unknids': 'unkids'
            },
            'ovm': {
                'fsroot': 'racf:fsroot',
                'vhome': 'racf:vhome',
                'vprogram': 'racf:vprogram',
                'vuid': 'racf:vuid'
            },
            'proxy': {
                'binddn': 'racf:binddn',
                'bindpw': 'racf:bindpw',
                'ldaphost': 'racf:ldaphost'
            },
            'tso': {
                'acctnum': 'acctnum',
                'command': 'command',
                'dest': 'dest',
                'hldclass': 'holdclass',
                'jobclass': 'jobclass',
                'maxsize': 'maxsize',
                'msgclass': 'msgclass',
                'proc': 'proc',
                'seclabel': 'seclabel',
                'size': 'size',
                'sysoutcl': 'sysclass',
                'unit': 'unit',
                'userdata': 'userdata'
            },
            'workattr': {
                'waaccnt': 'waaccnt',
                'waaddr1': 'waaddr1',
                'waaddr2': 'waaddr2',
                'waaddr3': 'waaddr3',
                'waaddr4': 'waaddr4',
                'wabldg': 'wabldg',
                'wadept': 'wadept',
                'waname': 'waname',
                'waroom': 'waroom',
                'waemail': 'waemail'
            }
        }
        self.segment_traits = {}
        self.trait_map = {}

    def is_special(self, userid: str) -> bool:
        result = self.extract({"userid": userid})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        if "SPECIAL" in profile["base"]["attributes"]:
            return True
        return False

    def set_special(self, userid: str) -> dict:
        return self.alter({"userid": userid, "special": True})

    def get_uid(self, userid: str) -> Union[str,int]:
        result = self.extract({"userid": userid, "omvs": True})
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        return profile["omvs"]["uid"]

    def set_uid(self, userid: str, uid: int) -> dict:
        return self.alter({"userid": userid, "uid": str(uid)})

    def is_special(self, userid: str) -> bool:
        result = self.extract(userid)
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        if "SPECIAL" in profile["base"]["attributes"]:
            return True
        return False

    def set_special(self, userid: str) -> dict:
        return self.alter({"userid": userid, "special": True})

    def get_uid(self, userid: str) -> Union[str,int]:
        result = self.extract(userid, additional_segments=["omvs"])
        profile = result["securityresult"]["user"]["commands"][0]["profile"]
        return profile["omvs"]["uid"]

    def set_uid(self, userid: str, uid: int) -> dict:
        return self.alter({"userid": userid, "uid": uid})

    def add(self, traits: dict) -> dict:
        userid = traits["userid"]
        self.build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self.build_segments(user_request)
        return self.make_request(user_request)

    def alter(self, traits: dict) -> dict:
        userid = traits["userid"]
        self.build_segment_dictionaries(traits)
        user_request = UserRequest(userid, "set")
        self.build_segments(user_request, alter=True)
        return self.make_request(user_request,3)

    def extract(self, traits: dict) -> dict:
        userid = traits["userid"]
        self.build_bool_segment_dictionaries(traits)
        user_request = UserRequest(userid, "listdata")
        self.build_segments(user_request, extract=True)
        result = self.make_request(user_request)
        if "error" in result["securityresult"]["user"]:
            raise SecurityRequestError(result)
        if (result["securityresult"]["returncode"] == 0 
                and result["securityresult"]["reasoncode"] == 0):
            self.__format_profile(result)
            return result
        raise SecurityRequestError(result)

    def delete(self, userid: str) -> dict:
        user_request = UserRequest(userid, "del")
        return self.make_request(user_request)

    def build_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            for segment in self.valid_segment_traits.keys():
                if trait in self.valid_segment_traits[segment].keys():
                    if not segment in self.segment_traits.keys():
                        self.segment_traits[segment] = {}
                    self.segment_traits[segment][trait] = traits[trait]
                    self.trait_map[trait] =  self.valid_segment_traits[segment][trait]

    def build_segments(
            self, 
            user_request: UserRequest, 
            alter=False, 
            extract=False
    ) -> None:
        for segment in self.segment_traits.keys():
            user_request.build_segment(
                segment, 
                self.segment_traits[segment], 
                self.trait_map, 
                alter=alter, 
                extract=extract
            )
        # Clear segments for new request
        self.segment_traits = {}
    
    def build_bool_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            if trait in self.valid_segment_traits.keys():
                self.segment_traits[trait] = traits[trait]

    def make_request(self, user_request: UserRequest, opts: int = 1) -> dict:
        result_xml = self.irrsmo00.call_racf(user_request.dump_request_xml(),opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()

    def __format_profile(self, result: dict) -> None:
        messages = result["securityresult"]["user"]["commands"][0]["messages"]
        profile = {}
        current_segment = "base"
        additional_segments = [
            f"{segment.upper()} INFORMATION" 
            for segment in self.valid_segment_traits
            if segment != "base"
        ]
        no_segment_information_keys = [f"NO {segment}" for segment in additional_segments]
        profile[current_segment] = {}
        profile[current_segment]["groups"] = {}
        i = 0
        while i < len(messages):
            if messages[i] == " " or messages[i] in no_segment_information_keys:
                i += 1
                continue
            if i < len(messages)-1 and messages[i] in additional_segments:
                current_segment = messages[i].split()[0].lower()
                profile[current_segment] = {}
                i += 2
            if (i < len(messages)-1 
                    and messages[i+1] == " ---------------------------------------------"
                ):
                    semi_tabular_data = messages[i:i+3]
                    self.__add_semi_tabular_data_to_segment(
                        profile[current_segment], semi_tabular_data
                    )
                    i += 2
            elif messages[i][:8] == "  GROUP=":
                group = messages[i].split("=")[1].split()[0]
                profile[current_segment]["groups"][group] = {}
                message = messages[i] + messages[i+1] + messages[i+2] + messages[i+3]
                self.__add_key_value_pairs_to_segment(
                    profile[current_segment]["groups"][group], message[17:]
                )
                i += 3
            elif "=" not in messages[i] and messages[i].strip()[:3] != "NO-":
                messages[i] = f"{messages[i]}={messages[i+1]}"
                self.__add_key_value_pairs_to_segment(
                    profile[current_segment], messages[i]
                )
                i += 1
            else:
                self.__add_key_value_pairs_to_segment(
                    profile[current_segment], messages[i]
                )
            i += 1
        del result["securityresult"]["user"]["commands"][0]["messages"]
        result["securityresult"]["user"]["commands"][0]["profile"] = profile

    def __add_semi_tabular_data_to_segment(
            self, 
            segment: dict, 
            semi_tabular_data: List[str]
    ) -> None:
        heading_tokens = list(filter(("").__ne__, semi_tabular_data[0].split("  ")))
        key_prefix = heading_tokens[0]
        keys = [f"{key_prefix}{key.strip()[1:-1]}" for key in heading_tokens[1:]]
        values = semi_tabular_data[-1].split()
        for i in range(len(keys)):
            key = keys[i].strip().lower().replace(" ", "").replace("-", "")
            segment[key] = self.__cast_value(values[i])

    def __add_key_value_pairs_to_segment(
            self,
            segment: dict, 
            message: str,
            list_fields=["attributes", "classauthorizations"]
    ) -> None:
        tokens = message.strip().split("=")
        key = tokens[0]
        for i in range(1, len(tokens)):
            sub_tokens = list(filter(("").__ne__, tokens[i].split("  ")))
            value = sub_tokens[0].strip()
            if key[:3] == "NO-":
                key = key[3:]
                value = "N/A"
            current_key = key.strip().lower().replace(" ", "").replace("-", "")
            if current_key in list_fields:
                if current_key not in segment:
                    segment[current_key] = []
                values = [self.__cast_value(value) for value in value.split() if value != "NONE"]
                segment[current_key] += values
            else:
                segment[current_key] = self.__cast_value(value)
            key = "".join(sub_tokens[1:])
            if len(sub_tokens) == 1:
                if i < len(tokens) -1 and " " in sub_tokens[0] and i != 0:
                    sub_tokens = sub_tokens[0].split()
                    segment[current_key] = self.__cast_value(sub_tokens[0])
                    key = sub_tokens[-1]
                else:
                    key = sub_tokens[0]

    def __cast_value(self, value: str) -> Union[None,int,float,str]:
        if value == "N/A" or value == "NONE" or value == "NONE SPECIFIED":
            return None
        if "." in value:
            try:
                return float(value)
            except ValueError:
                return value
        try:
            return int(value.replace(",", ""))
        except ValueError:
            return value 
