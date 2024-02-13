"""Exception to use when IRRSMO00 is unable to process a request."""

from typing import Union


class DownstreamFatalError(Exception):
    """
    Raised when IRRSMO00 returns with a SAF Return Code of 8,
    indicating that the request could not be processed.
    """

    def __init__(
        self,
        saf_return_code: int,
        racf_return_code: int,
        racf_reason_code: int,
        request_xml: bytes,
        run_as_userid: Union[str, None] = None,
        result_dictionary: dict = None,
    ) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.saf_return_code = saf_return_code
        self.racf_return_code = racf_return_code
        self.racf_reason_code = racf_reason_code
        self.request_xml = request_xml.decode("utf-8")
        self.message += (
            f"\n\nSAF Return Code: {self.saf_return_code}\nRACF Return Code:"
            + f" {self.racf_return_code}\nRACF Reason Code: {self.racf_reason_code}"
        )
        if result_dictionary is not None:
            self.message += (
                "\n\nSee results dictionary "
                + f"'{self.__class__.__name__}.result' for more details.\n"
                + "\n\nYou can also check the specified return and reason codes against "
                + "the documented IRRSMO00 return and reason codes for more information "
                + "about this error.\n"
                + "https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes"
            )
            self.result = result_dictionary
        elif (
            (self.saf_return_code == 8)
            and (self.racf_return_code == 200)
            and (self.racf_reason_code == 16)
        ):
            self.message += (
                "\n\nCheck to see if the proper RACF permissions are in place.\n"
                + "For 'set' or 'alter' functions, you must have at least 'READ' "
                + "access to 'IRR.IRRSMO00.PRECHECK' in the 'XFACILIT' class."
            )
        elif (
            (self.saf_return_code == 8)
            and (self.racf_return_code == 200)
            and (self.racf_reason_code == 8)
        ):
            self.message += (
                "\n\nCheck to see if the proper RACF permissions are in place.\n"
                + "For the 'run_as_userid' feature, you must have at least 'UPDATE' "
                + f"access to '{run_as_userid.upper()}.IRRSMO00' in the 'SURROGAT' class."
            )
        else:
            self.message += (
                "\n\nPlease check the specified return and reason codes against "
                + "the documented IRRSMO00 return and reason codes for more information "
                + "about this error.\n"
                + "https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes"
            )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message
