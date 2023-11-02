"""General Resource Profile Administration."""

from typing import List, Union

from pyracf.common.add_operation_error import AddOperationError
from pyracf.common.alter_operation_error import AlterOperationError
from pyracf.common.security_admin import SecurityAdmin
from pyracf.common.security_request_error import SecurityRequestError

from .resource_request import ResourceRequest


class ResourceAdmin(SecurityAdmin):
    """General Resaurce Profile Administration."""

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:application_data": "racf:appldata",
                "base:audit_alter:": "racf:audaltr",
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
                "cdtinfo:generic": "generic",
                "cdtinfo:genlist": "genlist",
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
                "generic": "generic",
                "genlist": "genlist",
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
            debug=debug,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            replace_existing_segment_traits=replace_existing_segment_traits,
            additional_secret_traits=additional_secret_traits,
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

    def get_my_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
        """Get the access associated with your own general resource profile."""
        profile = self.extract(resource, class_name, profile_only=True)
        return self._get_field(profile, "base", "yourAccess")

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
            self._build_segment_dictionaries(traits)
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
        self._build_segment_dictionaries(traits)
        profile_request = ResourceRequest(resource, class_name, "set")
        self._build_xml_segments(profile_request)
        return self._make_request(profile_request)

    def alter(self, resource: str, class_name: str, traits: dict) -> Union[dict, bytes]:
        """Alter an existing general resource profile."""
        if self._generate_requests_only:
            self._build_segment_dictionaries(traits)
            profile_request = ResourceRequest(resource, class_name, "set")
            self._build_xml_segments(profile_request, alter=True)
            return self._make_request(profile_request, irrsmo00_precheck=True)
        try:
            profile = self.extract(resource, class_name, profile_only=True)
        except SecurityRequestError:
            raise AlterOperationError(resource, class_name)
        if not self._get_field(profile, "base", "name") == resource.lower():
            raise AlterOperationError(resource, class_name)
        self._build_segment_dictionaries(traits)
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
        self._build_bool_segment_dictionaries(segments)
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
