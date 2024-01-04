---
layout: default
parent: Common
---

# Security Request Error

Understanding the `SecurityRequestError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _For an understanding of IRRSMO00 return and reason codes, see the [IRRSMO00 Return and Reason Codes](https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes) documentation._

&nbsp;

{: .note }
> _Any time the **SAF Return Code** is greater than `4`, a `[DownstreamFataError](../downstream_fatal_error)` will be raised._

&nbsp;

{: .warning }
> _A **SAF Return Code** of `4` from IRRSMO00 is indicative of a failure with one or more of the RACF operations performed by IRRSMO00, and pyRACF will always raise a `SecurityRequestError` to bring attention to these failures._

&nbsp;

When the **SAF Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`, a `SecurityRequestError` will be raised to indicate that the request failed. A `SecurityRequestError` can be handled as follows.

&nbsp;

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import SecurityRequestError

user_admin = UserAdmin()

try:
    user_admin.alter("squidwrd", traits={"base:password": "passwordtoolong"})
except SecurityRequestError as e:
    return_code = e.result["securityResult"]["user"]["returnCode"]
    reason_code = e.result["securityResult"]["user"]["reasonCode"]
    messages = "\n".join(e.result["securityResult"]["user"]["commands"][0]["messages"])
    print(f"Return Code: {return_code}")
    print(f"Reason Code: {reason_code}")
    print(f"Messages:\n\n{messages}")
```

###### Console Output
```console
Return Code: 4
Reason Code: 0
Messages: 

IKJ56717I INVALID PASSWORD
```

###### Security Result Dictionary as JSON
```json
{
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
          "safReturnCode": 8,
          "returnCode": 16,
          "reasonCode": 8,
          "image": "ALTUSER SQUIDWRD  PASSWORD    (passwordtoolong)",
          "messages": [
            "IKJ56717I INVALID PASSWORD"
          ]
        }
      ]
    },
    "returnCode": 4,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```