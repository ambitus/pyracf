---
layout: default
grand_parent: Common
parent: Exceptions
---

# Segment Error

Understanding the `SegmentError` exception.
{: .fs-6 .fw-300 }

&nbsp;

When an unknown **Segment** is provided in the parameters to a **Profile Extract** request, a `SegmentError` will be raised to indicate that the request cannot be built. A `SegmentError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import SegmentError

user_admin = UserAdmin()

try:
    user_admin.extract("squidwrd", segments=["ovms","rso"])
except SegmentError as e:
    print(e.message)
```

###### Console Output
```console
Unable to build Security Request.

'rso' is not a known segment for 'user'.
'ovms' is not a known segment for 'user'.

```