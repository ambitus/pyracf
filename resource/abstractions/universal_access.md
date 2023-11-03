---
layout: default
grand_parent: General Resource Admin
parent: Abstractions
---

# Universal Access

General Resource Profile Administration functions for checking a General Resource Profile's Universal Access Attribute. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.get_universal_access()`

```python
def get_universal_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check the **Universal Access Attribute** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should check the universal access attribute.

* `class_name`<br>
  The name of the **class** the general resource profile being checked belongs to.

#### 📤 Returns
* `Union[str, bytes, None]`<br>
  Returns `None` when the general resource profile has no **Universal Access** defined, otherwise returns the access level as a string. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_universal_access("TESTING","ELIJTEST")
"read"
```

## `ResourceAdmin.set_universal_access()`

```python
def set_universal_access(
    self,
    resource: str,
    class_name: str,
    universal_access: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Set the **Universal Access Attribute** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should set the universal access attribute.

* `class_name`<br>
  The name of the **class** the general resource profile being altered belongs to.

* `universal_access`<br>
  The **Universal Access** level to set for the specified general resource profile.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_universal_access("TESTING","ELIJTEST","ALTER")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  UACC        (Alter)","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  UACC        (Alter)",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```