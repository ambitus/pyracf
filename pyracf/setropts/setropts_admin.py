"""Set RACF Options Administration."""

from typing import List, Tuple, Union

from pyracf.common.security_admin import SecurityAdmin

from .setropts_requset import SetroptsRequest


class SetroptsAdmin(SecurityAdmin):
    """Set RACF Options Administration."""

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        add_field_data: Union[dict, None] = None,
        overwrite_field_data: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:active_class": "racf:classact",
                "base:addcreat": "racf:addcreat",
                "base:adsp": "racf:adsp",
                "base:applaudt": "racf:applaudt",
                "base:audit_class": "racf:audit",
                "base:catdsns": "racf:catdsns",
                "base:cmdviol": "racf:cmdviol",
                "base:compmode": "racf:compmode",
                "base:egn": "racf:egn",
                "base:erase": "racf:erase",
                "base:eraseall": "racf:eraseall",
                "base:erasesec": "racf:erasesec",
                "base:general_command_class": "racf:gencmd",
                "base:generic_profile_checking_class": "racf:generic",
                "base:generic_profile_sharing_class": "racf:genlist",
                "base:genowner": "racf:genowner",
                "base:global_access_class": "racf:global",
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
                "base:statistics_class": "racf:classtat",
                "base:tapedsn": "racf:tapedsn",
                "base:terminal": "racf:terminal",
                "base:warning": "racf:warning",
                "base:whenprog": "racf:whenprog",
            }
        }
        super().__init__(
            "systemSettings",
            debug=debug,
            generate_requests_only=generate_requests_only,
            add_field_data=add_field_data,
            overwrite_field_data=overwrite_field_data,
            additional_secret_traits=additional_secret_traits,
        )

    # ============================================================================
    # Password Rules
    # ============================================================================
    def get_password_rules(self) -> Union[dict, bytes]:
        """Get RACF password rules."""
        profile = self.list_racf_options(options_only=True)
        return self._get_field(profile, "passwordProcessingOptions", "syntaxRules")

    # ============================================================================
    # Raclist Refresh
    # ============================================================================
    def refresh_raclist(self, class_name: str) -> Union[dict, bytes]:
        """Refresh raclist."""
        result = self.alter(options={"base:raclist": class_name, "base:refresh": True})
        return self._to_steps(result)

    # ============================================================================
    # Get attributes
    # ============================================================================
    def get_class_attributes(self, class_name: str) -> Union[list, bytes]:
        """Get RACF get attributes."""
        profile = self.list_racf_options(options_only=True)
        if not isinstance(profile, dict):
            # Allows this function to work with "self.__generate_requests_only" mode.
            return profile
        return [
            class_type
            for class_type in profile["classes"].keys()
            if class_name.lower() in profile["classes"][class_type]
        ]

    # ============================================================================
    # Audit Class
    # ============================================================================
    def add_audit_class(self, class_name: str) -> Union[dict, bytes]:
        """Add a class to list of classes that RACF performs auditing for."""
        result = self.alter(options={"base:audit_class": class_name})
        return self._to_steps(result)

    def remove_audit_class(self, class_name: str) -> Union[dict, bytes]:
        """Remove a class from the list of classes that RACF performs auditing for."""
        result = self.alter(options={"delete:base:audit_class": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Active Class
    # ============================================================================
    def add_active_class(self, class_name: str) -> Union[dict, bytes]:
        """
        Add a class to the list of classes that RACF performs access authorization checking for.
        """
        result = self.alter(options={"base:active_class": class_name})
        return self._to_steps(result)

    def remove_active_class(self, class_name: str) -> Union[dict, bytes]:
        """
        Remove a class from the list of classes that
        RACF performs access authorization checking for.
        """
        result = self.alter(options={"delete:base:active_class": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Statistics Class
    # ============================================================================
    def add_statistics_class(self, class_name: str) -> Union[dict, bytes]:
        """Add a class to the list of classes that RACF collects statistics for."""
        result = self.alter(options={"base:statistics_class": class_name})
        return self._to_steps(result)

    def remove_statistics_class(self, class_name: str) -> Union[dict, bytes]:
        """Remove a class from the list of classes that RACF collects statistics for."""
        result = self.alter(options={"delete:base:statistics_class": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Generic Command Processing Class
    # ============================================================================
    def add_generic_command_processing_class(
        self, class_name: str
    ) -> Union[dict, bytes]:
        """
        Add a class to the list of classes that have
        generic profile command processing enabled.
        """
        result = self.alter(options={"base:general_command_class": class_name})
        return self._to_steps(result)

    def remove_generic_command_processing_class(
        self, class_name: str
    ) -> Union[dict, bytes]:
        """
        Remove a class from the list of classes that
        have generic profile command processing enabled.
        """
        result = self.alter(options={"delete:base:general_command_class": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Generic Profile Checking Class
    # ============================================================================
    def add_generic_profile_checking_class(self, class_name: str) -> Union[dict, bytes]:
        """Add a class to the list of classes that have generic profile checking enabled."""
        result = self.alter(options={"base:generic_profile_checking_class": class_name})
        return self._to_steps(result)

    def remove_generic_profile_checking_class(
        self, class_name: str
    ) -> Union[dict, bytes]:
        """Remove a class from the list of classes that have generic profile checking enabled."""
        result = self.alter(
            options={"delete:base:generic_profile_checking_class": class_name}
        )
        return self._to_steps(result)

    # ============================================================================
    # Generic Profile Sharing Class
    # ============================================================================
    def add_generic_profile_sharing_class(self, class_name: str) -> Union[dict, bytes]:
        """
        Add a class to the list of classes that are eligible for
        general resource profile sharing in common storage.
        """
        result = self.alter(options={"base:generic_profile_sharing_class": class_name})
        return self._to_steps(result)

    def remove_generic_profile_sharing_class(
        self, class_name: str
    ) -> Union[dict, bytes]:
        """
        Remove a class from the list of classes that are eligible
        for general resource profile sharing in common storage.
        """
        result = self.alter(
            options={"delete:base:generic_profile_sharing_class": class_name}
        )
        return self._to_steps(result)

    # ============================================================================
    # Global Access Class
    # ============================================================================
    def add_global_access_class(self, class_name: str) -> Union[dict, bytes]:
        """Add a class to the list of classes eligible for global access checking."""
        return self.alter(options={"base:global_access_class": class_name})

    def remove_global_access_class(self, class_name: str) -> Union[dict, bytes]:
        """Remove a class from the list of classes eligible for global access checking."""
        result = self.alter(options={"delete:base:global_access_class": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Raclist Class
    # ============================================================================
    def add_raclist_class(self, class_name: str) -> Union[dict, bytes]:
        """Add a class to list of classes that have in-storage profile sharing activated."""
        result = self.alter(options={"base:raclist": class_name})
        return self._to_steps(result)

    def remove_raclist_class(self, class_name: str) -> Union[dict, bytes]:
        """
        Remove a class from the list of classes that have in-storage profile sharing activated.
        """
        result = self.alter(options={"delete:base:raclist": class_name})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def list_racf_options(self, options_only: bool = False) -> Union[dict, bytes]:
        """List RACF options."""
        self._build_segment_dictionaries({"base:list": True})
        setropts_request = SetroptsRequest()
        self._add_traits_directly_to_request_xml_with_no_segments(setropts_request)
        result = self._extract_and_check_result(setropts_request)
        if options_only:
            return self._get_profile(result)
        return result

    def alter(self, options: dict = {}) -> Union[dict, bytes]:
        """Update RACF options."""
        self._build_segment_dictionaries(options)
        setropts_request = SetroptsRequest()
        self._add_traits_directly_to_request_xml_with_no_segments(setropts_request)
        return self._make_request(setropts_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile."""
        messages = result["securityResult"]["systemSettings"]["commands"][0]["messages"]
        # Remove leading/trailing whitespace from messages.
        messages = [message.strip() for message in messages]
        # Ensure that the key-value relationship token is consistent.
        # Change key/field names for easy parsing and categorization.
        messages_normalized = (
            "\n".join(messages)
            .replace("CURRENT OPTIONS:\n", "CURRENT OPTIONS: [OPTION] ")
            .replace("ERASE-ON-SCRATCH BY SECURITY LEVEL", "BY SECURITY LEVEL")
            .replace('"NEVER EXPIRES"', "NONE")
            .replace('"CATDSNS WARNING"', "WARNING")
            .replace('"MLS WARNING"', "WARNING")
            .replace('"MLACTIVE FAIL"', "FAIL")
            .replace('"', "")
            .replace("CURRENT OPTIONS:", "CURRENT OPTIONS")
            .replace(" / ", "_")
            .replace(": ", "= ")
            .replace(":\n", "=\n")
            .replace(" -- ", "--")
            .replace("LOGOPTIONS", "LOG")
            .replace("SUCCESSES CLASSES", "SUCCESS CLASSES")
            .replace("FAILURES CLASSES", "FAILURE CLASSES")
            .replace("SECLEVELAUDIT IS INACTIVE", "SECLEVELAUDIT IS NONE")
            .replace(
                "DATA SET MODELLING IS BEING DONE FOR GDGS.",
                "GENERATION DATA GROUP DATA SET MODELLING = TRUE",
            )
            .replace(
                "DATA SET MODELLING NOT BEING DONE FOR GDGS.",
                "GENERATION DATA GROUP DATA SET MODELLING = FALSE",
            )
            .replace(
                "SINGLE LEVEL NAMES NOT ALLOWED",
                "DATA SET SINGLE LEVEL NAME PREFIX = NONE",
            )
            .replace(" ARE NOT ALLOWED", " = FALSE")
            .replace(" ARE ALLOWED", " = TRUE")
            .replace(" NOT ALLOWED", " = FALSE")
            .replace(" IS ACTIVE", " = TRUE")
            .replace(" IS INACTIVE", " = FALSE")
            .replace(" IN EFFECT IS ", " = ")
            .replace(" IS IN EFFECT FOR THE", " = ")
            .replace(" IS IN EFFECT", " = TRUE")
            .replace(" IS NOT IN EFFECT", " = FALSE")
            .replace(" IS BEING DONE FOR", " = ")
            .replace(" IS BEING DONE", " = TRUE")
            .replace(" NOT BEING DONE FOR ", "")
            .replace(" IS ", " = ")
            .replace("TRUE,", "TRUE.")
            .replace("FUNCTION.", "")
            .replace(" OPTION =", " =")
            .replace("AUTOMATIC DATASET PROTECTION", "AUTOMATIC DATA SET PROTECTION")
            .replace("ENHANCED GENERIC NAMING", "DATA SET ENHANCED GENERIC NAMING")
            .replace("REAL DATA SET NAMES", "REAL DATA SET NAMES LOGGING")
            .replace("PROTECT-ALL", "DATA SET PROTECT-ALL")
            .replace("SECURITY RETENTION PERIOD", "DATA SET SECURITY RETENTION PERIOD")
            .replace("ERASE-ON-SCRATCH", "DATA SET ERASE-ON-SCRATCH")
            .replace("SINGLE LEVEL NAME PREFIX", "DATA SET SINGLE LEVEL NAME PREFIX")
            .replace("CATALOGUED DATA SETS ONLY", "CATALOGUED DATA SET ACCESS ONLY")
            .replace("ADDCREATOR", "DATA SET ADD CREATOR")
            .replace(
                "INACTIVE USERIDS ARE NOT BEING AUTOMATICALLY REVOKED.",
                "REVOKE USERIDS REVOKE AFTER = N/A",
            )
            .replace(
                "INACTIVE USERIDS ARE BEING AUTOMATICALLY REVOKED AFTER ",
                "REVOKE USERIDS REVOKE AFTER = ",
            )
            .replace("= =", "=")
            .replace("ATTRIBUTES = INITSTATS", "ATTRIBUTES = INITIALIZATION-STATISTICS")
            .replace("(PROGRAM", "(PROGRAM-CONTROL")
            .replace("TERMINAL(", "TERMINAL-ACCESS(")
            .replace("PASSWORD PROCESSING OPTIONS=", "")
            .replace(
                "THE ACTIVE PASSWORD ENCRYPTION ALGORITHM",
                "ACTIVE PASSWORD ENCRYPTION ALGORITHM",
            )
            .replace("SPECIAL CHARACTERS", "SPECIAL CHARACTERS ALLOWED")
            .replace(
                "NO PASSWORD HISTORY BEING MAINTAINED.",
                "PASSWORD HISTORY GENERATIONS = 0",
            )
            .replace(
                "GENERATIONS OF PREVIOUS PASSWORDS BEING MAINTAINED.",
                "PASSWORD HISTORY GENERATIONS = [TOKEN 0]",
            )
            .replace(
                "USERIDS NOT BEING AUTOMATICALLY REVOKED",
                "MAX UNSUCCESSFUL PASSWORD ATTEMPTS = NONE",
            )
            .replace(
                "CONSECUTIVE UNSUCCESSFUL PASSWORD ATTEMPTS, A USERID WILL BE REVOKED.",
                "MAX UNSUCCESSFUL PASSWORD ATTEMPTS = [TOKEN 1]",
            )
            .replace(
                "CONSECUTIVE UNSUCCESSFUL PASSWORD ATTEMPTS,\nA USERID WILL BE REVOKED.",
                "MAX UNSUCCESSFUL PASSWORD ATTEMPTS = [TOKEN 1]",
            )
            .replace(
                "NO INSTALLATION PASSWORD SYNTAX RULES ARE PRESENT.",
                "SYNTAX RULES = NONE",
            )
            .replace("INSTALLATION PASSWORD SYNTAX RULES", "SYNTAX RULES")
            .replace("W-NOVOWEL", "W-NO VOWEL")
            .replace("L-ALPHANUM", "L-ALPHANUMERIC")
            .replace("GLOBAL=YES RACLIST ONLY", "GLOBAL RACLIST ONLY CLASSES")
            .replace("GENLIST CLASSES =", "GENERIC PROFILE SHARING CLASSES =")
            .replace("SETR RACLIST CLASSES =", "RACLIST CLASSES =")
            .replace("KERBLVL =", "KERBEROS ENCRYPTION LEVEL =")
            .replace("JES-BATCHALLRACF", "JES-BATCH ALL")
            .replace("JES-XBMALLRACF", "JES-EXECUTION BATCH MONITOR ALL")
            .replace("JES-EARLYVERIFY", "JES-EARLY VERIFY")
            .replace("USER-ID FOR JES UNDEFINEDUSER", "JES UNDEFINED USER")
            .replace("USER-ID FOR JES NJEUSERID", "JES NETWORK USER")
            .replace("NO WRITE-DOWN", "MULTI-LEVEL NO WRITE-DOWN")
            .replace("SECLEVELAUDIT", "SECURITY LABEL LEVEL AUDITING")
            .replace("SECURITY LEVEL FOR AUDITING", "SECURITY LABEL LEVEL AUDITING")
            .replace("SECLABEL AUDIT", "SECURITY LABEL LABEL AUDITING")
            .replace("SECLABEL CONTROL", "SECURITY LABEL ALLOW CONTROL FOR READ ACCESS")
            .replace("COMPATIBILITY MODE", "SECURITY LABEL COMPATIBILITY MODE")
            .replace("GENERIC OWNER ONLY", "GENERIC RULES RESTRICT GENERIC OWNER")
            .replace(
                "LIST OF GROUPS ACCESS CHECKING",
                "GROUP RULES LIST OF GROUPS ACCESS CHECKING",
            )
            .replace(
                "PARTNER LU-VERIFICATION SESSIONKEY INTERVAL MAXIMUM/DEFAULT",
                "VTAM SESSION KEY VERIFICATION INTERVAL",
            )
            .replace(
                "PARTNER LU-VERIFICATION SESSIONKEY INTERVAL DEFAULT",
                "VTAM SESSION KEY VERIFICATION INTERVAL",
            )
            .replace("APPLAUDIT", "VTAM APPC TRANSACTION AUDIT")
            .splitlines()
        )
        # Merge multi-line fields into single line based on key-value relationship token.
        messages_with_merged_lists = []
        for line in messages_normalized:
            if "=" not in line and len(messages_with_merged_lists) != 0:
                messages_with_merged_lists[-1] += " " + line
            else:
                messages_with_merged_lists.append(line)
        # Build initial mapping according to key-value pair relationships
        profile_raw = []
        for line in messages_with_merged_lists:
            tokens = line.split("=")
            key_raw = tokens[0].strip()
            value_raw = "=".join(tokens[1:]).strip().rstrip(".")
            profile_raw.append((key_raw, value_raw))
        class_list_fields = [
            "STATISTICS",
            "ACTIVE CLASSES",
            "GENERIC PROFILE CLASSES",
            "GENERIC COMMAND CLASSES",
            "GENERIC PROFILE SHARING CLASSES",
            "GLOBAL CHECKING CLASSES",
            "RACLIST CLASSES",
            "GLOBAL RACLIST ONLY CLASSES",
            "LOG ALWAYS CLASSES",
            "LOG NEVER CLASSES",
            "LOG SUCCESS CLASSES",
            "LOG FAILURE CLASSES",
            "LOG DEFAULT CLASSES",
            "AUDIT CLASSES",
        ]
        generic_list_fields = ["DEFAULT RVARY PASSWORD"]
        password_processing_options = [
            "ACTIVE PASSWORD ENCRYPTION ALGORITHM",
            "PASSWORD CHANGE INTERVAL",
            "PASSWORD MINIMUM CHANGE INTERVAL",
            "MIXED CASE PASSWORD SUPPORT",
            "SPECIAL CHARACTERS ALLOWED",
            "PASSWORD HISTORY GENERATIONS",
            "MAX UNSUCCESSFUL PASSWORD ATTEMPTS",
            "PASSWORD EXPIRATION WARNING LEVEL",
            "SYNTAX RULES",
            "LEGEND",
        ]
        generic_subfield_map = {
            "JES": "jes",
            "REVOKE USERIDS": "revokeUserids",
            "MULTI-LEVEL": "multiLevelSecurity",
            "LANGUAGE DEFAULT": "languageDefaults",
            "DATA SET": "dataSets",
            "SECURITY LABEL": "securityLabels",
            "VTAM": "vtam",
            "KERBEROS": "kerberos",
            "GENERIC RULES": "genericRules",
            "GROUP RULES": "groupRules",
        }
        generic_subsubfield_map = {
            "MULTI-LEVEL": [
                "NO WRITE-DOWN",
                "SECURE",
                "ACTIVE",
            ],
            "DATA SET": ["CATALOGUED DATA SET ACCESS ONLY", "ERASE-ON-SCRATCH"],
        }
        profile = {}
        for key_raw, value_raw in profile_raw:
            if "[TOKEN " in value_raw:
                (key_raw, value_raw) = self.__fix_key_value_raw(key_raw, value_raw)
            key = self._profile_field_to_camel_case(key_raw.lower())
            if key_raw == "ATTRIBUTES":
                self.__add_attributes(profile, key, value_raw)
                continue
            elif key_raw in class_list_fields:
                self.__add_class_list(profile, key, value_raw)
                continue
            elif key_raw in generic_list_fields:
                value = self.__to_list(value_raw)
                if key in profile:
                    profile[key] += value
                else:
                    profile[key] = value
                continue
            elif key_raw in password_processing_options:
                self.__add_password_processing_options(profile, key, value_raw)
                continue
            elif self.__is_generic_subfield(key_raw, generic_subfield_map):
                self.__add_generic_subfield(
                    profile,
                    generic_subfield_map,
                    generic_subsubfield_map,
                    key_raw,
                    value_raw,
                )
                continue
            value = self._cast_from_str(value_raw)
            profile[key] = value
        del result["securityResult"]["systemSettings"]["commands"][0]["messages"]
        result["securityResult"]["systemSettings"]["commands"][0]["profiles"] = [
            profile
        ]

    def __fix_key_value_raw(self, key_raw: str, value_raw: str) -> Tuple[str, str]:
        """Normalize raw key-value pair."""
        key_tokens = key_raw.split()
        value_index = int(value_raw.split()[-1].rstrip("]"))
        value_raw = key_tokens[value_index]
        key_raw = " ".join(key_tokens[value_index + 1 :])
        return (key_raw, value_raw)

    def __add_attributes(self, profile: dict, key: str, value_raw: str):
        """Add attributes to the profile field"""
        if key not in profile:
            profile[key] = {}
        tokens = value_raw.split()
        for token in tokens:
            if "(" in token:
                subtokens = token.split("(")
                if subtokens[0] == "WHEN":
                    subsubtokens = subtokens[1].split("--")
                    attribute = subsubtokens[0]
                    value = subsubtokens[-1].rstrip(")").lower()
                elif subtokens[0] == "NOWHEN":
                    attribute = subtokens[1].rstrip(")")
                    value = False
                else:
                    attribute = subtokens[0]
                    value = subtokens[1].rstrip(")").lower()
            elif token[:2] == "NO":
                attribute = token[2:]
                value = False
            else:
                attribute = token
                value = True
            match attribute:
                case "SAUDIT":
                    attribute = "SPECIAL AUDIT"
                case "CMDVIOL":
                    attribute = "LOG COMMAND VIOLATIONS"
                case "OPERAUDIT":
                    attribute = "OPERATIONS AUDIT"
            attribute = self._profile_field_to_camel_case(attribute.lower())
            profile[key][attribute] = value

    def __to_list(self, value_raw: str, n: int = 1) -> List[str]:
        """Convert space delimited list into a list."""
        if value_raw == "NONE":
            return []
        tokens = value_raw.split()
        return [
            self._cast_from_str(" ".join(tokens[i : i + n]))
            for i in range(0, len(tokens), n)
        ]

    def __add_class_list(self, profile: dict, class_key: str, value_raw: str) -> None:
        """Add a class list to profile"""
        if "classes" not in profile:
            profile["classes"] = {}
        class_key = class_key.replace("Classes", "")
        profile["classes"][class_key] = self.__to_list(value_raw)

    def __add_password_processing_options(
        self, profile: dict, key: str, data: str
    ) -> None:
        """Add password processing options to profile."""
        if "passwordProcessingOptions" not in profile:
            profile["passwordProcessingOptions"] = {}
        if key == "syntaxRules":
            try:
                profile["passwordProcessingOptions"][key]["rules"]
            except KeyError:
                profile["passwordProcessingOptions"][key] = {"rules": []}
            if data == "NONE":
                return
            rule_tokens = [
                rule_token for rule_token in data.split("RULE") if rule_token != ""
            ]
            for rule_token in rule_tokens:
                length_chars = rule_token.lower().split("length(")[1].split(")")[0]
                if ":" in length_chars:
                    min_length = self._cast_from_str(length_chars.split(":")[0])
                    max_length = self._cast_from_str(length_chars.split(":")[1])
                else:
                    min_length = self._cast_from_str(length_chars)
                    max_length = self._cast_from_str(length_chars)
                chars = rule_token[-1 * max_length :].strip()
                profile["passwordProcessingOptions"][key]["rules"].append(
                    {
                        "minLength": min_length,
                        "maxLength": max_length,
                        "content": chars,
                    }
                )
            return
        elif key == "legend":
            legend = {}
            legend_tokens = data.split("-")
            for i in range(0, len(legend_tokens) - 1):
                legend_key = legend_tokens[i].split()[-1]
                if i + 1 == len(legend_tokens) - 1:
                    legend_value = legend_tokens[-1]
                else:
                    legend_value = " ".join(legend_tokens[i + 1].split()[:-1])
                legend[legend_key] = legend_value.lower()
            profile["passwordProcessingOptions"]["syntaxRules"][key] = legend
            return
        profile["passwordProcessingOptions"][key] = self._cast_from_str(data)

    def __is_generic_subfield(self, key_raw: str, generic_subfield_map: dict):
        """Check if a subfield is considered a generic subfield."""
        for subfield in generic_subfield_map.keys():
            if subfield in key_raw:
                return True
        return False

    def __add_generic_subfield(
        self,
        profile: dict,
        generic_subfield_map: dict,
        generic_subsubfield_map: dict,
        key_raw: str,
        value_raw: str,
    ) -> None:
        """Add a generic subfield to profile."""
        subdictionary = {}
        for subfield_token in generic_subsubfield_map.keys():
            if subfield_token in key_raw:
                for subsubfield_token in generic_subsubfield_map[subfield_token]:
                    if subsubfield_token in key_raw:
                        if "TRUE. CURRENT OPTIONS" in value_raw:
                            value_tokens = value_raw.split(". CURRENT OPTIONS")
                            subdictionary["enabled"] = self._cast_from_str(
                                value_tokens[0]
                            )
                            subdictionary[
                                "options"
                            ] = self.__process_generic_subsubfield_options(
                                value_tokens[1]
                            )
                        else:
                            subdictionary["enabled"] = self._cast_from_str(value_raw)
                            subdictionary["options"] = {}
        for subfield_token in generic_subfield_map.keys():
            if subfield_token in key_raw:
                key = generic_subfield_map[subfield_token]
                subkey_raw = key_raw.replace(subfield_token, "")
        if key not in profile:
            profile[key] = {}
        subkey = self._profile_field_to_camel_case(subkey_raw.lower())
        if subdictionary:
            profile[key][subkey] = subdictionary
        else:
            profile[key][subkey] = self._cast_from_str(value_raw)

    def __process_generic_subsubfield_options(self, subsubfield_options: str) -> dict:
        # Build a dictionary that represents the options associated with a generic subfield.
        subsubfield_option_tokens = subsubfield_options.split("[OPTION]")[1:]
        options_dictionary = {}
        for option in subsubfield_option_tokens:
            option_tokens = option.split("=")
            key = self._profile_field_to_camel_case(option_tokens[0].strip().lower())
            value = self._cast_from_str(option_tokens[1].strip())
            options_dictionary[key] = value
        return options_dictionary
