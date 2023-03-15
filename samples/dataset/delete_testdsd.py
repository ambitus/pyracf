"""Delete a data set profile."""

import json

from pyracf.dataset.dataset_admin import DatasetAdmin


def main():
    """Entrypoint."""
    dataset_admin = DatasetAdmin()

    datasetname = "ESWIFT.TEST.T1136242.P3020470"

    result = dataset_admin.delete(datasetname)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
