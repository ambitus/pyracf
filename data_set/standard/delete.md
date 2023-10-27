---
layout: default
grand_parent: Data Set Admin
parent: Standard
---

# Delete

Delete a data set profile.
{: .fs-6 .fw-300 }

## `DataSetAdmin.delete()`

```python
def delete(
    self, data_set: str, volume: Union[str, None] = None, generic: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Delete a **data set profile**.

#### 📥 Parameters
* `data_set`<br>
  The name of the **data set profile** being deleted.

* `volume`<br>
  A single **volume** name for this data set profile. This argument is optional. If `generic=True` is specified, volume is ignored.

* `generic`<br>
  A bool indicating whether to treat this profile as **generic** or not. This argument is optional and defaults to `False`.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `DataSetAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DataSetAdmin
>>> data_set_admin = DataSetAdmin()
>>> data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470")
{"securityResult":{"dataSet":{"name":"ESWIFT.TEST.T1136242.P3020470","operation":"del","generic":"no","requestId":"DatasetRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"DELDSD               ('ESWIFT.TEST.T1136242.P3020470')"}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "dataSet": {
      "name": "ESWIFT.TEST.T1136242.P3020470",
      "operation": "del",
      "generic": "no",
      "requestId": "DatasetRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "DELDSD               ('ESWIFT.TEST.T1136242.P3020470')"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```