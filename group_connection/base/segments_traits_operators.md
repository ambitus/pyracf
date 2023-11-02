---
layout: default
grand_parent: Group Connection Admin
parent: Base Functions
---

# Segments, Traits, and Operators

Information about group connection `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .experimental }
> _Note that just because a **Segment** is considered **Stable** that does not mean that all of the **Traits** in that **Segment** are considered **Stable**. See [Traits](#traits) for more detail._

&nbsp;

{: .warning }
> _There are no additional segments for **Group Connection** administartion._
> _Also, note that there is no **Profile Extract** function for **Group Connection** administration. Group connections can be extracted using **[`GroupAdmin.extract()`](../../../group/base/extract#groupadminextract)**._

&nbsp;

| **Segment** | **Description** |
| `Base` | Describes a general resource profile's **Base** attributes. |

### Traits

&nbsp;

{: .experimental }
> _**Traits** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .note }
> _Some **Traits** can be set to `False` to delete their existing values._

&nbsp;

When using the **[`ConnectionAdmin.connect()`](../connect#connectionadminconnect)** function, the following are valid group traits. Feel free to experiment with any of the other traits defined in `pyracf/connection/connection_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:special` | Set to `True` to give a user **RACF Special** authority within a group or `False` otherwise. | `bool` |
| `base:auditor` | Set to `True` to give a user **Auditor** authority within a group or `False` otherwise. | `bool` |
| `base:operations` | Set to `True` to give a user **Operator** authority within a group or `False` otherwise. | `bool` |
| `base:access` | Set to `True` to give a user the **Access** attribute with a group or `False` otherwise. | `bool` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |