---
layout: default
parent: Common
---

# UserID Error

Understanding the `UserIdError` exception.
{: .fs-6 .fw-300 }

&nbsp;

When a caller specifies a **z/OS userid** for pyRACF to run commands under, an `UserIdError` will be raised if the specified **z/OS userid** is not a string from 1 to 8 characters in length. An `UserIdError` can be handled as follows.

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