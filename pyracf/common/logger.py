"""Logging for pyRACF."""

import json
from typing import Union


class Logger:
    """Logging for pyRACF."""

    ansi_reset = "\033[0m"
    ansi_gray = "\033[2m"
    ansi_green = "\033[32m"
    ansi_blue = "\033[34m"
    ansi_orange = "\033[38;5;214m"
    ansi_cyan = "\033[96m"
    ansi_magenta = "\033[1;35m"

    debug_label = "[ Debug ]"

    def gray(self, string: str) -> str:
        """Make contents of string gray."""
        return self.__colorize_string(self.ansi_gray, string)

    def green(self, string: str) -> str:
        """Make contents of string green."""
        return self.__colorize_string(self.ansi_green, string)

    def blue(self, string: str) -> str:
        """Make contents of string blue."""
        return self.__colorize_string(self.ansi_blue, string)

    def orange(self, string: str) -> str:
        """Make contents of string orange."""
        return self.__colorize_string(self.ansi_orange, string)

    def cyan(self, string: str) -> str:
        """Make contents of string cyan."""
        return self.__colorize_string(self.ansi_cyan, string)

    def magenta(self, string: str) -> str:
        """Make contents of string magenta."""
        return self.__colorize_string(self.ansi_magenta, string)

    def __colorize_string(self, ansi_color: str, string: str) -> str:
        return f"{ansi_color}{string}{self.ansi_reset}"

    def log_dictionary(
        self, header_message: str, dictionary: dict, sanitize_string: Union[str, None]
    ) -> None:
        """JSONify and colorize a dictionary and log it to the console."""
        dictionary_json = json.dumps(dictionary, indent=4)
        if sanitize_string:
            dictionary_json = dictionary_json.replace(sanitize_string, "********")
        colorized_dictionary_json = self.colorize_json(dictionary_json)
        self.log_debug(f"{header_message}:\n\n{colorized_dictionary_json}")

    def log_debug(self, message: str) -> None:
        """Log function to use for debug logging."""
        print(f"{self.magenta(self.debug_label)} {message}")

    def colorize_json(self, json_text: str) -> str:
        """Add coloring to JSON string."""
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
                first_half = f"{tokens[0]}{self.cyan(key)}"
                second_half = self.__colorize_json_value(tokens[2:])
                line = first_half + second_half
            updated_json_text += f"{line}\n"
        return updated_json_text

    def __colorize_json_value(self, tokens: dict) -> str:
        if len(tokens) != 1:
            value = f'"{tokens[1]}"'
            second_half = f"{tokens[0]}{self.orange(value)}{''.join(tokens[2:])}"
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
                value = f"{self.blue(value)}"
            else:
                # numbers
                value = f"{self.green(value)}"
            second_half = f": {value}"
            if has_comma:
                second_half += ","
        return second_half

    def colorize_xml(self, xml_text: str) -> str:
        """Add coloring to XML string."""
        updated_xml_text = ""
        xml_lines = xml_text.splitlines()
        for line in xml_lines:
            tokens = line.split("<")
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
                if attributes[-1] == "/":
                    attributes = attributes[:-1]
                    tag_end = "/>"
            start_tag = (
                f"{self.gray(tag_start)}"
                + f"{self.blue(tag_name)}"
                + f"{self.__colorize_xml_attributes(attributes)}"
                + f"{self.gray(tag_end)}"
            )
            data = ""
            end_tag = ""
            if len(tokens) > 2:
                data = "".join(tokens[1].split(">")[1:])
                end_tag = (
                    f"{self.gray('</')}"
                    + f"{self.blue(tokens[-1][1:-1])}"
                    + f"{self.gray('>')}"
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
                        updated_xml_attributes += f"{self.orange(subtoken)} "
                    else:
                        updated_xml_attributes += f"{self.cyan(subtoken)}="
        return updated_xml_attributes.rstrip()

    def indent_xml(self, minified_xml: str) -> str:
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
            indented_xml += f"{'    ' * indent_level}{current_line}\n"
        return indented_xml[:-2]
