---
layout: default
grand_parent: User Admin
parent: Advanced
---

# Add

Create a new z/OS userid.
{: .fs-6 .fw-300 }

## `UserAdmin.add()`

```python
def add(self, userid: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../segments_traits_operators#segments) and [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> * _pyRACF encodes the data it passes to RACF in Code Page `IBM-1047`._
> * _If you are entering a password or phrase with special or national characters, users logging on from terminals using differnt or international codepages may experience errors._
> * _Please consult a list of invariant characters to use for such passwords or phrases if this applies to you._

&nbsp;

Create a new **z/OS userid**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** being created.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the user on creation. See [Traits](../segments_traits_operators#traits) to see what all of the valid **User Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **z/OS userid** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

The following example **creates** a **new user** with a userid of `squidwrd` and serveral **traits/attributes** as defined in the `traits` dictionary.

###### Python Script
```python
from pyracf import UserAdmin
user_admin = UserAdmin()

traits = {
    "base:name": "Squidward",
    "base:password": "K29521IO",
    "base:owner": "leonard",
    "base:special": False,
    "base:operations": True,
    "omvs:uid": 2424,
    "omvs:home_directory": "/u/squidwrd",
    "omvs:default_shell": "/bin/sh",
}

user_admin.add("squidwrd", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "set",
      "requestId": "UserRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ADDUSER SQUIDWRD ",
          "messages": [
            "ICH01024I User SQUIDWRD is defined as PROTECTED."
          ]
        },
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "ALTUSER SQUIDWRD  PASSWORD    (********) OWNER       (leonard) NOSPECIAL      OPERATIONS   OMVS     (HOME        ('/u/squidwrd') PROGRAM     ('/bin/sh'))"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```