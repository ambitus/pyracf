---
layout: default
grand_parent: Data Set Admin
parent: Abstractions
---

# Universal Access

Data Set Profile Administration functions for checking a data set profile's Universal Access Attribute. 
{: .fs-6 .fw-300 }

## `DataSetAdmin.get_universal_access()`

```python
def get_universal_access(self, data_set: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check the **Universal Access Attribute** for a data set profile.

#### 📥 Parameters
* `data_set`<br>
  The **data set profile** for which RACF should check the universal access attribute.

#### 📤 Returns
* `Union[str, bytes, None]`<br>
  Returns `None` when the data set profile has no **Universal Access** defined, otherwise returns the access level as a string. If the `DataSetAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DataSetAdmin
>>> data_set_admin = DataSetAdmin()
>>> data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470")
"read"
```

## `DataSetAdmin.set_universal_access()`

```python
def set_universal_access(self, data_set: str, universal_access: str) -> Union[dict, bytes]:
```

#### 📄 Description

Set the **Universal Access Attribute** for a data set profile.

#### 📥 Parameters
* `data_set`<br>
  The **data set profile** for which RACF should set the universal access attribute.

* `universal_access`<br>
  The **Universal Access** level to set for the specified data set profile.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `DataSetAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **data set profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DataSetAdmin
>>> data_set_admin = DataSetAdmin()
>>> data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470","ALTER")
{"securityResult":{"dataSet":{"name":"ESWIFT.TEST.T1136242.P3020470","operation":"set","generic":"no","requestId":"DatasetRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Alter)"}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult": {
      "dataSet": {
        "name": "ESWIFT.TEST.T1136242.P3020470",
        "operation": "set",
        "generic": "no",
        "requestId": "DatasetRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Alter)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```