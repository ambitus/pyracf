---
layout: default
grand_parent: Setropts Admin
parent: Abstractions
---

# Gencmd Classes

Setropts Administration functions for modifying if a class has the Generic Command attribute. 
{: .fs-6 .fw-300 }

## `SetroptsAdmin.add_generic_command_processing_classes()`

```python
def add_generic_command_processing_classes(self, class_names: Union[str, List[str]]) -> Union[dict, bytes]:
```

#### 📄 Description

Add a class to the list of classes that RACF will process **Generic Commands** for.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to add the generic command attribute to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.add_generic_command_processing_classes("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS      GENCMD    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult":{
      "systemSettings":{
        "operation":"set",
        "requestId":"SetroptsRequest",
        "commands":[
          {
            "safReturnCode":0,
            "returnCode":0,
            "reasonCode":0,
            "image":"SETROPTS      GENCMD    (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```


## `SetroptsAdmin.remove_generic_command_processing_classes()`

```python
def remove_generic_command_processing_classes(self, class_names: Union[str, List[str]]) -> Union[dict, bytes]:
```

#### 📄 Description

Remove a class from the list of classes that RACF will process **Generic Commands** for.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to remove the generic command attribute from.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.remove_generic_command_processing_classes("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS    NOGENCMD    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}

```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult":{
      "systemSettings":{
        "operation":"set",
        "requestId":"SetroptsRequest",
        "commands":[
          {
            "safReturnCode":0,
            "returnCode":0,
            "reasonCode":0,
            "image":"SETROPTS    NOGENCMD   (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```