from common.irrsmo00 import IRRSMO00
from genprof.ResourceRequest import ResourceRequest
from common.SecurityResult import SecurityResult
from common.SecurityRequestError import SecurityRequestError
from typing import Union, List


class ResourceAdmin():
    def __init__(self) -> None:
        self.irrsmo00 = IRRSMO00()
        self.valid_segment_traits = {
            'base': {
                'aclcnt': 'racf:aclcnt', 
                'aclacnt': 'racf:aclacnt', 
                'aclacs': 'racf:aclacs', 
                'aclid': 'racf:aclid', 
                'acl2cnt': 'racf:acl2cnt', 
                'acl2acnt': 'racf:acl2acnt', 
                'acl2acs': 'racf:acl2acs', 
                'acl2cond': 'racf:acl2cond', 
                'acl2ent': 'racf:acl2ent', 
                'acl2id': 'racf:acl2id', 
                'acsaltr': 'racf:acsaltr', 
                'acscntl': 'racf:acscntl', 
                'acsread': 'racf:acsread', 
                'acsupdt': 'racf:acsupdt', 
                'all': 'racf:all', 
                'appldata': 'racf:appldata', 
                'audaltr': 'racf:audaltr', 
                'audcntl': 'racf:audcntl', 
                'audnone': 'racf:audnone', 
                'audread': 'racf:audread', 
                'audupdt': 'racf:audupdt', 
                'authuser': 'racf:authuser', 
                'automatc': 'racf:automatc', 
                'category': 'racf:category', 
                'creatdat': 'racf:creatdat', 
                'data': 'racf:data', 
                'fclass': 'racf:fclass', 
                'fgeneric': 'racf:fgeneric', 
                'fprofile': 'racf:fprofile', 
                'fvolume': 'racf:fvolume', 
                'gaudaltr': 'racf:gaudaltr', 
                'gaudcntl': 'racf:gaudcntl', 
                'gaudnone': 'racf:gaudnone', 
                'gaudread': 'racf:gaudread', 
                'gaudupdt': 'racf:gaudupdt', 
                'generic': 'racf:generic', 
                'history': 'racf:history', 
                'lchgdat': 'racf:lchgdat', 
                'level': 'racf:level', 
                'lrefdat': 'racf:lrefdat', 
                'member': 'racf:member', 
                'noracf': 'racf:noracf', 
                'notify': 'racf:notify', 
                'noyourac': 'racf:noyourac', 
                'owner': 'racf:owner', 
                'profile': 'racf:profile', 
                'raudit': 'racf:raudit', 
                'resgroup': 'racf:resgroup', 
                'rgaudit': 'racf:rgaudit', 
                'seclabel': 'racf:seclabel', 
                'seclevel': 'racf:seclevel', 
                'singldsn': 'racf:singldsn', 
                'stats': 'racf:stats', 
                'timezone': 'racf:timezone', 
                'tvtoc': 'racf:tvtoc', 
                'uacc': 'racf:uacc', 
                'volume': 'racf:volume', 
                'warning': 'racf:warning', 
                'whendays': 'racf:whendays', 
                'whentime': 'racf:whentime'
            },
            'cdtinfo': {
                'cdtcase': 'case', 
                'cdtdftrc': 'defaultrc', 
                'cdtfirst': 'first', 
                'cdtgen': 'generic', 
                'cdtgenl': 'genlist', 
                'cdtgroup': 'grouping', 
                'cdtkeyql': 'keyqual', 
                'cdtmac': 'macprocessing', 
                'cdtmaxln': 'maxlenx', 
                'cdtmaxlx': 'maxlength', 
                'cdtmembr': 'member', 
                'cdtoper': 'operations', 
                'cdtother': 'other', 
                'cdtposit': 'posit', 
                'cdtprfal': 'profilesallowed', 
                'cdtracl': 'raclist', 
                'cdtsigl': 'signal', 
                'cdtslreq': 'seclabelrequired', 
                'cdtuacc': 'defaultuacc'
            },
            'cfdef': {
                'cfdtype': 'type', 
                'cffirst': 'first', 
                'cfhelp': 'help', 
                'cflist': 'listhead', 
                'cfmixed': 'mixed', 
                'cfmnval': 'minvalue', 
                'cfmxlen': 'maxlength', 
                'cfmxval': 'other', 
                'cfother': 'other', 
                'cfvalrx': 'racf:cfvalrx'
            },
            'csdata': {
                'custom-keyword': 'racf:custom-keyword'
            },
            'dlfdata': {
                'jobname': 'racf:jobname', 
                'retain': 'racf:retain'
            },
            'eim': {
                'domaindn': 'domaindn', 
                'kerbreg': 'kerberg', 
                'localreg': 'localreg', 
                'options': 'options', 
                'x509reg': 'X509reg'
            },
            'kerb': {
                'chkaddrs': 'checkaddrs', 
                'deftktlf': 'deftktlife', 
                'encrypt': 'encrypt', 
                'kerbname': 'kerbname', 
                'keyvers': 'racf:keyvers', 
                'maxtktlf': 'maxtktlf', 
                'mintktlf': 'mintklife', 
                'password': 'password'
            },
            'icsf': {
                'crtlbls': 'symexportcert', 
                'export': 'symexportable', 
                'keylbls': 'symexportkey', 
                'scpwrap': 'symcpacfwrap', 
                'scpret': 'symcpacfret', 
                'usage': 'asymusage'
            },
            'ictx': {
                'domap': 'domap', 
                'mapreq': 'mapreq', 
                'maptimeo': 'maptimeo', 
                'usemap': 'usemap'
            },
            'idtparms': {
                'sigtoken': 'sigtoken', 
                'sigseqn': 'sigseqnum', 
                'sigcat': 'sigcat', 
                'sigalg': 'sigalg', 
                'idttimeo': 'idttimeout', 
                'anyappl': 'anyappl'
            },
            'jes': {
                'keylabel': 'racf:keylabel'
            },
            'mfpolicy': {
                'factors': 'racf:factors', 
                'timeout': 'racf:timeout', 
                'reuse': 'racf:reuse'
            },
            'proxy': {
                'binddn': 'binddn', 
                'bindpw': 'bindpw', 
                'ldaphost': 'ldaphost'
            },
            'session': {
                'convsec': 'racf:convsec', 
                'interval': 'racf:interval', 
                'lock': 'racf:lock', 
                'sesskey': 'racf:sesskey'
            },
            'sigver': {
                'failload': 'failload', 
                'sigaudit': 'sigaudit', 
                'sigreqd': 'sigrequired'
            },
            'ssignon': {
                'keycrypt': 'racf:keycrypt', 
                'ptkeylab': 'ptkeylab', 
                'pttype': 'pttype', 
                'pttimeo': 'pttimeo', 
                'ptreplay': 'ptreplay', 
                'keylabel': 'racf:keylabel', 
                'keymask': 'racf:keymask'
            },
            'stdata': {
                'group': 'racf:group', 
                'privlege': 'racf:privlege', 
                'trace': 'racf:trace', 
                'trusted': 'racf:trusted', 
                'user': 'racf:user'
            },
            'svfmr': {
                'parmname': 'racf:parmname', 
                'script': 'racf:script'
            },
            'tme': {
                'children': 'racf:children', 
                'groups': 'racf:groups', 
                'parent': 'racf:parent', 
                'resource': 'racf:resource', 
                'roles': 'racf:roles'
}}
        self.segment_traits = {}
        self.trait_map = {}
    
    def get_uacc(self, resource_name: str, class_name: str) -> str:
        result = self.extract({'resourcename': resource_name, "classname": class_name})
        profile = result['securityresult']['resource']['commands'][0]['profile']
        return profile['base'].get('universal access')
    
    def set_uacc(self, resource_name: str, class_name: str, uacc: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "uacc": uacc})
    
    def get_your_acc(self, resource_name: str, class_name: str) -> str:
        result = self.extract({'resourcename': resource_name, "classname": class_name})
        profile = result['securityresult']['resource']['commands'][0]['profile']
        return profile['base'].get('your access')

    def add_category(self, resource_name: str, class_name: str, category_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addcategory": category_name})

    def del_category(self, resource_name: str, class_name: str, category_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delcategory": category_name})

    def add_member(self, resource_name: str, class_name: str, member_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addmember": member_name})

    def del_member(self, resource_name: str, class_name: str, member_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delmember": member_name})

    def add_volume(self, resource_name: str, class_name: str, volume_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addvolume": volume_name})

    def del_volume(self, resource_name: str, class_name: str, volume_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delvolume": volume_name})

    def set_jobname(self, resource_name: str, class_name: str, jobname_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setjobname": jobname_name})

    def add_jobname(self, resource_name: str, class_name: str, jobname_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addjobname": jobname_name})

    def del_jobname(self, resource_name: str, class_name: str, jobname_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "deljobname": jobname_name})

    def no_jobnames(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nojobname": "N/A"})

    def set_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setcrtlbls": crtlbl_name})

    def add_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addcrtlbls": crtlbl_name})

    def del_crtlbl(self, resource_name: str, class_name: str, crtlbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delcrtlbls": crtlbl_name})

    def no_crtlbls(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nocrtlbls": "N/A"})

    def set_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setkeylbls": keylbl_name})

    def add_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addkeylbls": keylbl_name})

    def del_keylbl(self, resource_name: str, class_name: str, keylbl_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delkeylbls": keylbl_name})

    def no_keylbls(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nokeylbls": "N/A"})

    def set_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setfactors": factor_name})

    def add_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addfactors": factor_name})

    def del_factor(self, resource_name: str, class_name: str, factor_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delfactors": factor_name})

    def no_factors(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nofactors": "N/A"})

    def set_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setchildren": child_name})

    def add_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addchildren": child_name})

    def del_child(self, resource_name: str, class_name: str, child_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delchildren": child_name})

    def no_children(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nochildren": "N/A"})

    def set_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setgroups": group_name})

    def add_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addgroups": group_name})

    def del_group(self, resource_name: str, class_name: str, group_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delgroups": group_name})

    def no_groups(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "nogroups": "N/A"})

    def set_resource(self, resource_name: str, class_name: str, tme_resource_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setresource": tme_resource_name})

    def add_resource(self, resource_name: str, class_name: str, tme_resource_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addresource": tme_resource_name})

    def del_resource(self, resource_name: str, class_name: str, tme_resource_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delresource": tme_resource_name})

    def no_resources(self, resource_name: str, class_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "noresource": "N/A"})

    def set_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "setroles": role_name})

    def add_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "addroles": role_name})

    def del_role(self, resource_name: str, class_name: str, role_name: str) -> str:
        return self.alter({'resourcename': resource_name, "classname": class_name, "delroles": role_name})

    def no_roles(self, resource_name: str, class_name: str) -> str: 
        return self.alter({'resourcename': resource_name, "classname": class_name, "noroles": "N/A"})


    def add(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request)
        return self.make_request(profile_request)

    def alter(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "set")
        self.build_segments(profile_request, alter=True)
        return self.make_request(profile_request,3)

    def extract(self, traits: dict) -> dict:
        resourcename = traits["resourcename"]
        classname = traits["classname"]
        self.build_bool_segment_dictionaries(traits)
        profile_request = ResourceRequest(resourcename, classname, "listdata")
        self.build_segments(profile_request, extract=True)
        result = self.make_request(profile_request)
        if "error" in result["securityresult"]["resource"]:
            raise SecurityRequestError(result)
        if (result["securityresult"]["returncode"] == 0 
                and result["securityresult"]["reasoncode"] == 0):
            self.__format_profile(result)
            return result
        raise SecurityRequestError(result)

    def delete(self, resourcename: str, classname: str) -> dict:
        profile_request = ResourceRequest(resourcename, classname, "del")
        return self.make_request(profile_request)

    def evaluate_trait(self, trait: str, segment: str, value: Union[str,list]):
        #print("Called to evaluate trait: %s for segment: %s" % (trait,segment))
        #print(self.valid_segment_traits.keys())
        if not segment in self.valid_segment_traits.keys():
            return -1
        #print(self.valid_segment_traits[segment].keys())
        if not trait in self.valid_segment_traits[segment].keys():
            if trait[:3] == 'add':
                operation = 'add'
                true_trait = trait[3:]
            elif trait[:2] == 'no':
                operation = 'del'
                true_trait = trait[2:]
            elif trait[:3] == 'del':
                operation = 'remove'
                true_trait = trait[3:]
            elif trait[:3] == 'set':
                operation = 'set'
                true_trait = trait[3:]
            else:
                return -1
            self.evaluate_trait(true_trait, segment, [value, operation])
            return 0
        #print("Assigning a value")
        #print(value)
        if not segment in self.segment_traits.keys():
            self.segment_traits[segment] = {}
        self.segment_traits[segment][trait] = value
        self.trait_map[trait] =  self.valid_segment_traits[segment][trait]
        return 0


    def build_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            if ':' in trait:
                segment = trait.split(':')[0]
                true_trait = trait.split(':')[1]
                self.evaluate_trait(true_trait,segment,traits[trait])
                continue
            for segment in self.valid_segment_traits.keys():
                self.evaluate_trait(trait,segment,traits[trait])


    def build_segments(
            self, 
            profile_request: ResourceRequest, 
            alter=False, 
            extract=False,
    ) -> None:
        for segment in self.segment_traits.keys():
            profile_request.build_segment(
                segment, 
                self.segment_traits[segment], 
                self.trait_map, alter=alter, 
                extract=extract
            )
        # Clear segments for new request
        self.segment_traits = {}
    
    def build_bool_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            if trait in self.valid_segment_traits.keys():
                self.segment_traits[trait] = traits[trait]

    def make_request(self, profile_request: ResourceRequest, opts: int = 1) -> dict:
        result_xml = self.irrsmo00.call_racf(profile_request.dump_request_xml(),opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()

    def __format_profile(self, result: dict) -> None:
        messages = result["securityresult"]["resource"]["commands"][0]["messages"]
        profile = {}
        current_segment = "base"
        profile[current_segment] = {}
        i = 0
        while i < len(messages):
            if messages[i] == " ":
                i += 1
                continue
            
            if '=' in messages[i]:
                field = messages[i].split('=')[0].strip().lower()
                profile[current_segment][field] = clean_and_separate(messages[i].split('=')[1])
                i += 1
                continue
            
            if ' INFORMATION' in messages[i]:
                if i < len(messages)-1 and '----------------' in messages[i+1]:
                    current_segment = messages[i].split(' INFORMATION')[0].strip().lower()
                    profile[current_segment] = {}
                    i+=2
                    continue
                elif messages[i].split(' ')[0] == "NO" and messages[i].split(' ')[2] == "INFORMATION":
                    current_segment = messages[i].split(' ')[1].strip().lower()
                    profile[current_segment] = {}
                    i+=1
                    continue
                
            
            if i < len(messages)-2 and ("   " in messages[i]) and ("--" in messages[i+1]):
                tmp_ind = [j for j in range(len(messages[i+1])) if messages[i+1][j] == '-']
                indexes = [tmp_ind[j] for j in range(len(tmp_ind)) if j == 0 or tmp_ind[j]-tmp_ind[j-1]>1]
                #print(tmp_ind,indexes)
                for j in range(len(indexes)):
                    if j < len(indexes) - 1:
                        ind_e0 = indexes[j+1]
                        ind_e1 = indexes[j+1]
                    else:
                        ind_e0 = len(messages[i])
                        ind_e1 = len(messages[i+2])
                    
                    field = messages[i][indexes[j]:ind_e0].strip().lower()
                    profile[current_segment][field] = clean_and_separate(messages[i+2][indexes[j]:ind_e1])
                i += 2
                continue
            
            if i < len(messages)-2 and ("-" in messages[i+1]):
                field = ' '.join([txt.lower().strip() for txt in list(filter(None,messages[i].split(' ')))])
                profile[current_segment][field] = clean_and_separate(messages[i+2])
                i += 2
                continue

            i += 1

        # Post processing
        if '(g)' in profile['base'].get('name'):
            profile['base']['generic'] = True
            profile['base']['name'] = cast_value(profile['base'].get('name')[0])
        else:
            profile['base']['generic'] = False
        
        if profile['base'].get('notify') == [None, 'user', 'to', 'be', 'notified']:
            profile['base']['notify'] = None
        
        del result["securityresult"]["resource"]["commands"][0]["messages"]
        result["securityresult"]["resource"]["commands"][0]["profile"] = profile

def cast_value(value: str) -> Union[None,int,float,str]:
    if value == "n/a" or value == "none" or value == "none specified" or value == 'no':
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

def clean_and_separate(value: str):
    cln_val = value.strip().lower()
    if ',' in cln_val:
        out = [cast_value(val.strip()) for val in cln_val.split(',') ]
    elif ' ' in cln_val:
        out = [cast_value(val.strip()) for val in cln_val.split(' ') ]
    else:
        out = cast_value(cln_val)
    return out