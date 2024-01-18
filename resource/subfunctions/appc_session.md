---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# APPC Session

Resource Administration subfunctions for APPC Session Administration.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **APPC Session** in your environment._
> _You may also have to refresh the **APPCLU** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **APPCLU** class._

## `ResourceAdmin.add_appc_session()`

```python
def add_appc_session(
    self, net_id: str, local_lu: str, partner_lu: str, traits: dict = {}
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **APPC Session** profile in the **APPCLU** class.

#### 📥 Parameters
* `net_id`<br>
  The **Network ID** of the **APPC Session** being defined.

* `local_lu`<br>
  The name of the **Local Logical Unit** of the **APPC Session** being defined.

* `partner_lu`<br>
  The name of the **Partner Logical Unit** of the **APPC Session** being defined.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.add_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU")
{'securityResult': {'resource': {'name': 'TSTNET.TSTLOCLU.TSTPRTLU', 'class': 'APPCLU', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU) '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTNET.TSTLOCLU.TSTPRTLU",
      "class":"APPCLU",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_appc_session()`

```python
def alter_appc_session(
    self, net_id: str, local_lu: str, partner_lu: str, traits: dict = {}
) -> Union[dict, bytes]:
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

Alter an existing **APPC Session** profile in the **APPCLU** class.

#### 📥 Parameters
* `net_id`<br>
  The **Network ID** of the **APPC Session** being altered.

* `local_lu`<br>
  The name of the **Local Logical Unit** of the **APPC Session** being altered.

* `partner_lu`<br>
  The name of the **Partner Logical Unit** of the **APPC Session** being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.alter_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU", traits={"session:locked": True})
{'securityResult': {'resource': {'name': 'TSTNET.TSTLOCLU.TSTPRTLU', 'class': 'APPCLU', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU)  SESSION  (   LOCK        )'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTNET.TSTLOCLU.TSTPRTLU",
      "class":"APPCLU",
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
          "image":"RALTER  APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU)  SESSION  (   LOCK        )"
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_appc_session()`

```python
def extract_appc_session(
    self, net_id: str, local_lu: str, partner_lu: str
) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **APPC Session** profile in the **APPCLU** class.

#### 📥 Parameters
* `net_id`<br>
  The **Network ID** of the **APPC Session** being extracted.

* `local_lu`<br>
  The name of the **Local Logical Unit** of the **APPC Session** being extracted.

* `partner_lu`<br>
  The name of the **Partner Logical Unit** of the **APPC Session** being extracted.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **SESSION** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU")
{"sessionKeyInterval": 5, "locked": True, "sessionKey": "e3c5e2e3d2c5e800", "securityCheckingLevel": "conv"}
```

###### Security Result Dictionary as JSON
```json
{
  "sessionKeyInterval": 5,
  "locked": true,
  "sessionKey": "e3c5e2e3d2c5e800",
  "securityCheckingLevel": "conv",
}
```

## `ResourceAdmin.delete_appc_session()`

```python
def delete_appc_session(
    self, net_id: str, local_lu: str, partner_lu: str
) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **APPC Session** profile in the **APPCLU** class.

#### 📥 Parameters
* `net_id`<br>
  The **Network ID** of the **APPC Session** being deleted.

* `local_lu`<br>
  The name of the **Local Logical Unit** of the **APPC Session** being deleted.

* `partner_lu`<br>
  The name of the **Partner Logical Unit** of the **APPC Session** being deleted.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.delete_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU")
{'securityResult': {'resource': {'name': 'TSTNET.TSTLOCLU.TSTPRTLU', 'class': 'APPCLU', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU) '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTNET.TSTLOCLU.TSTPRTLU",
      "class":"APPCLU",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE APPCLU             (TSTNET.TSTLOCLU.TSTPRTLU) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```