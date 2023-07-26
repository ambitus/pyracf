---
layout: default
grand_parent: Dataset Admin
parent: Standard
---

# Dataset Access Attribute

Dataset administration functions for checking a user's Dataset Access Attribute. 
{: .fs-6 .fw-300 }

## `DatasetAdmin.get_universal_access()`

```python
def get_universal_access(self, dataset: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check the **Universal Access Attribute** for a dataset profile.

#### 📥 Parameters
* `dataset`<br>
  The **Dataset Profile** for which RACF should check the universal access attribute.

#### 📤 Returns
* `Union[str,bytes,None]`<br>
  Returns `None` when the dataset profile has no **Universal Access** defined, otherwise returns the access level as a string. If the `DatasetAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470")
"read"
```

## `DatasetAdmin.set_universal_access()`

```python
def set_universal_access(self, dataset: str, universal_access: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Set the **Universal Access Attribute** for a dataset profile.

#### 📥 Parameters
* `dataset`<br>
  The **Dataset Profile** for which RACF should set the universal access attribute.

* `universal_access`<br>
  The **Universal Access** level to assign to the specified dataset profile.

#### 📤 Returns
* `Union[str,bytes,None]`<br>
  Returns `None` when the dataset profile has no **Universal Access** defined, otherwise returns the access level as a string. If the `DatasetAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470","ALTER")
{"securityResult":{"dataSet":{"name":"ESWIFT.TEST.T1136242.P3020470","operation":"set","generic":"no","requestId":"DatasetRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Alter)"}]},"returnCode":0,"reasonCode":0}}
```

```json
{
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
```