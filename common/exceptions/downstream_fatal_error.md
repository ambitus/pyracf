---
layout: default
grand_parent: Common
parent: Exceptions
---

# Downstream Fatal Error

Understanding the `DownstreamFatalError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _For an understanding of IRRSMO00 return and reason codes, see the [IRRSMO00 Return and Reason Codes](https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes) documentation._

&nbsp;

{: .note }
> _pyRACF expects IRRSMO00 to return a string containing XML data. If IRRSMO00 returns an empty string, or if the **SAF Return Code** in the result XML is greater than `4`, `DownstreamFatalError` is raised._

&nbsp;

pyRACF expects IRRSMO00 to return a non-empty result string after processing a request. If IRRSMO00 returns an empty result string or the **SAF Return Code** is greater than `4`, indicating that there was an issue with command image processing, a `DownstramFatalError` will be raised. It is possible that RACF commands are executed in this situation, but this is not the case for any known causes of this error.

## RACF Authorizations

&nbsp;

A common cause of this error is that the user does not have the proper RACF authorizations as outlined in [Our Dependencies Note](../../../index). One of the possible causes for this error is the user not having at least `READ` authority to the `IRR.IRRSMO00.PRECHECK` resource in the `XFACILIT` class, which is required for `set` or `alter` operations. See the [Check for & set up RACF Authorizations](../../misc/setup_precheck) documentation for more details. Another possible cause of this error is the user not having `ALTER` authority to the `userid.IRRSMO00` resource in the `SURROGAT` class, which is required to make security requests as another userid. Please review our [Run as Userid](../../class_attributes/run_as_userid) documentation for more information on this feature.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import DownstreamFatalError

user_admin = UserAdmin()

try:
    user_admin.set_uid("squidwrd", 123456)
except DownstreamFatalError as e:
    print(e.message)
```

###### Console Output
```console
Security request made to IRRSMO00 failed.

SAF Return Code: 8 
RACF Return Code: 200 
RACF Reason Code: 16

Check to see if the proper RACF permissions are in place.
For `set` or `alter` functions, you must have at least READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class.
```

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import DownstreamFatalError

user_admin = UserAdmin(run_as_userid="ESWIFT")

try:
    user_admin.set_uid("squidwrd", 123456)
except DownstreamFatalError as e:
    print(e.message)
```

###### Console Output
```console
Security request made to IRRSMO00 failed.

SAF Return Code: 8 
RACF Return Code: 200 
RACF Reason Code: 8

Check to see if the proper RACF permissions are in place.
For the `run_as_userid` feature, you must have at least UPDATE access to `ESWIFT.IRRSMO00` in the `SURROGAT` class.
```

## Improper Use of Traits

&nbsp;

As stated, `DownstreamFatalError` may also be raised if there is a problem with the data pyRACF passes to IRRSMO00. In this situation, you can review `DownstreamFatalError.request_xml` and `DownwstreamFatalError.result` for more information.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import DownstreamFatalError

user_admin = UserAdmin()

try:
    user_admin.alter("squidwrd", traits={"base:special": "STRING"})
except DownstreamFatalError as e:
    print(e.message)
```

###### Console Output
```console
Security request made to IRRSMO00 failed.

SAF Return Code: 8 
RACF Return Code: 2000 
RACF Reason Code: 76

See results dictionary 'DownstreamFatalError.result' for more details.

You can also check the specified return and reason codes against the IRRSMO00 documented return and reason codes for more information about this error.
https://www.ibm.com/docs/en/zos/3.1.0?topic=operations-return-reason-codes"
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "set",
      "requestId": "UserRequest",
      "error": {
        "errorFunction": 10,
        "errorCode": 2000,
        "errorReason": 76,
        "errorMessage": "Data may not be specified for a boolean field.",
        "errorOffset": 216,
        "textInError": "STRING"
      }
    },
    "returnCode": 2000,
    "reasonCode": 76,
    "runningUserid": "testuser"
  }
}
```