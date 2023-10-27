---
layout: default
grand_parent: Access Admin
parent: Advanced
---

# Segments, Traits, and Operators

Information about permission `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .experimental }
> _Note that just because a **Segment** is considered **Stable** that does not mean that all of the **Traits** in that **Segment** are considered **Stable**. See [Traits](#traits) for more detail._

&nbsp;

{: .warning }
> _There are no additional segments for **Access** administartion._
> _Also, note that there is no **Profile Extract** function for **Access** administration. Some access information can be extracted using **[`ResourceAdmin.extract()`](../../../resource/standard/extract#resourceadminextract)** or **[`DataSetAdmin.extract()`](../../../data_set/standard/extract#datasetadminextract)** depending on the type of profile in question._

&nbsp;

| **Segment** | **Description** |
| `Base` | Describes a permission's **Base** attributes. |

### Traits

&nbsp;

{: .experimental }
> _**Traits** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .note }
> _Some **Traits** can be set to `False` to delete their existing values._

&nbsp;

When using the **[`AccessAdmin.add()`](../add#accessadminadd)** and **[`AccessAdmin.alter()`](../alter#accessadminalter)** functions, the following are valid access traits. Feel free to experiment with any of the other traits defined in `pyracf/access/access_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:access` | Set the **access level** associated with the permission. | `str` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

{: .warning }
> _There are no traits that support operators for **Access** administartion._