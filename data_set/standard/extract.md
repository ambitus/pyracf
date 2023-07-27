---
layout: default
grand_parent: Data Set Admin
parent: Standard
---

# Profile Extract

Functions for extracting a dataset profile's data. 
{: .fs-6 .fw-300 }

## `DatasetAdmin.extract()`

```python
def extract(
    self, data_set: str, segments: dict = {}, volume: Union[str, None] = None, generic: bool = False, profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Extract a **dataset** profile's data.

#### 📥 Parameters
* `data_set`<br>
  The **dataset** profile to extract segment data from.

* `segments`<br>
  A dictionary of segments to extract. Each segment must be a boolean value where `True` indicates that the segment should be extracted and `False` indicates that the segment should not be extracted. Any segments omitted from the dictionary will not be extracted. The base sgement is included always.

* `volume`<br>
  A single **volume** name for this dataset. This argument is optional. If generic=`yes` is specified, volume is ignored.

* `generic`<br>
  A bool indicating whether to treat this profile as **generic** or not. This argument is optional and defaults to `no`.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_request_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **extracts** the **base segment** of the dataset profile `ESWIFT.TEST.T1136242.P3020470`. The base segment is extracted by default no other segments are specified or extracted. Also note that if any segments were specified in the `segments` dictionary with a value of `False`, those segments also would not be extracted.

###### Python REPL
```python
>>> from pyracf import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470")
{"securityResult":{"dataSet":{"name":"ESWIFT.TEST.T1136242.P3020470","operation":"listdata","generic":"no","requestId":"DatasetRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470')","profiles":[{"base":{"name":"eswift.test.t1136242.p3020470","level":0,"owner":"eswift","universalAccess":"read","warning":null,"erase":null,"auditing":{"failures":"read"},"notify":null,"yourAccess":"alter","creationGroup":"sys1","dataSetType":"non-vsam","volumes":["usrat2"],"installationData":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "dataSet": {
      "name": "ESWIFT.TEST.T1136242.P3020470",
      "operation": "listdata",
      "generic": "no",
      "requestId": "DatasetRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470')",
          "profiles": [
            {
              "base": {
                "name": "eswift.test.t1136242.p3020470",
                "level": 0,
                "owner": "eswift",
                "universalAccess": "read",
                "warning": null,
                "erase": null,
                "auditing": {
                  "failures": "read"
                },
                "notify": null,
                "yourAccess": "alter",
                "creationGroup": "sys1",
                "dataSetType": "non-vsam",
                "volumes": [
                  "usrat2"
                ],
                "installationData": null,
                "generic": false
              }
            }
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```

