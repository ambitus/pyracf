"""Base Class for RACF Administration Interface."""

import platform
import re
import xml.etree.ElementTree
from datetime import datetime
from typing import Any, List, Tuple, Union

from .exceptions.downstream_fatal_error import DownstreamFatalError
from .exceptions.security_request_error import SecurityRequestError
from .exceptions.segment_error import SegmentError
from .exceptions.segment_trait_error import SegmentTraitError
from .exceptions.userid_error import UserIdError
from .irrsmo00 import IRRSMO00
from .security_request import SecurityRequest
from .security_result import SecurityResult
from .utilities.dumper import Dumper
from .utilities.logger import Logger


class SecurityAdmin:
    """Base Class for RACF Administration Interface."""

    _common_base_traits_data_set_generic = {
        "base:aclcnt": "racf:aclcnt",
        "base:aclacnt": "racf:aclacnt",
        "base:aclacs": "racf:aclacs",
        "base:aclid": "racf:aclid",
        "base:acl2cnt": "racf:acl2cnt",
        "base:acl2acnt": "racf:acl2acnt",
        "base:acl2acs": "racf:acl2acs",
        "base:acl2cond": "racf:acl2cond",
        "base:acl2ent": "racf:acl2ent",
        "base:acl2id": "racf:acl2id",
        "base:acsaltr": "racf:acsaltr",
        "base:acscntl": "racf:acscntl",
        "base:acsread": "racf:acsread",
        "base:acsupdt": "racf:acsupdt",
        "base:all": "racf:all",
        "base:audaltr": "racf:audaltr",
        "base:audcntl": "racf:audcntl",
        "base:audnone": "racf:audnone",
        "base:audread": "racf:audread",
        "base:audupdt": "racf:audupdt",
        "base:authuser": "racf:authuser",
        "base:fvolume": "racf:fvolume",
        "base:gaudaltr": "racf:gaudaltr",
        "base:gaudcntl": "racf:gaudcntl",
        "base:gaudnone": "racf:gaudnone",
        "base:gaudread": "racf:gaudread",
        "base:gaudupdt": "racf:gaudupdt",
        "base:generic": "racf:generic",
    }

    _valid_segment_traits = {}
    _extracted_key_value_pair_segment_traits_map = {}
    _case_sensitive_extracted_values = []
    __running_userid = None
    _logger = Logger()
    __dumper = Dumper()

    def __init__(
        self,
        profile_type: str,
        irrsmo00_result_buffer_size: Union[int, None] = None,
        debug: bool = False,
        dump_mode: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
        run_as_userid: Union[str, None] = None,
    ) -> None:
        self.__secret_traits = {
            "base:password": "racf:password",
            "base:passphrase": "racf:phrase",
        }
        if irrsmo00_result_buffer_size:
            if (
                not isinstance(irrsmo00_result_buffer_size, int)
                or irrsmo00_result_buffer_size < 10000
            ):
                raise ValueError(
                    "IRRSMO00 result buffer size must be an "
                    + "integer value greater than or equal to '10000'."
                )
            elif irrsmo00_result_buffer_size > 100000000:
                self._logger.log_warning(
                    "IRRSMO00 result buffer sizes greater than '100000000' may "
                    + "result in a 'SIGKILL' signal to be raised, which is NOT "
                    + "recoverable and will lead to the Python process that "
                    + "pyRACF is running under to be killed."
                )
            self.__irrsmo00 = IRRSMO00(result_buffer_size=irrsmo00_result_buffer_size)
        else:
            self.__irrsmo00 = IRRSMO00()
        self._profile_type = profile_type
        self._segment_traits = {}
        # used to preserve segment traits for debug logging.
        self.__preserved_segment_traits = {}
        self._trait_map = {}
        self.__debug = debug
        if self.__debug:
            self._logger.log_warning(
                "'Debug Logging' is enabled. This feature should only "
                + "be used for development and debugging."
            )
        self.__dump_mode = dump_mode
        if self.__dump_mode:
            self._logger.log_warning(
                "'Dump Mode' is enabled. This feature should only "
                + "be used for development and debugging."
            )
        self._generate_requests_only = generate_requests_only
        if update_existing_segment_traits is not None:
            self._logger.log_experimental("Update Existing Segment Traits")
            self.__update_valid_segment_traits(update_existing_segment_traits)
        if replace_existing_segment_traits is not None:
            self._logger.log_experimental("Replace Existing Segment Traits")
            self.__replace_valid_segment_traits(replace_existing_segment_traits)
        if additional_secret_traits is not None:
            self._logger.log_experimental("Add Additional Secret Traits")
            self.__add_additional_secret_traits(additional_secret_traits)
        self.set_running_userid(run_as_userid)

    # ============================================================================
    # Run as Other User ID
    # ============================================================================
    def set_running_userid(self, userid: Union[str, None]) -> None:
        if userid is None:
            self.__running_userid = None
            return
        if not isinstance(userid, str) or len(userid) > 8 or userid == "":
            raise UserIdError(userid)
        self.__running_userid = userid.upper()

    def get_running_userid(self) -> Union[str, None]:
        if isinstance(self.__running_userid, str):
            return self.__running_userid.lower()
        return self.__running_userid

    # ============================================================================
    # Customize Segment Traits
    # ============================================================================
    def __update_valid_segment_traits(self, update_valid_segment_traits: dict) -> None:
        """Update fields to valid segment traits dictionary."""
        for segment in update_valid_segment_traits:
            if segment in self._valid_segment_traits:
                self._valid_segment_traits[segment].update(
                    update_valid_segment_traits[segment]
                )
            else:
                self._valid_segment_traits[segment] = update_valid_segment_traits[
                    segment
                ]

    def __replace_valid_segment_traits(self, new_valid_segment_traits: dict) -> None:
        """Replace field data in valid segment traits dictionary"""
        self._valid_segment_traits = new_valid_segment_traits

    # ============================================================================
    # Dump Mode
    # ============================================================================
    def __raw_dump(self) -> None:
        raw_result_xml = self.__irrsmo00.get_raw_result_xml()
        dump_file_path = self.__dumper.raw_dump(raw_result_xml)
        self._logger.log_info(
            f"Raw security result XML has been written to '{dump_file_path}'.\n"
        )
        if self.__debug:
            # Note, since the hex dump is logged to the console,
            # secrets will be redacted.
            self._logger.log_hex_dump(raw_result_xml, self.__secret_traits)

    # ============================================================================
    # Secrets Redaction
    # ============================================================================
    def __add_additional_secret_traits(self, additional_secret_traits: list) -> None:
        """Add additional fields to be redacted in logger output."""
        for secret in additional_secret_traits:
            if secret in self.__secret_traits:
                continue
            if ":" not in secret:
                continue
            segment = secret.split(":")[0]
            if segment not in self._valid_segment_traits:
                continue
            if secret not in self._valid_segment_traits[segment]:
                continue
            self.__secret_traits[secret] = self._valid_segment_traits[segment][secret]

    # ============================================================================
    # Request Execution
    # ============================================================================
    def _extract_and_check_result(
        self,
        security_request: SecurityRequest,
    ) -> dict:
        """Extract a RACF profile."""
        result = self._make_request(security_request)
        if self._generate_requests_only:
            return result
        self._format_profile(result)
        if self.__debug:
            # No need to redact anything here since the result dictionary
            # already has secrets redacted when it is built, and profile
            # extract doesn't return any secrets anyways.
            self._logger.log_dictionary("Result Dictionary (Formatted Profile)", result)
        return result

    def _make_request(
        self,
        security_request: SecurityRequest,
        irrsmo00_precheck: bool = False,
    ) -> Union[dict, bytes]:
        """
        Make request to IRRSMO00.
        Note: Secrets are redacted from all data returned to the user and log messages.
        """
        if self.__debug:
            self._logger.log_dictionary(
                "Request Dictionary",
                self.__preserved_segment_traits,
                secret_traits=self.__secret_traits,
            )
            self._logger.log_xml(
                "Request XML",
                security_request.dump_request_xml(encoding="utf-8"),
                secret_traits=self.__secret_traits,
            )
        request_xml = self._logger.redact_request_xml(
            security_request.dump_request_xml(encoding="utf-8"),
            secret_traits=self.__secret_traits,
        )
        if self._generate_requests_only:
            self.__clear_state(security_request)
            return request_xml
        raw_result = self._logger.redact_result_xml(
            self.__irrsmo00.call_racf(
                security_request.dump_request_xml(),
                irrsmo00_precheck,
                self.__running_userid,
            ),
            self.__secret_traits,
        )
        self.__clear_state(security_request)
        if isinstance(raw_result, list):
            # When IRRSMO00 encounters some errors, it returns no result XML string.
            # When this happens, the C code instead surfaces the return and reason
            # codes which causes a DownstreamFatalError to be raised.
            raise DownstreamFatalError(
                saf_return_code=raw_result[0],
                racf_return_code=raw_result[1],
                racf_reason_code=raw_result[2],
                request_xml=request_xml,
                run_as_userid=self.get_running_userid(),
            )
        if self.__debug:
            # No need to redact anything here since the raw result XML
            # already has secrets redacted when it is built.
            self._logger.log_xml("Result XML", raw_result)
        try:
            result = SecurityResult(raw_result, self.get_running_userid())
        except xml.etree.ElementTree.ParseError as e:
            # If the result XML cannot be parsed, a dump of the raw result
            # XML will be created to aid in problem determination.
            self._logger.log_fatal(
                "Unable to parse security result XML returned by IRRSMO00."
            )
            self.__raw_dump()
            self.__irrsmo00.clear_raw_result_xml()
            # After creating the dump, re-raise the exception.
            raise e
        if self.__dump_mode:
            # If in dump mode a dump of the raw result XML
            # will be created even if the raw security result was
            # able to be processed successfully.
            self.__raw_dump()
        self.__irrsmo00.clear_raw_result_xml()
        if self.__debug:
            # No need to redact anything here since the result dictionary
            # already has secrets redacted when it is built.
            self._logger.log_dictionary(
                "Result Dictionary", result.get_result_dictionary()
            )
        result_dictionary = result.get_result_dictionary()
        if result_dictionary["securityResult"]["returnCode"] >= 8:
            # All return codes greater than or equal to 8 are indicative of an issue
            # with IRRSMO00 that would stop RACF from generating a command image.
            # The user should interogate the result dictionary attached to the
            # DownstreamFatalError as well as the return and reason codes to resolve
            # the problem.
            raise DownstreamFatalError(
                saf_return_code=8,
                racf_return_code=result_dictionary["securityResult"]["returnCode"],
                racf_reason_code=result_dictionary["securityResult"]["reasonCode"],
                request_xml=request_xml,
                run_as_userid=self.get_running_userid(),
                result_dictionary=result_dictionary,
            )
        if result_dictionary["securityResult"]["returnCode"] != 0:
            # All remaining non-zero return codes should cause a SecurityRequestError
            # to be raised. Even if a return code of 4 is not indicative of a problem,
            # it is up to the user to interogate the result dictionary attached to the
            # SecurityRequestError and decided whether or not the return code 4 is
            # indicative of a problem.
            raise SecurityRequestError(result_dictionary)
        return result_dictionary

    def _to_steps(self, results: Union[List[dict], dict, bytes]) -> Union[dict, bytes]:
        """
        Build a steps dictionary composed of each result dictionary
        in a result dictionary list, where the result dictionary list is
        assumed to be ordered chronologically in ascending order with respect
        to when each corresponding request was made.

        Note: for generate request only mode (for testing purposes),
        all of the request xml bytes should just be concatenated together.
        """
        if isinstance(results, dict) or isinstance(results, bytes):
            results = [results]
        if self._generate_requests_only:
            concatenated_xml = b""
            for request_xml in results:
                if request_xml:
                    concatenated_xml += request_xml
            return concatenated_xml
        pre_processed_results = []
        for result in results:
            if not result:
                continue
            if list(result.keys())[0] == "step1":
                for result_dictionary in result.values():
                    pre_processed_results.append(result_dictionary)
                continue
            pre_processed_results.append(result)
        steps_dictionary = {}
        for step, result_dictionary in enumerate(pre_processed_results):
            steps_dictionary[f"step{step + 1}"] = result_dictionary
        return steps_dictionary

    # ============================================================================
    # Request Dictionary Building
    # ============================================================================
    def __clear_state(self, security_request: SecurityRequest) -> None:
        """Clear state for new request."""
        self._segment_traits = {}
        self._trait_map = {}
        self.__preserved_segment_traits = {}
        del security_request

    def __validate_and_add_trait(
        self, trait: str, segment: str, value: Union[str, dict]
    ):
        """Validate the specified trait exists in the specified segment."""
        if segment not in self._valid_segment_traits:
            return False
        if trait not in self._valid_segment_traits[segment]:
            tokens = trait.split(":")
            operation = tokens[0]
            if operation not in ["add", "remove", "delete"] or len(tokens) == 1:
                return False
            trait = trait[len(operation) + 1 :]
            if trait not in self._valid_segment_traits[segment]:
                return False
            value_operation_dictionary = {"value": value, "operation": operation}
        else:
            operation = None
            if isinstance(value, bool) and not value:
                operation = "delete"
            value_operation_dictionary = {"value": value, "operation": operation}
        if segment not in self._segment_traits:
            self._segment_traits[segment] = {}
        self._segment_traits[segment][trait] = value_operation_dictionary
        self._trait_map[trait] = self._valid_segment_traits[segment][trait]
        return True

    def _build_segment_dictionary(self, segments: List[str]) -> None:
        """Build segment dictionaries for profile extract."""
        bad_segments = []
        for segment in segments:
            if segment in self._valid_segment_traits:
                self._segment_traits[segment] = True
            else:
                bad_segments.append(segment)
        if bad_segments:
            self.__clear_state(SecurityRequest)
            raise SegmentError(bad_segments, self._profile_type)
        # preserve segment traits for debug logging.
        self.__preserved_segment_traits = self._segment_traits

    def _build_segment_trait_dictionary(self, traits: dict) -> None:
        """Build segemnt dictionaries for each segment."""
        bad_traits = []
        for trait in traits:
            trait_valid = False
            for segment in self._valid_segment_traits:
                trait_valid = self.__validate_and_add_trait(
                    trait, segment, traits[trait]
                )
                if trait_valid:
                    break
            if not trait_valid:
                bad_traits.append(trait)
        if bad_traits:
            self.__clear_state(SecurityRequest)
            raise SegmentTraitError(bad_traits, self._profile_type)

        # preserve segment traits for debug logging.
        self.__preserved_segment_traits = self._segment_traits

    def _build_xml_segments(
        self,
        security_request: SecurityRequest,
        alter: bool = False,
        extract: bool = True,
    ) -> None:
        """Build XML representation of segments."""
        security_request._build_segments(
            self._segment_traits, self._trait_map, alter=alter, extract=extract
        )

    def _add_traits_directly_to_request_xml_with_no_segments(
        self, security_request: SecurityRequest, alter: bool = False
    ) -> None:
        """Add traits as directly to request xml without building segments."""
        for segment, traits in self._segment_traits.items():
            if segment == "base":
                security_request._build_segment(
                    None, traits, self._trait_map, alter=alter
                )

    # ============================================================================
    # Profile Dictionary Building
    # ============================================================================
    def _get_profile(
        self, result: Union[dict, bytes], index: int = 0
    ) -> Union[dict, bytes]:
        """Extract the profile section from a result dictionary."""
        if self._generate_requests_only:
            # Allows this function to work with "self._generate_requests_only" mode.
            return result
        return result["securityResult"][self._profile_type]["commands"][0]["profiles"][
            index
        ]

    def _get_field(
        self,
        profile: Union[dict, bytes],
        segment: str,
        field: str,
        string: bool = False,
    ) -> Union[bytes, Any, None]:
        """Extract the value of a field from a segment in a profile."""
        if self._generate_requests_only:
            # Allows this function to work with "self._generate_requests_only" mode.
            return profile
        try:
            field = profile[segment][field]
            if string and field is not None:
                return str(field)
            return field
        except KeyError:
            return None

    def _format_profile(self, result: dict):
        """Placeholder for format profile function for profile extract."""

    def _format_profile_generic(self, messages: str) -> None:
        """Generic profile formatter shared by two or more RACF profile formats."""
        profile = {}
        current_segment = "base"
        (
            additional_segment_keys,
            no_segment_information_keys,
        ) = self.__build_additional_segment_keys()
        profile[current_segment] = {}
        i = 0
        while i < len(messages):
            if (
                messages[i] == " "
                or messages[i] in no_segment_information_keys
                or messages[i] is None
            ):
                i += 1
                continue
            if i < len(messages) - 1 and messages[i] in additional_segment_keys:
                current_segment = messages[i].split()[0].lower()
                profile[current_segment] = {}
                i += 2
            if self._profile_type in ("dataSet", "resource"):
                i = self.__format_data_set_generic_profile_data(
                    messages, profile, current_segment, i
                )
            if self._profile_type == "user":
                i = self.__format_user_profile_data(
                    messages, profile, current_segment, i
                )
            if self._profile_type == "group":
                i = self.__format_group_profile_data(
                    messages, profile, current_segment, i
                )
            i += 1
        return profile

    def __format_data_set_generic_profile_data(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> int:
        """Specialized logic for formatting DataSet/General Resource profile data."""
        list_fields = ["volumes"]
        messages[i] = (
            messages[i]
            .replace("DATASET", "DATA SET")
            .replace("VOLUMES ON WHICH DATA SET RESIDES", "VOLUMES")
            .replace(" IS ", " = ")
        )
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
            i += 2
        elif (
            i < len(messages) - 2
            and messages[i + 1] is not None
            and ("-" in messages[i + 1])
        ):
            self.__format_tabular_data(
                messages, profile, current_segment, i, list_fields
            )
            i += 1
        elif "NO INSTALLATION DATA" in messages[i]:
            profile[current_segment]["installationData"] = None
        elif "UNLOCKED" in messages[i]:
            profile[current_segment]["locked"] = False
        elif "LOCKED" in messages[i]:
            profile[current_segment]["locked"] = True
        if "INFORMATION FOR DATA SET" in messages[i]:
            profile[current_segment]["name"] = (
                messages[i].split("INFORMATION FOR DATA SET ")[1].lower()
            )
        return i

    def __format_user_profile_data(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> int:
        """Specialized logic for formatting user profile data."""
        if messages[i][:1] == " ":
            messages[i] = (
                messages[i]
                .replace("PASSDATE=", "PASSWORD-DATE=")
                .replace("PASS-INTERVAL=", "PASSWORD-INTERVAL=")
                .replace("PHRASEDATE=", "PASSPHRASE-DATE=")
            )
        if (
            i < len(messages) - 1
            and messages[i + 1] == " ---------------------------------------------"
        ):
            semi_tabular_data = messages[i : i + 3]
            self.__add_semi_tabular_data_to_segment(
                current_segment, profile[current_segment], semi_tabular_data
            )
            i += 2
        elif messages[i][:8] == "  GROUP=":
            if "groups" not in profile[current_segment]:
                profile[current_segment]["groups"] = {}
            group = messages[i].split("=")[1].split()[0]
            profile[current_segment]["groups"][group] = {}
            message = messages[i] + messages[i + 1] + messages[i + 2] + messages[i + 3]
            self.__add_key_value_pairs_to_segment(
                current_segment, profile[current_segment]["groups"][group], message[17:]
            )
            i += 3
        elif "=" not in messages[i] and messages[i].strip()[:3] != "NO-":
            messages[i] = f"{messages[i]}={messages[i + 1]}"
            self.__add_key_value_pairs_to_segment(
                current_segment, profile[current_segment], messages[i]
            )
            i += 1
        else:
            self.__add_key_value_pairs_to_segment(
                current_segment, profile[current_segment], messages[i]
            )
        return i

    def __format_group_profile_data(
        self, messages: List[str], profile: dict, current_segment: str, i: int
    ) -> int:
        """Specialized logic for formatting user profile data."""
        list_fields = ["users", "subgroups"]
        if "users" in profile[current_segment].keys() and i < len(messages) - 2:
            self.__format_user_list_data(messages, profile, current_segment, i)
            i += 2
        elif (
            "USER(S)=      ACCESS=      ACCESS COUNT=      UNIVERSAL ACCESS="
            in messages[i]
        ):
            profile[current_segment]["users"] = []
        elif "=" in messages[i]:
            self.__add_key_value_pairs_to_segment(
                current_segment, profile[current_segment], messages[i]
            )
        elif "NO " in messages[i]:
            field_name = self._profile_field_to_camel_case(
                current_segment, messages[i].split("NO ")[1].strip().lower()
            )
            if field_name in list_fields:
                profile[current_segment][field_name] = []
            else:
                profile[current_segment][field_name] = None
        elif "TERMUACC" in messages[i]:
            if "NO" in messages[i]:
                profile[current_segment]["terminalUniversalAccess"] = False
            else:
                profile[current_segment]["terminalUniversalAccess"] = True
        elif "INFORMATION FOR GROUP" in messages[i]:
            profile[current_segment]["name"] = (
                messages[i].split("INFORMATION FOR GROUP ")[1].lower()
            )
        return i

    def __format_user_list_data(
        self, messages: list, profile: dict, current_segment: str, i: int
    ) -> None:
        profile[current_segment]["users"].append({})
        user_index = len(profile[current_segment]["users"]) - 1
        user_fields = [
            field.strip() for field in messages[i].split(" ") if field.strip()
        ]

        profile[current_segment]["users"][user_index]["userid"] = self._cast_from_str(
            user_fields[0]
        )
        profile[current_segment]["users"][user_index]["access"] = self._cast_from_str(
            user_fields[1]
        )
        profile[current_segment]["users"][user_index]["accessCount"] = (
            self._cast_from_str(user_fields[2])
        )
        profile[current_segment]["users"][user_index]["universalAccess"] = (
            self._cast_from_str(user_fields[3])
        )

        self.__add_key_value_pairs_to_segment(
            current_segment,
            profile[current_segment]["users"][user_index],
            messages[i + 1],
        )

        self.__add_key_value_pairs_to_segment(
            current_segment,
            profile[current_segment]["users"][user_index],
            messages[i + 2],
        )

    def __build_additional_segment_keys(self) -> Tuple[str, str]:
        """Build keys for detecting additional segments in RACF profile data."""
        additional_segment_keys = [
            f"{segment.upper()} INFORMATION"
            for segment in self._valid_segment_traits
            if segment != "base"
        ]
        no_segment_information_keys = [
            f"NO {segment}" for segment in additional_segment_keys
        ]
        return (additional_segment_keys, no_segment_information_keys)

    def __add_semi_tabular_data_to_segment(
        self, segment_name: str, segment: dict, semi_tabular_data: List[str]
    ) -> None:
        """Add semi-tabular data as key-value pairs to segment dictionary."""
        heading_tokens = list(filter(("").__ne__, semi_tabular_data[0].split("  ")))
        key_prefix = heading_tokens[0]
        keys = [f"{key_prefix} {key.strip()[1:-1]}" for key in heading_tokens[1:]]
        values = semi_tabular_data[-1].split()
        keys_length = len(keys)
        for i in range(keys_length):
            key = self._profile_field_to_camel_case(
                segment_name, keys[i].strip().lower()
            )
            segment[key] = self._cast_from_str(values[i])

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
        indexes_length = len(indexes)
        for j in range(indexes_length):
            if j < indexes_length - 1:
                ind_e0 = indexes[j + 1] - 1
                ind_e1 = indexes[j + 1] - 1
            else:
                ind_e0 = len(messages[i])
                ind_e1 = len(messages[i + 2])

            field = self._profile_field_to_camel_case(
                current_segment, messages[i][indexes[j] : ind_e0].strip().lower()
            )
            profile[current_segment][field] = self._clean_and_separate(
                messages[i + 2][indexes[j] : ind_e1]
            )

    def __format_tabular_data(
        self,
        messages: List[str],
        profile: dict,
        current_segment: str,
        i: int,
        list_fields: List[str] = ["volumes"],
    ) -> None:
        field = " ".join(
            [txt.lower().strip() for txt in list(filter(None, messages[i].split(" ")))]
        )
        field = self._profile_field_to_camel_case(current_segment, field)
        values = (
            [messages[i + 2]]
            if "," not in messages[i + 2]
            else messages[i + 2].split(",")
        )
        for value in values:
            if "(" in value:
                value_tokens = value.split("(")
                subfield = self._profile_field_to_camel_case(
                    current_segment, value_tokens[0].lower()
                )
                if field not in profile[current_segment]:
                    profile[current_segment][field] = {
                        subfield: self._clean_and_separate(value_tokens[-1].rstrip(")"))
                    }
                else:
                    profile[current_segment][field][subfield] = (
                        self._clean_and_separate(value_tokens[-1].rstrip(")"))
                    )
            elif field in list_fields:
                profile[current_segment][field] = []
                profile[current_segment][field].append(self._clean_and_separate(value))
            else:
                profile[current_segment][field] = self._clean_and_separate(value)
        return

    def __add_key_value_pairs_to_segment(
        self,
        segment_name: str,
        segment: dict,
        message: str,
    ) -> None:
        """Add a key value pair to a segment dictionary."""
        list_fields = ["attributes", "classAuthorizations", "connectAttributes"]
        tokens = message.strip().split("=")
        key = tokens[0]
        for i in range(1, len(tokens)):
            sub_tokens = list(filter(("").__ne__, tokens[i].split("  ")))
            if not sub_tokens:
                value = "NONE"
            else:
                value = sub_tokens[0].strip()
            if key[:3] == "NO-":
                key = key[3:]
                value = "N/A"
            current_key = self._profile_field_to_camel_case(segment_name, key.lower())
            if current_key in list_fields:
                if current_key not in segment:
                    segment[current_key] = []
                values = [
                    str(self._cast_from_str(value))
                    for value in value.split()
                    if value != "NONE"
                ]
                segment[current_key] += values
            else:
                case_sensitive = False
                if current_key in self._case_sensitive_extracted_values:
                    case_sensitive = True
                segment[current_key] = self._cast_from_str(
                    value, case_sensitive=case_sensitive
                )
            key = "".join(sub_tokens[1:])
            if len(sub_tokens) == 1:
                if i < len(tokens) - 1 and " " in sub_tokens[0] and i != 0:
                    sub_tokens = sub_tokens[0].split()
                    segment[current_key] = self._cast_from_str(sub_tokens[0])
                    key = sub_tokens[-1]
                else:
                    key = sub_tokens[0]

    def __add_key_value_pair_to_profile(
        self, message: str, profile: dict, current_segment: str
    ) -> None:
        """Generic function for extracting key-value pair from RACF profile data."""
        field = self._profile_field_to_camel_case(
            current_segment, message.split("=")[0].strip().lower()
        )
        profile[current_segment][field] = self._clean_and_separate(
            message.split("=")[1]
        )

    def _clean_and_separate(self, value: str) -> Union[list, str]:
        """Clean cast and separate comma and space delimited data."""
        cln_val = value.strip().lower()
        if "," in cln_val:
            out = [self._cast_from_str(val.strip()) for val in cln_val.split(",")]
        elif " " in cln_val:
            out = [self._cast_from_str(val.strip()) for val in cln_val.split(" ")]
        else:
            out = self._cast_from_str(cln_val)
        if isinstance(out, list):
            if None in out:
                return None
            if "days" in out:
                del out[out.index("days")]
                if len(out) == 1:
                    return out[0]
            open_ind = []
            close_ind = []
            cln_ind = []
            for i, val in enumerate(out):
                val = str(val)
                if "(" in val and ")" not in val:
                    open_ind.append(i)
                if ")" in val and "(" not in val:
                    close_ind.append(i)
            if not open_ind and not close_ind:
                return out
            for i, ind in enumerate(open_ind):
                out[ind] = " ".join(out[ind : (close_ind[i] + 1)])
                cln_ind = cln_ind + [*range(ind, close_ind[i] + 1)][1:]
            cln_ind.reverse()
            for i in cln_ind:
                del out[i]

        return out

    def _cast_from_str(
        self,
        value: str,
        case_sensitive: bool = False,
    ) -> Union[None, bool, int, float, str]:
        """Cast null values floats and integers."""
        if not case_sensitive:
            value = value.lower()
        if value in (
            "n/a",
            "none",
            "none specified",
            "no",
            "None",
            "unknown",
            "unlimited",
            "",
        ):
            return None
        if value in (
            "in effect",
            "active",
            "active.",
            "being done.",
            "in effect.",
            "allowed.",
            "being done",
            "true",
        ):
            return True
        if value in (
            "not in effect",
            "inactive",
            "not allowed.",
            "not being done",
            "false",
        ):
            return False
        if "days" in value and any(chr.isdigit() for chr in value):
            digits = "".join([chr for chr in value if chr.isdigit()])
            return int(digits)
        if "in effect for the " in value and " function." in value:
            return value.split("in effect for the ")[1].split(" function.")[0]
        return self.__cast_num(value)

    def __cast_num(self, value: str) -> Union[int, float, str]:
        value = value.strip()
        if "." in value or "," in value:
            try:
                # Convert Julian timestamps to standard date format.
                t = "-"
                if platform.system() == "Windows":
                    # Allows unit tests to be run on Windows.
                    t = "#"
                build_standard_date = f"%{t}m/%{t}d/%Y"
                build_standard_date_with_time = f"%{t}m/%{t}d/%Y %{t}I:%M %p"
                julian_regex = r"\d\d.\d\d\d$"
                julian_with_time_regex = r"\d\d.\d\d\d/\d\d:\d\d:\d\d$"
                expanded_non_julian_date_regex = r"[a-z]* (\d\d|\d), \d\d\d\d$"
                if re.match(julian_regex, value):
                    read_julian_date = "%y.%j"
                    date = datetime.strptime(value, read_julian_date)
                    return date.strftime(build_standard_date)
                elif re.match(julian_with_time_regex, value):
                    read_julian_date_with_time = "%y.%j/%H:%M:%S"
                    date = datetime.strptime(value, read_julian_date_with_time)
                    return date.strftime(build_standard_date_with_time)
                elif re.match(expanded_non_julian_date_regex, value):
                    read_expanded_non_julian_date = "%B %d, %Y"
                    date = datetime.strptime(value, read_expanded_non_julian_date)
                    return date.strftime(build_standard_date)
            except ValueError:
                return None
            try:
                return float(value)
            except ValueError:
                return value
        try:
            return int(value.replace(",", ""))
        except ValueError:
            return value

    def _profile_field_to_camel_case(self, segment: str, field: str) -> str:
        """Convert a space delimited profile field to camel case."""
        if segment in self._extracted_key_value_pair_segment_traits_map:
            if field in self._extracted_key_value_pair_segment_traits_map[segment]:
                return self._extracted_key_value_pair_segment_traits_map[segment][field]
        field_tokens = field.replace("-", " ").replace(",", "").split()
        return field_tokens[0] + "".join(
            [field_token.title() for field_token in field_tokens[1:]]
        )
