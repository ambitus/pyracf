---
layout: default
grand_parent: Group Admin
parent: Advanced
---

# Alter

Alter an existing group.
{: .fs-6 .fw-300 }

## `GroupAdmin.alter()`

```python
def alter(self, group: str, traits: dict) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .warning }
> _Alter operations in pyracf require READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class_
> _This function will not produce output unless the user running the command has this access._

&nbsp;

Alter an existing **group**.

#### 📥 Parameters
* `group`<br>
  The **group** being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be altered. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Group Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `GroupAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** a group called `testgrp0` with **traits/attributes** to alter specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import GroupAdmin
group_admin = GroupAdmin()

traits = {
    "omvs:gid": 2048,
    "ovm:gid": 256,
}

group_admin.alter("testgrp0", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "group": {
      "name": "TESTGRP0",
      "operation": "set",
      "requestId": "GroupRequest",
      "info": [
        "Definition exists. Add command skipped due  to precheck option"
      ],
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTGROUP TESTGRP0  OMVS     (GID         (2048)) OVM      (GID         (256))"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```