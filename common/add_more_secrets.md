---
layout: default
parent: Common
---

# Add More Secrets

Define additional "secrets" to be redacted in pyracf output.
{: .fs-6 .fw-300 }

&nbsp;

**Add additional secrets**  allows pyracf to redact values beyond passwords and password phrases. When these traits are specified on input, the values will appear redacted in logger output as well as output xml and json objects. This can be specified on any "Admin" object by setting the `generate_requests_only` class attribute to a dictionary containing the `valid_segment_traits` information for the chosen attributes through the class constructor.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(add_additional_secrets={'omvs:uid':'uid'})
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
