---
layout: default
parent: Common
---

# Downstream Fatal Error

Understanding the `DownstreamFatalError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _pyRACF requires a response xml string from an internal call to the IRRSMO00 callable service to provide proper output. If the response string that pyRACF receives is empty, or if IRRSMO00 indicates a failing return code, pyRACF raises a `DownstreamFatalError` and terminates processing the response from IRRSMO00._

&nbsp;

After executing any operation, pyRACF expects a non-empty response string from IRRSMO00 that indicates a RACF command image was built and processed in order to parse such a response and surface information back to the user. When pyRACF detects an empty response string, or a return code indicating an issue with command image processing, a `DownstramFatalError` is raised and processing terminates. It is possible that the command was executed prior to reaising this error, but this is not the case for any known causes of this error.

## RACF Authorizations

&nbsp;

A common cause of this error is that the user does not have proper RACF authorizations as outlined in [our dependencies note](../../index). One of the possible failures is `READ` authority to the `IRR.IRRSMO00.PRECHECK` resource in the `XFACILIT` class, which is required for `set` or `alter` operations. If you are not certain if you have this authority or if this has been established in your environment, please consult our [Check for & set up RACF Authorizations](../check_for_and_setup_RACF_authorizations) documentation. The other possibility is `ALTER` authority to the `userid.IRRSMO00` resource in the `SURROGAT` class, which is required to run pyRACF commands as another userid. Please review our [run as userid](../run_as_userid) documentation for more information on this feature.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import DownstreamFatalError

user_admin = UserAdmin()

try:
    user_admin.set_uid("squidwrd", 123456)
except AddOperationError as e:
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
except AddOperationError as e:
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

As stated, this error can also appear if IRRSMO00 raises a problem with data passed in from pyRACF. This may happen when pyRACF receives data or data-types that do not align with use-cases for the traits in use. In this case, or others where a response is returned from IRRSMO00, you can review the initial command as well as error messages and information in the `result` dictionary as a part of the error.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import DownstreamFatalError

user_admin = UserAdmin()

try:
    user_admin.alter("squidwrd", traits={"base:special": "STRING"})
except AddOperationError as e:
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