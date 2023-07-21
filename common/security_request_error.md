---
layout: default
parent: Common
---

# Security Request Error

Understanding the `SecurityRequestError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _Note that even though a **Return Code** of `4` is generally indicatidve of a warning that in many cases can be ignored, pyRACF will still raise a `SecurityRequestError` to bring attention to the warning since a **Return Code** of `4` is sometimes indicative of a problem._

&nbsp;

When the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`, a `SecurityRequestError` will be raised to indicate that the request failed. A `SecurityRequestError` can be handled as follows.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import SecurityRequestError

try:
    user_admin.alter("squidwrd", traits={"base:password": "passwordtoolong"})
except SecurityRequestError as e
    return_code = e.result["securityResult"]["user"]["returnCode"]
    reason_code = e.result["securityResult"]["user"]["reasonCode"]
    error_message = "\n".join(e.result["securityResult"]["user"]["commands"][0]["messages"])
    print(f"Return Code: {return_code}")
    print(f"Reason Code: {reason_code}")
    print(f"Error Message: {error_mesage}")
```

###### Console Output
```console
Return Code: 4
Reason Code: 4
Error Message: IKJ56717I INVALID PASSWORD
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
    "reasonCode": 4
  }
}
```