from pyracf.access.access_admin import AccessAdmin
from pyracf.genprof.resource_admin import ResourceAdmin
from pyracf.setropts.setropts_admin import SetroptsAdmin


def main():
    access_admin = AccessAdmin()
    setropts_admin = SetroptsAdmin()
    resource_admin = ResourceAdmin()

    testing_profile = "TESTING"
    testing_class = "ELIJTEST"
    testing_access = "READ"
    testing_id = "ESWIFT"

    curr_acc = resource_admin.get_your_acc(testing_profile, testing_class)
    if curr_acc is None:
        curr_acc = "None"
    print("Your access at start: %s" % curr_acc)

    if not (resource_admin.get_your_acc(testing_profile, testing_class) is None):
        print(
            "You have at least READ access to %s of class %s already. Exiting now..."
            % (testing_profile, testing_class)
        )
        return

    traits = {
        "resourcename": testing_profile,
        "classname": testing_class,
        "access": testing_access,
        "id": testing_id,
    }
    result = access_admin.add(traits)
    if not (
        result["securityresult"]["permission"]["commands"][0]["safreturncode"] == 0
        and result["securityresult"]["permission"]["commands"][0]["returncode"] == 0
    ):
        print(
            "Failed to define %s access to %s of class: %s for userid: %s. Exiting now..."
            % (testing_access, testing_profile, testing_class, testing_id)
        )
        return -1
    print(
        "Defined %s access to %s of class: %s for userid: %s."
        % (testing_access, testing_profile, testing_class, testing_id)
    )

    curr_acc = resource_admin.get_your_acc(testing_profile, testing_class)
    if curr_acc is None:
        curr_acc = "None"
    print("Your access after definition: %s" % curr_acc)

    class_types = setropts_admin.get_class_types(testing_class)
    if not ("raclist" in " ".join(class_types)):
        print(
            "Class %s is not RACLISTED, you should have your access. Exiting now..."
            % testing_class
        )
        return

    setropts_admin.refresh(testing_class)
    print("Issued RACLIST REFRESH for class %s" % testing_class)

    curr_acc = resource_admin.get_your_acc(testing_profile, testing_class)
    if curr_acc is None:
        curr_acc = "None"
    print("Your access after refresh: %s" % curr_acc)


if __name__ == "__main__":
    main()
