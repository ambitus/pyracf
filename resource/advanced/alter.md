---
layout: default
grand_parent: General Resource Admin
parent: Advanced
---

# Alter

Alter an existing general resource profile.
{: .fs-6 .fw-300 }

## `ResourceAdmin.alter()`

```python
def alter(self, resource: str, class_name: str, traits: dict) -> Union[dict, bytes]:
```

{: .warning }
> _Alter operations in pyracf require READ access to IRR.IRRSMO00.PRECHECK in the XFACILIT class_
> _This function will not produce output unless the user running the command has this access._

#### 📄 Description

Alter an existing **general resource** profile.

#### 📥 Parameters
* `resource`<br>
  The name of the **resource** profile being altered.

* `class_name`<br>
  The name of the **class** the resource profile being altered belongs to.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** a resource profile called `ESWIFT.TEST.T1136242.P3020470` with **traits/attributes** to alter specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()

traits = {
    "base:universal_access": "Read",
    "base:owner": "eswift",
}

resource_admin.alter("TESTING","ELIJTEST", traits=traits)
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
      "info": [
        "Definition exists. Add command skipped due  to precheck option"
      ],
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "RALTER  ELIJTEST             (TESTING)  UACC        (Read) OWNER       (eswift)",
          "messages": [
            "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```