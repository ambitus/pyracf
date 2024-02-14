---
layout: default
grand_parent: Common
parent: Exceptions
---

# Alter Operation Error

Understanding the `AlterOperationError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _An **Alter** operation targeting a profile that does **NOT** exist already could end up effectively performing an **Add** operation to create a new profile. pyRACF will always raise an `AlterOperationError` and refuse to perform the requested operation to bring attention to this condition._

&nbsp;

Prior to executing an **Alter** operation, a **Profile Extract** is attempted to determine whether the profile already exists. If the **Return Code** and the **Messages** returned by the **Extract** operation indicate that the profile does **NOT** exist, an `AlterOperationError` will be raised and the requseted **Alter** operation will **NOT** be executed. An `AlterOperationError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import AlterOperationError

user_admin = UserAdmin()

try:
    user_admin.alter("squidwrd")
except AlterOperationError as e:
    print(e.message)
```

###### Console Output
```console
Refusing to make security request to IRRSMO00.

Target profile 'squidwrd' does not exist as a 'user' profile.
```