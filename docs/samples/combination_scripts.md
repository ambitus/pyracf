:warning: _Ensure that pyRACF is __[installed](../../README.md#installation)__ as a **Python package** before you run these samples._

# Run Set Combination Script Samples

:warning: _Run the following samples from the **root directory** of this **repository**._

## Dynamically add Read Access Permission to a profile

```shell
$ python3 samples/combo/grant_dynamic_access.py
```

```shell
Your access at start: None
Defined READ access to TESTING of class: ELIJTEST for userid: ESWIFT.
Your access after definition: None
Issued RACLIST REFRESH for class ELIJTEST
Your access after refresh: read
```

```shell
Your access at start: None
Defined READ access to TESTING of class: ELIJTEST for userid: ESWIFT.
Your access after definition: read
Class ELIJTEST is not RACLISTED, access is updated. Exiting now...
```

```shell
Your access at start: alter
You have at least READ access to TESTING of class ELIJTEST already. Exiting now...
```

## Dynamically remove Read Access Permission from a profile

```shell
$ python3 samples/combo/grant_dynamic_access.py
```

```shell
Your access at start: alter
Deleted permission to TESTING of class: ELIJTEST for userid: ESWIFT.
Your access after deletion: alter
Issued RACLIST REFRESH for class ELIJTEST
Your access after refresh: None
```

```shell
Your access at start: alter
Deleted permission to TESTING of class: ELIJTEST for userid: ESWIFT.
Your access after deletion: None
Class ELIJTEST is not RACLISTED, access is updated. Exiting now...
```

```shell
Your access at start: None
You have no access to TESTING of class ELIJTEST already. Exiting now...
```

