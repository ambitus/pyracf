---
layout: default
parent: Common
---

# Debug Logging

How to enable debug logging
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

{: .note }
> _Whenever a user password is set using the `base:password` trait in the `UserAdmin` class, all instances of the specified password will be redacted from debug log messages._

&nbsp;

Debug logging can be enabled on any "Admin" class by setting the `debug` class attrubute to `True` through the constructor. Once enabled, the metadata for the following steps will be printed to the console.

&nbsp;

* Pre-processed request dictionary
* Security request XML generated from the pre-processed request dictionary.
* Security result XML returned from IRRSMO00.
* Security result dictionary built from security result XML
* Post-processed security result dictionary for profile extract.

## Example

&nbsp;

{: .note }
> _If your terminal supports it, all output will be printed to the console with **sytax highlighting** using **ANSI escape sequences**._

###### Python Script
```python
from pyracf import UserAdmin
user_admin = UserAdmin(debug=True)

user_admin.extract("squidwrd")
```

###### Console Output
```

                                 [pyRACF:Debug]
                               Request Dictionary
                              UserAdmin.extract()


{}


                                 [pyRACF:Debug]
                                  Request XML
                              UserAdmin.extract()


<securityrequest xmlns="http://www.ibm.com/systems/zos/saf" xmlns:racf="http://www.ibm.com/systems/zos/racf">
  <user name="squidwrd" operation="listdata" requestid="UserRequest"/>
</securityrequest>


                                 [pyRACF:Debug]
                                   Result XML
                              UserAdmin.extract()


<?xml version="1.0" encoding="IBM-1047"?>
<securityresult xmlns="http://www.ibm.com/systems/zos/saf/IRRSMO00Result1">
  <user name="SQUIDWRD" operation="listdata" requestid="UserRequest">
    <command>
      <safreturncode>0</safreturncode>
      <returncode>0</returncode>
      <reasoncode>0</reasoncode>
      <image>LISTUSER SQUIDWRD </image>
      <message>USER=SQUIDWRD  NAME=UNKNOWN  OWNER=LEONARD   CREATED=23.193</message>
      <message> DEFAULT-GROUP=SYS1     PASSDATE=N/A    PASS-INTERVAL=N/A PHRASEDATE=N/A</message>
      <message> ATTRIBUTES=PROTECTED</message>
      <message> REVOKE DATE=NONE   RESUME DATE=NONE</message>
      <message> LAST-ACCESS=UNKNOWN</message>
      <message> CLASS AUTHORIZATIONS=NONE</message>
      <message> NO-INSTALLATION-DATA</message>
      <message> NO-MODEL-NAME</message>
      <message> LOGON ALLOWED   (DAYS)          (TIME)</message>
      <message> ---------------------------------------------</message>
      <message> ANYDAY                          ANYTIME</message>
      <message>  GROUP=SYS1      AUTH=USE      CONNECT-OWNER=LEONARD   CONNECT-DATE=23.193</message>
      <message>    CONNECTS=    00  UACC=NONE     LAST-CONNECT=UNKNOWN</message>
      <message>    CONNECT ATTRIBUTES=NONE</message>
      <message>    REVOKE DATE=NONE   RESUME DATE=NONE</message>
      <message>SECURITY-LEVEL=NONE SPECIFIED</message>
      <message>CATEGORY-AUTHORIZATION</message>
      <message> NONE SPECIFIED</message>
      <message>SECURITY-LABEL=NONE SPECIFIED</message>
    </command>
  </user>
  <returncode>0</returncode>
  <reasoncode>0</reasoncode>
</securityresult>


                                 [pyRACF:Debug]
                               Result Dictionary
                              UserAdmin.extract()


{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "listdata",
      "requestId": "UserRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTUSER SQUIDWRD ",
          "messages": [
            "USER=SQUIDWRD  NAME=UNKNOWN  OWNER=LEONARD   CREATED=23.193",
            " DEFAULT-GROUP=SYS1     PASSDATE=N/A    PASS-INTERVAL=N/A PHRASEDATE=N/A",
            " ATTRIBUTES=PROTECTED",
            " REVOKE DATE=NONE   RESUME DATE=NONE",
            " LAST-ACCESS=UNKNOWN",
            " CLASS AUTHORIZATIONS=NONE",
            " NO-INSTALLATION-DATA",
            " NO-MODEL-NAME",
            " LOGON ALLOWED   (DAYS)          (TIME)",
            " ---------------------------------------------",
            " ANYDAY                          ANYTIME",
            "  GROUP=SYS1      AUTH=USE      CONNECT-OWNER=LEONARD   CONNECT-DATE=23.193",
            "    CONNECTS=    00  UACC=NONE     LAST-CONNECT=UNKNOWN",
            "    CONNECT ATTRIBUTES=NONE",
            "    REVOKE DATE=NONE   RESUME DATE=NONE",
            "SECURITY-LEVEL=NONE SPECIFIED",
            "CATEGORY-AUTHORIZATION",
            " NONE SPECIFIED",
            "SECURITY-LABEL=NONE SPECIFIED"
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}


                                 [pyRACF:Debug]
                     Result Dictionary (Formatted Profile)
                              UserAdmin.extract()


{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "listdata",
      "requestId": "UserRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTUSER SQUIDWRD ",
          "profiles": [
            {
              "base": {
                "user": "squidwrd",
                "name": null,
                "owner": "leonard",
                "created": "7/12/2023",
                "defaultGroup": "sys1",
                "passwordDate": null,
                "passwordInterval": null,
                "passphraseDate": null,
                "attributes": [
                  "protected"
                ],
                "revokeDate": null,
                "resumeDate": null,
                "lastAccess": null,
                "classAuthorizations": [],
                "logonAllowedDays": "anyday",
                "logonAllowedTime": "anytime",
                "groups": {
                  "SYS1": {
                    "auth": "use",
                    "connectOwner": "leonard",
                    "connectDate": "7/12/2023",
                    "connects": 0,
                    "uacc": null,
                    "lastConnect": null,
                    "connectAttributes": [],
                    "revokeDate": null,
                    "resumeDate": null
                  }
                },
                "securityLevel": null,
                "categoryAuthorization": null,
                "securityLabel": null
              }
            }
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```