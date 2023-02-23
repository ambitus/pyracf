"""Generic Security Result Parser."""

import defusedxml.ElementTree as XMLParser


class SecurityResult:
    """Generic Security Result Parser."""

    def __init__(self, result_xml: str) -> None:
        self.result = XMLParser.fromstring(result_xml)
        self.result_dictionary = {"securityresult": {}}
        self.__extract_results()

    def __extract_results(self) -> None:
        """Extract XML results into a dictionary."""
        self.definition = self.result[0]
        definition_tag = self.definition.tag.split("}")[-1]
        self.result_dictionary["securityresult"][
            definition_tag
        ] = self.definition.attrib
        self.definition_dictionary = self.result_dictionary["securityresult"][
            definition_tag
        ]
        if self.definition[0].tag.split("}")[-1] == "info":
            self.__extract_info()
        if self.definition[0].tag.split("}")[-1] == "error":
            self.__extract_error()
        else:
            self.__extract_commands()
        return_code = self.result[1]
        self.result_dictionary["securityresult"]["returncode"] = int(return_code.text)
        reason_code = self.result[1]
        self.result_dictionary["securityresult"]["reasoncode"] = int(reason_code.text)

    def __extract_info(self) -> None:
        """Extract info section from XML into a list."""
        self.definition_dictionary["info"] = []
        info = self.definition_dictionary["info"]
        print(self.definition[0].tag)
        while self.definition[0].tag.split("}")[-1] == "info":
            item = self.definition[0]
            if item.tag.split("}")[-1] != "info":
                return
            info.append(item.text)
            self.definition.remove(item)
            try:
                self.definition[0].tag.split("}")[-1]
            except IndexError:
                return

    def __extract_commands(self) -> None:
        """Extract commands section from XML into a list."""
        self.definition_dictionary["commands"] = []
        commands = self.definition_dictionary["commands"]
        for command in self.definition:
            command_dictionary = {}
            commands.append(command_dictionary)
            for item in command:
                item_tag = item.tag.split("}")[-1]
                if item_tag == "message":
                    if "messages" not in command_dictionary:
                        command_dictionary["messages"] = []
                    command_dictionary["messages"].append(item.text)
                try:
                    command_dictionary[item_tag] = int(item.text)
                except ValueError:
                    command_dictionary[item_tag] = item.text

    def __extract_error(self) -> None:
        """Extract error section from XML into a dictionary."""
        self.definition_dictionary["error"] = {}
        error = self.definition[0]
        for item in error:
            item_tag = item.tag.split("}")[-1]
            try:
                self.definition_dictionary["error"][item_tag] = int(item.text)
            except ValueError:
                self.definition_dictionary["error"][item_tag] = item.text

    def get_result_dictionary(self) -> dict:
        """Return result dictionary."""
        return self.result_dictionary
