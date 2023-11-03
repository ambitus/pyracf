---
layout: default
grand_parent: General Resource Admin
parent: Base Functions
---

# Segments, Traits, and Operators

Information about general resource profile `segments` dictionaries, `traits` dictionaries, and `operators`.
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
> _The `base` segment is **always included** in **[`ResourceAdmin.extract()`](../extract#resourceadminextract)** by default._

&nbsp;

When using the **[`ResourceAdmin.extract()`](../extract#resourceadminextract)** function, the following is the current list of additional segments that have been tested and validated. Feel free to experiment with any of the segments defined in `pyracf/resource/resource_admin.py` in the pyRACF source code.

&nbsp;

| **Segment** | **Description** |
| `base` | Describes a general resource profile's **Base** attributes. |
| `cdtinfo` | Describes a general resource profile's **Resource Class** attributes. |
| `cfdef` | Describes a general resource profile's **Custom Field** attributes. |
| `kerb` | Describes a general resource profile's **Kerberos Realm** attributes. |
| `session` | Describes a general resource profile's **APPC Session** attributes. |
| `sigver` | Describes a general resource profile's **Signed Program** attributes. |
| `stdata` | Describes a general resource profile's **Started Task** attributes. |

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
| `cdtinfo:case_allowed` | Set the **Case Allowed** for the names of profiles in this resource class. | `str`, `False` |
| `cdtinfo:default_racroute_return_code` | Set the **Default Return Code** for requests to access profiles in this resource class. | `int`, `False` |
| `cdtinfo:valid_first_characters` | Set the **Valid Character Types** for the first characters in names of profiles in this resource class. | `str`, `False` |
| `cdtinfo:grouping_class_name` | Set the **Grouping Class** name associated with this resource class. | `str`, `False` |
| `cdtinfo:key_qualifiers` | Set the number of **Qualifiers** used to determine a match for profiles in this resource class | `int` |
| `cdtinfo:max_length` | Set the **Maximum Length** for the names of profiles within this resource class. | `str`, `False` |
| `cdtinfo:max_length_entityx` | Set the **Maximum Length** for the names of profiles when a RACROUTE macro is invoked with the ENTITYX keyword within this resource class. | `str`, `False` |
| `cdtinfo:valid_other_characters` | Set the **Valid Character Types** for the other characters in names of profiles in this resource class. | `str`, `False` |
| `cdtinfo:posit_number` | Set the **Posit Number** for this resource class. This controls flags that control many RACF processing options. | `int`, `False` |
| `cdtinfo:profiles_allowed` | Specifies whether or not **Profiles are Allowed** for this resource class. | `bool` |
| `cdtinfo:raclist_allowed` | Specifies whether or not this class is **Allowed to be Raclisted**. | `bool` |
| `cdtinfo:default_universal_access` | Set the **Default Universal Access Value** for profiles in this resource class. | `str`, `False` |
| `cfdef:help_text` | Set the **Help Text** for this custom field. | `str` |
| `cfdef:valid_first_characters` | Set the **Valid Character Types** for the first characters in values for this custom field. | `str` |
| `cfdef:valid_other_characters` | Set the **Valid Character Types** for the other characters in values for this custom field. | `str` |
| `kerb:key_encryption_type` | Set the **Encryption Algorithms** for this kerberos realm. | `str`, `False` |
| `sigver:log_signature_verification_events` | Specifies whether to **Audit Signature Verification Events** for this signed program. | `str`, `False` |
| `stdata:group` | Set the **Group** to associate with this started task. | `str`, `False` |
| `stdata:privileged` | Specify whether or not this started task runs with the **RACF Privileged** attribute. | `bool` |
| `stdata:trace` | Specify whether or not this started task should issue a message to the operator to **Trace** use of this entry. | `bool` |
| `stdata:trusted` | Specify whether or not this started task runs with the **RACF Trusted** attribute. | `bool` |
| `stdata:user` | Set the **User ID** to associate with this started task. | `str`, `False` |


### Operators

Operators can be prepended to traits using the following syntax: `<operator>:<segment>:<trait>`

&nbsp;

**Valid Operators**: `add`, `remove`, `delete`

### Key-Value Pair Traits

Operators are generally not needed for **key-value pair traits**. For key-value pair traits, setting the value to a non-`False` value with no operator will generally set or overwrite the trait and setting the value to `False` will generally unset or disable the trait.

### List Traits

| **Trait** | **Operator Usage** |
| | |