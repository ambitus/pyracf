# Getters and Setters

## `get_uacc`
```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_uacc("ESWIFT.TEST.T1136242.P3020470")
'alter'
```

## `set_uacc`
```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.set_uacc("ESWIFT.TEST.T1136242.P3020470","READ")
{'securityresult': {'dataset': {'name': 'ESWIFT.TEST.T1136242.P3020470', 'operation': 'set', 'generic': 'no', 'requestid': 'DatasetRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (READ)"}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `get_your_acc`
```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_your_acc("ESWIFT.TEST.T1136242.P3020470")
'alter'
```

&nbsp;

# Run Data Set Profile Administration Samples

:warning: _Run samples from the `irrsmo00` directory._

## Add a Dataset Profile

```shell
$ python3 samples/dataset/add_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "set",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ADDSD                ('ESWIFT.TEST.T1136242.P3020470') "
                },
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (None) OWNER       (eswift)"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Alter a Dataset Profile

```shell
$ python3 samples/dataset/alter_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "set",
            "generic": "no",
            "requestid": "DatasetRequest",
            "info": [
                "Definition exists. Add command skipped due  to precheck option"
            ],
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Read) OWNER       (eswift)"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Delete a Dataset Profile

```shell
$ python3 samples/dataset/delete_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "del",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "DELDSD               ('ESWIFT.TEST.T1136242.P3020470') "
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Extract a Dataset Profile

```shell
$ python3 samples/dataset/extract_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "listdata",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470') ",
                    "message": "NO INSTALLATION DATA",
                    "profile": {
                        "base": {
                            "level": 0,
                            "owner": "eswift",
                            "universal access": "read",
                            "warning": null,
                            "erase": null,
                            "auditing": "failures(read)",
                            "notify": null,
                            "your access": "alter",
                            "creation group": "sys1",
                            "dataset type": "non-vsam",
                            "volumes on which dataset resides": "usrat2",
                            "installation data": null
                        }
                    }
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```