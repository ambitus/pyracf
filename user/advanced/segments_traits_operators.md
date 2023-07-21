---
layout: default
grand_parent: User Admin
parent: Advanced
---

# Segments, Traits, and Operators

Relevant information about using `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .note }
> _The `base` segment is **always included** in **[`UserAdmin.extract()`](../../standard/extract#useradminextract)** by default._

&nbsp;

When using the **[`UserAdmin.extract()`](../../standard/extract#useradminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the other segments defined in `pyracf/user/user_admin.py` in the pyRACF source code.

&nbsp;

| **Segment** | **Description** |
| `omvs` | Describes a user's **z/OS Unix System Services** attributes. |

### Traits

&nbsp;

{: .note }
> _All **key-value pair traits** can be set to `False` in **[`UserAdmin.alter()`](../alter#useradminalter)** to indicate that they should be removed or unset._

&nbsp;

When using the **[`UserAdmin.add()`](../add#useradminadd)** and **[`UserAdmin.alter()`](../alter#useradminalter)** functions, the following are valid user traits. Feel free to experiment with any of the other traits defined in `pyracf/user/user_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:special` | Set to `True` to give a user **RACF Special** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:auditor` | Set to `True` to give a user **Auditor** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:operations` | Set to `True` to give a user **Operator** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:name` | Set a name of the person that the **z/OS userid** belongs to. | Add: `str`<br>Alter: `str`, `False` |
| `base:owner` | Set a **z/OS userid** as the owner of the **z/OS userid** being altered/created. | Add: `str`<br>Alter: `str`, `False` |
| `base:password` | Set a user's password. | Add: `str`<br>Alter: `str`, `False` |
| `base:class_authorizations` | Modify a user's **Class Authorizations**. | Add: `str`, `List[str]`<br>Alter: `str`, `List[str]` |
| `omvs:uid` | Set a user's **z/OS Unix System Services UID**. | Add: `int`, `str`<br>Alter: `int`, `str`, `False` |
| `omvs:home` | Set a user's **z/OS Unix System Services Home Directory**. | Add: `str`<br>Alter: `str`, `False` |
| `omvs:program` | Set the user's **z/OS Unix System Services Program/Default Shell**. | Add: `str`<br>Alter: `str`, `False` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| `base:class_authorizations` | Use the `add` operator to add new **Class Authorizations** and `remove` to remove **Class Authorizations**. |