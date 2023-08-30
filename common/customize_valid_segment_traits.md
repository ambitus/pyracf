---
layout: default
parent: Common
---

# Customize Valid Segment Traits

Add to or overwrite the valid segment traits used in pyracf.
{: .fs-6 .fw-300 }

&nbsp;

**Update existing segment traits**  allows a user to add additional fields to pyracf's `valid_segment_traits` library. This can allow for pyracf to access custom field data in the csdata segment, and may also allow functionality on other platforms with alternative trait mappings. This can be specified on any "Admin" object by setting the `update_existing_segment_traits` class attribute to a dictionary containing the `valid_segment_traits` information for the new fields through the class constructor.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(update_existing_segment_traits={'csdata':{'csdata:newfield':'newfield'}})

```

&nbsp;

**Overwrite segment traits**  allows a user to overwrite the fields of pyracf's `valid_segment_traits` library. This can allow for pyracf to access custom field data in the csdata segment, and may also allow functionality on other platforms with alternative trait mappings. Another possible use case of this, would be to set up certain scripts with access to only a specific list of traits, thereby preventing them from even being capable of making certain changes. This can be specified on any "Admin" object by setting the `overwrite_segment_traits` class attribute to a dictionary containing the `valid_segment_traits` information for the new fields through the class constructor.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(overwrite_segment_traits={'base':{'base:password':'racf:password'}})

```
