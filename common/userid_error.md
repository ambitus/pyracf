---
layout: default
parent: Common
---

# UserID Error

Understanding the `UserIdError` exception.
{: .fs-6 .fw-300 }

&nbsp;

When the **Running Userid** is being set through an "Admin" object constructor or the `set_running_userid()` function on an "Admin" object, a `UserIdError` will be raised if the specified **z/OS userid** is not a string between 1 to 8 characters in length. A `UserIdError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import UserIdError

user_admin = UserAdmin()

try:
    user_admin.set_running_userid("squidwrdtest")
except UserIdError as e:
    print(e.message)
```

###### Console Output
```console
Unable to run as userid 'SQUIDWRDTEST'. Userid must be a string value between 1 to 8 characters in length.

```