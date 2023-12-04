"""Generic Security Result Parser."""

import getpass
import re
from typing import Union
from xml.etree.ElementTree import Element  # Only used for type hints.

import defusedxml.ElementTree as XMLParser


class SecurityResult:
    """Generic Security Result Parser."""

    def __init__(
        self, result_xml: str, running_userid: Union[str, None] = None
    ) -> None:
        self.__result = XMLParser.fromstring(result_xml)
        self.__result_dictionary = {"securityResult": {}}
        self.__extract_results()
        if running_userid is not None:
            self.__result_dictionary["securityResult"][
                "runningUserid"
            ] = running_userid.lower()
        else:
            self.__result_dictionary["securityResult"][
                "runningUserid"
            ] = getpass.getuser().lower()

    def __extract_results(self) -> None:
        """Extract XML results into a dictionary."""
        self.__definition = self.__result[0]
        return_code = int(self.__result[1].text)
        reason_code = int(self.__result[2].text)
        self.__definition.attrib["requestId"] = self.__definition.attrib["requestid"]
        del self.__definition.attrib["requestid"]
        definition_tag = self.__to_pascal_case(self.__definition.tag.split("}")[-1])
        self.__result_dictionary["securityResult"][
            definition_tag
        ] = self.__definition.attrib
        self.__definition_dictionary = self.__result_dictionary["securityResult"][
            definition_tag
        ]
        filter_out_extra_messages = False
        if return_code == 0 and self.__definition_dictionary["operation"] == "listdata":
            filter_out_extra_messages = True
        try:
            if self.__definition[0].tag.split("}")[-1] == "info":
                self.__extract_info()
            if self.__definition[0].tag.split("}")[-1] == "error":
                self.__extract_error()
            else:
                self.__extract_commands(filter_out_extra_messages)
        except IndexError:
            # Index Error indicates that there is no
            # additional information to extract from the definition.
            pass
        self.__result_dictionary["securityResult"]["returnCode"] = return_code
        self.__result_dictionary["securityResult"]["reasonCode"] = reason_code

    def __extract_info(self) -> None:
        """Extract info section from XML into a list."""
        self.__definition_dictionary["info"] = []
        info = self.__definition_dictionary["info"]
        while self.__definition[0].tag.split("}")[-1] == "info":
            item = self.__definition[0]
            if item.tag.split("}")[-1] != "info":
                return
            info.append(item.text)
            self.__definition.remove(item)

    def __extract_commands(self, filter_out_extra_messages: bool) -> None:
        """Extract commands section from XML into a list."""
        self.__definition_dictionary["commands"] = []
        commands = self.__definition_dictionary["commands"]
        for command in self.__definition:
            self.__extract_command(commands, command, filter_out_extra_messages)

    def __extract_command(
        self,
        commands: dict,
        command: Element,
        filter_out_extra_messages: bool,
    ) -> None:
        command_dictionary = {}
        commands.append(command_dictionary)
        message_id_regex = r"[A-Z]{3}[0-9]{5}[A-Z]"
        for item in command:
            item_tag = self.__to_pascal_case(item.tag.split("}")[-1])
            if item_tag == "message":
                if "messages" not in command_dictionary:
                    command_dictionary["messages"] = []
                if item.text:
                    if filter_out_extra_messages and re.match(
                        message_id_regex, item.text
                    ):
                        continue
                command_dictionary["messages"].append(item.text)
            else:
                try:
                    command_dictionary[item_tag] = int(item.text)
                except ValueError:
                    command_dictionary[item_tag] = item.text

    def __extract_error(self) -> None:
        """Extract error section from XML into a dictionary."""
        self.__definition_dictionary["error"] = {}
        error = self.__definition[0]
        for item in error:
            item_tag = self.__to_pascal_case(item.tag.split("}")[-1])
            try:
                self.__definition_dictionary["error"][item_tag] = int(item.text)
            except ValueError:
                self.__definition_dictionary["error"][item_tag] = item.text

    def __to_pascal_case(self, key: str) -> str:
        """Convert result dictionary keys to pascal case."""
        match (key):
            case "returncode":
                return "returnCode"
            case "reasoncode":
                return "reasonCode"
            case "safreturncode":
                return "safReturnCode"
            case "errorfunction":
                return "errorFunction"
            case "errorcode":
                return "errorCode"
            case "errorreason":
                return "errorReason"
            case "errormessage":
                return "errorMessage"
            case "erroroffset":
                return "errorOffset"
            case "textinerror":
                return "textInError"
            case "groupconnection":
                return "groupConnection"
            case "dataset":
                return "dataSet"
            case "systemsettings":
                return "systemSettings"
            case _:
                return key

    def get_result_dictionary(self) -> dict:
        """Return result dictionary."""
        return self.__result_dictionary
