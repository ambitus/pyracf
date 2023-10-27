---
layout: default
parent: Common
---

# Segment Error

Understanding the `SegmentError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _A **Segment** unknown to pyracf would generate an improper **EXTRACT** request to IRRSMO00. Pyracf will always raise a `SegmentError` to bring attention to any unknown values prior to executing such a request._

&nbsp;

When any **Segment** unknown to pyracf appears as a parameter to an **EXTRACT** request, a `SegmentError` will be raised to indicate that the request failed to build. A `SegmentError` can be handled as follows.

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