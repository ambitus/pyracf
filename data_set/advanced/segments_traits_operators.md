---
layout: default
grand_parent: Dataset Admin
parent: Advanced
---

# Segments, Traits, and Operators

Relevant information about using `segments` dictionaries, `traits` dictionaries, and `operators`.
{: .fs-6 .fw-300 }

### Segments

&nbsp;

{: .note }
> _The `base` segment is **always included** in **[`DatasetAdmin.extract()`](../../standard/extract#datasetadminextract)** by default._

&nbsp;

When using the **[`DatasetAdmin.extract()`](../../standard/extract#datasetadminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the segments defined in `pyracf/dataset/dataset_admin.py` in the pyRACF source code.

&nbsp;

| **Segment** | **Description** |
| | |

### Traits

&nbsp;

{: .note }
> _All **key-value pair traits** can be set to `False` in **[`DatasetAdmin.alter()`](../alter#datasetadminalter)** to indicate that they should be removed or unset._

&nbsp;

When using the **[`DatasetAdmin.add()`](../add#datasetadminadd)** and **[`DatasetAdmin.alter()`](../alter#datasetadminalter)** functions, the following are valid dataset traits. Feel free to experiment with any of the other traits defined in `pyracf/dataset/dataset_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:universal_access` | Set a dataset's **Universal Access** level. | Add: `str`<br>Alter: `str` |


### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |