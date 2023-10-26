---
layout: default
grand_parent: Setropts Admin
parent: Advanced
---

# Options and Operators

Information about setropts `options` dictionaries and `operators`.
{: .fs-6 .fw-300 }


### Options

&nbsp;

{: .experimental }
> _**Options** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .experimental }
> _All functionality dependent on **[`SetroptsAdmin.list_racf_options()`](../../standard/list_racf_options#setroptsadminlist_racf_options)** is considered **Experimental**. See **[`SetroptsAdmin.list_racf_options()`](../../standard/list_racf_options#setroptsadminlist_racf_options)** for more details._

&nbsp;

{: .note }
> _Some **Options** can be set to `False` to delete their existing values._

&nbsp;

When using the **[`SetroptsAdmin.alter()`](../alter#setroptsadminalter)** function, the following are valid setropts options. Feel free to experiment with any of the other options defined in `pyracf/setropts/setropts_admin.py` in the pyRACF source code.

&nbsp;

Options use the following syntax: `<segment>:<options>`

&nbsp;

| **Option** | **Description** | **Valid Types** |
| `base:raclist` | Add a class to the list of **raclisted** classes in RACF.  | `str` |
| `base:audit_classes` | Add a class to the list of **audited** classes in RACF. | `str` |
| `base:active_classes` | Add a class to the list of **active** classes in RACF.  | `str` |
| `base:statiscs_class` | Track **statistics** for a specicified class.  | `str` |
| `base:general_command_classes` | Allow **generic profile command** processing for a specified class. | `str` |
| `base:generic_profile_checking_classes` | Allow **generic profile checking** for a specified class. | `str` |
| `base:generic_profile_sharing_classes` | Allow sharing of in-storage **generic profiles** for a specified class. | `str` |
| `base:global_access_classes` | Add a class to the list of **global access checking** classes in RACF.  | `str` |
| `base:refresh` | **Refresh** the in-storage profiles for Genric, Global, or Raclist classes. | `bool` |

### Operators

Operators can be prepended to options using the following syntax: `<operator>:<segment>:<options>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Options

Operators are generally not needed for **key-value pair options**. For key-value pair options, setting the value to a non-`False` value with no operator will generally set or overwrite the option and setting the value to `False` will generally unset or disable the option.

### List Options

| **Option** | **Operator Usage** |
| `base:raclist` | Use the `add` operator to add new classes to the list of **raclisted** classes and `delete` to remove the class.  |
| `base:audit_class` | Use the `add` operator to add new classes to the list of **audited** classes and `delete` to remove the class.  |
| `base:active_class` | Use the `add` operator to add new classes to the list of **active** classes and `delete` to remove the class.  |
| `base:statiscs_class` | Use the `add` operator to add new classes to the list of classes with **statistics** tracked and `delete` to remove the class.  |
| `base:general_command_class` | Use the `add` operator to add new classes to the list of classes with **generic profile command** processing allowed and `delete` to remove the class.  |
| `base:generic_profile_checking_class` | Use the `add` operator to add new classes to the list of classes with **generic profile checking** allowed and `delete` to remove the class.  |
| `base:generic_profile_sharing_class` | Use the `add` operator to add new classes to the list of classes with **generic profile** sharing allowed and `delete` to remove the class.  |
| `base:global_access_class` | Use the `add` operator to add new classes to the list of classes with **global access** checking allowed and `delete` to remove the class.  |