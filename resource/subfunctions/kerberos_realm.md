---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# Kerberos Realm

Resource Administration subfunctions for Kerberos Realm Administration.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **Kerberos Realm** in your environment._
> _You may also have to refresh the **REALM** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **REALM** class._

## `ResourceAdmin.add_kerberos_realm()`

```python
def add_kerberos_realm(self, kerberos_realm_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **Kerberos Realm** profile in the **REALM** class.

#### 📥 Parameters
* `kerberos_realm_name`<br>
  The name of the **Kerberos Realm** profile being defined to the **REALM** class.

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
resource_admin.add_kerberos_realm("TSTREALM")
{'securityResult': {'resource': {'name': 'TSTREALM', 'class': 'REALM', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE REALM             (TSTREALM) ', 'messages': ['ICH10006I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTREALM",
      "class":"REALM",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE REALM             (TSTREALM) ",
          "messages":[
            "ICH10006I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_kerberos_realm()`

```python
def alter_kerberos_realm(self, kerberos_realm_name: str, traits: dict = {}) -> Union[dict, bytes]:
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

Alter an existing **Kerberos Realm** profile in the **REALM** class.

#### 📥 Parameters
* `kerberos_realm_name`<br>
  The name of the **Kerberos Realm** profile being defined to the **REALM** class.

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
resource_admin.alter_kerberos_realm("TSTREALM", traits={"kerb:encryption_algorithms": "AES128"})
{'securityResult': {'resource': {'name': 'TSTREALM', 'class': 'REALM', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  REALM             (TSTREALM)  KERB     (ENCRYPT     (AES128))', 'messages': ['ICH11009I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTREALM",
      "class":"REALM",
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
          "image":"RALTER  REALM             (TSTREALM)  KERB     (ENCRYPT     (AES128))",
          "messages":[
            "ICH11009I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_kerberos_realm()`

```python
def extract_kerberos_realm(self, kerberos_realm_name: str ) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **Kerberos Realm** profile in the **REALM** class.

#### 📥 Parameters
* `kerberos_realm_name`<br>
  The name of the **Kerberos Realm** profile being defined to the **REALM** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **KERB** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_kerberos_realm("TSTTSKEL")
{'user': '', 'group': '', 'trusted': 'yes', 'privileged': None, 'trace': None}
```

###### Trait Dictionary as JSON
```json
{
  "user": "",
  "group": "",
  "trusted": "yes",
  "privileged": null,
  "trace": null
}
```

## `ResourceAdmin.delete_kerberos_realm()`

```python
def delete_kerberos_realm(self, kerberos_realm_name: str ) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **Kerberos Realm** profile in the **REALM** class.

#### 📥 Parameters
* `kerberos_realm_name`<br>
  The name of the **Kerberos Realm** profile being defined to the **REALM** class.

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
resource_admin.delete_kerberos_realm("TSTREALM")
{'securityResult': {'resource': {'name': 'TSTREALM', 'class': 'REALM', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE REALM             (TSTREALM) ', 'messages': ['ICH12002I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTREALM",
      "class":"REALM",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE REALM             (TSTREALM) ",
          "messages":[
            "ICH12002I RACLISTED PROFILES FOR REALM WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```