"""General Resource Profile Administration."""

from collections import Counter
from typing import List, Union

from pyracf.common.exceptions.add_operation_error import AddOperationError
from pyracf.common.exceptions.alter_operation_error import AlterOperationError
from pyracf.common.exceptions.security_request_error import SecurityRequestError
from pyracf.common.security_admin import SecurityAdmin

from .resource_request import ResourceRequest


class ResourceAdmin(SecurityAdmin):
    """General Resaurce Profile Administration."""

    def __init__(
        self,
        irrsmo00_result_buffer_size: Union[int, None] = None,
        debug: bool = False,
        dump_mode: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
        run_as_userid: Union[str, None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:application_data": "racf:appldata",
                "base:audit_alter": "racf:audaltr",
                "base:audit_control": "racf:audcntl",
                "base:audit_none": "racf:audnone",
                "base:audit_read": "racf:audread",
                "base:audit_update": "racf:audupdt",
                "base:security_categories": "racf:category",
                "base:installation_data": "racf:data",
                "base:model_profile_class": "racf:fclass",
                "base:model_profile_generic": "racf:fgeneric",
                "base:model_profile": "racf:fprofile",
                "base:model_profile_volume": "racf:fvolume",
                "base:global_audit_alter": "racf:gaudaltr",
                "base:global_audit_control": "racf:gaudcntl",
                "base:global_audit_none": "racf:gaudnone",
                "base:global_audit_read": "racf:gaudread",
                "base:global_audit_update": "racf:gaudupdt",
                "base:level": "racf:level",
                "base:member": "racf:member",
                "base:notify_userid": "racf:notify",
                "base:owner": "racf:owner",
                "base:security_label": "racf:seclabel",
                "base:security_level": "racf:seclevel",
                "base:single_data_set_tape_volume": "racf:singldsn",
                "base:time_zone": "racf:timezone",
                "base:tape_vtoc": "racf:tvtoc",
                "base:universal_access": "racf:uacc",
                "base:volumes": "racf:volume",
                "base:warn_on_insufficient_access": "racf:warning",
                "base:terminal_access_allowed_days": "racf:whendays",
                "base:terminal_access_allowed_time": "racf:whentime",
            },
            "cdtinfo": {
                "cdtinfo:case_allowed": "case",
                "cdtinfo:default_racroute_return_code": "defaultrc",
                "cdtinfo:valid_first_characters": "first",
                "cdtinfo:generic_profile_checking": "generic",
                "cdtinfo:generic_profile_sharing": "genlist",
                "cdtinfo:grouping_class_name": "grouping",
                "cdtinfo:key_qualifiers": "keyqual",
                "cdtinfo:manditory_access_control_processing": "macprocessing",
                "cdtinfo:max_length": "maxlenx",
                "cdtinfo:max_length_entityx": "maxlength",
                "cdtinfo:member_class_name": "member",
                "cdtinfo:operations": "operations",
                "cdtinfo:valid_other_characters": "other",
                "cdtinfo:posit_number": "posit",
                "cdtinfo:profiles_allowed": "profilesallowed",
                "cdtinfo:raclist_allowed": "raclist",
                "cdtinfo:send_enf_signal_on_profile_creation": "signal",
                "cdtinfo:security_label_required": "seclabelrequired",
                "cdtinfo:default_universal_access": "defaultuacc",
            },
            "cfdef": {
                "cfdef:custom_field_data_type": "type",
                "cfdef:valid_first_characters": "first",
                "cfdef:help_text": "help",
                "cfdef:list_heading_text": "listhead",
                "cfdef:mixed_case_allowed": "mixed",
                "cfdef:min_numeric_value": "minvalue",
                "cfdef:max_field_length": "mxlength",
                "cfdef:max_numeric_value": "maxvalue",
                "cfdef:valid_other_characters": "other",
                "cfdef:validation_rexx_exec": "racf:cfvalrx",
            },
            "dlfdata": {
                "dlfdata:job_names": "racf:jobname",
                "dlfdata:retain": "racf:retain",
            },
            "eim": {
                "eim:domain_distinguished_name": "domaindn",
                "eim:kerberos_registry": "kerberg",
                "eim:local_registry": "localreg",
                "eim:options": "options",
                "eim:x509_registry": "X509reg",
            },
            "kerb": {
                "kerb:validate_addresses": "checkaddrs",
                "kerb:default_ticket_life": "deftktlife",
                "kerb:encryption_algorithms": "encrypt",
                "kerb:realm_name": "kerbname",
                "kerb:max_ticket_life": "maxtktlf",
                "kerb:min_ticket_life": "mintklife",
                "kerb:password": "password",
            },
            "icsf": {
                "icsf:symmetric_export_certificates": "symexportcert",
                "icsf:exportable_public_keys": "symexportable",
                "icsf:symmetric_export_public_keys": "symexportkey",
                "icsf:symmetric_cpacf_rewrap": "symcpacfwrap",
                "icsf:symmetric_cpacf_rewrap_return": "symcpacfret",
                "icsf:asymetric_key_usage": "asymusage",
            },
            "ictx": {
                "ictx:use_identity_map": "domap",
                "ictx:require_identity_mapping": "mapreq",
                "ictx:identity_map_timeout": "maptimeo",
                "ictx:cache_application_provided_identity_map": "usemap",
            },
            "idtparms": {
                "idtparms:token": "sigtoken",
                "idtparms:sequence_number": "sigseqnum",
                "idtparms:category": "sigcat",
                "idtparms:signature_algorithm": "sigalg",
                "idtparms:identity_token_timeout": "idttimeout",
                "idtparms:use_for_any_application": "anyappl",
            },
            "jes": {"jes:key_label": "racf:keylabel"},
            "mfpolicy": {
                "mfpolicy:factors": "racf:factors",
                "mfpolicy:token_timeout": "racf:timeout",
                "mfpolicy:reuse_token": "racf:reuse",
            },
            "proxy": {
                "proxy:bind_distinguished_name": "binddn",
                "proxy:bind_password": "bindpw",
                "proxy:ldap_host": "ldaphost",
            },
            "session": {
                "session:security_checking_level": "racf:convsec",
                "session:session_key_interval": "racf:interval",
                "session:locked": "racf:lock",
                "session:session_key": "racf:sesskey",
            },
            "sigver": {
                "sigver:fail_program_load_condition": "failload",
                "sigver:log_signature_verification_events": "sigaudit",
                "sigver:signature_required": "sigrequired",
            },
            "ssignon": {
                "ssignon:encrypt_legacy_pass_ticket_key": "racf:keycrypt",
                "ssignon:enhanced_pass_ticket_label": "ptkeylab",
                "ssignon:enhanced_pass_ticket_type": "pttype",
                "ssignon:enhanced_pass_ticket_timeout": "pttimeo",
                "ssignon:enhanced_pass_ticket_replay": "ptreplay",
                "ssignon:legacy_pass_ticket_label": "racf:keylabel",
                "ssignon:mask_legacy_pass_ticket_key": "racf:keymask",
            },
            "stdata": {
                "stdata:group": "racf:group",
                "stdata:privileged": "racf:privlege",
                "stdata:trace": "racf:trace",
                "stdata:trusted": "racf:trusted",
                "stdata:user": "racf:user",
            },
            "svfmr": {
                "svfmr:parameter_list_name": "racf:parmname",
                "svfmr:script_name": "racf:script",
            },
            "tme": {
                "tme:children": "racf:children",
                "tme:groups": "racf:groups",
                "tme:parent": "racf:parent",
                "tme:resource": "racf:resource",
                "tme:roles": "racf:roles",
            },
        }
        self._extracted_key_value_pair_segment_traits_map = {
            "cdtinfo": {
                "case": "caseAllowed",
                "defaultrc": "defaultRacrouteReturnCode",
                "first": "validFirstCharacters",
                "generic": "genericProfileChecking",
                "genlist": "genericProfileSharing",
                "group": "groupingClassName",
                "keyqualifiers": "keyQualifiers",
                "macprocessing": "manditoryAccessControlProcessing",
                "maxlenx": "maxLength",
                "maxlength": "maxLengthEntityx",
                "member": "memberClassName",
                "operations": "operations",
                "other": "validOtherCharacters",
                "posit": "positNumber",
                "profilesallowed": "profilesAllowed",
                "raclist": "raclistAllowed",
                "signal": "sendEnfSignalOnProfileCreation",
                "seclabelsrequired": "securityLabelsRequired",
                "defaultuacc": "defaultUniversalAccess",
            },
            "cfdef": {
                "type": "customFieldDataType",
                "first": "validFirstCharacters",
                "help": "helpText",
                "listhead": "listHeadingText",
                "mixed": "mixedCaseAllowed",
                "minvalue": "minNumericValue",
                "mxlength": "maxFieldLength",
                "maxvalue": "maxNumericValue",
                "other": "validOtherCharacters",
                "cfvalrx": "validationRexxExec",
            },
            "kerb": {
                "checkaddrs": "validateAddresses",
                "deftktlife": "defaultTicketLife",
                "encrypt": "encryptionAlgorithms",
                "kerbname": "realmName",
                "maxtktlf": "maxTicketLife",
                "mintklife": "minTicketLife",
            },
            "session": {
                "convsec": "securityCheckingLevel",
                "interval": "sessionKeyInterval",
                "lock": "locked",
                "sesskey": "sessionKey",
            },
            "sigver": {
                "failload": "failProgramLoadCondition",
                "sigaudit": "logSignatureVerificationEvents",
                "sigrequired": "signatureRequired",
            },
        }
        super().__init__(
            "resource",
            irrsmo00_result_buffer_size=irrsmo00_result_buffer_size,
            debug=debug,
            dump_mode=dump_mode,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            replace_existing_segment_traits=replace_existing_segment_traits,
            additional_secret_traits=additional_secret_traits,
            run_as_userid=run_as_userid,
        )

    # ============================================================================
    # Universal Access
    # ============================================================================
    def get_universal_access(
        self, resource: str, class_name: str
    ) -> Union[str, bytes, None]:
        """Get the universal access for general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "universalAccess")

    def set_universal_access(
        self,
        resource: str,
        class_name: str,
        universal_access: str,
    ) -> Union[dict, bytes]:
        """Set the universal access for a general resource profile."""
        result = self.alter(
            resource, class_name, {"base:universal_access": universal_access}
        )
        return self._to_steps(result)

    # ============================================================================
    # Individual Access
    # ============================================================================
    def get_my_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
        """Get your own level of access associated with a general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "yourAccess")

    def get_user_access(
        self, resource: str, class_name: str, userid: str
    ) -> Union[str, bytes, None]:
        """Get a target user's own level of access associated with a general resource profile."""
        original_userid = self.get_running_userid()
        self.set_running_userid(userid)
        profile = self.extract(resource, class_name, profile_only=True)
        self.set_running_userid(original_userid)
        return self._get_field(profile, "base", "yourAccess")

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    def get_audit_rules(
        self, resource: str, class_name: str
    ) -> Union[dict, bytes, None]:
        """Get the auditing rules associated with this general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "auditing")

    def overwrite_audit_rules_by_attempt(
        self,
        resource: str,
        class_name: str,
        success: Union[str, None] = None,
        failure: Union[str, None] = None,
        all: Union[str, None] = None,
    ) -> Union[dict, bytes]:
        """
        Overwrites the auditing rules for this general resource profile with new
        rules to audit based on specified access attempts.
        """
        self.__validate_access_levels(success, failure, all)
        traits = {}
        if success is not None:
            traits[f"base:audit_{success}"] = "success"
        if failure is not None:
            traits[f"base:audit_{failure}"] = "failure"
        if all is not None:
            traits[f"base:audit_{all}"] = "all"
        result = self.alter(resource, class_name, traits=traits)
        return self._to_steps(result)

    def alter_audit_rules_by_attempt(
        self,
        resource: str,
        class_name: str,
        success: Union[str, None] = None,
        failure: Union[str, None] = None,
        all: Union[str, None] = None,
    ) -> Union[dict, bytes]:
        """
        Alters the auditing rules for this general resource profile with new rules
        to audit by access level, preserving existing non-conflicting rules.
        """
        self.__validate_access_levels(success, failure, all)
        audit_rules = self.get_audit_rules(resource, class_name)
        traits = {}
        if "success" in audit_rules:
            traits[f"base:audit_{audit_rules['success']}"] = "success"
        if "failures" in audit_rules:
            traits[f"base:audit_{audit_rules['failures']}"] = "failure"
        if "all" in audit_rules:
            traits[f"base:audit_{audit_rules['all']}"] = "all"
        if success is not None:
            traits[f"base:audit_{success}"] = "success"
        if failure is not None:
            traits[f"base:audit_{failure}"] = "failure"
        if all is not None:
            traits[f"base:audit_{all}"] = "all"
        result = self.alter(resource, class_name, traits=traits)
        return self._to_steps(result)

    def overwrite_audit_rules_by_access_level(
        self,
        resource: str,
        class_name: str,
        alter: Union[str, None] = None,
        control: Union[str, None] = None,
        read: Union[str, None] = None,
        update: Union[str, None] = None,
    ) -> Union[dict, bytes]:
        """
        Overwrites the auditing rules for this general resource profile with new
        rules to audit based on specified access levels.
        """
        traits = {}
        if alter is not None:
            traits["base:audit_alter"] = alter
        if control is not None:
            traits["base:audit_control"] = control
        if read is not None:
            traits["base:audit_read"] = read
        if update is not None:
            traits["base:audit_update"] = update
        result = self.alter(resource, class_name, traits=traits)
        return self._to_steps(result)

    def alter_audit_rules_by_access_level(
        self,
        resource: str,
        class_name: str,
        alter: Union[str, None] = None,
        control: Union[str, None] = None,
        read: Union[str, None] = None,
        update: Union[str, None] = None,
    ) -> Union[dict, bytes]:
        """
        Alters the auditing rules for this general resource profile with a new
        rule to audit alter access, preserving existing non-conflicting rules.
        """
        audit_rules = self.get_audit_rules(resource, class_name)
        traits = {}
        if "success" in audit_rules:
            traits[f"base:audit_{audit_rules['success']}"] = "success"
        if "failures" in audit_rules:
            traits[f"base:audit_{audit_rules['failures']}"] = "failure"
        if "all" in audit_rules:
            traits[f"base:audit_{audit_rules['all']}"] = "all"
        if alter is not None:
            traits["base:audit_alter"] = alter
        if control is not None:
            traits["base:audit_control"] = control
        if read is not None:
            traits["base:audit_read"] = read
        if update is not None:
            traits["base:audit_update"] = update
        result = self.alter(resource, class_name, traits=traits)
        return self._to_steps(result)

    def remove_all_audit_rules(
        self, resource: str, class_name: str
    ) -> Union[dict, bytes]:
        """Clears the auditing rules completely."""
        result = self.alter(resource, class_name, {"base:audit_none": True})
        return self._to_steps(result)

    # ============================================================================
    # Class Administration
    # ============================================================================
    def add_resource_class(
        self, class_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new general resource class."""
        return self.add(resource=class_name, class_name="CDT", traits=traits)

    def alter_resource_class(
        self, class_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing general resource class."""
        return self.alter(resource=class_name, class_name="CDT", traits=traits)

    def extract_resource_class(self, class_name: str) -> Union[dict, bytes]:
        """Extract the attributes of a general resource class."""
        profile = self.extract(
            resource=class_name,
            class_name="CDT",
            segments=["cdtinfo"],
            profile_only=True,
        )
        return profile["cdtinfo"]

    def delete_resource_class(self, class_name: str) -> Union[dict, bytes]:
        """Delete a general resource class."""
        return self.delete(resource=class_name, class_name="CDT")

    # ============================================================================
    # Started Task Administration
    # ============================================================================
    def add_started_task(
        self, started_task_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new started task profile."""
        return self.add(resource=started_task_name, class_name="STARTED", traits=traits)

    def alter_started_task(
        self, started_task_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing started task profile."""
        return self.alter(
            resource=started_task_name, class_name="STARTED", traits=traits
        )

    def extract_started_task(self, started_task_name: str) -> Union[dict, bytes]:
        """Extract the attributes of a started task profile."""
        profile = self.extract(
            resource=started_task_name,
            class_name="STARTED",
            segments=["stdata"],
            profile_only=True,
        )
        return profile["stdata"]

    def delete_started_task(self, started_task_name: str) -> Union[dict, bytes]:
        """Delete a started task profile."""
        return self.delete(resource=started_task_name, class_name="STARTED")

    # ============================================================================
    # Custom Field Administration
    # ============================================================================
    def add_custom_field(
        self, custom_field_name: str, custom_field_type: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new custom field."""
        full_profile_name = f"{custom_field_type}.csdata.{custom_field_name}"
        return self.add(resource=full_profile_name, class_name="CFIELD", traits=traits)

    def alter_custom_field(
        self, custom_field_name: str, custom_field_type: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing custom field."""
        full_profile_name = f"{custom_field_type}.csdata.{custom_field_name}"
        return self.alter(
            resource=full_profile_name, class_name="CFIELD", traits=traits
        )

    def extract_custom_field(
        self, custom_field_name: str, custom_field_type: str
    ) -> Union[dict, bytes]:
        """Extract the attributes of a custom field."""
        full_profile_name = f"{custom_field_type}.csdata.{custom_field_name}"
        profile = self.extract(
            resource=full_profile_name,
            class_name="CFIELD",
            segments=["cfdef"],
            profile_only=True,
        )
        return profile["cfdef"]

    def delete_custom_field(
        self, custom_field_name: str, custom_field_type: str
    ) -> Union[dict, bytes]:
        """Delete a custom field."""
        full_profile_name = f"{custom_field_type}.csdata.{custom_field_name}"
        return self.delete(resource=full_profile_name, class_name="CFIELD")

    # ============================================================================
    # Kerberos Realm Administration
    # ============================================================================
    def add_kerberos_realm(
        self, kerberos_realm_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new kerberos realm profile."""
        return self.add(resource=kerberos_realm_name, class_name="REALM", traits=traits)

    def alter_kerberos_realm(
        self, kerberos_realm_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing kerberos realm profile."""
        return self.alter(
            resource=kerberos_realm_name, class_name="REALM", traits=traits
        )

    def extract_kerberos_realm(self, kerberos_realm_name: str) -> Union[dict, bytes]:
        """Extract the attributes of a kerberos realm profile."""
        profile = self.extract(
            resource=kerberos_realm_name,
            class_name="REALM",
            segments=["kerb"],
            profile_only=True,
        )
        return profile["kerb"]

    def delete_kerberos_realm(self, kerberos_realm_name: str) -> Union[dict, bytes]:
        """Delete a kerberos realm profile."""
        return self.delete(resource=kerberos_realm_name, class_name="REALM")

    # ============================================================================
    # Signed Program Administration
    # ============================================================================
    def add_signed_program(
        self, signed_program_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new signed program profile."""
        if "sigver:library" in traits:
            traits["base:member"] = traits["sigver:library"]
            del traits["sigver:library"]
        return self.add(
            resource=signed_program_name, class_name="PROGRAM", traits=traits
        )

    def alter_signed_program(
        self, signed_program_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing signed program profile."""
        if "sigver:library" in traits:
            traits["base:member"] = traits["sigver:library"]
            del traits["sigver:library"]
        return self.alter(
            resource=signed_program_name, class_name="PROGRAM", traits=traits
        )

    def extract_signed_program(self, signed_program_name: str) -> Union[dict, bytes]:
        """Extract the attributes of a signed program profile."""
        profile = self.extract(
            resource=signed_program_name,
            class_name="PROGRAM",
            segments=["sigver"],
            profile_only=True,
        )
        profile["sigver"]["library"] = profile["base"].get("member")
        return profile["sigver"]

    def delete_signed_program(self, signed_program_name: str) -> Union[dict, bytes]:
        """Delete a signed program profile."""
        return self.delete(resource=signed_program_name, class_name="PROGRAM")

    # ============================================================================
    # APPC Session Administration
    # ============================================================================
    def add_appc_session(
        self, net_id: str, local_lu: str, partner_lu: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new APPC session profile."""
        full_profile_name = f"{net_id}.{local_lu}.{partner_lu}"
        return self.add(resource=full_profile_name, class_name="APPCLU", traits=traits)

    def alter_appc_session(
        self, net_id: str, local_lu: str, partner_lu: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Alter an existing APPC session profile."""
        full_profile_name = f"{net_id}.{local_lu}.{partner_lu}"
        return self.alter(
            resource=full_profile_name, class_name="APPCLU", traits=traits
        )

    def extract_appc_session(
        self, net_id: str, local_lu: str, partner_lu: str
    ) -> Union[dict, bytes]:
        """Extract the attributes of a APPC session profile."""
        full_profile_name = f"{net_id}.{local_lu}.{partner_lu}"
        profile = self.extract(
            resource=full_profile_name,
            class_name="APPCLU",
            segments=["session"],
            profile_only=True,
        )
        return profile["session"]

    def delete_appc_session(
        self, net_id: str, local_lu: str, partner_lu: str
    ) -> Union[dict, bytes]:
        """Delete a APPC session."""
        full_profile_name = f"{net_id}.{local_lu}.{partner_lu}"
        return self.delete(resource=full_profile_name, class_name="APPCLU")

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(
        self, resource: str, class_name: str, traits: dict = {}
    ) -> Union[dict, bytes]:
        """Create a new general resource profile."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            profile_request = ResourceRequest(resource, class_name, "set")
            self._build_xml_segments(profile_request)
            return self._make_request(profile_request)
        try:
            profile = self.extract(resource, class_name, profile_only=True)
            if self._get_field(profile, "base", "name") == resource.lower():
                raise AddOperationError(resource, class_name)
        except SecurityRequestError as exception:
            if not exception.contains_error_message(self._profile_type, "ICH13003I"):
                raise exception
        self._build_segment_trait_dictionary(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self._build_xml_segments(profile_request)
        return self._make_request(profile_request)

    def alter(self, resource: str, class_name: str, traits: dict) -> Union[dict, bytes]:
        """Alter an existing general resource profile."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            profile_request = ResourceRequest(resource, class_name, "set")
            self._build_xml_segments(profile_request, alter=True)
            return self._make_request(profile_request, irrsmo00_precheck=True)
        try:
            profile = self.extract(resource, class_name, profile_only=True)
        except SecurityRequestError as exception:
            raise AlterOperationError(resource, class_name) from exception
        if not self._get_field(profile, "base", "name") == resource.lower():
            raise AlterOperationError(resource, class_name)
        self._build_segment_trait_dictionary(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self._build_xml_segments(profile_request, alter=True)
        return self._make_request(profile_request, irrsmo00_precheck=True)

    def extract(
        self,
        resource: str,
        class_name: str,
        segments: List[str] = [],
        profile_only: bool = False,
    ) -> Union[dict, bytes]:
        """Extract a general resource profile."""
        self._build_segment_dictionary(segments)
        resource_request = ResourceRequest(resource, class_name, "listdata")
        self._build_xml_segments(resource_request, extract=True)
        result = self._extract_and_check_result(resource_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(self, resource: str, class_name: str) -> Union[dict, bytes]:
        """Delete a general resource profile."""
        profile_request = ResourceRequest(resource, class_name, "del")
        return self._make_request(profile_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["resource"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "CLASS      NAME" in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            # Post processing
            if "(g)" in profile["base"].get("name"):
                profile["base"]["generic"] = True
                profile["base"]["name"] = self._cast_from_str(
                    profile["base"].get("name")[0]
                )
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityResult"]["resource"]["commands"][0]["messages"]
        result["securityResult"]["resource"]["commands"][0]["profiles"] = profiles

    def __validate_access_levels(
        self,
        success: Union[str, None] = None,
        failure: Union[str, None] = None,
        all: Union[str, None] = None,
    ):
        valid_access_levels = ("alter", "control", "read", "update")
        value_error_text = (
            "Valid access levels include 'alter', 'control', 'read', and 'update'."
        )
        bad_access_levels = []
        for attempt_argument in (success, failure, all):
            if (
                attempt_argument is not None
                and str(attempt_argument).lower() not in valid_access_levels
            ):
                bad_access_levels.append(attempt_argument)
        match len(bad_access_levels):
            case 0:
                self.__check_for_duplicates([success, failure, all], "Access Level")
                return
            case 1:
                value_error_text = (
                    f"'{bad_access_levels[0]}' is not a valid access level. "
                    + f"{value_error_text}"
                )
            case 2:
                value_error_text = (
                    f"'{bad_access_levels[0]}' and '{bad_access_levels[1]}' are not valid "
                    + f"access levels. {value_error_text}"
                )
            case _:
                bad_access_levels = [
                    f"'{bad_access_level}'" for bad_access_level in bad_access_levels
                ]
                bad_access_levels[-1] = f"and {bad_access_levels[-1]} "
                value_error_text = (
                    f"{', '.join(bad_access_levels)}are not valid access levels. "
                    + f"{value_error_text}"
                )
        raise ValueError(value_error_text)

    def __check_for_duplicates(self, argument_list: list, argument: str) -> None:
        duplicates = [
            key
            for (key, value) in Counter(argument_list).items()
            if (value > 1 and key is not None)
        ]
        if duplicates == []:
            return
        value_error_text = []
        for duplicate in duplicates:
            value_error_text.append(
                f"'{duplicate}' is provided as an '{argument}' multiple times, which is not "
                + "allowed."
            )
        raise ValueError("\n".join(value_error_text))
