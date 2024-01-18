---
layout: default
grand_parent: Access Admin
parent: Base Functions
---

# Permit

Create or change a permission
{: .fs-6 .fw-300 }

## `AccessAdmin.permit()`

```python
def permit(
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

&nbsp;

{: .experimental }
> _Only a subset of available **Traits** are considered **Stable**. See [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

Create or change a **permission**.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** to permit this permission to.
* `class`<br>
  The **class** that the specified resource profile belongs to.
* `auth_id`<br>
  The **z/OS userid or group name** of the user or group to receive the change in permission.

* `traits`<br>
  A dictionary of **traits/attributes** that should be assigned to this permission for the specified user to the specified resource. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Access Traits** are.

* `volume`<br>
  The **volume** that the specified data set resides on (ignored unless the **class** is `DATASET`).
* `generic`<br>
  Specifies whether the resource is **generic** or not (ignored unless the **class** is `DATASET`).

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `AccessAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **permits** an existing **permission** for the **z/OS userid** `eswift` to the **general resource profile** `testing` in the **class** `elijtest` with one **trait/attribute** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import AccessAdmin
access_admin = AccessAdmin()

traits = {
    "base:access": "NONE",
}

access_admin.permit("TESTING", "ELIJTEST", "ESWIFT", traits=traits)
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
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```