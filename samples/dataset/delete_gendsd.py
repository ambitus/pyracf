"""Delete a data set profile."""

import json

from pyracf.dataset.dataset_admin import DatasetAdmin


def main():
    """Entrypoint."""
    dataset_admin = DatasetAdmin()

    datasetname = "ESWIFT.TEST.**"

    result = dataset_admin.delete(datasetname)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
