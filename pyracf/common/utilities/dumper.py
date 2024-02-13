"""Create raw dump files containing raw result XML returned by IRRSMO00."""

import hashlib
import os
from datetime import datetime


class Dumper:
    def raw_dump(self, raw_result_xml: bytes) -> str:
        """Dump raw result XML returned by IRRSMO00 to a dump file."""
        dot_pyracf_directory = os.path.join(os.path.expanduser("~"), ".pyracf")
        dump_directory = os.path.join(dot_pyracf_directory, "dump")
        if not os.path.exists(dump_directory):
            os.makedirs(dump_directory, mode=0o700)
        # umask may override the permission bits we set
        # upon creation of directories. It also is a possiblity
        # that existing directories have permssion bits set that
        # are too permissive, so always exlpicitely setting the
        # the permission bits on directories using os.chmod()
        # ensures that directories always have the the correct
        # permissions.
        if oct(os.stat(dot_pyracf_directory).st_mode)[-3:] != "700":
            os.chmod(dot_pyracf_directory, 0o700)
        if oct(os.stat(dump_directory).st_mode)[-3:] != "700":
            os.chmod(dump_directory, 0o700)
        timestamp = self.__get_timestamp()
        md5_hash = hashlib.md5(raw_result_xml).hexdigest()
        dump_file_name = f"pyracf.{timestamp}.{md5_hash}.dump"
        dump_file_path = os.path.join(dump_directory, dump_file_name)
        with open(dump_file_path, "wb", opener=self.__opener) as dump_file_writer:
            dump_file_writer.write(raw_result_xml)
        return dump_file_path

    def __opener(self, path: str, flags: int) -> int:
        return os.open(path, flags, 0o600)

    def __get_timestamp(self) -> str:
        """
        'datetime' is immutable, so we need this function to allow the
        timestamp generataion function to be mocked for unit tests.
        """
        return datetime.now().strftime("%Y%m%d-%H%M%S")
