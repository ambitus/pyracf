---
layout: default
grand_parent: Setropts Admin
parent: Abstractions
---

# Statistics Classes

Setropts Administration functions for modifying if a class has the Statistics attribute. 
{: .fs-6 .fw-300 }

## `SetroptsAdmin.add_statistics_classes()`

```python
def add_statistics_classes(self, class_names: Union[str, List[str]]) -> Union[dict, bytes]:
```

#### 📄 Description

Add a class to the list of classes that RACF will collect **Statistics** for.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to add the statistics attribute to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.add_statistics_classes("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS      STATISTICS    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image":"SETROPTS      STATISTICS    (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```


## `SetroptsAdmin.remove_statistics_classes()`

```python
def remove_statistics_classes(self, class_names: Union[str, List[str]]) -> Union[dict, bytes]:
```

#### 📄 Description

Remove a class from the list of classes that RACF will collect **Statistics** for.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to remove the statistics attribute from.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.remove_statistics_classes("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS    NOSTATISTICS    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0}}}

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
            "image":"SETROPTS    NOSTATISTICS    (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```