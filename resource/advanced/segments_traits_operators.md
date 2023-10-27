---
layout: default
grand_parent: General Resource Admin
parent: Advanced
---

# Segments, Traits, and Operators

Information about general resource profile `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .experimental }
> _**Segments** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .note }
> _The `base` segment is **always included** in **[`ResourceAdmin.extract()`](../../standard/extract#resourceadminextract)** by default._

&nbsp;

{: .warning }
> _Note that just because a **Segment** is considered **Stable** that does not mean that all of the **Traits** in that **Segment** are considered **Stable**. See [Traits](#traits) for more detail._

&nbsp;

When using the **[`ResourceAdmin.extract()`](../../standard/extract#resourceadminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the segments defined in `pyracf/resource/resource_admin.py` in the pyRACF source code.

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

When using the **[`ResourceAdmin.add()`](../add#resourceadminadd)** and **[`ResourceAdmin.alter()`](../alter#resourceadminalter)** functions, the following are valid resource traits. Feel free to experiment with any of the other traits defined in `pyracf/resource/resource_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:universal_access` | Set a resource's **Universal Access** level. | `str` |


### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |