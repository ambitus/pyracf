---
layout: default
parent: Common
---

# Security Request Error

Understanding the `SecurityRequestError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _A **Return Code** of anything other than `0` from IRRSMO00 is indicative of a failure with one or more of the operations performed by IRRSMO00, and pyracf will always raise a `SecurityRequestError` to bring attention to these failures._

&nbsp;

When the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`, a `SecurityRequestError` will be raised to indicate that the request failed. A `SecurityRequestError` can be handled as follows.

&nbsp;

For an understanding of return or reason codes returned from IRRSMO00, you can review [IRRSMO00's Return and Reason Codes documentation]](https://www.ibm.com/docs/en/zos/2.3.0?topic=operations-return-reason-codes). The 'Messages' list shown in the sample below also contains any error messages or other such information. 

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