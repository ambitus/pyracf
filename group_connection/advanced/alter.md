---
layout: default
grand_parent: Group Connection Admin
parent: Advanced
---

# Alter

Alter an existing group connection.
{: .fs-6 .fw-300 }

## `ConnectionAdmin.alter()`

```python
def alter(self, userid: str, group: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Traits** are considered **Stable**. See [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Alter operations in pyracf require READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class_
> _This function will not produce output unless the user running the command has this access._

&nbsp;

Alter an existing **group connection**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's connection to the specified group is being altered.
* `group`<br>
  The **group** where the specified user's connection is being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that will be altered for the specified user's connection to the specifed group. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Group Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alteres** an **existing group connection** where the connection of **z/OS userid** `squidwrd` to **group** `testgrp0` will be altered with the **traits/attributes** defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import ConnectionAdmin
connection_admin = ConnectionAdmin()

traits = {
    "base:auditor": False,
    "base:operations": False,
    "base:special": True
}

connection_admin.alter("squidwrd", "testgrp0", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "groupConnection": {
      "name": "SQUIDWRD",
      "group": "TESTGRP0",
      "operation": "set",
      "requestId": "ConnectionRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) NOAUDITOR      NOOPERATIONS   SPECIAL     "
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```