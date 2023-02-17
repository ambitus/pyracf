from dataset.DatasetAdmin import DatasetAdmin
import json


def main():
    dataset_admin = DatasetAdmin()

    traits = {
        "datasetname": "ESWIFT.TEST.T1136242.P3020470"
    }

    result = dataset_admin.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
