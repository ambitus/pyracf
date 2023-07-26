---
layout: default
grand_parent: Group Connection Admin
parent: Advanced
---

# Segments, Traits, and Operators

Relevant information about using `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .warning }
> _There are no additional segments for **Group Connection** administartion._
> _Also, note that there is no **Profile Extract** function for **Group Connection** administration. Group connections can be extracted using **[`GroupAdmin.extract()`](../../../group/standard/extract#groupadminextract)**._

&nbsp;

### Traits

&nbsp;

{: .note }
> _All **key-value pair traits** can be set to `False` in **[`ConnectionAdmin.alter()`](../alter#connectionadminalter)** to indicate that they should be removed or unset._

&nbsp;

When using the **[`ConnectionAdmin.add()`](../add#connectionadminadd)** and **[`ConnectionAdmin.alter()`](../alter#connectionadminalter)** functions, the following are valid group traits. Feel free to experiment with any of the other traits defined in `pyracf/connection/connection_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:special` | Set to `True` to give a user **RACF Special** authority within a group or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:auditor` | Set to `True` to give a user **Auditor** authority within a group or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:operations` | Set to `True` to give a user **Operator** authority within a group or `False` otherwise. | Add: `bool`<br>Alter: `bool` |
| `base:access` | Set to `True` to give a user the **Access** attribute with a group or `False` otherwise. |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |