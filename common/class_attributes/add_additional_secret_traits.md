---
layout: default
grand_parent: Common
parent: Class Attributes
---

# Add Additional Secret Traits

Add additional secrets to be redacted in debug log output and any returned result dictionaries or request xml.
{: .fs-6 .fw-300 }

&nbsp;

{: .experimental }
> _This feature will successfully remove references to the additional secrets in the **RACF Command Image** in the **Result XML** and debug logging output, but additional messages may contain secret values from these traits, especially if bad data is provided._

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

The `additional_secret_traits` constructor argument allows values beyond passwords and password phrases to be redacted. When the `additional_secret_traits` constructor argument is provided upon instantiation of any "Admin" object, the values that correspond to the trait keys provided will be redacted in debug log output as well as any returned result dictionaries or request xml when using the corresponding "Admin" object instance.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(additional_secret_traits=['omvs:uid'])
>>> user_admin.add("squidwrd",traits={'omvs:uid':123456})
{'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['ICH01024I User SQUIDWRD is defined as PROTECTED.']}, {'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (********))'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
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
