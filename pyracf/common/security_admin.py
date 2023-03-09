"""Base Class for RACF Administration Interface."""

from typing import List, Tuple, Union

from pyracf.common.irrsmo00 import IRRSMO00
from pyracf.common.security_request import SecurityRequest
from pyracf.common.security_request_error import SecurityRequestError
from pyracf.common.security_result import SecurityResult


class SecurityAdmin:
    """Base Class for RACF Administration Interface."""

    def __init__(self) -> None:
        self.irrsmo00 = IRRSMO00()
        self.valid_segment_traits = {}
        self.common_base_traits_dataset_generic = {
            "aclcnt": "racf:aclcnt",
            "aclacnt": "racf:aclacnt",
            "aclacs": "racf:aclacs",
            "aclid": "racf:aclid",
            "acl2cnt": "racf:acl2cnt",
            "acl2acnt": "racf:acl2acnt",
            "acl2acs": "racf:acl2acs",
            "acl2cond": "racf:acl2cond",
            "acl2ent": "racf:acl2ent",
            "acl2id": "racf:acl2id",
            "acsaltr": "racf:acsaltr",
            "acscntl": "racf:acscntl",
            "acsread": "racf:acsread",
            "acsupdt": "racf:acsupdt",
            "all": "racf:all",
            "audaltr": "racf:audaltr",
            "audcntl": "racf:audcntl",
            "audnone": "racf:audnone",
            "audread": "racf:audread",
            "audupdt": "racf:audupdt",
            "authuser": "racf:authuser",
            "fvolume": "racf:fvolume",
            "gaudaltr": "racf:gaudaltr",
            "gaudcntl": "racf:gaudcntl",
            "gaudnone": "racf:gaudnone",
            "gaudread": "racf:gaudread",
            "gaudupdt": "racf:gaudupdt",
            "generic": "racf:generic",
        }
        self.segment_traits = {}
        self.trait_map = {}
        self.profile_type = None

    def extract_and_check_result(self, security_request: SecurityRequest) -> dict:
        """Extract a RACF profile."""
        result = self.make_request(security_request)
        if "error" in result["securityresult"][self.profile_type]:
            raise SecurityRequestError(result)
        if (
            result["securityresult"]["returncode"] == 0
            and result["securityresult"]["reasoncode"] == 0
        ):
            self.format_profile(result)
            return result
        raise SecurityRequestError(result)

    def build_bool_segment_dictionaries(self, traits: dict) -> None:
        """Build segment dictionaries for profile extract."""
        for trait in traits:
            if trait in self.valid_segment_traits:
                self.segment_traits[trait] = traits[trait]

    def make_request(self, security_request: SecurityRequest, opts: int = 1) -> dict:
        """Make request to IRRSMO00."""
        result_xml = self.irrsmo00.call_racf(security_request.dump_request_xml(), opts)
        results = SecurityResult(result_xml)
        return results.get_result_dictionary()

    def format_profile(self, result: dict):
        """Placeholder for format profile function for profile extract."""

    def format_profile_generic(
        self, messages: str, valid_segment_traits: dict, profile_type: str
    ) -> None:
        """Generic profile formatter shared by two or more RACF profile formats."""
        profile = {}
        current_segment = "base"
        (
            additional_segment_keys,
            no_segment_information_keys,
        ) = self.__build_additional_segment_keys(valid_segment_traits)
        profile[current_segment] = {}
        i = 0
        while i < len(messages):
            if messages[i] == " " or messages[i] in no_segment_information_keys:
                i += 1
                continue
            if i < len(messages) - 1 and messages[i] in additional_segment_keys:
                current_segment = messages[i].split()[0].lower()
                profile[current_segment] = {}
                i += 2
            if profile_type in ("dataset", "generic"):
                i = self.__format_data_set_generic_profile_data(
                    messages, profile, current_segment, i
                )
            if profile_type == "user":
                i = self.__format_user_profile_data(
                    messages, profile, current_segment, i
                )
            i += 1
        return profile

    def __format_data_set_generic_profile_data(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> int:
        """Specialized logic for formatting DataSet/General Resource profile data."""
        if "=" in messages[i]:
            self.__add_key_value_pair_to_profile(
                messages[i],
                profile,
                current_segment,
            )
        elif (
            i < len(messages) - 2
            and ("  " in messages[i])
            and ("--" in messages[i + 1])
        ):
            self.__format_semi_tabular_data(messages, profile, current_segment, i)
            i += 1
        elif i < len(messages) - 2 and ("-" in messages[i + 1]):
            field = " ".join(
                [
                    txt.lower().strip()
                    for txt in list(filter(None, messages[i].split(" ")))
                ]
            )
            profile[current_segment][field] = self.clean_and_separate(messages[i + 2])
            i += 1
        elif "NO INSTALLATION DATA" in messages[i]:
            profile[current_segment]["installation data"] = None
        return i

    def __format_user_profile_data(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> int:
        """Specialized logic for formatting user profile data."""
        if (
            i < len(messages) - 1
            and messages[i + 1] == " ---------------------------------------------"
        ):
            semi_tabular_data = messages[i : i + 3]
            self.__add_semi_tabular_data_to_segment(
                profile[current_segment], semi_tabular_data
            )
            i += 2
        elif messages[i][:8] == "  GROUP=":
            if "groups" not in profile[current_segment]:
                profile[current_segment]["groups"] = {}
            group = messages[i].split("=")[1].split()[0]
            profile[current_segment]["groups"][group] = {}
            message = messages[i] + messages[i + 1] + messages[i + 2] + messages[i + 3]
            self.__add_key_value_pairs_to_segment(
                profile[current_segment]["groups"][group], message[17:]
            )
            i += 3
        elif "=" not in messages[i] and messages[i].strip()[:3] != "NO-":
            messages[i] = f"{messages[i]}={messages[i+1]}"
            self.__add_key_value_pairs_to_segment(profile[current_segment], messages[i])
            i += 1
        else:
            self.__add_key_value_pairs_to_segment(profile[current_segment], messages[i])
        return i

    def __build_additional_segment_keys(
        self, valid_segment_traits: dict
    ) -> Tuple[str, str]:
        """Build keys for detecting additional segments in RACF profile data."""
        additional_segment_keys = [
            f"{segment.upper()} INFORMATION"
            for segment in valid_segment_traits
            if segment != "base"
        ]
        no_segment_information_keys = [
            f"NO {segment}" for segment in additional_segment_keys
        ]
        return (additional_segment_keys, no_segment_information_keys)

    def __add_semi_tabular_data_to_segment(
        self, segment: dict, semi_tabular_data: List[str]
    ) -> None:
        """Add semi-tabular data as key-value pairs to segment dictionary."""
        heading_tokens = list(filter(("").__ne__, semi_tabular_data[0].split("  ")))
        key_prefix = heading_tokens[0]
        keys = [f"{key_prefix}{key.strip()[1:-1]}" for key in heading_tokens[1:]]
        values = semi_tabular_data[-1].split()
        keys_length = len(keys)
        for i in range(keys_length):
            key = keys[i].strip().lower().replace(" ", "").replace("-", "")
            segment[key] = self.cast_value(values[i])

    def __format_semi_tabular_data(
        self,
        messages: List[str],
        profile: dict,
        current_segment: str,
        i: int,
    ) -> None:
        """Generic function for parsing semitabular data from RACF profile data."""
        tmp_ind = [j for j in range(len(messages[i + 1])) if messages[i + 1][j] == "-"]
        indexes = [
            tmp_ind[j]
            for j in range(len(tmp_ind))
            if j == 0 or tmp_ind[j] - tmp_ind[j - 1] > 1
        ]
        # print(tmp_ind,indexes)
        indexes_length = len(indexes)
        for j in range(indexes_length):
            if j < indexes_length - 1:
                ind_e0 = indexes[j + 1]
                ind_e1 = indexes[j + 1]
            else:
                ind_e0 = len(messages[i])
                ind_e1 = len(messages[i + 2])

            field = messages[i][indexes[j] : ind_e0].strip().lower()
            profile[current_segment][field] = self.clean_and_separate(
                messages[i + 2][indexes[j] : ind_e1]
            )

    def __add_key_value_pairs_to_segment(
        self,
        segment: dict,
        message: str,
    ) -> None:
        """Add a key value pair to a sgement dictionary."""
        list_fields = ["attributes", "classauthorizations"]
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
                values = [
                    self.cast_value(value) for value in value.split() if value != "NONE"
                ]
                segment[current_key] += values
            else:
                segment[current_key] = self.cast_value(value)
            key = "".join(sub_tokens[1:])
            if len(sub_tokens) == 1:
                if i < len(tokens) - 1 and " " in sub_tokens[0] and i != 0:
                    sub_tokens = sub_tokens[0].split()
                    segment[current_key] = self.cast_value(sub_tokens[0])
                    key = sub_tokens[-1]
                else:
                    key = sub_tokens[0]

    def __add_key_value_pair_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> None:
        """Generic function for extracting key-value pair from RACF profile data."""
        field = message.split("=")[0].strip().lower()
        profile[current_segment][field] = self.clean_and_separate(message.split("=")[1])

    def clean_and_separate(self, value: str) -> Union[list, str]:
        """Clean cast and separate comma and space delimited data."""
        cln_val = value.strip().lower()
        if "," in cln_val:
            out = [self.cast_value(val.strip()) for val in cln_val.split(",")]
        elif " " in cln_val:
            out = [self.cast_value(val.strip()) for val in cln_val.split(" ")]
        else:
            out = self.cast_value(cln_val)

        if isinstance(out, list):
            open_ind = []
            close_ind = []
            cln_ind = []
            for i,val in enumerate(out):
                if "(" in val and ")" not in val:
                    open_ind.append(i)
                if ")" in val and "(" not in val:
                    close_ind.append(i)
            if not open_ind and not close_ind:
                return out
            for i,ind in enumerate(open_ind):
                out[ind] = " ".join(out[ind : (close_ind[i] + 1)])
                cln_ind = cln_ind + [*range(ind, close_ind[i] + 1)][1:]
            cln_ind.reverse()
            for i in cln_ind:
                del out[i]

        return out

    def cast_value(self, value: str) -> Union[None, int, float, str]:
        """Cast null values floats and integers."""
        value = value.lower()
        if value in ("n/a", "none", "none specified", "no", "None"):
            return None
        if value in (
            "in effect",
            "active",
            "active.",
            "being done.",
            "in effect.",
            "allowed.",
            "being done",
        ):
            return True
        if value in ("not in effect", "inactive", "not allowed.", "not being done"):
            return False
        if "days" in value and any(chr.isdigit() for chr in value):
            digits = "".join([chr for chr in value if chr.isdigit()])
            return int(digits)
        if "in effect for the " in value and " function." in value:
            return value.split("in effect for the ")[1].split(" function.")[0]
        if "." in value:
            try:
                return float(value)
            except ValueError:
                return value
        try:
            return int(value.replace(",", ""))
        except ValueError:
            return value

    def __validate_trait(self, trait: str, segment: str, value: Union[str, list]):
        """Validate the specified trait exists in the specified segment"""
        if segment not in self.valid_segment_traits:
            return -1
        if trait not in self.valid_segment_traits[segment]:
            if trait[:3] == "add":
                operation = "add"
                true_trait = trait[3:]
            elif trait[:2] == "no":
                operation = "del"
                true_trait = trait[2:]
            elif trait[:3] == "del":
                operation = "remove"
                true_trait = trait[3:]
            elif trait[:3] == "set":
                operation = "set"
                true_trait = trait[3:]
            else:
                return -1
            self.__validate_trait(true_trait, segment, [value, operation])
            return 0
        if segment not in self.segment_traits:
            self.segment_traits[segment] = {}
        self.segment_traits[segment][trait] = value
        self.trait_map[trait] = self.valid_segment_traits[segment][trait]
        return 0

    def build_segment_dictionaries(self, traits: dict) -> None:
        """Build segemnt dictionaries for each segment."""
        for trait in traits:
            if ":" in trait:
                segment = trait.split(":")[0]
                true_trait = trait.split(":")[1]
                self.__validate_trait(true_trait, segment, traits[trait])
                continue
            for segment in self.valid_segment_traits:
                self.__validate_trait(trait, segment, traits[trait])
