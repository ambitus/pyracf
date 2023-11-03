---
layout: default
grand_parent: Group Admin
parent: Base Functions
---

# Segments, Traits, and Operators

Information about group `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .experimental }
> _**Segments** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .experimental }
> _Note that just because a **Segment** is considered **Stable** that does not mean that all of the **Traits** in that **Segment** are considered **Stable**. See [Traits](#traits) for more detail._

&nbsp;

{: .note }
> _The `base` segment is **always included** in **[`GroupAdmin.extract()`](../extract#groupadminextract)** by default._

&nbsp;

When using the **[`GroupAdmin.extract()`](../extract#groupadminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the other segments defined in `pyracf/group/group_admin.py` in the pyRACF source code.

&nbsp;

| **Segment** | **Description** |
| `base` | Describes a group's **Base** attributes. |
| `omvs` | Describes a groups's **z/OS Unix System Services** attributes. |
| `ovm` | Describes a groups **z/VM Open Extensions** attributes. |

### Traits

&nbsp;

{: .experimental }
> _**Traits** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .note }
> _Some **Traits** can be set to `False` to delete their existing values._

&nbsp;

When using the **[`GroupAdmin.add()`](../add#groupadminadd)** and **[`GroupAdmin.alter()`](../alter#groupadminalter)** functions, the following are valid group traits. Feel free to experiment with any of the other traits defined in `pyracf/group/group_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `omvs:gid` | Set a group's **z/OS Unix System Services GID**. | `int`, `False` |
| `ovm:gid` | Set a group's **z/VM Open Extensions GID**. | `int`, `False` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |