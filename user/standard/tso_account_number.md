---
layout: default
grand_parent: User Admin
parent: Standard
---

# TSO Account Number

User administration functions for accessing and modifying a user's TSO Account Number. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_tso_account_number()`

```python
def get_tso_account_number(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Get a user's **TSO Account Number**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Account Number** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **TSO Account Number** or `None` if it is not set or if the user does not have a **TSO segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_tso_account_number("squidwrd")
'sb29'
```

## `UserAdmin.set_tso_account_number()`

```python
def set_tso_account_number(
    self, userid: str, account_number: Union[str, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Change a user's **TSO Account Number**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Account Number** is being changed.

* `account_number`<br>
  The **TSO Account Number** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_tso_account_number("squidwrd", "2425")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD  TSO      (ACCTNUM     ('2425'))"}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  TSO      (ACCTNUM     ('2425'))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```