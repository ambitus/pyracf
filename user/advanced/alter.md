---
layout: default
grand_parent: User Admin
parent: Advanced
---

# Alter

Alter an existing z/OS userid.
{: .fs-6 .fw-300 }

## `UserAdmin.alter()`

```python
def alter(self, userid: str, traits: dict) -> Union[dict, bytes]:
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

{: .warning }
> * _pyRACF encodes the data it passes to RACF in Code Page `IBM-1047`._
> * _If you are entering a password or phrase with special or national characters, users logging on from terminals using differnt or international codepages may experience errors._
> * _Please consult a list of invariant characters to use for such passwords or phrases if this applies to you._


&nbsp;

Alter an existing **z/OS userid**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be altered. See [Traits](../segments_traits_operators#traits) to see what all of the valid **User Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **alters** a user with a userid of `squidwrd` and **traits/attributes** to alter are specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import UserAdmin
user_admin = UserAdmin()

traits = {
    "base:special": False,
    "base:operations": True,
    "omvs:home_directory": "/u/clarinet",
    "omvs:default_shell": False,
}

user_admin.alter("squidwrd", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "set",
      "requestId": "UserRequest",
      "info": [
        "Definition exists. Add command skipped due  to precheck option"
      ],
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTUSER SQUIDWRD  NOSPECIAL      OPERATIONS   OMVS     (HOME        ('/u/clarinet') NOPROGRAM     )"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```