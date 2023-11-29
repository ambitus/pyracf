"""Exception to use when no data is returned by IRRSMO00."""
from typing import Union


class NullResponseError(Exception):
    """
    Raised when no xml string is returned by IRRSMO00.
    """

    def __init__(self, xml_str: str, run_as_userid: Union[str, None] = None) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.saf_return_code = xml_str[0]
        self.racf_return_code = xml_str[1]
        self.racf_reason_code = xml_str[2]
        self.message += (
            f"\nSAF Return Code: {self.saf_return_code} / RACF Return Code:"
            + f" {self.racf_return_code} / RACF Reason Code: {self.racf_reason_code}"
        )
        if (
            (self.saf_return_code == 8)
            and (self.racf_return_code == 200)
            and (self.racf_reason_code == 16)
        ):
            self.message += (
                "\n\nCheck to see if the proper RACF permissions are in place.\n"
                + "For `set` or `alter` functions, you must have at least READ "
                + "access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class."
            )
        elif (
            (self.saf_return_code == 8)
            and (self.racf_return_code == 200)
            and (self.racf_reason_code == 8)
        ):
            self.message += (
                "\n\nCheck to see if the proper RACF permissions are in place.\n"
                + "For the `run_as_userid` feature, you must have at least UPDATE"
                + f" access to `{run_as_userid}.IRRSMO00` in the `SURROGAT` class."
            )
        else:
            self.message += (
                "\n\nPlease check the specified return and reason codes against"
                + " the IRRSMO00 documented return and reason codes for more information"
                + " about this error.\n"
                + "(https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes)"
            )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message
