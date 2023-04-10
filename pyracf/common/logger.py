"""Logging for pyRACF."""


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

    def log_debug(self, message: str) -> None:
        """Log function to use for debug logging."""
        print(f"{self.ansi_magenta}{self.debug_label}{self.ansi_reset} {message}")

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
                first_half = (
                    f'{tokens[0]}{self.ansi_cyan}"{tokens[1]}"{self.ansi_reset}'
                )
                second_half = self.__colorize_json_value(tokens[2:])
                line = first_half + second_half
            updated_json_text += f"{line}\n"
        return updated_json_text

    def __colorize_json_value(self, tokens: dict) -> str:
        if len(tokens) != 1:
            second_half = (
                f"{tokens[0]}"
                + f'{self.ansi_orange}"{tokens[1]}"{self.ansi_reset}'
                + f'{"".join(tokens[2:])}'
            )
        else:
            skip_values = ["{", "[", "{}", "[]"]
            if "," in tokens[0]:
                value = tokens[0][2:-1]
                has_comma = True
            else:
                value = tokens[0][2:]
                has_comma = False
            if value in skip_values:
                pass
            elif value == "null":
                value = f"{self.ansi_blue}{value}{self.ansi_reset}"
            else:
                value = f"{self.ansi_green}{value}{self.ansi_reset}"
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
            if tag_name[0] == "/":
                tag_start = "</"
                tag_name = tag_name[1:]
            if ">" in tag_name:
                tag_name = tag_name.split(">")[0]
                tag_tokens = []
            attributes = " ".join(tag_tokens[1:])[: -len(tag_end)]
            start_tag = (
                f"{self.ansi_gray}{tag_start}{self.ansi_reset}"
                + f"{self.ansi_blue}{tag_name}{self.ansi_reset}"
                + f"{self.__colorize_xml_attributes(attributes)}"
                + f"{self.ansi_gray}{tag_end}{self.ansi_reset}"
            )
            data = ""
            end_tag = ""
            if len(tokens) > 2:
                data = "".join(tokens[1].split(">")[1:])
                end_tag = (
                    f"{self.ansi_gray}</{self.ansi_reset}"
                    + f"{self.ansi_blue}{tokens[-1][1:-1]}{self.ansi_reset}"
                    + f"{self.ansi_gray}>{self.ansi_reset}"
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
                        updated_xml_attributes += (
                            f"{self.ansi_orange}{subtoken}{self.ansi_reset} "
                        )
                    else:
                        updated_xml_attributes += (
                            f"{self.ansi_cyan}{subtoken}{self.ansi_reset}="
                        )
        return updated_xml_attributes.rstrip()
