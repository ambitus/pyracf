"""Update user access to a specific resource dynamically"""


from pyracf.access.access_admin import AccessAdmin
from pyracf.genprof.resource_admin import ResourceAdmin
from pyracf.setropts.setropts_admin import SetroptsAdmin


def update_access_dynamic(func: str = "add") -> int:
    """Entrypoint"""
    access_admin = AccessAdmin()
    setropts_admin = SetroptsAdmin()
    resource_admin = ResourceAdmin()

    test_profile = "TESTING"
    test_class = "ELIJTEST"
    test_access = "READ"
    test_id = "ESWIFT"

    curr_acc = resource_admin.get_your_acc(test_profile, test_class)
    if curr_acc is None:
        curr_acc = "None"
    print(f"Your access at start: {curr_acc}")

    if func == "add":
        if not resource_admin.get_your_acc(test_profile, test_class) is None:
            print(
                f"You have at least READ access to {test_profile} of class {test_class}"
                " already. Exiting now..."
            )
            return 0
        traits = {
            "resourcename": test_profile,
            "classname": test_class,
            "access": test_access,
            "id": test_id,
        }
        result = access_admin.add(traits)
        if not (
            result["securityresult"]["permission"]["commands"][0]["safreturncode"] == 0
            and result["securityresult"]["permission"]["commands"][0]["returncode"] == 0
        ):
            print(
                f"Failed to define {test_access} access to {test_profile} of class: {test_class}"
                f" for userid: {test_id}. Exiting now..."
            )
            return -1
        print(
            f"Defined {test_access} access to {test_profile} of class: {test_class}"
            f" for userid: {test_id}."
        )
    else:
        if resource_admin.get_your_acc(test_profile, test_class) is None:
            print(
                f"You have no access to {test_profile} of class {test_class}"
                " already. Exiting now..."
            )
            return 0
        traits = {
            "resourcename": test_profile,
            "classname": test_class,
            "id": test_id,
        }
        result = access_admin.delete(traits)
        if not (
            result["securityresult"]["permission"]["commands"][0]["safreturncode"] == 0
            and result["securityresult"]["permission"]["commands"][0]["returncode"] == 0
        ):
            print(
                f"Failed to delete permission to {test_profile} of class: {test_class}"
                f" for userid: {test_id}. Exiting now..."
            )
            return -1
        print(
            f"Deleted permission to {test_profile} of class: {test_class} for userid: {test_id}."
        )

    curr_acc = resource_admin.get_your_acc(test_profile, test_class)
    if curr_acc is None:
        curr_acc = "None"
    if func == "add":
        print(f"Your access after definition: {curr_acc}")
    else:
        print(f"Your access after deletion: {curr_acc}")

    class_types = setropts_admin.get_class_types(test_class)
    if "raclist" not in " ".join(class_types):
        print(f"Class {test_class} is not RACLISTED, access is updated. Exiting now...")
        return 0

    setropts_admin.refresh(test_class)
    print(f"Issued RACLIST REFRESH for class {test_class}")

    curr_acc = resource_admin.get_your_acc(test_profile, test_class)
    if curr_acc is None:
        curr_acc = "None"
    print(f"Your access after refresh: {curr_acc}")
    return 0
