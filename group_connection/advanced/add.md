---
layout: default
grand_parent: Group Connection Admin
parent: Advanced
---

# Add

Create a new group connection.
{: .fs-6 .fw-300 }

## `ConnectionAdmin.add()`

```python
def add(self, userid: str, group: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Traits** are considered **Stable**. See [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

Create a new **group connection**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to connect to the specified group.
* `group`<br>
  The **group** to connect the specified user to.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the user within the group on creation of the connection. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Group Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **creates** a **new group connection** where the **z/OS userid** `squidwrd` is connected to the **group** `testgrp0` with two **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import ConnectionAdmin
connection_admin = ConnectionAdmin()

traits = {
    "base:auditor": True,
    "base:operations": True,
}

connection_admin.add("squidwrd", "testgrp0", traits=traits)
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
          "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) AUDITOR      OPERATIONS  "
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```