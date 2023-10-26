---
layout: default
parent: Common
---

# Replace Existing Segment Traits

Replace existing valid segment traits dictionary.
{: .fs-6 .fw-300 }

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

{: .note}
 > _The use of the word **replace** is used to indicate that the existing `_valid_segment_traits` dictionary that belongs to an "Admin" object will be comepletely replaced with the dictionary that the user specifies through the `replace_existing_segment_traits` constructor argument of said "Admin" object._

&nbsp;

The existing `_valid_segment_traits` dictionary belonging to an "Admin" object that defines the mappings between pyRACF segment/trait keys to IRRSMO00 XML fields can be **replaced** with a user specified dictionary that defines custom mappings by setting the `replace_existing_segment_traits` constructor of said "Admin" object. This can allow for pyRACF to access custom field data in the `csdata` segment, and may also enable compatibility with other security managers with alternative mappings. Another possible use case of this feature would be to implement tools/utilities that only have access to a specific set of traits, thereby preventing them from being able to make certain changes.

## Example

###### Python Script
```python
from pyracf import UserAdmin

segment_traits = {
    "base" : {
        "base:password": "racf:password"
    }
}

user_admin = UserAdmin(replace_existing_segment_traits=segment_traits)
```
