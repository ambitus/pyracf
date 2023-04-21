"""
Utilities for reading and transforming XML and dictionary samples.

Note that request samples should not include the "<?xml version='1.0' encoding='cp1047'?>"
header since the test cases use an override to dump request XML as utf-8, which causes the
xml generated to have no header.

Also note that XML and json samples should contain indintation for readability.
The 'minify_xml' function handles the process of removing leading/trailing
white space and new lines for XML files. JSON files are read into a dictionary
using the 'json' library.
"""

import json
import os
from typing import Union


def minify_xml(xml: Union[str, bytes]) -> Union[str, bytes]:
    """Remove leading/trailing white space and new lines."""
    tokens = [line.strip() for line in xml.splitlines()]
    if isinstance(xml, bytes):
        return b"".join(tokens)
    return "".join(tokens)


def get_xml(xml_file: str, mode="r") -> Union[str, bytes]:
    """Read in an XML sample."""
    if mode == "r":
        with open(xml_file, "r", encoding="utf-8") as xml_file_handle:
            return minify_xml(xml_file_handle.read())
    with open(xml_file, "rb") as xml_file_handle:
        return minify_xml(xml_file_handle.read())


def get_dictionary(json_file: str) -> dict:
    """Read in a dictionary sample from a JSON file."""
    with open(json_file, "r", encoding="utf-8") as json_file_handle:
        return json.load(json_file_handle)


def get_log(log_file: str) -> str:
    """Read in a log file sample as a string."""
    with open(log_file, "r", encoding="utf-8") as log_file_handle:
        return log_file_handle.read()


def get_sample(sample_file: str, function_group: str) -> Union[str, bytes]:
    """
    Read in a sample file based on the following folder and naming conventions:
    * <function group>/<function_group>_result_samples (result samples)
    * <function group>/<function_group>_request_samples (request samples)
    * <function group>/<function_group>_log_samples (log samples)
    * '.json' files get parsed into dictionaries
    * '.xml' files get loaded as strings for result samples and bytes objects for request samples.
    * '.log' files get loaded as strings.
    """
    pwd = os.path.dirname(__file__)
    result_samples = f"{pwd}/{function_group}/{function_group}_result_samples"
    request_samples = f"{pwd}/{function_group}/{function_group}_request_samples"
    log_samples = f"{pwd}/{function_group}/{function_group}_log_samples"
    if f"{function_group}_result" in sample_file:
        result_sample_file = f"{result_samples}/{sample_file}"
        if sample_file[-4:] == ".xml":
            return get_xml(result_sample_file)
        return get_dictionary(result_sample_file)
    if sample_file[-4:] != ".log":
        return get_xml(f"{request_samples}/{sample_file}", mode="rb")
    return get_log(f"{log_samples}/{sample_file}")
