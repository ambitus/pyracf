from common.irrsmo00 import IRRSMO00
from setropts.SetroptsRequest import SetroptsRequest
from common.SecurityResult import SecurityResult
from common.SecurityRequestError import SecurityRequestError
from typing import Union, List


class SetroptsAdmin():
    def __init__(self) -> None:
        self.irrsmo00 = IRRSMO00()
        self.valid_segment_traits = {
            'base': {
                'addcreat': 'racf:addcreat',
                'adsp': 'racf:adsp',
                'applaudt': 'racf:applaudt',
                'audit': 'racf:audit',
                'catdsns': 'racf:catdsns',
                'classact': 'racf:classact',
                'classtat': 'racf:classtat',
                'cmdviol': 'racf:cmdviol',
                'compmode': 'racf:compmode',
                'egn': 'racf:egn',
                'erase': 'racf:erase',
                'eraseall': 'racf:eraseall',
                'erasesec': 'racf:erasesec',
                'gencmd': 'racf:gencmd',
                'generic': 'racf:generic',
                'genlist': 'racf:genlist',
                'genowner': 'racf:genowner',
                'global': 'racf:global',
                'grplist': 'racf:grplist',
                'history': 'racf:history',
                'inactive': 'racf:inactive',
                'initstat': 'racf:initstat',
                'interval': 'racf:interval',
                'jesbatch': 'racf:jesbatch',
                'jesearly': 'racf:jesearly',
                'jesnje': 'racf:jesnje',
                'jesundef': 'racf:jesundef',
                'jesxbm': 'racf:jesxbm',
                'kerblvl': 'racf:kerblvl',
                'list': 'racf:list',
                'logalwys': 'racf:logalwys',
                'logdeflt': 'racf:logdeflt',
                'logfail': 'racf:logfail',
                'lognever': 'racf:lognever',
                'logsucc': 'racf:logsucc',
                'minchang': 'racf:minchang',
                'mixdcase': 'racf:mixdcase',
                'mlactive': 'racf:mlactive',
                'mlfs': 'racf:mlfs',
                'mlipc': 'racf:mlipc',
                'mlnames': 'racf:mlnames',
                'mlquiet': 'racf:mlquiet',
                'mls': 'racf:mls',
                'mlstable': 'racf:mlstable',
                'model': 'racf:model',
                'modgdg': 'racf:modgdg',
                'modgroup': 'racf:modgroup',
                'moduser': 'racf:moduser',
                'operaudt': 'racf:operaudt',
                'phrint': 'racf:phrint',
                'prefix': 'racf:prefix',
                'primlang': 'racf:primlang',
                'protall': 'racf:protall',
                'pwdalg': 'racf:pwdalg',
                'pwdspec': 'racf:pwdspec',
                'raclist': 'racf:raclist',
                'noraclist': "racf:raclist",
                'realdsn': 'racf:realdsn',
                'refresh': 'racf:refresh',
                'retpd': 'racf:retpd',
                'revoke': 'racf:revoke',
                'rules': 'racf:rules',
                'rule1': 'racf:rule1',
                'rule2': 'racf:rule2',
                'rule3': 'racf:rule3',
                'rule4': 'racf:rule4',
                'rule5': 'racf:rule5',
                'rule6': 'racf:rule6',
                'rule7': 'racf:rule7',
                'rule8': 'racf:rule8',
                'rvarswpw': 'racf:rvarswpw',
                'rvarstpw': 'racf:rvarstpw',
                'saudit': 'racf:saudit',
                'seclabct': 'racf:seclabct',
                'seclang': 'racf:seclang',
                'sessint': 'racf:sessint',
                'slabaudt': 'racf:slabaudt',
                'slbysys': 'racf:slbysys',
                'slevaudt': 'racf:slevaudt',
                'tapedsn': 'racf:tapedsn',
                'terminal': 'racf:terminal',
                'warning': 'racf:warning',
                'whenprog': 'racf:whenprog'
            }
        }

        self.segment_traits = {}
        self.trait_map = {}

    def get_password_rules(self) -> str:
        result = self.list()
        profile = result['securityresult']['systemsettings']['commands'][0]['profile']
        return profile['password processing options'].get('rules')
    
    def refresh(self, class_name: str) -> str:
        return self.command({"raclist": class_name, 'refresh': True})
    
    def get_class_types(self, class_name: str) -> list:
        result = self.list()
        profile = result['securityresult']['systemsettings']['commands'][0]['profile']
        class_info = []
        for key in profile.keys():
            if ' classes' in key and profile[key] is not None:
                if class_name.lower().strip() in profile[key]:
                    class_info.append(key.replace(' classes','').strip())
            if ' raclist only' in key and profile[key] is not None:
                if class_name.lower().strip() in profile[key]:
                    class_info.append(key.replace(' raclist only','').strip())
        return class_info
    
    def audit_add(self, class_name: str) -> dict:
        traits = {'audit': class_name}
        return self.command(traits)
    
    def audit_del(self, class_name: str) -> dict:
        traits = {'noaudit': class_name}
        return self.command(traits)
    
    def classact_add(self, class_name: str) -> dict:
        traits = {'classact': class_name}
        return self.command(traits)
    
    def classact_del(self, class_name: str) -> dict:
        traits = {'noclassact': class_name}
        return self.command(traits)

    def classstat_add(self, class_name: str) -> dict:
        traits = {'classstat': class_name}
        return self.command(traits)
    
    def classstat_del(self, class_name: str) -> dict:
        traits = {'noclassstat': class_name}
        return self.command(traits)
    
    def gencmd_add(self, class_name: str) -> dict:
        traits = {'gencmd': class_name}
        return self.command(traits)
    
    def gencmd_del(self, class_name: str) -> dict:
        traits = {'nogencmd': class_name}
        return self.command(traits)

    def generic_add(self, class_name: str) -> dict:
        traits = {'generic': class_name}
        return self.command(traits)
    
    def generic_del(self, class_name: str) -> dict:
        traits = {'nogeneric': class_name}
        return self.command(traits)
    
    def genlist_add(self, class_name: str) -> dict:
        traits = {'genlist': class_name}
        return self.command(traits)
    
    def genlist_del(self, class_name: str) -> dict:
        traits = {'nogenlist': class_name}
        return self.command(traits)

    def global_add(self, class_name: str) -> dict:
        traits = {'global': class_name}
        return self.command(traits)
    
    def global_del(self, class_name: str) -> dict:
        traits = {'noglobal': class_name}
        return self.command(traits)
    
    def raclist_add(self, class_name: str) -> dict:
        traits = {'raclist': class_name}
        return self.command(traits)
    
    def raclist_del(self, class_name: str) -> dict:
        traits = {'noraclist': class_name}
        return self.command(traits)


    def list(self) -> dict:
        self.build_segment_dictionary({'list': True})
        setropts_request = SetroptsRequest()
        self.build_segment(setropts_request)
        result = self.make_request(setropts_request)
        if "error" in result["securityresult"]["systemsettings"]:
            raise SecurityRequestError(result)
        if (result["securityresult"]["returncode"] == 0 
                and result["securityresult"]["reasoncode"] == 0):
            self.__format_profile(result)
            return result
        raise SecurityRequestError(result)

    def command(self, traits: dict) -> dict:
        self.build_segment_dictionary(traits)
        setropts_request = SetroptsRequest()
        self.build_segment(setropts_request)
        return self.make_request(setropts_request)

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
        self.segment_traits[trait] = value
        self.trait_map[trait] =  self.valid_segment_traits[segment][trait]
        return 0

    def build_segment_dictionary(self, traits: dict) -> None:
        for trait in traits:
            if ':' in trait:
                segment = trait.split(':')[0]
                true_trait = trait.split(':')[1]
                self.evaluate_trait(true_trait,segment,traits[trait])
                continue
            for segment in self.valid_segment_traits.keys():
                self.evaluate_trait(trait,segment,traits[trait])

    def build_segment(self, profile_request: SetroptsRequest, alter=False) -> None:
        profile_request.build_segment(False, self.segment_traits, self.trait_map, alter=alter)
        # Clear segments for new request
        self.segment_traits = {}

    def make_request(self, profile_request: SetroptsRequest, opts: int = 1) -> dict:
        result_xml = self.irrsmo00.call_racf(profile_request.dump_request_xml(),opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()

    def __format_profile(self, result: dict) -> None:
        messages = result["securityresult"]["systemsettings"]["commands"][0]["messages"]
        profile = {}
        current_segment = None
        i = 0
        while i < len(messages):
            if messages[i] == " ":
                i += 1
                continue
            
            if ' = ' in messages[i]:
                field = messages[i].split(' = ')[0].strip().lower()
                if current_segment:
                    profile[current_segment][field] = clean_and_separate(messages[i].split(' = ')[1])
                else:
                    profile[field] = clean_and_separate(messages[i].split(' = ')[1])
                i += 1
                continue

            if '  ' in messages[i]:
                if "classes" in field:
                    new_val = clean_and_separate(messages[i].replace('  ',''))
                    if isinstance(new_val,str):
                        profile[field].append(new_val)
                    else:
                        profile[field].extend(new_val)
                    i += 1
                    continue
                elif "rules" in field and current_segment == "password processing options" and "LEGEND:" not in messages[i]:
                    length_chars = messages[i].lower().split('length(')[1].split(')')[0]
                    if ':' in length_chars:
                        minlength = cast_value(length_chars.split(':')[0])
                        maxlength = cast_value(length_chars.split(':')[1])
                    else:
                        minlength = cast_value(length_chars)
                        maxlength = cast_value(length_chars)
                    chars = messages[i][-maxlength:]
                    profile[current_segment][field].append({'minlength': minlength, 'maxlength': maxlength, 'content': chars})
                    i += 1
                    continue
            
            if ' : ' in messages[i]:
                field = messages[i].split(' : ')[0].strip().lower().replace("user-id for jes ","").replace(" is","")
                if current_segment:
                    profile[current_segment][field] = clean_and_separate(messages[i].split(' : ')[1].replace(" / ","/"))
                else:
                    profile[field] = clean_and_separate(messages[i].split(' : ')[1].replace(" / ","/"))
                i += 1
                continue


            if 'IS ' in messages[i]:
                field = messages[i].split('IS ')[0].strip().lower().replace(' option','').replace(' in effect','').replace("the active ","")
                if "CURRENT OPTIONS:" in messages[i] and i < len(messages) - 1:
                    profile[field] = cast_value(messages[i+1].split('"')[1:2][0].strip().lower())
                    i += 2
                    continue
                else:
                    if current_segment:
                        profile[current_segment][field] = cast_value(messages[i].split('IS ')[1].strip().lower())
                    else:
                        profile[field] = cast_value(messages[i].split('IS ')[1].strip().lower())
                    i += 1
                    continue
            
            if 'ARE ' in messages[i]:
                field = messages[i].split('ARE ')[0].strip().lower()
                if current_segment:
                    profile[current_segment][field] = cast_value(messages[i].split('ARE ')[1].strip().lower())
                else:
                    profile[field] = cast_value(messages[i].split('ARE ')[1].strip().lower())
                i += 1
                continue

            if " BEING MAINTAINED." in messages[i]:
                cln_msg = messages[i].strip().lower().replace(" being maintained.","")
                field = "history"
                if "no password history" in cln_msg:
                    profile[current_segment][field] = 0
                else:
                    profile[current_segment][field] = cast_value(cln_msg.split(' ')[0])
                i += 1
                continue
            
            if ", A USERID WILL BE REVOKED." in messages[i]:
                field = "revoke"
                profile[current_segment][field] = cast_value(messages[i].split("AFTER ")[1].split(" CONSECUTIVE")[0].strip())
                i += 1
                continue
            elif "USERIDS NOT BEING AUTOMATICALLY REVOKED." in messages[i]:
                field = "revoke"
                profile[current_segment][field] = 0
                i += 1
                continue

            if "PASSWORD PROCESSING OPTIONS:" in messages[i]:
                current_segment = "password processing options"
                profile[current_segment] = {}
                i += 1
                continue
            elif "INSTALLATION PASSWORD SYNTAX RULES:" in messages[i]:
                field = "rules"
                profile[current_segment][field] = []
                i += 1
                continue
            elif "LEGEND:" in messages[i]:
                current_segment = None
                field = ""
                i += 1
                continue

            i += 1

        # Post processing
        tmp = profile['partner lu-verification sessionkey interval maximum/default']
        profile['sessionkey interval'] = tmp
        del profile['partner lu-verification sessionkey interval maximum/default']
        if not profile['password processing options']['rules']:

            profile['password processing options']['rules'] = []
        else:
            for i in range(len(profile['password processing options']['rules'])):
                content = profile['password processing options']['rules'][i]['content']
                profile['password processing options']['rules'][i]['legend'] = content_keyword_map(content)
        
        del result["securityresult"]["systemsettings"]["commands"][0]["messages"]
        result["securityresult"]["systemsettings"]["commands"][0]["profile"] = profile

def cast_value(value: str) -> Union[None,int,float,str]:
    if value == "n/a" or value == "none" or value == "none specified" or value == 'no':
        return None
    if value == "in effect" or value == "active" or value == "being done." or value == "in effect." or value == "allowed.":
        return True
    if value == "not in effect" or value == "inavtive" or value == "not allowed.":
        return False
    if " days" in value:
        return cast_value(value.replace(" days","").strip())
    if "." in value:
        try:
            return float(value)
        except ValueError:
            return value
    try:
        return int(value.replace(",", ""))
    except ValueError:
        return value 

def clean_and_separate(value: str) -> Union[list,str]:
    cln_val = value.strip().lower()
    if ',' in cln_val:
        out = [cast_value(val.strip()) for val in cln_val.split(',') ]
    elif ' ' in cln_val:
        out = [cast_value(val.strip()) for val in cln_val.split(' ') ]
    else:
        out = cast_value(cln_val)
    return out

def content_keyword_map(content: str) -> dict:
    map_dict = {
        "A" : "ALPHA", "C" : "CONSONANT", "L" : "ALPHANUM", "N" : "NUMERIC",
        "V" : "VOWEL", "W" : "NOVOWEL", "*" : "ANYTHING", "c" : "MIXED CONSONANT",
        "m" : "MIXED NUMERIC", "v" : "MIXED VOWEL", "$" : "NATIONAL", "s" : "SPECIAL",
        "x" : "MIXED ALL"
    }
    out = {}
    for char in content:
        if char not in out.keys():
            out[char] = map_dict[char]
    return out