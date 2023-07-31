---
layout: default
grand_parent: Access Admin
parent: Advanced
---

# Alter

Create a new permission.
{: .fs-6 .fw-300 }

## `AccessAdmin.alter()`

```python
    def alter(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
```

#### 📄 Description

Alter an existing **permission**.

#### 📥 Parameters
* `resource`<br>
  The **resource profile** to alter this permission to.
* `class`<br>
  The **class** that the specified resource profile belongs to.
* `auth_id`<br>
  The **z/OS userid or group name** of the user or group to receive the change in permission.

* `traits`<br>
  A dictionary of **traits/attributes** that should be assigned to this permission for the specified user to the specified resource. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Access Traits** are.

* `volume`<br>
  The **volume** that the specified dataset resides on (ignored unless the **class** is `DATASET`).
* `generic`<br>
  Specifies whether the resource is **generic** or not (ignored unless the **class** is `DATASET`).

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `AccessAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** an existing **permission** for the **z/OS userid** `eswift` to the **resource profile** `testing` in the **class** `elijtest` with one **trait/attribute** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import AccessAdmin
access_admin = AccessAdmin()

traits = {
    "base:access": "NONE",
}

access_admin.alter("TESTING", "ELIJTEST", "ESWIFT", traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "permission": {
      "name": "TESTING",
      "class": "ELIJTEST",
      "operation": "set",
      "requestId": "AccessRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "PERMIT               TESTING CLASS(ELIJTEST)  ACCESS      (NONE) ID          (ESWIFT)",
          "messages": [
            "ICH06011I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```