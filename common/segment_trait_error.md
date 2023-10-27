---
layout: default
parent: Common
---

# Segment Trait Error

Understanding the `SegmentTraitError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _A **Segment-Trait Combination** unknown to pyracf would generate an improper request to IRRSMO00. Pyracf will always raise a `SegmentTraitError` to bring attention to any unknown values prior to executing such a request._

&nbsp;

When any **Segment-Trait Combination** unknown to pyracf appears as a parameter to a request, a `SegmentError` will be raised to indicate that the request failed to build. A `SegmentError` can be handled as follows.

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
except SegmentError as e:
    print(e.message)
```

###### Console Output
```console
Unable to build Security Request.

'base:passwrd' is not a known segment-trait combination for 'user'.
'ovms:home' is not a known segment-trait combination for 'user'.
'ovms:program' is not a known segment-trait combination for 'user'.

```