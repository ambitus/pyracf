---
layout: default
grand_parent: Common
parent: Exceptions
---

# Segment Trait Error

Understanding the `SegmentTraitError` exception.
{: .fs-6 .fw-300 }


&nbsp;

When any unknown **Segment-Trait Combination** is provided in the parameters to a **Non-Profile Extract** request, a `SegmentTraitError` will be raised to indicate that the request cannot be built. A `SegmentTraitError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import SegmentError

user_admin = UserAdmin()
traits = {
    "base:name": "Squidward",
    "base:passwrd": "K29521IO",
    "base:owner": "leonard",
    "base:special": False,
    "base:operations": True,
    "omvs:uid": 2424,
    "omvs:home": "/u/squidwrd",
    "omvs:program": "/bin/sh",
}

try:
    user_admin.alter("squidwrd", traits=traits)
except SegmentTraitError as e:
    print(e.message)
```

###### Console Output
```console
Unable to build Security Request.

'base:passwrd' is not a known segment-trait combination for 'user'.
'ovms:home' is not a known segment-trait combination for 'user'.
'ovms:program' is not a known segment-trait combination for 'user'.

```