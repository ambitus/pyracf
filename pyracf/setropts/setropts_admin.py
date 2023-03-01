"""Set RACF Options Administration."""

from typing import List, Tuple

from pyracf.common.security_admin import SecurityAdmin
from pyracf.setropts.setropts_requset import SetroptsRequest


class SetroptsAdmin(SecurityAdmin):
    """Set RACF Options Administration."""

    def __init__(self) -> None:
        super().__init__()
        self.valid_segment_traits = {
            "base": {
                "addcreat": "racf:addcreat",
                "adsp": "racf:adsp",
                "applaudt": "racf:applaudt",
                "audit": "racf:audit",
                "catdsns": "racf:catdsns",
                "classact": "racf:classact",
                "classtat": "racf:classtat",
                "cmdviol": "racf:cmdviol",
                "compmode": "racf:compmode",
                "egn": "racf:egn",
                "erase": "racf:erase",
                "eraseall": "racf:eraseall",
                "erasesec": "racf:erasesec",
                "gencmd": "racf:gencmd",
                "generic": "racf:generic",
                "genlist": "racf:genlist",
                "genowner": "racf:genowner",
                "global": "racf:global",
                "grplist": "racf:grplist",
                "history": "racf:history",
                "inactive": "racf:inactive",
                "initstat": "racf:initstat",
                "interval": "racf:interval",
                "jesbatch": "racf:jesbatch",
                "jesearly": "racf:jesearly",
                "jesnje": "racf:jesnje",
                "jesundef": "racf:jesundef",
                "jesxbm": "racf:jesxbm",
                "kerblvl": "racf:kerblvl",
                "list": "racf:list",
                "logalwys": "racf:logalwys",
                "logdeflt": "racf:logdeflt",
                "logfail": "racf:logfail",
                "lognever": "racf:lognever",
                "logsucc": "racf:logsucc",
                "minchang": "racf:minchang",
                "mixdcase": "racf:mixdcase",
                "mlactive": "racf:mlactive",
                "mlfs": "racf:mlfs",
                "mlipc": "racf:mlipc",
                "mlnames": "racf:mlnames",
                "mlquiet": "racf:mlquiet",
                "mls": "racf:mls",
                "mlstable": "racf:mlstable",
                "model": "racf:model",
                "modgdg": "racf:modgdg",
                "modgroup": "racf:modgroup",
                "moduser": "racf:moduser",
                "operaudt": "racf:operaudt",
                "phrint": "racf:phrint",
                "prefix": "racf:prefix",
                "primlang": "racf:primlang",
                "protall": "racf:protall",
                "pwdalg": "racf:pwdalg",
                "pwdspec": "racf:pwdspec",
                "raclist": "racf:raclist",
                "noraclist": "racf:raclist",
                "realdsn": "racf:realdsn",
                "refresh": "racf:refresh",
                "retpd": "racf:retpd",
                "revoke": "racf:revoke",
                "rules": "racf:rules",
                "rule1": "racf:rule1",
                "rule2": "racf:rule2",
                "rule3": "racf:rule3",
                "rule4": "racf:rule4",
                "rule5": "racf:rule5",
                "rule6": "racf:rule6",
                "rule7": "racf:rule7",
                "rule8": "racf:rule8",
                "rvarswpw": "racf:rvarswpw",
                "rvarstpw": "racf:rvarstpw",
                "saudit": "racf:saudit",
                "seclabct": "racf:seclabct",
                "seclang": "racf:seclang",
                "sessint": "racf:sessint",
                "slabaudt": "racf:slabaudt",
                "slbysys": "racf:slbysys",
                "slevaudt": "racf:slevaudt",
                "tapedsn": "racf:tapedsn",
                "terminal": "racf:terminal",
                "warning": "racf:warning",
                "whenprog": "racf:whenprog",
            }
        }
        self.profile_type = "systemsettings"

    def get_password_rules(self) -> str:
        """Get RACF password rules."""
        result = self.list_ropts()
        profile = result["securityresult"]["systemsettings"]["commands"][0]["profile"]
        return profile["password processing options"].get("rules")

    def refresh(self, class_name: str) -> str:
        """Refresh raclist."""
        return self.command({"raclist": class_name, "refresh": True})

    def get_class_types(self, class_name: str) -> list:
        """Get RACF class types."""
        result = self.list_ropts()
        profile = result["securityresult"]["systemsettings"]["commands"][0]["profile"]
        class_info = []
        for key in profile.keys():
            if " classes" in key and profile[key] is not None:
                if class_name.lower().strip() in profile[key]:
                    class_info.append(key.replace(" classes", "").strip())
            if " raclist only" in key and profile[key] is not None:
                if class_name.lower().strip() in profile[key]:
                    class_info.append(key.replace(" raclist only", "").strip())
        return class_info

    def audit_add(self, class_name: str) -> dict:
        """Add a class to the "Audit" list."""
        traits = {"audit": class_name}
        return self.command(traits)

    def audit_del(self, class_name: str) -> dict:
        """Delete a class from the "Audit" list."""
        traits = {"noaudit": class_name}
        return self.command(traits)

    def classact_add(self, class_name: str) -> dict:
        """Add a class to the "Active" list."""
        traits = {"classact": class_name}
        return self.command(traits)

    def classact_del(self, class_name: str) -> dict:
        """Remove a class from the "Active" list."""
        traits = {"noclassact": class_name}
        return self.command(traits)

    def classstat_add(self, class_name: str) -> dict:
        """Add a class to the "Statistics" list."""
        traits = {"classstat": class_name}
        return self.command(traits)

    def classstat_del(self, class_name: str) -> dict:
        """Remove a class from the "Statistics" list."""
        traits = {"noclassstat": class_name}
        return self.command(traits)

    def gencmd_add(self, class_name: str) -> dict:
        """Add a class to the "Generic Command Classes" list."""
        traits = {"gencmd": class_name}
        return self.command(traits)

    def gencmd_del(self, class_name: str) -> dict:
        """Remove a class from the "Generic Command Classes" list."""
        traits = {"nogencmd": class_name}
        return self.command(traits)

    def generic_add(self, class_name: str) -> dict:
        """Add a class to the "Generic Profile Classes" list."""
        traits = {"generic": class_name}
        return self.command(traits)

    def generic_del(self, class_name: str) -> dict:
        """Remove a class from the "Generic Profile Classes" list."""
        traits = {"nogeneric": class_name}
        return self.command(traits)

    def genlist_add(self, class_name: str) -> dict:
        """Add a class to the "GenList" list."""
        traits = {"genlist": class_name}
        return self.command(traits)

    def genlist_del(self, class_name: str) -> dict:
        """Remove a class from the "GenList" list."""
        traits = {"nogenlist": class_name}
        return self.command(traits)

    def global_add(self, class_name: str) -> dict:
        """Add a class to the "Global Access Checking" list."""
        traits = {"global": class_name}
        return self.command(traits)

    def global_del(self, class_name: str) -> dict:
        """Remove a class from the "Global Access Checking" list."""
        traits = {"noglobal": class_name}
        return self.command(traits)

    def raclist_add(self, class_name: str) -> dict:
        """Add a class to the "SETR Raclist" list."""
        traits = {"raclist": class_name}
        return self.command(traits)

    def raclist_del(self, class_name: str) -> dict:
        """Remove a class from the "SETR Raclist" list."""
        traits = {"noraclist": class_name}
        return self.command(traits)

    def list_ropts(self) -> dict:
        """List RACF options."""
        self.build_segment_dictionary({"list": True})
        setropts_request = SetroptsRequest()
        self.build_segment(setropts_request)
        return self.extract_and_check_result(setropts_request)

    def command(self, traits: dict) -> dict:
        """Run a set RACF options command."""
        self.build_segment_dictionary(traits)
        setropts_request = SetroptsRequest()
        self.build_segment(setropts_request)
        return self.make_request(setropts_request)

    def build_segment_dictionary(self, traits: dict) -> None:
        """Build segemnt dictionary for only base segment."""
        for trait in traits:
            if ':' in trait:
                segment = trait.split(':')[0]
                true_trait = trait.split(':')[1]
                self.__validate_trait(true_trait,segment,traits[trait])
                continue
            self.__validate_trait(trait,'base',traits[trait])
        
        self.segment_traits = self.segment_traits['base']

    def build_segment(self, profile_request: SetroptsRequest, alter=False) -> None:
        """Build XML representation of segment."""
        profile_request.build_segment(
            False, self.segment_traits, self.trait_map, alter=alter
        )
        # Clear segments for new request
        self.segment_traits = {}

    def format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityresult"]["systemsettings"]["commands"][0]["messages"]
        profile = {}
        current_segment = None
        i = 0
        while i < len(messages):
            if messages[i] == " ":
                i += 1
                continue
            if " = " in messages[i]:
                field = self.__add_key_value_pair_to_profile(
                    messages[i],
                    profile,
                    current_segment,
                )
                i += 1
                continue
            if "  " in messages[i]:
                result = self.__add_classes_and_rules_to_profile(
                    messages[i],
                    profile,
                    current_segment,
                    field,
                )
                if result == 1:
                    i += 1
                    continue
            if " : " in messages[i]:
                field = self.__add_colon_field_to_profile(
                    messages[i],
                    profile,
                    current_segment,
                )
                i += 1
                continue
            if "IS " in messages[i]:
                (i, field) = self.__add_is_field_to_profile(
                    messages, profile, current_segment, i
                )
                continue
            other_keys = (
                "ARE ",
                "BEING MAINTAINED.",
                ", A USERID WILL BE REVOKED.",
                ", A USERID WILL BE REVOKED.",
                "USERIDS NOT BEING AUTOMATICALLY REVOKED.",
                "PASSWORD PROCESSING OPTIONS:",
                "INSTALLATION PASSWORD SYNTAX RULES:",
                "LEGEND:",
            )
            for key in other_keys:
                if key in messages[i]:
                    (current_segment, field) = self.__add_other_keys_to_profile(
                        messages[i],
                        profile,
                        current_segment,
                    )
            i += 1

        # Post processing
        tmp = profile["partner lu-verification sessionkey interval maximum/default"]
        profile["sessionkey interval"] = tmp
        del profile["partner lu-verification sessionkey interval maximum/default"]
        if not profile["password processing options"]["rules"]:
            profile["password processing options"]["rules"] = []
        else:
            for i in range(len(profile["password processing options"]["rules"])):
                content = profile["password processing options"]["rules"][i]["content"]
                profile["password processing options"]["rules"][i][
                    "legend"
                ] = self.__content_keyword_map(content)

        del result["securityresult"]["systemsettings"]["commands"][0]["messages"]
        result["securityresult"]["systemsettings"]["commands"][0]["profile"] = profile

    def __add_other_keys_to_profile(
        self,
        message: str,
        profile: dict,
        current_segment: str,
    ) -> Tuple[str, str]:
        """Add other keys to profile."""
        if "ARE " in message:
            field = self.__add_are_field_to_profile(message, profile, current_segment)
        elif " BEING MAINTAINED." in message:
            field = self.__add_being_maintained_field_to_profile(
                message, profile, current_segment
            )
        elif ", A USERID WILL BE REVOKED." in message:
            field = "revoke"
            profile[current_segment][field] = self.__cast_value(
                message.split("AFTER ")[1].split(" CONSECUTIVE")[0].strip()
            )
        elif "USERIDS NOT BEING AUTOMATICALLY REVOKED." in message:
            field = "revoke"
            profile[current_segment][field] = 0
        elif "PASSWORD PROCESSING OPTIONS:" in message:
            current_segment = "password processing options"
            profile[current_segment] = {}
        elif "INSTALLATION PASSWORD SYNTAX RULES:" in message:
            field = "rules"
            profile[current_segment][field] = []
        elif "LEGEND:" in message:
            current_segment = None
            field = ""
        return (current_segment, field)

    def __add_key_value_pair_to_profile(
        self,
        message: str,
        profile: dict,
        current_segment: str,
    ) -> str:
        """Add key-value pair values to profile."""
        field = message.split(" = ")[0].strip().lower()
        if current_segment:
            profile[current_segment][field] = self.__clean_and_separate(
                message.split(" = ")[1]
            )
        else:
            profile[field] = self.__clean_and_separate(message.split(" = ")[1])
        return field

    def __add_classes_and_rules_to_profile(
        self, message: str, profile: dict, current_segment: str, field: str
    ) -> int:
        """Add classes and rules to profile."""
        if "classes" in field:
            new_val = self.__clean_and_separate(message.replace("  ", ""))
            if isinstance(new_val, str):
                profile[field].append(new_val)
            else:
                profile[field].extend(new_val)
            return 1
        if (
            "rules" in field
            and current_segment == "password processing options"
            and "LEGEND:" not in message
        ):
            length_chars = message.lower().split("length(")[1].split(")")[0]
            if ":" in length_chars:
                minlength = self.__cast_value(length_chars.split(":")[0])
                maxlength = self.__cast_value(length_chars.split(":")[1])
            else:
                minlength = self.__cast_value(length_chars)
                maxlength = self.__cast_value(length_chars)
            chars = message[-1 * maxlength :]
            profile[current_segment][field].append(
                {
                    "minlength": minlength,
                    "maxlength": maxlength,
                    "content": chars,
                }
            )
            return 1
        return 0

    def __add_colon_field_to_profile(
        self,
        message: str,
        profile: dict,
        current_segment: str,
    ) -> str:
        """Add colon field to profile."""
        field = (
            message.split(" : ")[0]
            .strip()
            .lower()
            .replace("user-id for jes ", "")
            .replace(" is", "")
        )
        if current_segment:
            profile[current_segment][field] = self.__clean_and_separate(
                message.split(" : ")[1].replace(" / ", "/")
            )
        else:
            profile[field] = self.__clean_and_separate(
                message.split(" : ")[1].replace(" / ", "/")
            )
        return field

    def __add_is_field_to_profile(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> Tuple[int, str]:
        """Add is field to profile"""
        field = (
            messages[i]
            .split("IS ")[0]
            .strip()
            .lower()
            .replace(" option", "")
            .replace(" in effect", "")
            .replace("the active ", "")
        )
        if "CURRENT OPTIONS:" in messages[i] and i < len(messages) - 1:
            profile[field] = self.__cast_value(
                messages[i + 1].split('"')[1:2][0].strip().lower()
            )
            i += 2
            return (i, field)
        if current_segment:
            profile[current_segment][field] = self.__cast_value(
                messages[i].split("IS ")[1].strip().lower()
            )
        else:
            profile[field] = self.__cast_value(
                messages[i].split("IS ")[1].strip().lower()
            )
        i += 1
        return (i, field)

    def __add_are_field_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> str:
        """Add are field to profile"""
        field = message.split("ARE ")[0].strip().lower()
        if current_segment:
            profile[current_segment][field] = self.__cast_value(
                message.split("ARE ")[1].strip().lower()
            )
        else:
            profile[field] = self.__cast_value(message.split("ARE ")[1].strip().lower())
        return field

    def __add_being_maintained_field_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> str:
        """Add being maintained field to profile."""
        cln_msg = message.strip().lower().replace(" being maintained.", "")
        field = "history"
        if "no password history" in cln_msg:
            profile[current_segment][field] = 0
        else:
            profile[current_segment][field] = self.__cast_value(cln_msg.split(" ")[0])
        return field

    def __content_keyword_map(self, content: str) -> dict:
        """Map content letter to kepword."""
        map_dict = {
            "A": "ALPHA",
            "C": "CONSONANT",
            "L": "ALPHANUM",
            "N": "NUMERIC",
            "V": "VOWEL",
            "W": "NOVOWEL",
            "*": "ANYTHING",
            "c": "MIXED CONSONANT",
            "m": "MIXED NUMERIC",
            "v": "MIXED VOWEL",
            "$": "NATIONAL",
            "s": "SPECIAL",
            "x": "MIXED ALL",
        }
        out = {}
        for char in content:
            if char not in out:
                out[char] = map_dict[char]
        return out
