---
layout: default
grand_parent: User Admin
parent: Base Functions
---

# Segments, Traits, and Operators

Information about user `segments` dictionaries, `traits` dictionaries, and `operators`.
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
> _The `base` segment is **always included** in **[`UserAdmin.extract()`](../extract#useradminextract)** by default._

&nbsp;

When using the **[`UserAdmin.extract()`](../extract#useradminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the other segments defined in `pyracf/user/user_admin.py` in the pyRACF source code.

&nbsp;

| **Segment** | **Description** |
| `base` | Describes a user's **Base** attributes. |
| `omvs` | Describes a user's **z/OS Unix System Services** attributes. |
| `tso` | Describes a user's **TSO** attributes. |

### Traits

&nbsp;

{: .experimental }
> _**Traits** that are **NOT** documented below are considered **Experimental**._

&nbsp;

{: .note }
> _Some **Traits** can be set to `False` to delete their existing values._

&nbsp;

When using the **[`UserAdmin.add()`](../add#useradminadd)** and **[`UserAdmin.alter()`](../alter#useradminalter)** functions, the following are valid user traits. Feel free to experiment with any of the other traits defined in `pyracf/user/user_admin.py` in the pyRACF source code.

&nbsp;

Traits use the following syntax: `<segment>:<trait>`

&nbsp;

| **Trait** | **Description** | **Valid Types** |
| `base:special` | Set to `True` to give a user **RACF Special** authority or `False` otherwise. | `bool` |
| `base:operations` | Set to `True` to give a user **Operator** authority or `False` otherwise. | `bool` |
| `base:auditor` | Set to `True` to give a user **Auditor** authority or `False` otherwise. | `bool` |
| `base:password` | Set a user's **Password**. | `str`, `False` |
| `base:passphrase` | Set a user's **Passphrase**. | `str`, `False` |
| `base:class_authorizations` | Modify a user's **Class Authorizations**. | `str`, `List[str]` |
| `base:revoke_date` | Set a user's **Revoke Date**. | `str`, `False` |
| `base:resume_date` | Set a user's **Resume Date**. | `str`, `False` |
| `base:name` | Set a user's **Name**. | `str`, `False` |
| `base:owner` | Set a **z/OS userid** as the owner of the **z/OS userid** being altered/created. | `str` |
| `omvs:uid` | Set a user's **z/OS Unix System Services UID**. | `int`, `False` |
| `omvs:max_address_space_size` | Set a user's **z/OS Unix System Services Max Address Space Size**. | `int`, `False` |
| `omvs:max_cpu_time` | Set a user's **z/OS Unix System Services Max CPU Time**. | `int`, `False` |
| `omvs:max_files_per_process` | Set a user's **z/OS Unix System Services Max Files Per Process**. | `int`, `False` |
| `omvs:max_non_shared_memory` | Set a user's **z/OS Unix System Services Max Non-Shared Memory**. | `str`, `False` |
| `omvs:max_file_mapping_pages` | Set a user's **z/OS Unix System Services Max File Mapping Pages**. | `int`, `False` |
| `omvs:max_processes` | Set a user's **z/OS Unix System Services Max Processes**. | `int`, `False` |
| `omvs:max_shared_memory` | Set a user's **z/OS Unix System Services Max Shared Memory**. | `str`, `False` |
| `omvs:home_directory` | Set a user's **z/OS Unix System Services Home Directory**. | `str`, `False` |
| `omvs:default_shell` | Set the user's **z/OS Unix System Services Default Shell**. | `str`, `False` |
| `tso:account_number` | Set a user's **TSO Account Number**. | `str`, `False` |
| `tso:logon_command` | Set a user's **TSO Logon Command**. | `str`, `False` |
| `tso:hold_class` | Set a user's **TSO Hold Class**. | `str`, `False` |
| `tso:max_region_size` | Set a user's **TSO Max Region Size**. | `int`, `False` |
| `tso:message_class` | Set a user's **TSO Message Class**. | `str`, `False` |
| `tso:logon_procedure` | Set a user's **TSO Logon Procedure**. | `str`, `False` |
| `tso:default_region_size` | Set a user's **TSO Default Region Size**. | `int`, `False` |
| `tso:sysout_class` | Set a user's **TSO Sysout Class**. | `str`, `False` |
| `tso:user_data` | Set a user's **TSO User Data**. | `str`, `False` |
| `tso:data_set_allocation_unit` | Set a user's **TSO Data Set Allocation Unit**. | `str`, `False` |

### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally delete its existing value.

### List Traits

| **Trait** | **Operator Usage** |
| `base:class_authorizations` | Use the `add` operator to add new **Class Authorizations** and `remove` to remove **Class Authorizations**. |