"""User Administration."""

from typing import List, Union

from pyracf.common.exceptions.add_operation_error import AddOperationError
from pyracf.common.exceptions.alter_operation_error import AlterOperationError
from pyracf.common.exceptions.security_request_error import SecurityRequestError
from pyracf.common.security_admin import SecurityAdmin

from .user_request import UserRequest


class UserAdmin(SecurityAdmin):
    """User Administration."""

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
                "base:automatic_data_set_protection": "racf:adsp",
                "base:auditor": "racf:auditor",
                "base:default_group_authority": "racf:auth",
                "base:security_categories": "racf:category",
                "base:class_authorizations": "racf:clauth",
                "base:installation_data": "racf:data",
                "base:default_group": "defgroup",
                "base:password_expired": "racf:expired",
                "base:group": "racf:group",
                "base:group_data_set_access": "racf:grpacc",
                "base:model_data_set": "racf:model",
                "base:name": "name",
                "base:require_operator_id_card": "racf:oidcard",
                "base:operations": "racf:oper",
                "base:owner": "racf:owner",
                "base:password": "racf:password",
                "base:passphrase": "racf:phrase",
                "base:restrict_global_access_checking": "racf:rest",
                "base:resume_date": "resumedate",
                "base:revoke_date": "revokedate",
                "base:audit_responsibility": "racf:roaudit",
                "base:security_label": "seclabel",
                "base:security_level": "racf:seclevel",
                "base:special": "racf:special",
                "base:universal_access": "racf:uacc",
                "base:audit_logging": "uaudit",
                "base:logon_allowed_days": "whendays",
                "base:logon_allowed_time": "whentime",
            },
            "cics": {
                "cics:operator_classes": "racf:opclass",
                "cics:operator_id": "opident",
                "cics:operator_priority": "opprty",
                "cics:rsl_key": "racf:rslkey",
                "cics:timeout": "timeout",
                "cics:tsl_key": "racf:tslkey",
                "cics:xrf_sign_off": "force",
            },
            "dce": {
                "dce:auto_login": "autolog",
                "dce:name": "dcename",
                "dce:home_cell": "homecell",
                "dce:home_cell_uuid": "homeuuid",
                "dce:uuid": "uuid",
            },
            "dfp": {
                "dfp:data_application": "dataappl",
                "dfp:data_class": "dataclas",
                "dfp:management_class": "mgmtclass",
                "dfp:storage_class": "storclas",
            },
            "eim": {"eim:ldap_bind_profile": "racf:ldapprof"},
            "kerb": {
                "kerb:encryption_algorithm": "racf:encrypt",
                "kerb:name": "racf:kerbname",
                "kerb:max_ticket_life": "racf:maxtktlf",
            },
            "language": {
                "language:primary": "primary",
                "language:secondary": "secondary",
            },
            "lnotes": {"lnotes:zos_short_name": "racf:sname"},
            "mfa": {
                "mfa:factor": "racf:factor",
                "mfa:active": "racf:facactv",
                "mfa:tags": "racf:factags",
                "mfa:password_fallback": "racf:mfaflbk",
                "mfa:policy": "racf:mfapolnm",
            },
            "nds": {"nds:username": "racf:uname"},
            "netview": {
                "netview:default_console": "consid",
                "netview:security_check": "secctl",
                "netview:domains": "nvdomains",
                "netview:logon_commands": "ic",
                "netview:recieve_unsolicited_messages": "msgrec",
                "netview:graphic_monitor_facility_admin": "racf:ngmfadmn",
                "netview:view_span": "gmfadmin",
                "netview:operator_scope_classes": "racf:opclass",
            },
            "omvs": {
                "omvs:max_address_space_size": "assize",
                "omvs:auto_uid": "racf:autouid",
                "omvs:max_cpu_time": "cputime",
                "omvs:max_files_per_process": "filemax",
                "omvs:home_directory": "home",
                "omvs:max_non_shared_memory": "memlim",
                "omvs:max_file_mapping_pages": "mmaparea",
                "omvs:max_processes": "procmax",
                "omvs:default_shell": "pgm",
                "omvs:shared": "racf:shared",
                "omvs:max_shared_memory": "shmemmax",
                "omvs:max_threads": "threads",
                "omvs:uid": "uid",
            },
            "operparm": {
                "operparm:alternate_console_group": "altgrp",
                "operparm:recieve_automated_messages": "auto",
                "operparm:command_target_systems": "cmdsys",
                "operparm:recieve_delete_operator_messages": "dom",
                "operparm:recieve_hardcopy_messages": "hc",
                "operparm:recieve_internal_console_messages": "intid",
                "operparm:console_searching_key": "key",
                "operparm:message_level": "racf:level",
                "operparm:log_command_responses": "logcmd",
                "operparm:message_format": "mform",
                "operparm:migration_id": "migid",
                "operparm:events_to_monitor": "mon",
                "operparm:message_scope": "racf:mscope",
                "operparm:operator_command_authority": "auth",
                "operparm:recieve_routing_codes": "routcode",
                "operparm:message_queue_storage": "storage",
                "operparm:recieve_undelivered_messages": "ud",
                "operparm:recieve_messages_from_unknown_console_ids": "unkids",
            },
            "ovm": {
                "ovm:file_system_root": "racf:fsroot",
                "ovm:home_directory": "racf:vhome",
                "ovm:default_shell": "racf:vprogram",
                "ovm:uid": "racf:vuid",
            },
            "proxy": {
                "proxy:bind_distinguished_name": "racf:binddn",
                "proxy:bind_password": "racf:bindpw",
                "proxy:ldap_host": "racf:ldaphost",
            },
            "tso": {
                "tso:account_number": "acctnum",
                "tso:logon_command": "command",
                "tso:sysout_destination_id": "dest",
                "tso:hold_class": "holdclass",
                "tso:job_class": "jobclass",
                "tso:max_region_size": "maxsize",
                "tso:message_class": "msgclass",
                "tso:logon_procedure": "proc",
                "tso:security_label": "seclabel",
                "tso:default_region_size": "size",
                "tso:sysout_class": "sysclass",
                "tso:data_set_allocation_unit": "unit",
                "tso:user_data": "userdata",
            },
            "workattr": {
                "workattr:account_number": "waaccnt",
                "workattr:sysout_address_1": "waaddr1",
                "workattr:sysout_address_2": "waaddr2",
                "workattr:sysout_address_3": "waaddr3",
                "workattr:sysout_address_4": "waaddr4",
                "workattr:sysout_building": "wabldg",
                "workattr:sysout_department": "wadept",
                "workattr:sysout_user": "waname",
                "workattr:sysout_room": "waroom",
                "workattr:sysout_email": "waemail",
            },
        }
        self._extracted_key_value_pair_segment_traits_map = {
            "omvs": {
                "home": "homeDirectory",
                "program": "defaultShell",
                "cputimemax": "maxCpuTime",
                "assizemax": "maxAddressSpaceSize",
                "fileprocmax": "maxFilesPerProcess",
                "procusermax": "maxProcesses",
                "threadsmax": "maxThreads",
                "mmapareamax": "maxFileMappingPages",
                "memlimit": "maxNonSharedMemory",
                "shmemmax": "maxSharedMemory",
            },
            "tso": {
                "acctnum": "accountNumber",
                "holdclass": "holdClass",
                "jobclass": "jobClass",
                "msgclass": "messageClass",
                "proc": "logonProcedure",
                "size": "defaultRegionSize",
                "maxsize": "maxRegionSize",
                "sysoutclass": "sysoutClass",
                "unit": "dataSetAllocationUnit",
                "userdata": "userData",
                "command": "logonCommand",
            },
        }
        self._case_sensitive_extracted_values = ["homeDirectory", "defaultShell"]
        super().__init__(
            "user",
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
    # Special Authority
    # ============================================================================
    def has_special_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has RACF special authority."""
        profile = self.extract(userid, profile_only=True)
        return "special" in profile["base"]["attributes"]

    def give_special_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user RACF special authority."""
        result = self.alter(userid, traits={"base:special": True})
        return self._to_steps(result)

    def take_away_special_authority(
        self,
        userid: str,
    ) -> Union[dict, bytes]:
        """Remove a user's RACF special authority."""
        result = self.alter(userid, traits={"base:special": False})
        return self._to_steps(result)

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def has_operations_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has operations authority."""
        profile = self.extract(userid, profile_only=True)
        return "operations" in profile["base"]["attributes"]

    def give_operations_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user operations authority."""
        result = self.alter(userid, traits={"base:operations": True})
        return self._to_steps(result)

    def take_away_operations_authority(self, userid: str) -> Union[dict, bytes]:
        """Remove a user's operations authority."""
        result = self.alter(userid, traits={"base:operations": False})
        return self._to_steps(result)

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def has_auditor_authority(self, userid: str) -> Union[bool, bytes]:
        """Check if a user has auditor authority."""
        profile = self.extract(userid, profile_only=True)
        return "auditor" in profile["base"]["attributes"]

    def give_auditor_authority(self, userid: str) -> Union[dict, bytes]:
        """Give a user auditor authority."""
        result = self.alter(userid, traits={"base:auditor": True})
        return self._to_steps(result)

    def take_away_auditor_authority(self, userid: str) -> Union[dict, bytes]:
        """Remove a user's auditor authority."""
        result = self.alter(userid, traits={"base:auditor": False})
        return self._to_steps(result)

    # ============================================================================
    # Password
    # ============================================================================
    def set_password(
        self, userid: str, password: Union[str, bool], expired: Union[bool, None] = None
    ) -> Union[dict, bytes]:
        """Set a user's password."""
        traits = {"base:password": password}
        if expired is not None:
            traits["base:password_expired"] = expired
        result = self.alter(userid, traits=traits)
        return self._to_steps(result)

    # ============================================================================
    # Passphrase
    # ============================================================================
    def set_passphrase(
        self,
        userid: str,
        passphrase: Union[str, bool],
        expired: Union[bool, None] = None,
    ) -> Union[dict, bytes]:
        """Set a user's passphrase."""
        traits = {"base:passphrase": passphrase}
        if expired is not None:
            traits["base:password_expired"] = expired
        result = self.alter(userid, traits=traits)
        return self._to_steps(result)

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def get_class_authorizations(self, userid: str) -> Union[List[str], bytes]:
        """Get a user's class authorizations."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "classAuthorizations")

    def set_class_authorizations(
        self, userid: str, class_authorizations: List[str]
    ) -> Union[dict, bytes]:
        """
        Set a user's class authorizations.
        removes the user's current class authorizations and then recreates
        the class authorizations list using the list that the user provides.
        """
        delete_result = self.remove_all_class_authorizations(userid)
        add_result = self.add_class_authorizations(userid, class_authorizations)
        return self._to_steps([delete_result, add_result])

    def add_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> Union[dict, bytes]:
        """Add one or more classes to a user's class authorizations."""
        result = self.alter(
            userid, traits={"add:base:class_authorizations": class_authorizations}
        )
        return self._to_steps(result)

    def remove_class_authorizations(
        self, userid: str, class_authorizations: Union[str, List[str]]
    ) -> Union[dict, bytes]:
        """Remove one or more classes from a user's class authorizations."""
        result = self.alter(
            userid, traits={"remove:base:class_authorizations": class_authorizations}
        )
        return self._to_steps(result)

    def remove_all_class_authorizations(self, userid: str) -> Union[dict, bool, bytes]:
        """Remove all classes from a users class authorizations."""
        current_class_authorizations = self.get_class_authorizations(userid)
        if not current_class_authorizations:
            return False
        return self.remove_class_authorizations(userid, current_class_authorizations)

    # ============================================================================
    # Revoke Date
    # ============================================================================
    def get_revoke_date(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's revoke date."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "revokeDate", string=True)

    def set_revoke_date(
        self, userid: str, revoke_date: Union[str, bool]
    ) -> Union[dict, bytes]:
        """Set a user's revoke date."""
        result = self.alter(userid, traits={"base:revoke_date": revoke_date})
        return self._to_steps(result)

    # ============================================================================
    # Resume Date
    # ============================================================================
    def get_resume_date(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's resume date."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "resumeDate", string=True)

    def set_resume_date(
        self, userid: str, resume_date: Union[str, bool]
    ) -> Union[dict, bytes]:
        """Set a user's resume date."""
        result = self.alter(userid, traits={"base:resume_date": resume_date})
        return self._to_steps(result)

    # ============================================================================
    # Owner
    # ============================================================================
    def get_owner(self, userid: str) -> Union[str, bytes]:
        """Get a user's owner."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "owner", string=True)

    def set_owner(self, userid: str, owner: str) -> Union[dict, bytes]:
        """Set a user's owner."""
        result = self.alter(userid, traits={"base:owner": owner})
        return self._to_steps(result)

    # ============================================================================
    # Name
    # ============================================================================
    def get_name(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's name."""
        profile = self.extract(userid, profile_only=True)
        return self._get_field(profile, "base", "name", string=True)

    def set_name(self, userid: str, name: Union[str, bool]) -> Union[dict, bytes]:
        """Set a user's name."""
        result = self.alter(userid, traits={"base:name": name})
        return self._to_steps(result)

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def get_omvs_uid(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS UID."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "uid")

    def set_omvs_uid(self, userid: str, uid: Union[int, bool]) -> Union[dict, bytes]:
        """Set a user's OMVS UID."""
        result = self.alter(userid, traits={"omvs:uid": uid})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Address Space Size
    # ============================================================================
    def get_omvs_max_address_space_size(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max address space size."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxAddressSpaceSize")

    def set_omvs_max_address_space_size(
        self,
        userid: str,
        max_address_space_size: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max address space size."""
        result = self.alter(
            userid, traits={"omvs:max_address_space_size": max_address_space_size}
        )
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max CPU Time
    # ============================================================================
    def get_omvs_max_cpu_time(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max cpu time."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxCpuTime")

    def set_omvs_max_cpu_time(
        self,
        userid: str,
        max_cpu_time: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max cpu time."""
        result = self.alter(userid, traits={"omvs:max_cpu_time": max_cpu_time})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Files Per Process
    # ============================================================================
    def get_omvs_max_files_per_process(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max files per process."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxFilesPerProcess")

    def set_omvs_max_files_per_process(
        self,
        userid: str,
        max_files_per_process: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max files per process."""
        result = self.alter(
            userid, traits={"omvs:max_files_per_process": max_files_per_process}
        )
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Non-Shared Memory
    # ============================================================================
    def get_omvs_max_non_shared_memory(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS max non-shared memory."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxNonSharedMemory", string=True)

    def set_omvs_max_non_shared_memory(
        self,
        userid: str,
        max_non_shared_memory: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max non-shared memory."""
        result = self.alter(
            userid, traits={"omvs:max_non_shared_memory": max_non_shared_memory}
        )
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max File Mapping Pages
    # ============================================================================
    def get_omvs_max_file_mapping_pages(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max file mapping pages."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxFileMappingPages")

    def set_omvs_max_file_mapping_pages(
        self,
        userid: str,
        max_file_mapping_pages: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max file mapping pages."""
        result = self.alter(
            userid, traits={"omvs:max_file_mapping_pages": max_file_mapping_pages}
        )
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Processes
    # ============================================================================
    def get_omvs_max_processes(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max processes."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxProcesses")

    def set_omvs_max_processes(
        self,
        userid: str,
        max_processes: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max processes."""
        result = self.alter(userid, traits={"omvs:max_processes": max_processes})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Shared Memory
    # ============================================================================
    def get_omvs_max_shared_memory(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS max shared memory."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxSharedMemory", string=True)

    def set_omvs_max_shared_memory(
        self,
        userid: str,
        max_shared_memory: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max shared memory."""
        result = self.alter(
            userid, traits={"omvs:max_shared_memory": max_shared_memory}
        )
        return self._to_steps(result)

    # ============================================================================
    # OMVS Max Threads
    # ============================================================================
    def get_omvs_max_threads(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's OMVS max threads."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "maxThreads")

    def set_omvs_max_threads(
        self,
        userid: str,
        max_threads: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS max threads."""
        result = self.alter(userid, traits={"omvs:max_threads": max_threads})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Home Directory
    # ============================================================================
    def get_omvs_home_directory(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS home directory."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "homeDirectory", string=True)

    def set_omvs_home_directory(
        self,
        userid: str,
        home_directory: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS home directory."""
        result = self.alter(userid, traits={"omvs:home_directory": home_directory})
        return self._to_steps(result)

    # ============================================================================
    # OMVS Default Shell
    # ============================================================================
    def get_omvs_default_shell(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's OMVS default shell."""
        profile = self.extract(userid, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "defaultShell", string=True)

    def set_omvs_default_shell(
        self,
        userid: str,
        default_shell: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's OMVS default shell."""
        result = self.alter(userid, traits={"omvs:default_shell": default_shell})
        return self._to_steps(result)

    # ============================================================================
    # TSO Account Number
    # ============================================================================
    def get_tso_account_number(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO account number."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "accountNumber", string=True)

    def set_tso_account_number(
        self,
        userid: str,
        account_number: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO account number."""
        result = self.alter(userid, traits={"tso:account_number": account_number})
        return self._to_steps(result)

    # ============================================================================
    # TSO Logon Command
    # ============================================================================
    def get_tso_logon_command(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO logon command."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "logonCommand", string=True)

    def set_tso_logon_command(
        self,
        userid: str,
        logon_command: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO logon command."""
        result = self.alter(userid, traits={"tso:logon_command": logon_command})
        return self._to_steps(result)

    # ============================================================================
    # TSO Hold Class
    # ============================================================================
    def get_tso_hold_class(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO hold class."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "holdClass", string=True)

    def set_tso_hold_class(
        self,
        userid: str,
        hold_class: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO hold class."""
        result = self.alter(userid, traits={"tso:hold_class": hold_class})
        return self._to_steps(result)

    # ============================================================================
    # TSO Max Region Size
    # ============================================================================
    def get_tso_max_region_size(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's TSO max region size."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "maxRegionSize")

    def set_tso_max_region_size(
        self,
        userid: str,
        max_region_size: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO max region size."""
        result = self.alter(userid, traits={"tso:max_region_size": max_region_size})
        return self._to_steps(result)

    # ============================================================================
    # TSO Message Class
    # ============================================================================
    def get_tso_message_class(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO message class."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "messageClass", string=True)

    def set_tso_message_class(
        self,
        userid: str,
        message_class: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO message class."""
        result = self.alter(userid, traits={"tso:message_class": message_class})
        return self._to_steps(result)

    # ============================================================================
    # TSO Logon Procedure
    # ============================================================================
    def get_tso_logon_procedure(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO logon procedure."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "logonProcedure", string=True)

    def set_tso_logon_procedure(
        self,
        userid: str,
        logon_procedure: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO logon procedure."""
        result = self.alter(userid, traits={"tso:logon_procedure": logon_procedure})
        return self._to_steps(result)

    # ============================================================================
    # TSO Default Region Size
    # ============================================================================
    def get_tso_default_region_size(self, userid: str) -> Union[int, None, bytes]:
        """Get a user's TSO default region size."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "defaultRegionSize")

    def set_tso_default_region_size(
        self,
        userid: str,
        default_region_size: Union[int, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO default region size."""
        result = self.alter(
            userid, traits={"tso:default_region_size": default_region_size}
        )
        return self._to_steps(result)

    # ============================================================================
    # TSO Sysout Class
    # ============================================================================
    def get_tso_sysout_class(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO sysout class."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "sysoutClass", string=True)

    def set_tso_sysout_class(
        self,
        userid: str,
        sysout_class: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO sysout class."""
        result = self.alter(userid, traits={"tso:sysout_class": sysout_class})
        return self._to_steps(result)

    # ============================================================================
    # TSO User Data
    # ============================================================================
    def get_tso_user_data(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO user data."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "userData", string=True)

    def set_tso_user_data(
        self,
        userid: str,
        user_data: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO user data."""
        result = self.alter(userid, traits={"tso:user_data": user_data})
        return self._to_steps(result)

    # ============================================================================
    # TSO Data Set Allocation Unit
    # ============================================================================
    def get_tso_data_set_allocation_unit(self, userid: str) -> Union[str, None, bytes]:
        """Get a user's TSO data set allocation unit."""
        profile = self.extract(userid, segments=["tso"], profile_only=True)
        return self._get_field(profile, "tso", "dataSetAllocationUnit", string=True)

    def set_tso_data_set_allocation_unit(
        self,
        userid: str,
        data_set_allocation_unit: Union[str, bool],
    ) -> Union[dict, bytes]:
        """Set a user's TSO data set allocation unit."""
        result = self.alter(
            userid, traits={"tso:data_set_allocation_unit": data_set_allocation_unit}
        )
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, userid: str, traits: dict = {}) -> Union[dict, bytes]:
        """Create a new user."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            user_request = UserRequest(userid, "set")
            self._build_xml_segments(user_request)
            return self._make_request(user_request)
        try:
            self.extract(userid)
        except SecurityRequestError as exception:
            if not exception.contains_error_message(self._profile_type, "ICH30001I"):
                raise exception
            self._build_segment_trait_dictionary(traits)
            user_request = UserRequest(userid, "set")
            self._build_xml_segments(user_request)
            return self._make_request(user_request)
        raise AddOperationError(userid, self._profile_type)

    def alter(self, userid: str, traits: dict) -> Union[dict, bytes]:
        """Alter an existing user."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            user_request = UserRequest(userid, "set")
            self._build_xml_segments(user_request, alter=True)
            return self._make_request(user_request, irrsmo00_precheck=True)
        try:
            self.extract(userid)
        except SecurityRequestError as exception:
            raise AlterOperationError(userid, self._profile_type) from exception
        self._build_segment_trait_dictionary(traits)
        user_request = UserRequest(userid, "set")
        self._build_xml_segments(user_request, alter=True)
        return self._make_request(user_request, irrsmo00_precheck=True)

    def extract(
        self, userid: str, segments: List[str] = [], profile_only: bool = False
    ) -> Union[dict, bytes]:
        """Extract a user's profile."""
        self._build_segment_dictionary(segments)
        user_request = UserRequest(userid, "listdata")
        self._build_xml_segments(user_request, extract=True)
        result = self._extract_and_check_result(user_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(self, userid: str) -> Union[dict, bytes]:
        """Delete a user."""
        user_request = UserRequest(userid, "del")
        return self._make_request(user_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["user"]["commands"][0]["messages"]
        userid = result["securityResult"]["user"]["name"]
        exclude_command_audit_trail_string = f"Command Audit Trail for USER {userid}"
        if exclude_command_audit_trail_string in messages:
            messages = messages[: messages.index(exclude_command_audit_trail_string)]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "USER=" in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            profiles.append(profile)

        # Post processing
        del result["securityResult"]["user"]["commands"][0]["messages"]
        result["securityResult"]["user"]["commands"][0]["profiles"] = profiles
