from pyracf import ResourceAdmin, SecurityRequestError


def setup_precheck():
    resource_admin = ResourceAdmin()
    try:
        access = resource_admin.get_my_access("IRR.IRRSMO00.PRECHECK", "XFACILIT")
    except SecurityRequestError:
        traits_precheck = {"base:universal_access": "None"}
        result = resource_admin.add(
            "IRR.IRRSMO00.PRECHECK", "XFACILIT", traits=traits_precheck
        )
        print(
            "'IRR.IRRSMO00.PRECHECK' is now defined with a 'Universal Access' of 'NONE'.\n"
            + "Contact your security administrator for 'READ' access before using pyRACF.\n"
            + "Other users of pyRACF will also need to have at least 'READ' access.\n"
            + "You may also need to refresh the 'XFACILIT' class.\n"
            + "Review our documentation at https://ambitus.github.io/pyracf/ as well!"
        )
        return result
    if access:
        print(
            "'IRR.IRRSMO00.PRECHECK' is already defined, "
            + f"and you already have '{access.upper()}' access!\n"
            + "You are ready to start using pyRACF!\n"
            + "Please ensure other users of pyRACF also have at least 'READ' access.\n"
            + "Review our documentation at https://ambitus.github.io/pyracf/ as well!"
        )
        return True
    print(
        "'IRR.IRRSMO00.PRECHECK' is already defined, but you have no access.\n"
        + "Contact your security administrator for 'READ' access before using pyRACF.\n"
        + "Review our documentation at https://ambitus.github.io/pyracf/ as well!"
    )
    return False
