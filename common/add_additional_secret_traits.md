---
layout: default
parent: Common
---

# Add Additional Secret Traits

Add additional secrets to be redacted in debug log output and any returned result dictionaries or request xml.
{: .fs-6 .fw-300 }

&nbsp;

The `add_additional_secrets` class attribute allows values beyond passwords and password phrases to be redacted. When the `add_additional_secrets` class attribute is set through the class constructor of any "Admin" object, the values that correspond to the trait keys provided will be redacted in debug log output as well as any returned result dictionaries or request xml.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(add_additional_secrets=['omvs:uid'])
>>> user_admin.add("squidwrd",traits={'omvs:uid':123456})
{'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['ICH01024I User SQUIDWRD is defined as PROTECTED.']}, {'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (********))'}]}, 'returnCode': 0, 'reasonCode': 0}}

```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "user":{
      "name":"SQUIDWRD",
      "operation":"set",
      "requestId":"UserRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"ADDUSER SQUIDWRD ",
          "messages":[
            "ICH01024I User SQUIDWRD is defined as PROTECTED."
          ]
        },
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"ALTUSER SQUIDWRD  OMVS     (UID         (********))"
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```
