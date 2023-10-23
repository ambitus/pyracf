---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Max File Mapping Pages

User administration functions for accessing and modifying a user's z/OS Unix System Services Max File Mapping Pages. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_max_file_mapping_pages()`

```python
def get_omvs_max_file_mapping_pages(self, userid: str) -> Union[int, None, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Get a user's **z/OS Unix System Services Max File Mapping Pages**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max File Mapping Pages** is being requested.

#### 📤 Returns
* `Union[int, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Max File Mapping Pages** or `None` if it is not set or if the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_max_file_mapping_pages("squidwrd")
350
```

## `UserAdmin.set_omvs_max_file_mapping_pages()`

```python
def set_omvs_max_file_mapping_pages(
    self, userid: str, max_file_mapping_pages: Union[int, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Change a user's **z/OS Unix System Services Max File Mapping Pages**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max File Mapping Pages** is being set.

* `max_file_mapping_pages`<br>
  The **z/OS Unix System Services Max File Mapping Pages** to set for the specified user or `False` to delete the current value.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_omvs_max_file_mapping_pages("squidwrd", 400)
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (MMAPAREAMAX (400))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "user": {
        "name": "SQUIDWRD",
        "operation": "set",
        "requestId": "UserRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "ALTUSER SQUIDWRD  OMVS     (MMAPAREAMAX (400))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```