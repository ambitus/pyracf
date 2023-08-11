---
layout: default
parent: Common
---

# Customize Field Data

Add or overwrite the field data used in pyracf.
{: .fs-6 .fw-300 }

&nbsp;

**Add field data**  allows a user to add additional fields to pyracf's `valid_segment_traits library`. This can allow for pyracf to access custom field data in the csdata segment, and may also allow functionality on other platforms with alternative trait mappings. This can be specified on any "Admin" object by setting the `add_field_data` class attribute to a dictionary containing the `valid_segment_traits` information for the new fields through the class constructor.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(add_field_data={'csdata:newfield':'newfield'})

```

&nbsp;

**Overwrite field data**  allows a user to overwrite the fields of pyracf's `valid_segment_traits` library. This can allow for pyracf to access custom field data in the csdata segment, and may also allow functionality on other platforms with alternative trait mappings. Another possible use case of this, would be to set up certain scripts with access to only a specific list of traits, thereby preventing them from even being capable of making certain changes. This can be specified on any "Admin" object by setting the `overwrite_field_data` class attribute to a dictionary containing the `valid_segment_traits` information for the new fields through the class constructor.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(overwrite_field_data={'base:password':'racf:password'})

```
