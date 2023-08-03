"""Generic Security Result Parser."""

from xml.etree.ElementTree import Element  # Only used for type hints.

import defusedxml.ElementTree as XMLParser


class SecurityResult:
    """Generic Security Result Parser."""

    def __init__(self, result_xml: str) -> None:
        self.__result = XMLParser.fromstring(result_xml)
        self.__result_dictionary = {"securityResult": {}}
        self.__extract_results()

    def __extract_results(self) -> None:
        """Extract XML results into a dictionary."""
        self.definition = self.__result[0]
        self.definition.attrib["requestId"] = self.definition.attrib["requestid"]
        del self.definition.attrib["requestid"]
        definition_tag = self.__to_pascal_case(self.definition.tag.split("}")[-1])
        self.__result_dictionary["securityResult"][
            definition_tag
        ] = self.definition.attrib
        self.definition_dictionary = self.__result_dictionary["securityResult"][
            definition_tag
        ]
        try:
            if self.definition[0].tag.split("}")[-1] == "info":
                self.__extract_info()
            if self.definition[0].tag.split("}")[-1] == "error":
                self.__extract_error()
            else:
                self.__extract_commands()
        except IndexError:
            # Index Error indicates that there is no
            # additional information to extract from the definition.
            pass
        return_code = self.__result[1]
        self.__result_dictionary["securityResult"]["returnCode"] = int(return_code.text)
        reason_code = self.__result[2]
        self.__result_dictionary["securityResult"]["reasonCode"] = int(reason_code.text)

    def __extract_info(self) -> None:
        """Extract info section from XML into a list."""
        self.definition_dictionary["info"] = []
        info = self.definition_dictionary["info"]
        while self.definition[0].tag.split("}")[-1] == "info":
            item = self.definition[0]
            if item.tag.split("}")[-1] != "info":
                return
            info.append(item.text)
            self.definition.remove(item)

    def __extract_commands(self) -> None:
        """Extract commands section from XML into a list."""
        self.definition_dictionary["commands"] = []
        commands = self.definition_dictionary["commands"]
        for command in self.definition:
            self.__extract_command(commands, command)

    def __extract_command(self, commands: dict, command: Element) -> None:
        command_dictionary = {}
        commands.append(command_dictionary)
        for item in command:
            item_tag = self.__to_pascal_case(item.tag.split("}")[-1])
            if item_tag == "message":
                if "messages" not in command_dictionary:
                    command_dictionary["messages"] = []
                command_dictionary["messages"].append(item.text)
            else:
                try:
                    command_dictionary[item_tag] = int(item.text)
                except ValueError:
                    command_dictionary[item_tag] = item.text

    def __extract_error(self) -> None:
        """Extract error section from XML into a dictionary."""
        self.definition_dictionary["error"] = {}
        error = self.definition[0]
        for item in error:
            item_tag = self.__to_pascal_case(item.tag.split("}")[-1])
            try:
                self.definition_dictionary["error"][item_tag] = int(item.text)
            except ValueError:
                self.definition_dictionary["error"][item_tag] = item.text

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
