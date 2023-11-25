from pyracf import ResourceAdmin, SecurityRequestError


def define_precheck_profile():
    resource_admin = ResourceAdmin()
    try:
        access = resource_admin.get_my_access("IRR.IRRSMO00.PRECHECK", "XFACILIT")
    except SecurityRequestError:
        traits_precheck = {"base:universal_access": "None"}
        result = resource_admin.add(
            "IRR.IRRSMO00.PRECHECK", "XFACILIT", traits=traits_precheck
        )
        print(
            "IRR.IRRSMO00.PRECHECK is now defined with a `Universal Access` of None."
            + "\nContact your security administrator for READ access before using pyRACF."
            + "\nOther users of pyRACF will also need to have at least read access."
            + "\nYou may also need to REFRESH the `XFACILIT` class."
            + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!"
        )
        return result
    if access:
        print(
            f"IRR.IRRSMO00.PRECHECK is already defined, and you already have {access} access!"
            + "\nYou are ready to start using pyRACF!"
            + "\nPlease ensure other users of pyRACF also have at least read access."
            + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!"
        )
        return True
    print(
        "IRR.IRRSMO00.PRECHECK is already defined, but you have no access."
        + "\nContact your security administrator for READ access before using pyRACF."
        + "\nReview our documentation at https://ambitus.github.io/pyracf/ as well!"
    )
    return False
