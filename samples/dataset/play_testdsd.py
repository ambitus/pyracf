from dataset.DatasetAdmin import DatasetAdmin
import json

def main():
    dataset_admin = DatasetAdmin()

    dsn = "ESWIFT.TEST.T1136242.P3020470"

    traits = {
        "datasetname": dsn,
        "uacc": "None",
        "owner": "eswift",
        "roles": "test1"
    }

    result = dataset_admin.add(traits)
    print(json.dumps(result, indent=4))
    print(dataset_admin.extract({'datasetname': dsn}))
    print(dataset_admin.add_role(dsn,"test2"))
    print(dataset_admin.extract({'datasetname': dsn}))
    print(dataset_admin.add_role(dsn,"test3"))
    print(dataset_admin.extract({'datasetname': dsn}))
    print(dataset_admin.remove_role(dsn,"test1"))
    print(dataset_admin.extract({'datasetname': dsn}))
    print(dataset_admin.no_roles(dsn))
    print(dataset_admin.extract({'datasetname': dsn}))



if __name__ == "__main__":
    main()
