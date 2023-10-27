---
layout: default
parent: Common
---

# Add Operation Error

Understanding the `AddOperationError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _An **Add** operation targeting an existing profile could end up effectively performing an **Alter** operation on this profile. Pyracf will always raise an `AddOperationError` to bring attention to these failures before attempting the **Add** operation._

&nbsp;

When pyracf executes an **Add** operation, it first performs an **Extract** to evaluate whether the profile already exists. If the **Return Code** and the **Messages** returned by the **Extract** operation indicate that the profile already exists, an `AddOperationError` will be raised to indicate that the request failed. An `AddOperationError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import AddOperationError

user_admin = UserAdmin()

try:
    user_admin.add("squidwrd")
except AddOperationError as e:
    print(e.message)
```

###### Console Output
```console
Security request made to IRRSMO00 failed.

Target profile 'squidwrd' already exists as a 'user' profile.
```