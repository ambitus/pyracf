---
layout: default
parent: Common
---

# Add Operation Error

Understanding the `AddOperationError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _An **Add** operation targeting an existing profile could end up effectively performing an **Alter** operation on an existing profile. pyRACF will always raise an `AddOperationError` and **refuse** to perform the requested operation to bring attention to this condition._

&nbsp;

Prior to executing an **Add** operation, a **Profile Extract** is attempted to determine whether the profile already exists. If the **Return Code** and the **Messages** returned by the **Profile Extract** operation indicate that the profile already exists, an `AddOperationError` will be raised and the requested **Add** operation will **NOT** be executed. An `AddOperationError` can be handled as follows.

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
Refusing to make security request to IRRSMO00.

Target profile 'squidwrd' already exists as a 'user' profile.
```