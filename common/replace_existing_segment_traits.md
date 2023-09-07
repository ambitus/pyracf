---
layout: default
parent: Common
---

# Replace Existing Segment Traits

Replace existing valid secret traits dictionary.
{: .fs-6 .fw-300 }

&nbsp;

The existing `_valid_segment_traits` dictionary that defines the mappings between pyRACF segment/trait keys to IRRSMO00 XML fields can be **replaced** with a user specified dictionary that defines custom mappings by setting the `replace_existing_segment_traits` class attribute on any "Admin" object. This can allow for pyRACF to access custom field data in the `csdata` segment, and may also enable compatibility with other security managers with alternative mappings. Another possible use case of this feature would be to implement tools/utilities that only have access to a specific set of traits, thereby preventing them from being able to make certain changes.

## Example

###### Python Script
```python
from pyracf import UserAdmin

segment_traits = {
    "base" : {
        "base:password": "racf:password"
    }
}

user_admin = UserAdmin(replace_segment_traits=segment_traits)
```
