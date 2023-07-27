---
layout: default
grand_parent: Data Set Admin
parent: Advanced
---

# Alter

Alter an existing dataset profile.
{: .fs-6 .fw-300 }

## `DatasetAdmin.alter()`

```python
def alter(
    self, data_set: str, traits: dict, volume: Union[str, None] = None, generic: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Alter an existing **dataset** profile.

#### 📥 Parameters
* `data_set`<br>
  The name of the **dataset** profile being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the dataset on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Dataset Traits** are.

* `volume`<br>
  A single **volume** name for this dataset. This argument is optional. If generic=`yes` is specified, volume is ignored.

* `generic`<br>
  A bool indicating whether to treat this profile as **generic** or not. This argument is optional and defaults to `no`.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `DatasetAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** a dataset profile called `ESWIFT.TEST.T1136242.P3020470` with **traits/attributes** to alter specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import DatasetAdmin
dataset_admin = DatasetAdmin()

traits = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}

dataset_admin.alter("ESWIFT.TEST.T1136242.P3020470", traits=traits)
```

###### Security Result Dictionary as JSON
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
          "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Read) OWNER       (eswift)"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```