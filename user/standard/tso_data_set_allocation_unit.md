---
layout: default
grand_parent: User Admin
parent: Standard
---

# TSO Data Set Allocation Unit

User administration functions for accessing and modifying a user's TSO Data Set Allocation Unit. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_tso_data_set_allocation_unit()`

```python
def get_tso_data_set_allocation_unit(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **TSO Data Set Allocation Unit**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Data Set Allocation Unit** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **TSO Data Set Allocation Unit** or `None` if it is not set or if the user does not have a **TSO segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_tso_data_set_allocation_unit("squidwrd")
'sysda'
```

## `UserAdmin.set_tso_data_set_allocation_unit()`

```python
def set_tso_data_set_allocation_unit(
    self, userid: str, data_set_allocation_unit: Union[str, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **TSO Data Set Allocation Unit**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Data Set Allocation Unit** is being changed.

* `data_set_allocation_unit`<br>
  The **TSO Data Set Allocation Unit** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_tso_data_set_allocation_unit("squidwrd", "CHMBK")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  TSO      (UNIT        (CHMBK))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  TSO      (UNIT        (CHMBK))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```