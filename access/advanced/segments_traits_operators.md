---
layout: default
grand_parent: Access Admin
parent: Advanced
---

# Segments, Traits, and Operators

Relevant information about using `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .warning }
> _There are no additional segments for **Access** administartion._
> _Also, note that there is no **Profile Extract** function for **Access** administration. Some access information can be extracted using **[`ResourceAdmin.extract()`](../../../resource/standard/extract#resourceadminextract)** or **[`DataSetAdmin.extract()`](../../../dataset/standard/extract#datasetadminextract)** depending on the type of profile in question._

&nbsp;

### Traits

&nbsp;

{: .note }
> _All **key-value pair traits** can be set to `False` in **[`AccessAdmin.alter()`](../alter#accessadminalter)** to indicate that they should be removed or unset._

&nbsp;

When using the **[`AccessAdmin.add()`](../add#accessadminadd)** and **[`AccessAdmin.alter()`](../alter#accessadminalter)** functions, the following are valid group traits. Feel free to experiment with any of the other traits defined in `pyracf/access/access_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:access` | Set the **access level** associated with the permission. | Add: `str`<br>Alter: `str` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

{: .warning }
> _There are no traits that support operators for **Access** administartion._