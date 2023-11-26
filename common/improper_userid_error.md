---
layout: default
parent: Common
---

# Improper UserID Error

Understanding the `ImproperUserIDError` exception.
{: .fs-6 .fw-300 }

&nbsp;

When a caller specifies a **z/OS userid** for pyRACF to run commands under, an `ImproperUserIDError` will be raised if the specified **z/OS userid** is not a string from 1 to 8 characters in length. An `ImproperUserIDError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import ImproperUserIDError

user_admin = UserAdmin()

try:
    user_admin.set_running_userid("squidwrdtest")
except ImproperUserIDError as e:
    print(e.message)
```

###### Console Output
```console
Cannot run under this userid. SQUIDWRDTEST is not a string from 1 to 8 characters in length.

```