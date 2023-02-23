# pyRACF Documentation

pyRACF provides a simplified interface to IBMs security product Resource Access Control Facility aka RACF. Python programmers can use this as a way to manage their RACF environment without having to understand the underlying z/OS interfaces.

The pyRACF implementation relies on the R_SecMgtOper. The architectural decision for this interface can be found in the [choose-RACF-interface.md](../adr/choose-RACF-interface.md) file.

There is a small amount of C code written to connect Python with the underlying R_SecMgtOper macro and marshalling and demarshalling the data becomes relatively simple.

## Installation

Information on how to __install__ pyRACF can be found __[here](../README.md#installation)__.
There will ultimately be a PyPi version of pyRACF that will be able to be installed from PyPi directly.

## Use

This will evolve over time. Currently the examples found in the __[samples](../samples)__ directory will provide some understanding of how to call the capabilities.

&nbsp;

### [User Administration](samples/user_admin.md)

### [General Resource Profile](samples/resource_admin.md)

### [Data Set Profile Administration](samples/dataset_admin.md)

### [Access Administration](samples/access_admin.md)

### [Set RACF Options](samples/setropts_admin.md)