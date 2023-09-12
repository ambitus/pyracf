"""Logging for pyRACF."""

import inspect
import json
import os
import re
from typing import Union


class Logger:
    """Logging for pyRACF."""

    __ansi_reset = "\033[0m"
    __ansi_gray = "\033[2m"
    __ansi_green = "\033[32m"
    __ansi_blue = "\033[34m"
    __ansi_orange = "\033[38;5;214m"
    __ansi_cyan = "\033[96m"
    __ansi_purple_background = "\033[1;45m"

    def __gray(self, string: str) -> str:
        """Make contents of string gray."""
        return self.__colorize_string(self.__ansi_gray, string)

    def __green(self, string: str) -> str:
        """Make contents of string green."""
        return self.__colorize_string(self.__ansi_green, string)

    def __blue(self, string: str) -> str:
        """Make contents of string blue."""
        return self.__colorize_string(self.__ansi_blue, string)

    def __orange(self, string: str) -> str:
        """Make contents of string orange."""
        return self.__colorize_string(self.__ansi_orange, string)

    def __cyan(self, string: str) -> str:
        """Make contents of string cyan."""
        return self.__colorize_string(self.__ansi_cyan, string)

    def __purple_background(self, string: str) -> str:
        """Make contents of string magenta."""
        return self.__colorize_string(self.__ansi_purple_background, string)

    def __colorize_string(self, ansi_color: str, string: str) -> str:
        return f"{ansi_color}{string}{self.__ansi_reset}"

    def log_dictionary(
        self,
        header_message: str,
        dictionary: dict,
        secret_traits: dict = {},
    ) -> None:
        """JSONify and colorize a dictionary and log it to the console."""
        if secret_traits:
            dictionary = self.__redact_request_dictionary(dictionary, secret_traits)
        dictionary_json = json.dumps(dictionary, indent=2)
        colorized_dictionary_json = self.__colorize_json(dictionary_json)
        self.log_debug(header_message, colorized_dictionary_json)

    def log_xml(
        self,
        header_message: str,
        xml_string: Union[str, bytes],
        secret_traits: dict = {},
    ) -> None:
        """Indent and colorize XML string and log it to the console."""
        if isinstance(xml_string, bytes):
            xml_string = xml_string.decode(encoding="utf-8")
        if secret_traits:
            xml_string = self.redact_request_xml(xml_string, secret_traits)
        indented_xml_string = self.__indent_xml(xml_string)
        colorized_indented_xml_string = self.__colorize_xml(indented_xml_string)
        self.log_debug(header_message, colorized_indented_xml_string)

    def log_debug(self, header_message: str, message: str) -> None:
        """Log function to use for debug logging."""
        stack = list(reversed(inspect.stack()))
        admin_class_calls = [
            (os.path.basename(stack[i].filename), stack[i].function)
            for i in range(len(stack) - 1)
            if os.path.basename(stack[i + 1].filename).split("_")[-1] == "admin.py"
        ][1:]
        user_call = admin_class_calls[0]
        class_tokens = [
            token.title() for token in user_call[0].split(".")[0].split("_")
        ]
        admin_class = "".join(class_tokens)
        function_called_by_user = f"{admin_class}.{user_call[1]}()"
        header = (
            f"{self.__purple_background(' '*79)}\n"
            + f"{self.__purple_background('[pyRACF:Debug]'.center(79))}\n"
            + f"{self.__purple_background(header_message.center(79))}\n"
            + f"{self.__purple_background(function_called_by_user.center(79))}\n"
            + f"{self.__purple_background(' '*79)}\n"
        )
        print(f"{header}\n{message}")

    def __redact_request_dictionary(
        self,
        dictionary: dict,
        secret_traits: dict,
    ) -> dict:
        """
        Redact a list of specified secret traits in a request dictionary.
        While this flow is technically used in extract functions, there are no traits to redact.
        """
        for trait in secret_traits:
            segment = trait.split(":")[0]
            if not dictionary.get(segment, {}).get(trait, {}).get("value", None):
                continue
            dictionary[segment][trait]["value"] = "********"
        return dictionary

    def __redact_string(
        self,
        input_string: str,
        start_ind: int,
        end_pattern: str,
    ):
        """
        Redacts characters in a string between a starting index and ending pattern.
        Replaces the identified characters with '********' regardless of the original length.
        """
        pre_keyword = input_string[:start_ind]
        post_keyword = end_pattern.join(input_string[start_ind:].split(end_pattern)[1:])
        return pre_keyword + "********" + end_pattern + post_keyword

    def redact_request_xml(
        self,
        xml_string: Union[str, bytes],
        secret_traits: dict,
    ) -> Union[str, bytes]:
        """
        Redact a list of specific secret traits in a request xml string or bytes object.
        Based the following xml pattern:
            '<xmltag attribute="any">xml value</xmltag>'
        This function also accounts for any number of arbitrary xml attributes.
        """
        is_bytes = False
        if isinstance(xml_string, bytes):
            is_bytes = True
            xml_string = xml_string.decode("utf-8")
        for xml_key in secret_traits.values():
            match = re.search(rf"\<{xml_key}+[^>]*\>", xml_string)
            if not match:
                continue
            xml_string = self.__redact_string(xml_string, match.end(), f"</{xml_key}")
        if is_bytes:
            xml_string = xml_string.encode("utf-8")
        return xml_string

    def redact_result_xml(
        self,
        xml_string: str,
        secret_traits: dict,
    ) -> str:
        """
        Redacts a list of specific secret traits in a result xml string.
        Based on the following RACF command pattern:
            'TRAIT (value)'
        This function also accounts for varied amounts of whitespace in the pattern.
        """
        for xml_key in secret_traits.values():
            racf_key = xml_key.split(":")[1] if ":" in xml_key else xml_key
            match = re.search(rf"{racf_key.upper()} +\(", xml_string)
            if not match:
                continue
            xml_string = self.__redact_string(xml_string, match.end(), ") ")
        return xml_string

    def __colorize_json(self, json_text: str) -> str:
        updated_json_text = ""
        json_lines = json_text.splitlines()
        for line in json_lines:
            tokens = line.split('"')
            if len(tokens) < 3:
                pass
            elif len(tokens[2]) == 0 or len(tokens[2]) == 1:
                line = self.__colorize_json_value(tokens)
            elif tokens[2][0] == ":":
                key = f'"{tokens[1]}"'
                first_half = f"{tokens[0]}{self.__cyan(key)}"
                second_half = self.__colorize_json_value(tokens[2:])
                line = first_half + second_half
            updated_json_text += f"{line}\n"
        return updated_json_text

    def __colorize_json_value(self, tokens: dict) -> str:
        if len(tokens) != 1:
            value = f'"{tokens[1]}"'
            second_half = f"{tokens[0]}{self.__orange(value)}{''.join(tokens[2:])}"
        else:
            skip_values = ["{", "[", "{}", "[]"]
            blue_values = ["null", "true", "false"]
            if "," in tokens[0]:
                value = tokens[0][2:-1]
                has_comma = True
            else:
                value = tokens[0][2:]
                has_comma = False
            if value in skip_values:
                pass
            elif value in blue_values:
                # null and booleans
                value = f"{self.__blue(value)}"
            else:
                # numbers
                value = f"{self.__green(value)}"
            second_half = f": {value}"
            if has_comma:
                second_half += ","
        return second_half

    def __colorize_xml(self, xml_text: str) -> str:
        updated_xml_text = ""
        xml_lines = xml_text.splitlines()
        for line in xml_lines:
            tokens = line.split("<")
            if ">" in tokens[1] and not tokens[1][-1] == ">":
                tag_tokens = tokens[1].split(">")[0].split()
            else:
                tag_tokens = tokens[1].split()
            tag_name = tag_tokens[0]
            tag_start = "<"
            tag_end = ">"
            if tag_name[0] == "?":
                tag_start = "<?"
                tag_end = "?>"
                tag_name = tag_name[1:]
            elif tag_name[0] == "/":
                tag_start = "</"
                tag_name = tag_name[1:]
            if ">" in tag_name:
                tag_name = tag_name.split(">")[0]
                tag_tokens = []
            attributes = " ".join(tag_tokens[1:])[: -len(tag_end)]
            if len(attributes) > 0:
                if attributes.count('"') % 2:
                    attributes = attributes + '"'
                if attributes[-1] == "/":
                    attributes = attributes[:-1]
                    tag_end = "/>"
            start_tag = (
                f"{self.__gray(tag_start)}"
                + f"{self.__blue(tag_name)}"
                + f"{self.__colorize_xml_attributes(attributes)}"
                + f"{self.__gray(tag_end)}"
            )
            data = ""
            end_tag = ""
            if len(tokens) > 2:
                data = "".join(tokens[1].split(">")[1:])
                end_tag = (
                    f"{self.__gray('</')}"
                    + f"{self.__blue(tokens[-1][1:-1])}"
                    + f"{self.__gray('>')}"
                )
            line = tokens[0] + start_tag + data + end_tag
            updated_xml_text += f"{line}\n"
        return updated_xml_text

    def __colorize_xml_attributes(self, xml_attributes: str) -> str:
        attribute_tokens = xml_attributes.split("=")
        updated_xml_attributes = " "
        if len(attribute_tokens) != 1:
            for token in attribute_tokens:
                subtokens = token.split()
                for subtoken in subtokens:
                    if '"' in subtoken:
                        updated_xml_attributes += f"{self.__orange(subtoken)} "
                    else:
                        updated_xml_attributes += f"{self.__cyan(subtoken)}="
        return updated_xml_attributes.rstrip()

    def __indent_xml(self, minified_xml: str) -> str:
        """Used to indent XML for readability in debug logging."""
        indent_level = 0
        indented_xml = ""
        xml_tokens = minified_xml.split("><")
        for i in range(1, len(xml_tokens)):
            previous_line = xml_tokens[i - 1]
            current_line = xml_tokens[i]
            if previous_line[:5] == "<?xml":
                indented_xml += f"{previous_line}>\n"
            elif i == 1:
                indented_xml += f"{previous_line}>\n"
                indent_level += 1
            elif (
                "</" not in previous_line
                and previous_line[0] != "/"
                and previous_line[-1] != "/"
            ):
                indent_level += 1
            if current_line[0] == "/":
                indent_level -= 1
            current_line = f"<{current_line}>"
            indented_xml += f"{'  ' * indent_level}{current_line}\n"
        return indented_xml[:-2]
