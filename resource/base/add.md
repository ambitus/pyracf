---
layout: default
grand_parent: General Resource Admin
parent: Base Functions
---

# Add

Create a new general resource profile.
{: .fs-6 .fw-300 }

## `ResourceAdmin.add()`

```python
def add(self, resource: str, class_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../segments_traits_operators#segments) and [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

Create a new **general resource profile**.

#### 📥 Parameters
* `resource`<br>
  The name of the **general resource profile** being created.

* `class_name`<br>
  The name of the **class** the general resource profile being created belongs to.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **creates** a **new general resource profile** called `TESTING` in the `ELIJTEST` class with two **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()

traits = {
    "base:universal_access": "None",
    "base:owner": "eswift",
}

resource_admin.add("TESTING","ELIJTEST", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "resource": {
      "name": "TESTING",
      "class": "ELIJTEST",
      "operation": "set",
      "requestId": "ResourceRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "RDEFINE ELIJTEST             (TESTING) ",
          "messages": [
            "ICH10006I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        },
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "RALTER  ELIJTEST             (TESTING)  UACC        (None) OWNER       (eswift)",
          "messages": [
            "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
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