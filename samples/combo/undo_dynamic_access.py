from access.AccessAdmin import AccessAdmin
from setropts.SetroptsAdmin import SetroptsAdmin
from genprof.ResourceAdmin import ResourceAdmin
import json

def main():
    access_admin = AccessAdmin()
    setropts_admin = SetroptsAdmin()
    resource_admin = ResourceAdmin()

    testing_profile = "TESTING"
    testing_class = "ELIJTEST"
    testing_access = "READ"
    testing_id = "ESWIFT"

    curr_acc = resource_admin.get_your_acc(testing_profile,testing_class)
    if curr_acc == None:
        curr_acc = "None"
    print("Your access at start: %s" % curr_acc)
    
    traits = {
        "resourcename": testing_profile,
        "classname": testing_class,
        "id": testing_id
    }
    result = access_admin.delete(traits)
    if not (result['securityresult']['permission']['commands'][0]['safreturncode'] == 0 and result['securityresult']['permission']['commands'][0]['returncode'] == 0):
        print("Failed to delete permission to %s of class: %s for userid: %s. Exiting now..." % (testing_profile,testing_class,testing_id))
        return -1
    print("Deleted permission to %s of class: %s for userid: %s." % (testing_profile,testing_class,testing_id))

    curr_acc = resource_admin.get_your_acc(testing_profile,testing_class)
    if curr_acc == None:
        curr_acc = "None"
    print("Your access after permission deletion: %s" % curr_acc)

    class_types = setropts_admin.get_class_types(testing_class)
    if not ('raclist' in ' '.join(class_types)):
        print("Class %s is not RACLISTED, permission should be removed. Exiting now...")
    
    setropts_admin.refresh(testing_class)
    print("Issued RACLIST REFRESH for class %s" % testing_class)

    curr_acc = resource_admin.get_your_acc(testing_profile,testing_class)
    if curr_acc == None:
        curr_acc = "None"
    print("Your access after refresh: %s" % curr_acc)

if __name__ == "__main__":
    main()
