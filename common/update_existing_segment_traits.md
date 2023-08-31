---
layout: default
parent: Common
---

# Update Existing Segment Traits

Update existing valid secret traits dictionary.
{: .fs-6 .fw-300 }

&nbsp;

The existing `_valid_segment_traits` dictionary that defines the mappings between pyRACF segment/trait keys to IRRSMO00 XML fields can be **overlayed** with a user specified dictionary that defines custom mappings by setting the `update_existing_segment_traits` class attribute on any "Admin" object. This can allow for pyRACF to access custom field data in the `csdata` segment, and may also enable compatibility with other security managers with alternative mappings.

## Example

###### Python Script
```python 
from pyracf import UserAdmin

segment_traits = {
    "csdata": {
        "csdata:newfield": "newfield"
    }
}

user_admin = UserAdmin(update_existing_segment_traits=segment_traits)
```
