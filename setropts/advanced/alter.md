---
layout: default
grand_parent: Setropts Admin
parent: Advanced
---

# Alter

Alter the current RACF Options.
{: .fs-6 .fw-300 }

## `SetroptsAdmin.alter()`

```python
def alter(self, options: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

Alter the current **RACF Options**.

#### 📥 Parameters
* `options`<br>
  A dictionary of the **RACF Options** being altered. See [Options](../options_operators#options) to see what all of the valid **RACF Options** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `SetroptsAdmin.generate_request_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** the RACF Options with **options** to alter specified in the `options` dictionary.


###### Python Script

```python
from pyracf import GrouAdmin
setropts_admin = SetroptsAdmin()

options = {
    "base:raclist": "ELIJTEST",
}

setropts_admin.alter(options=options)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "systemSettings": {
      "operation": "set",
      "requestId": "SetroptsRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "SETROPTS      RACLIST     (elijtest)",
          "messages": [
            "ICH14063I SETROPTS command complete."
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```