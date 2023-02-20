import json

from pyracf.dataset.DatasetAdmin import DatasetAdmin


def main():
    dataset_admin = DatasetAdmin()

    traits = {
        "datasetname": "ESWIFT.TEST.T1136242.P3020470",
        "uacc": "Read",
        "owner": "eswift",
    }

    result = dataset_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
