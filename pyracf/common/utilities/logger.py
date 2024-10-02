"""Logging for pyRACF."""

import inspect
import json
import os
import re
import struct
from typing import List, Union


class Logger:
    """Logging for pyRACF."""

    __ansi_reset = "\033[0m"
    __ansi_gray = "\033[2m"
    __ansi_green = "\033[32m"
    __ansi_red = "\033[0;31m"
    __ansi_yellow = "\033[1;33m"
    __ansi_blue = "\033[34m"
    __ansi_light_blue = "\033[1;34m"
    __ansi_orange = "\033[38;5;214m"
    __ansi_cyan = "\033[96m"
    __ansi_purple_background = "\033[1;45m"

    def __gray(self, string: str) -> str:
        """Make the text in a string gray."""
        return self.__colorize_string(self.__ansi_gray, string)

    def __green(self, string: str) -> str:
        """Make the text in a string green."""
        return self.__colorize_string(self.__ansi_green, string)

    def __red(self, string: str) -> str:
        """Make the text in a string red."""
        return self.__colorize_string(self.__ansi_red, string)

    def __yellow(self, string: str) -> str:
        """Make the text in a string yellow."""
        return self.__colorize_string(self.__ansi_yellow, string)

    def __blue(self, string: str) -> str:
        """Make the text in a string blue."""
        return self.__colorize_string(self.__ansi_blue, string)

    def __light_blue(self, string: str) -> str:
        """Make the text in a string light blue."""
        return self.__colorize_string(self.__ansi_light_blue, string)

    def __orange(self, string: str) -> str:
        """Make the text in a string orange."""
        return self.__colorize_string(self.__ansi_orange, string)

    def __cyan(self, string: str) -> str:
        """Make the text in a string cyan."""
        return self.__colorize_string(self.__ansi_cyan, string)

    def __purple_background(self, string: str) -> str:
        """Make background color of a string magenta."""
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

    def log_info(self, message: str):
        """Log an informational message to the console."""
        print(f"[ {self.__cyan('INFO')} ] {message}")

    def log_warning(self, message: str):
        """Log a warning message to the console."""
        print(f"[ {self.__yellow('WARN')} ] {message}")

    def log_fatal(self, message: str):
        """Log a fatal error message to the console."""
        print(f"[ {self.__red('FATAL')} ] {message}")

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
            f"{self.__purple_background(' ' * 79)}\n"
            + f"{self.__purple_background('[pyRACF:Debug]'.center(79))}\n"
            + f"{self.__purple_background(header_message.center(79))}\n"
            + f"{self.__purple_background(function_called_by_user.center(79))}\n"
            + f"{self.__purple_background(' ' * 79)}\n"
        )
        print(f"{header}\n{message}")

    def log_experimental(self, feature: str) -> None:
        self.log_warning(
            f"'{feature}' is an experimental feature. This feature is "
            + "subject to major changes and even being removed entirely."
        )

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
        input_string: Union[str, bytes],
        trait_key: str,
    ) -> Union[str, bytes]:
        r"""
        Redacts characters in a string between a starting index and ending tag.
        Replaces the identified characters with '********' regardless of the original length.

        This function employs the following regular expressions explained below

        Regex 1 ("quoted") - {trait_key.upper()}( +){{0,}}\(\'.*?(?<!\')\'\)
        This is designed to match the pattern TRAIT('value') by matching the TRAIT name, a
        variable (potentially zero) amount of spaces, then the ('value') portion which must
        start and end with (' and '), but can conceivably contain any characters, but a negative
        lookbehind is used to look for any unescaped single quotes that would indicate the matching
        of ') is otherwise a coincidence.

        Regex 2 ("nested") - {trait_key.upper()}( +){{0,}}\([^)]*\(.*\)( +){{0,}}\)
        This is designed to match the pattern TRAIT( subtrait1(value) subtrait2(value)) by
        matching the TRAIT name, a variable (potentially zero) amount of spaces, then the
        ( subtrait1(value) subtrait2(value)) portion which must start and end with ( and ),
        but must also contain a'(' before the ')'. This indicates that there is a "nested"
        structure rather than a sequential one. In the example, this portion of the pattern
        matches '( subtrait1(', but would not match '(value) subtrait2(' because of the ')'
        character between the two '(' characters. The pattern looks for these nested open
        parenthesis as a sequence would have a ')' character between them. Then the expression
        allows any non-newline characters to handle all possible trait values and subtrait names
        followed by the "end pattern" of ')' and ')' separated by a variable (potentially zero)
        whitespace.

        If neither of these two patterns is found for a supplied trait_key, then it is assumed
        this trait is set with the default pattern below.

        Regex 3 ("default") - {trait_key.upper()}( +){{0,}}\(.*?(?<!\\)\)
        This is designed to match the pattern TRAIT(value) by matching the TRAIT name, a variable
        (potentially zero) amount of spaces, then the (value) portion which must start and end
        with '(' and ')', but can conceivably contain any characters, but a negative lookbehind
        is used to look for any escape character '\' that would indicate the matching of the
        '(' and ')' is otherwise a coincidence.

        In all replacement expressions, the variable amounts of whitespace are captured so that
        they can be preserved by this redaction operations.

        """
        asterisks = "********"
        is_bytes = False
        quoted_regex = rf"{trait_key.upper()}( +){{0,}}\(\'.*?(?<!\')\'\)"
        nested_regex = rf"{trait_key.upper()}( +){{0,}}\([^)]*\(.*\)( +){{0,}}\)"
        default_regex = rf"{trait_key.upper()}( +){{0,}}\(.*?(?<!\\)\)"
        redacted_regex = rf"{trait_key.upper()}\1({asterisks})"
        redacted_w_quotes_regex = rf"{trait_key.upper()}\1('{asterisks}')"
        if isinstance(input_string, bytes):
            input_string = input_string.decode("cp1047")
            is_bytes = True
        quoted = re.search(quoted_regex, input_string)
        nested = re.search(nested_regex, input_string)
        if quoted is not None:
            input_string = re.sub(
                quoted_regex,
                redacted_w_quotes_regex,
                input_string,
            )
        else:
            if nested is not None:
                input_string = re.sub(
                    nested_regex,
                    redacted_regex,
                    input_string,
                )
            else:
                input_string = re.sub(
                    default_regex,
                    redacted_regex,
                    input_string,
                )
        if is_bytes:
            return input_string.encode("cp1047")
        return input_string

    def redact_request_xml(
        self,
        xml_string: Union[str, bytes],
        secret_traits: dict,
    ) -> Union[str, bytes]:
        r"""
        Redact a list of specific secret traits in a request xml string or bytes object.
        Based the following xml pattern:
            '<xmltag attribute="any">xml value</xmltag>'
        This function also accounts for any number of arbitrary xml attributes.

        This function employs the following regular expression:
        {xml_key}(.*)>.*<\/{xml_key} - Designed to match the above pattern by starting and ending
        with the xmltag string as shown, but the starting tag allows for any characters between
        "xmltag" and the > character to allow for the attribute specification shown above. This
        results in the starting of the xml as {xml_key}(.*)> and the ending as <\/{xml_key}.
        The characters between the xml tags are "captured" as a variable and preserved by the
        substitution operation through the use of the \1 supplied in the replacement string.
        Between these tags, any non-newline characters are allowed using the .* expression.
        """
        is_bytes = False
        if isinstance(xml_string, bytes):
            is_bytes = True
            xml_string = xml_string.decode("utf-8")
        for xml_key in secret_traits.values():
            start_tag_end_tag_regex = rf"{xml_key}(.*)>.*<\/{xml_key}"
            redacted_regex = rf"{xml_key}\1>********</{xml_key}"
            # Delete operation has no end tag and and redaction should not be attempted.
            #
            # Redact this:
            # <tag operation="set">secret</tag>
            #
            # Don't try to redact this:
            # <tag operation="del" />
            xml_string = re.sub(
                start_tag_end_tag_regex,
                redacted_regex,
                xml_string,
            )
        if is_bytes:
            xml_string = xml_string.encode("utf-8")
        return xml_string

    def redact_result_xml(
        self,
        security_result: Union[str, bytes, List[int]],
        secret_traits: dict,
        racf_trait_and_message_key_map: dict = {},
    ) -> str:
        r"""
        Redacts a list of specific secret traits in a result xml string.
        Based on the following RACF command patterns:
            'TRAIT (value)'
            'TRAIT (subtrait1(value) subtrait2(value))
            "TRAIT ('value')"
        This function also accounts for varied amounts of whitespace in the pattern.

        This function employs the following regular expression:
        <message>([A-Z]*[0-9]*[A-Z]) [^<>]*{racf_key.upper()}[^<>]*<\/message>" -
        Designed to match the above pattern by starting and ending with the message xml tag
        string as shown, the value of the message is targeted based on the racf_key. This
        should capture only messages that contain information about a redacted key.
        The message identifier is "captured" as a variable and preserved by the substitution
        operation through the use of the \1 supplied in the replacement string.
        """
        if isinstance(security_result, list):
            return security_result
        for xml_key in secret_traits.values():
            racf_key = xml_key.split(":")[1] if ":" in xml_key else xml_key
            if racf_key in racf_trait_and_message_key_map.get("trait_map", {}):
                racf_key = racf_trait_and_message_key_map["trait_map"][racf_key]
            racf_command_argument_regex = rf"{racf_key.upper()}( +){{0,}}\("
            if isinstance(security_result, bytes):
                match = re.search(
                    racf_command_argument_regex, security_result.decode("cp1047")
                )
            else:
                match = re.search(rf"{racf_key.upper()}( +){{0,}}\(", security_result)
            if not match:
                continue
            security_result = self.__redact_string(security_result, racf_key)
            if racf_key in racf_trait_and_message_key_map.get("message_map", {}):
                racf_key = racf_trait_and_message_key_map["message_map"][racf_key]
            racf_message_regex = (
                r"<message>([A-Z]*[0-9]*[A-Z]) [^<>]*"
                + rf"{racf_key.upper()}[^<>]*<\/message>"
            )
            redacted_racf_message_regex = (
                rf"<message>REDACTED MESSAGE CONCERNING {racf_key.upper()}, "
                + r"REVIEW DOCUMENTATION OF \1 FOR MORE INFORMATION</message>"
            )
            if isinstance(security_result, bytes):
                security_result = re.sub(
                    racf_message_regex,
                    redacted_racf_message_regex,
                    security_result.decode("cp1047"),
                ).encode("cp1047")
            else:
                security_result = re.sub(
                    racf_message_regex,
                    redacted_racf_message_regex,
                    security_result,
                )
        return security_result

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

    def log_hex_dump(
        self,
        raw_result_xml: bytes,
        secret_traits: dict,
        racf_trait_and_message_key_map: dict,
    ) -> None:
        """
        Log the raw result XML returned by IRRSMO00 as a hex dump.
        """
        hex_row = ""
        hex_row_size = 0
        interpreted_row = ""
        i = 0
        hex_dump = ""
        # Redact secrets from raw result because we are logging it to the console.
        raw_result_xml = self.redact_result_xml(
            raw_result_xml,
            secret_traits,
            racf_trait_and_message_key_map,
        )
        for byte in raw_result_xml:
            color_function = self.__green
            char = struct.pack("B", byte).decode("cp1047")
            # Non-displayable characters should be interpreted as '.'.
            match len(repr(char)):
                # All non-displayable characters should be red.
                # Two exceptions are 0x00 and 0xff, which are
                # overriden later on.
                case 6:
                    color_function = self.__red
                    char = "."
                # '\t', '\r', and '\n' control characters should be yellow.
                case 4:
                    color_function = self.__yellow
                    char = "."
            if byte == 0:
                # Null bytes (0x00) should have no color.
                # 'str()' will return an unmodified version of the string passed to it.
                color_function = str
            elif byte == 255:
                # 0xFF should be light blue.
                color_function = self.__light_blue
            hex_row += f"{color_function(hex(byte)[2:].rjust(2, '0'))}"
            hex_row_size += 2
            interpreted_row += f"{color_function(char)}"
            i += 1
            if i % 2 == 0:
                hex_row += " "
                hex_row_size += 1
            if i % 16 == 0:
                row_index = hex(i - 16)[2:].rjust(8, "0")
                hex_dump += f"{row_index}: {hex_row} {interpreted_row}\n"
                hex_row = ""
                hex_row_size = 0
                interpreted_row = ""
        if interpreted_row != "":
            row_index = hex(i - len(interpreted_row))[2:].rjust(8, "0")
            interpreted_row = " " * (40 - hex_row_size) + interpreted_row
            hex_dump += f"{row_index}: {hex_row} {interpreted_row}\n"
        self.log_debug("Hex Dump", hex_dump)
