---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# Resource Class

Resource Administration subfunctions for Resource Class Administration.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **Resource Class** in your environment._
> _You may also have to refresh the **CDT** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **CDT** class._

## `ResourceAdmin.add_resource_class()`

```python
def add_resource_class(self, class_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **Resource Class** profile in the **CDT** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Resource Class** profile being defined to the **CDT** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
class_traits = {
     "cdtinfo:case_allowed": "UPPER",
     "cdtinfo:valid_first_characters": "ALPHA",
     "cdtinfo:valid_other_characters": ["ALPHA" , "NUMERIC"],
     "cdtinfo:max_length": 246,
     "cdtinfo:max_length_entityx": 246,
     "cdtinfo:key_qualifiers": 0,
     "cdtinfo:profiles_allowed": "YES",
     "cdtinfo:posit_number": 200,
     "cdtinfo:default_racroute_return_code": 8,
     "cdtinfo:default_universal_access": "NONE",
     "cdtinfo:raclist_allowed": "ALLOWED",
}
resource_admin.add_resource_class("SHELCITY",traits=class_traits)
{'securityResult': {'resource': {'name': 'SHELCITY', 'class': 'CDT', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE CDT             (SHELCITY) ', 'messages': ['ICH10006I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED.', 'IRR52205I Warning: CDTINFO segment is required for the CDT class.']}, {'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  CDT             (SHELCITY)  CDTINFO  (CASE        (UPPER) FIRST       (ALPHA) OTHER       (ALPHA NUMERIC) MAXLENX     (246) MAXLENGTH   (246) KEYQUALIFIER(0) PROFILESALLO(YES) POSIT       (200) DEFAULTRC   (8) DEFAULTUACC (NONE) RACLIST     (ALLOWED))', 'messages': ['IRR52199I Warning: Class name SHELCITY does not contain a national character nor a number.', 'ICH11009I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"SHELCITY",
      "class":"CDT",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE CDT             (SHELCITY) ",
          "messages":[
            "ICH10006I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED.",
            "IRR52205I Warning: CDTINFO segment is required for the CDT class."
          ]
        },
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RALTER  CDT             (SHELCITY)  CDTINFO  (CASE        (UPPER) FIRST       (ALPHA) OTHER       (ALPHA NUMERIC) MAXLENX     (246) MAXLENGTH   (246) KEYQUALIFIER(0) PROFILESALLO(YES) POSIT       (200) DEFAULTRC   (8) DEFAULTUACC (NONE) RACLIST     (ALLOWED))",
          "messages":[
            "IRR52199I Warning: Class name SHELCITY does not contain a national character nor a number.",
            "ICH11009I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_resource_class()`

```python
def alter_resource_class(self, class_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Alter operations in pyracf require READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class_
> _This function will not produce output unless the user running the command has this access._

&nbsp;

Alter an existing **Resource Class** profile in the **CDT** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Resource Class** profile being defined to the **CDT** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
class_traits = {
    "cdtinfo:valid_first_characters": ["ALPHA", "NUMERIC"],
    "cdtinfo:valid_other_characters": ["ALPHA"],
    "cdtinfo:profiles_allowed": "NO",
    "cdtinfo:default_racroute_return_code": 4,
    "cdtinfo:default_universal_access": "READ",
}
resource_admin.alter_resource_class("SHELCITY",traits=class_traits)
{'securityResult': {'resource': {'name': 'SHELCITY', 'class': 'CDT', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  CDT             (SHELCITY)  CDTINFO  (FIRST       (ALPHA NUMERIC) OTHER       (ALPHA) PROFILESALLO(NO) DEFAULTRC   (4) DEFAULTUACC (READ))', 'messages': ['IRR52199I Warning: Class name SHELCITY does not contain a national character nor a number.', 'ICH11009I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"SHELCITY",
      "class":"CDT",
      "operation":"set",
      "requestId":"ResourceRequest",
      "info":[
        "Definition exists. Add command skipped due  to precheck option"
      ],
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RALTER  CDT             (SHELCITY)  CDTINFO  (FIRST       (ALPHA NUMERIC) OTHER       (ALPHA) PROFILESALLO(NO) DEFAULTRC   (4) DEFAULTUACC (READ))",
          "messages":[
            "IRR52199I Warning: Class name SHELCITY does not contain a national character nor a number.",
            "ICH11009I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_resource_class()`

```python
def extract_resource_class(self, class_name: str ) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **Resource Class** profile in the **CDT** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Resource Class** profile being defined to the **CDT** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **CDTINFO** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_resource_class("SHELCITY")
{'case': 'upper', 'defaultrc': 8, 'defaultuacc': None, 'first': 'alpha', 'genlist': 'disallowed', 'generic': 'allowed', 'group': '', 'keyqualifiers': 0, 'macprocessing': 'normal', 'maxlength': 246, 'maxlenx': 246, 'member': '', 'operations': None, 'other': ['alpha', 'numeric'], 'posit': 200, 'profilesallowed': 'yes', 'raclist': 'allowed', 'seclabelsrequired': None, 'signal': None}
```

###### Trait Dictionary as JSON
```json
{
  "case": "upper",
  "defaultrc": 8,
  "defaultuacc": null,
  "first": "alpha",
  "genlist": "disallowed",
  "generic": "allowed",
  "group": "",
  "keyqualifiers": 0,
  "macprocessing": "normal",
  "maxlength": 246,
  "maxlenx": 246,
  "member": "",
  "operations": null,
  "other": [
    "alpha",
    "numeric"
  ],
  "posit": 200,
  "profilesallowed": "yes",
  "raclist": "allowed",
  "seclabelsrequired": null,
  "signal": null
}
```

## `ResourceAdmin.delete_resource_class()`

```python
def delete_resource_class(self, class_name: str ) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **Resource Class** profile in the **CDT** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Resource Class** profile being defined to the **CDT** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.delete_resource_class("SHELCITY")
{'securityResult': {'resource': {'name': 'SHELCITY', 'class': 'CDT', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE CDT             (SHELCITY) ', 'messages': ['ICH12002I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"SHELCITY",
      "class":"CDT",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE CDT             (SHELCITY) ",
          "messages":[
            "ICH12002I RACLISTED PROFILES FOR CDT WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```