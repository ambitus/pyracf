import getpass
import json

from pyracf import DownstreamFatalError, UserAdmin


def main():
    user_admin = UserAdmin()
    userid = getpass.getuser()
    profile = user_admin.extract(userid)
    json_profile = json.dumps(profile, indent=2)
    print(f"Profile extract for userid '{userid}' was successful:\n\n{json_profile}\n")

    # The following testcase is designed to test the DownstreamFatalError's null response
    # trigger by attempting to run as a userid for 'NOTAUSER' which is assumed to not
    # exist as a valid userid in this environment. If 'NOTAUSER' is a user, the test
    # will still function correctly as long as the tester does not have at least 'UPDATE'
    # access to 'NOTAUSER.IRRSMO00' in the 'SURROGAT' class.
    user_admin.set_running_userid("NOTAUSER")
    try:
        user_admin.extract(userid)
    except DownstreamFatalError as exception:
        if (
            (exception.saf_return_code == 8)
            and (exception.racf_return_code == 200)
            and (exception.racf_reason_code == 8)
        ):
            print(f"DownstreamFatalError occured as intended:\n\n{exception.message}\n")
            return 0
    return 1


if __name__ == "__main__":
    main()
