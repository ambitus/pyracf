---
layout: default
grand_parent: Dataset Admin
parent: Advanced
---

# Add

Create a new dataset profile.
{: .fs-6 .fw-300 }

## `DatasetAdmin.add()`

```python
def add(
    self, data_set: str, traits: dict, volume: Union[str, None] = None, generic: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Create a new **dataset** profile.

#### 📥 Parameters
* `data_set`<br>
  The name of the **dataset** profile being created.

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

The following example **creates** a **new dataset** profile called `ESWIFT.TEST.T1136242.P3020470` with two **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import DatasetAdmin
dataset_admin = DatasetAdmin()

traits = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

dataset_admin.add("ESWIFT.TEST.T1136242.P3020470", traits=traits)
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
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ADDSD                ('ESWIFT.TEST.T1136242.P3020470')"
        },
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (None) OWNER       (eswift)"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```

#### 💻 Example

The following example **creates** a **new generic dataset** profile called `ESWIFT.TEST.**` with two **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import DatasetAdmin
dataset_admin = DatasetAdmin()

traits = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

dataset_admin.add("ESWIFT.TEST.**", traits=traits, generic=True)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "dataSet": {
      "generic": "yes",
      "name": "ESWIFT.TEST.**",
      "operation": "set",
      "requestId": "DatasetRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ADDSD                ('ESWIFT.TEST.**')  GENERIC     "
        },
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTDSD               ('ESWIFT.TEST.**')  GENERIC      UACC        (None) OWNER       (eswift)"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```