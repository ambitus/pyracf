"""Set RACF Options Administration."""

from typing import List, Tuple

from pyracf.common.security_admin import SecurityAdmin

from .setropts_requset import SetroptsRequest


class SetroptsAdmin(SecurityAdmin):
    """Set RACF Options Administration."""

    def __init__(
        self, debug: bool = False, generate_requests_only: bool = False
    ) -> None:
        super().__init__(
            "systemsettings", debug=debug, generate_requests_only=generate_requests_only
        )
        self._valid_segment_traits = {
            "base": {
                "base:addcreat": "racf:addcreat",
                "base:adsp": "racf:adsp",
                "base:applaudt": "racf:applaudt",
                "base:audit": "racf:audit",
                "base:catdsns": "racf:catdsns",
                "base:classact": "racf:classact",
                "base:classtat": "racf:classtat",
                "base:cmdviol": "racf:cmdviol",
                "base:compmode": "racf:compmode",
                "base:egn": "racf:egn",
                "base:erase": "racf:erase",
                "base:eraseall": "racf:eraseall",
                "base:erasesec": "racf:erasesec",
                "base:gencmd": "racf:gencmd",
                "base:generic": "racf:generic",
                "base:genlist": "racf:genlist",
                "base:genowner": "racf:genowner",
                "base:global": "racf:global",
                "base:grplist": "racf:grplist",
                "base:history": "racf:history",
                "base:inactive": "racf:inactive",
                "base:initstat": "racf:initstat",
                "base:interval": "racf:interval",
                "base:jesbatch": "racf:jesbatch",
                "base:jesearly": "racf:jesearly",
                "base:jesnje": "racf:jesnje",
                "base:jesundef": "racf:jesundef",
                "base:jesxbm": "racf:jesxbm",
                "base:kerblvl": "racf:kerblvl",
                "base:list": "racf:list",
                "base:logalwys": "racf:logalwys",
                "base:logdeflt": "racf:logdeflt",
                "base:logfail": "racf:logfail",
                "base:lognever": "racf:lognever",
                "base:logsucc": "racf:logsucc",
                "base:minchang": "racf:minchang",
                "base:mixdcase": "racf:mixdcase",
                "base:mlactive": "racf:mlactive",
                "base:mlfs": "racf:mlfs",
                "base:mlipc": "racf:mlipc",
                "base:mlnames": "racf:mlnames",
                "base:mlquiet": "racf:mlquiet",
                "base:mls": "racf:mls",
                "base:mlstable": "racf:mlstable",
                "base:model": "racf:model",
                "base:modgdg": "racf:modgdg",
                "base:modgroup": "racf:modgroup",
                "base:moduser": "racf:moduser",
                "base:operaudt": "racf:operaudt",
                "base:phrint": "racf:phrint",
                "base:prefix": "racf:prefix",
                "base:primlang": "racf:primlang",
                "base:protall": "racf:protall",
                "base:pwdalg": "racf:pwdalg",
                "base:pwdspec": "racf:pwdspec",
                "base:raclist": "racf:raclist",
                "base:realdsn": "racf:realdsn",
                "base:refresh": "racf:refresh",
                "base:retpd": "racf:retpd",
                "base:revoke": "racf:revoke",
                "base:rules": "racf:rules",
                "base:rule1": "racf:rule1",
                "base:rule2": "racf:rule2",
                "base:rule3": "racf:rule3",
                "base:rule4": "racf:rule4",
                "base:rule5": "racf:rule5",
                "base:rule6": "racf:rule6",
                "base:rule7": "racf:rule7",
                "base:rule8": "racf:rule8",
                "base:rvarswpw": "racf:rvarswpw",
                "base:rvarstpw": "racf:rvarstpw",
                "base:saudit": "racf:saudit",
                "base:seclabct": "racf:seclabct",
                "base:seclang": "racf:seclang",
                "base:sessint": "racf:sessint",
                "base:slabaudt": "racf:slabaudt",
                "base:slbysys": "racf:slbysys",
                "base:slevaudt": "racf:slevaudt",
                "base:tapedsn": "racf:tapedsn",
                "base:terminal": "racf:terminal",
                "base:warning": "racf:warning",
                "base:whenprog": "racf:whenprog",
            }
        }

    def get_password_rules(self) -> str:
        """Get RACF password rules."""
        result = self.list_racf_options()
        profile = result["securityresult"]["systemsettings"]["commands"][0]["profile"]
        return profile["password processing options"].get("rules")

    def refresh_raclist(self, class_name: str) -> str:
        """Refresh raclist."""
        return self.alter(options={"base:raclist": class_name, "base:refresh": True})

    def get_class_types(self, class_name: str) -> list:
        """Get RACF class types."""
        result = self.list_racf_options()
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

    def add_audit_class(self, class_name: str) -> dict:
        """Add a class to list of classes that RACF performs auditing for."""
        return self.alter(options={"base:audit": class_name})

    def remove_audit_class(self, class_name: str) -> dict:
        """Remove a class from the list of classes that RACF performs auditing for."""
        return self.alter(options={"delete:base:audit": class_name})

    def add_active_class(self, class_name: str) -> dict:
        """
        Add a class to the list of classes that RACF performs access authorization checking for.
        """
        return self.alter(options={"base:classact": class_name})

    def remove_active_class(self, class_name: str) -> dict:
        """
        Remove a class from the list of classes that
        RACF performs access authorization checking for.
        """
        return self.alter(options={"delete:base:classact": class_name})

    def add_statistics_class(self, class_name: str) -> dict:
        """Add a class to the list of classes that RACF collects statistics for."""
        return self.alter(options={"base:classtat": class_name})

    def remove_statistics_class(self, class_name: str) -> dict:
        """Remove a class from the list of classes that RACF collects statistics for."""
        return self.alter(options={"delete:base:classtat": class_name})

    def add_generic_command_processing_class(self, class_name: str) -> dict:
        """
        Add a class to the list of classes that have
        generic profile command processing enabled.
        """
        return self.alter(options={"base:gencmd": class_name})

    def remove_generic_command_processing_class(self, class_name: str) -> dict:
        """
        Remove a class from the list of classes that
        have generic profile command processing enabled.
        """
        return self.alter(options={"delete:base:gencmd": class_name})

    def add_generic_profile_checking_class(self, class_name: str) -> dict:
        """Add a class to the list of classes that have generic profile checking enabled."""
        return self.alter(options={"base:generic": class_name})

    def remove_generic_profile_checking_class(self, class_name: str) -> dict:
        """Remove a class from the list of classes that have generic profile checking enabled."""
        return self.alter(options={"delete:base:generic": class_name})

    def add_generic_profile_sharing_class(self, class_name: str) -> dict:
        """
        Add a class to the list of classes that are eligible for
        general resource profile sharing in common storage.
        """
        return self.alter(options={"base:genlist": class_name})

    def remove_generic_profile_sharing_class(self, class_name: str) -> dict:
        """
        Remove a class from the list of classes that are eligible
        for general resource profile sharing in common storage.
        """
        return self.alter(options={"delete:base:genlist": class_name})

    def add_global_access_class(self, class_name: str) -> dict:
        """Add a class to the list of classes eligible for global access checking."""
        return self.alter(options={"base:global": class_name})

    def remove_global_access_class(self, class_name: str) -> dict:
        """Remove a class from the list of classes eligible for global access checking."""
        return self.alter(options={"delete:base:global": class_name})

    def add_raclist_class(self, class_name: str) -> dict:
        """Add a class to list of classes that have in-storage profile sharing activated."""
        options = {"base:raclist": class_name}
        return self.alter(options=options)

    def remove_raclist_class(self, class_name: str) -> dict:
        """
        Remove a class from the list of classes that have in-storage profile sharing activated.
        """
        options = {"delete:base:raclist": class_name}
        return self.alter(options=options)

    # ============================================================================
    # Core Functions
    # ============================================================================
    def list_racf_options(self) -> dict:
        """List RACF options."""
        self.__build_segment_dictionary({"base:list": True})
        setropts_request = SetroptsRequest()
        self.__build_segment(setropts_request)
        return self._extract_and_check_result(
            setropts_request,
        )

    def alter(self, options: dict = {}) -> dict:
        """Update RACF options."""
        self.__build_segment_dictionary(options)
        setropts_request = SetroptsRequest()
        self.__build_segment(setropts_request)
        return self.make_request(setropts_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def __build_segment_dictionary(self, traits: dict) -> None:
        """Build segemnt dictionary for only base segment."""
        self._build_segment_dictionaries(traits)
        self._segment_traits = self._segment_traits["base"]

    def __build_segment(self, profile_request: SetroptsRequest, alter=False) -> None:
        """Build XML representation of segment."""
        profile_request.build_segment(
            False, self._segment_traits, self._trait_map, alter=alter
        )
        # Clear segments for new request
        self._segment_traits = {}

    def _format_profile(self, result: dict) -> None:
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
            if " " in messages[i]:
                retcode = self.__add_classes_and_rules_to_profile(
                    messages[i],
                    profile,
                    current_segment,
                    field,
                )
                if retcode == 1:
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
                " NOT BEING DONE",
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
        elif " NOT BEING DONE" in message:
            field = self.__add_being_done_field_to_profile(
                message, profile, current_segment
            )
        elif ", A USERID WILL BE REVOKED." in message:
            field = "revoke"
            profile[current_segment][field] = self._cast_from_str(
                message.split("AFTER ")[1].split(" CONSECUTIVE")[0].strip()
            )
        elif "USERIDS NOT BEING AUTOMATICALLY REVOKED." in message:
            field = "revoke"
            profile[current_segment][field] = 0
        elif "PASSWORD PROCESSING OPTIONS:" in message:
            current_segment = "password processing options"
            profile[current_segment] = {}
            field = ""
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
            profile[current_segment][field] = self._clean_and_separate(
                message.split(" = ")[1]
            )
        else:
            profile[field] = self._clean_and_separate(message.split(" = ")[1])
        return field

    def __add_classes_and_rules_to_profile(
        self, message: str, profile: dict, current_segment: str, field: str
    ) -> int:
        """Add classes and rules to profile."""
        if "classes" in field:
            new_val = self._clean_and_separate(message.replace("  ", ""))
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
                minlength = self._cast_from_str(length_chars.split(":")[0])
                maxlength = self._cast_from_str(length_chars.split(":")[1])
            else:
                minlength = self._cast_from_str(length_chars)
                maxlength = self._cast_from_str(length_chars)
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
            profile[current_segment][field] = self._clean_and_separate(
                message.split(" : ")[1].replace(" / ", "/")
            )
        else:
            profile[field] = self._clean_and_separate(
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

        messages[i] = messages[i].replace(" FOR GDGS.", "")

        if "CURRENT OPTIONS:" in messages[i] and i < len(messages) - 1:
            profile[field] = self._cast_from_str(
                messages[i + 1].split('"')[1:2][0].strip().lower()
            )
            i += 2
            return (i, field)
        if current_segment:
            profile[current_segment][field] = self._cast_from_str(
                messages[i].split("IS ")[1].strip().lower()
            )
        else:
            if field not in profile:
                profile[field] = self._cast_from_str(
                    messages[i].split("IS ")[1].strip().lower()
                )
            else:
                profile[field] = [profile[field]]
                profile[field].append(
                    self._cast_from_str(messages[i].split("IS ")[1].strip().lower())
                )
        i += 1
        return (i, field)

    def __add_are_field_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> str:
        """Add are field to profile"""
        field = message.split("ARE ")[0].strip().lower()
        if current_segment:
            profile[current_segment][field] = self._cast_from_str(
                message.split("ARE ")[1].strip().lower()
            )
        else:
            profile[field] = self._cast_from_str(
                message.split("ARE ")[1].strip().lower()
            )
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
            profile[current_segment][field] = self._cast_from_str(cln_msg.split(" ")[0])
        return field

    def __add_being_done_field_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> str:
        """Add being done field to profile."""
        cln_msg = message.strip().lower().replace(" for gdgs.")
        field = cln_msg.replace(" not being done", "")
        profile[current_segment][field] = self._cast_from_str(cln_msg[len(field) :])
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
