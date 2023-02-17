from common.irrsmo00 import IRRSMO00
from dataset.DatasetRequest import DatasetRequest
from common.SecurityResult import SecurityResult
from common.SecurityRequestError import SecurityRequestError
from typing import Union, List


class DatasetAdmin():
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
                'altvol': 'racf:altvol',
                'audaltr': 'racf:audaltr',
                'audcntl': 'racf:audcntl',
                'audnone': 'racf:audnone',
                'audread': 'racf:audread',
                'audupdt': 'racf:audupdt',
                'authuser': 'racf:authuser',
                'category': 'racf:category',
                'creatdat': 'racf:creatdat',
                'data': 'racf:data',
                'dsns': 'racf:dsns',
                'dstype': 'racf:dstype',
                'erase': 'racf:erase',
                'fclass': 'racf:fclass',
                'fgeneric': 'racf:fgeneric',
                'fileseq': 'racf:fileseq',
                'from': 'racf:from',
                'fvolume': 'racf:fvolume',
                'gaudaltr': 'racf:gaudaltr',
                'gaudcntl': 'racf:gaudcntl',
                'gaudnone': 'racf:gaudnone',
                'gaudread': 'racf:gaudread',
                'gaudupdt': 'racf:gaudupdt',
                'generic': 'racf:generic',
                'groupds': 'racf:groupds',
                'groupnm': 'racf:groupnm',
                'history': 'racf:history',
                'id': 'racf:id',
                'lchgdat': 'racf:lchgdat',
                'level': 'racf:level',
                'lrefdat': 'racf:lrefdat',
                'model': 'racf:model',
                'noracf': 'racf:noracf',
                'notify': 'racf:notify',
                'owner': 'racf:owner',
                'prefix': 'racf:prefix',
                'profile': 'racf:profile',
                'raudit': 'racf:raudit',
                'retpd': 'racf:retpd',
                'rgaudit': 'racf:rgaudit',
                'seclabel': 'racf:seclabel',
                'seclevel': 'racf:seclevel',
                'set': 'racf:set',
                'setonly': 'racf:setonly',
                'stats': 'racf:stats',
                'tape': 'racf:tape',
                'uacc': 'racf:uacc',
                'unit': 'racf:unit',
                'volume': 'racf:volume',
                'volser': 'racf:volser',
                'warning': 'racf:warning'
            },
            'csdata': {
                'custom-keyword': 'racf:custom-keyword'
            },
            'dfp': {
                'resowner': 'racf:resowner',
                'datakey': 'racf:datakey'
            },
            'tme': {
                'roles': 'racf:roles'
            }
        }
        self.segment_traits = {}
        self.trait_map = {}

    def get_uacc(self, dataset_name: str) -> str:
        result = self.extract({"datasetname": dataset_name})
        profile = result['securityresult']['dataset']['commands'][0]['profile']
        return profile['base'].get('universal access')
    
    def set_uacc(self, dataset_name: str, uacc: str) -> str:
        return self.alter({"datasetname": dataset_name, "uacc": uacc})
    
    def get_your_acc(self, dataset_name: str) -> str:
        result = self.extract({"datasetname": dataset_name})
        profile = result['securityresult']['dataset']['commands'][0]['profile']
        return profile['base'].get('your access')
    
    def add_category(self, dataset_name: str, category_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "addcategory": category_name})

    def del_category(self, dataset_name: str, category_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "delcategory": category_name})

    def add_volume(self, dataset_name: str, volume_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "addvolume": volume_name})

    def del_volume(self, dataset_name: str, volume_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "delvolume": volume_name})

    def add_role(self, dataset_name: str, role_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "addroles": role_name})

    def remove_role(self, dataset_name: str, role_name: str) -> str:
        return self.alter({"datasetname": dataset_name, "delroles": role_name})

    def no_roles(self, dataset_name: str) -> str: #test this
        return self.alter({"datasetname": dataset_name, "noroles": True})

    def add(self, traits: dict) -> dict:
        datasetname = traits["datasetname"]
        if "generic" in traits.keys():
            generic = traits["generic"]
        else:
            generic = "no"
        if "volid" in traits.keys():
            volid = traits["volid"]
        else:
            volid = ''
        self.build_segment_dictionaries(traits)
        dataset_request = DatasetRequest(datasetname, "set", generic, volid)
        self.build_segments(dataset_request)
        return self.make_request(dataset_request)

    def alter(self, traits: dict) -> dict:
        datasetname = traits["datasetname"]
        if "generic" in traits.keys():
            generic = traits["generic"]
        else:
            generic = "no"
        if "volid" in traits.keys():
            volid = traits["volid"]
        else:
            volid = ''
        self.build_segment_dictionaries(traits)
        dataset_request = DatasetRequest(datasetname, "set", generic, volid)
        self.build_segments(dataset_request, alter=True)
        return self.make_request(dataset_request,3)
    
    def extract(self, traits: dict) -> dict:
        datasetname = traits["datasetname"]
        if "generic" in traits.keys():
            generic = traits["generic"]
        else:
            generic = "no"
        if "volid" in traits.keys():
            volid = traits["volid"]
        else:
            volid = ''
        self.build_bool_segment_dictionaries(traits)
        dataset_request = DatasetRequest(datasetname, "listdata", generic, volid)
        self.build_segments(dataset_request, extract=True)
        result = self.make_request(dataset_request)
        if "error" in result["securityresult"]["dataset"]:
            raise SecurityRequestError(result)
        if (result["securityresult"]["returncode"] == 0 
                and result["securityresult"]["reasoncode"] == 0):
            self.__format_profile(result)
            return result
        raise SecurityRequestError(result)


    def delete(self, datasetname: str, generic: str = "no", volid: str = "") -> dict:
        dataset_request = DatasetRequest(datasetname, "del", generic, volid)
        return self.make_request(dataset_request)

    def build_segment_dictionaries(self, traits: dict) -> None:
        for trait in traits:
            alt_trait = trait
            if trait[:3] == 'add':
                operation = 'add'
                trait = trait[3:]
            elif trait[:2] == 'no':
                operation = 'del'
                trait = trait[2:]
            elif trait[:3] == 'del':
                operation = 'remove'
                trait = trait[3:]  
            else:
                operation = ""
            for segment in self.valid_segment_traits.keys():
                if trait in self.valid_segment_traits[segment].keys():
                    if not segment in self.segment_traits.keys():
                        self.segment_traits[segment] = {}
                    if not (operation == ""):
                        self.segment_traits[segment][trait] = [traits[alt_trait], operation]
                    else:
                        self.segment_traits[segment][trait] = traits[trait]
                    self.trait_map[trait] =  self.valid_segment_traits[segment][trait]

    def build_segments(
            self, 
            dataset_request: DatasetRequest, 
            alter=False, 
            extract=False
    ) -> None:
        for segment in self.segment_traits.keys():
            dataset_request.build_segment(
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

    def make_request(self, dataset_request: DatasetRequest, opts: int = 1) -> dict:
        result_xml = self.irrsmo00.call_racf(dataset_request.dump_request_xml(),opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()

    def __format_profile(self, result: dict) -> None:
        messages = result["securityresult"]["dataset"]["commands"][0]["messages"]
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
                
            
            if i < len(messages)-2 and ("  " in messages[i]) and ("--" in messages[i+1]):
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
            
            if 'NO INSTALLATION DATA' in messages[i]:
                profile[current_segment]['installation data'] = None
            i += 1
        
        if profile['base'].get('installation data'):
            profile['base']['installation data'] = ' '.join(profile['base']['installation data'])
            
        if profile['base'].get('notify') == [None, 'user', 'to', 'be', 'notified']:
            profile['base']['notify'] = None
        
        del result["securityresult"]["dataset"]["commands"][0]["messages"]
        result["securityresult"]["dataset"]["commands"][0]["profile"] = profile

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