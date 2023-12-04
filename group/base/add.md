---
layout: default
grand_parent: Group Admin
parent: Base Functions
---

# Add

Create a new group.
{: .fs-6 .fw-300 }

## `GroupAdmin.add()`

```python
def add(self, group: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../segments_traits_operators#segments) and [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

Create a new **group**.

#### 📥 Parameters
* `group`<br>
  The **group** being created.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the group on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Group Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `GroupAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **group** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **creates** a **new group** called `testgrp0` with two **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import GroupAdmin
group_admin = GroupAdmin()

traits = {
    "ovms:gid": 1024,
    "ovm:gid": 512,
}

group_admin.add("testgrp0", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "group": {
      "name": "TESTGRP0",
      "operation": "set",
      "requestId": "GroupRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ADDGROUP TESTGRP0 "
        },
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTGROUP TESTGRP0  OMVS     (GID         (1024)) OVM      (GID         (512))"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```