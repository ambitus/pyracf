---
layout: default
parent: Common
---

# Update Existing Segment Traits

Update existing valid segment traits dictionary.
{: .fs-6 .fw-300 }

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

{: .note}
 > _The use of the word **update** is used to indicate that any mappings specified in the `update_existing_segment_traits` constructor argument of an "Admin" object will be written to the existing `_valid_segment_traits` dictionary belonging to said "Admin" object meaning that this results in a modification of the existing `_valid_segment_traits` dictionary. Any segment/trait mappings in the dictionary provided through the `update_existing_segment_traits` constructor argument of an "Admin" object that match segment/trait mappings in the existing `_valid_segment_traits` dictionary belonging to said "Admin" object will be replaced. Any segment/traits mappings in the dictionary provided through the `update_existing_sgement_traits` contructor argument of an "Admin" object that do **NOT** match segment/trait mappings in the existing `_valid_segment_traits` dictionary of said "Admin" object will be added._

&nbsp;

The existing `_valid_segment_traits` dictionary that defines the mappings between pyRACF segment/trait keys to IRRSMO00 XML fields can be **updated** using a user specified dictionary that defines custom mappings by setting the `update_existing_segment_traits` consturctor argument upon creation of any "Admin" object. This can allow for pyRACF to access custom field data in the `csdata` segment, and may also enable compatibility with other security managers with alternative mappings.

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
