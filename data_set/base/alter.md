---
layout: default
grand_parent: Data Set Admin
parent: Base Functions
---

# Alter

Alter an existing data set profile.
{: .fs-6 .fw-300 }

## `DataSetAdmin.alter()`

```python
def alter(
    self, data_set: str, traits: dict, volume: Union[str, None] = None, generic: bool = False
) -> Union[dict, bytes]:
```


#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../segments_traits_operators#segments) and [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Alter operations in pyracf require READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class_
> _This function will not produce output unless the user running the command has this access._

&nbsp;

Alter an existing **data set profile**.

#### 📥 Parameters
* `data_set`<br>
  The name of the **data set profile** being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the data set profile on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Data Set Traits** are.

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
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **data set profile** cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **alters** a data set profile called `ESWIFT.TEST.T1136242.P3020470` with **traits/attributes** to alter specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import DataSetAdmin
data_set_admin = DataSetAdmin()

traits = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}

data_set_admin.alter("ESWIFT.TEST.T1136242.P3020470", traits=traits)
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
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```