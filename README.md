# pyRACF

Python interface i
nto the RACF management application programming interface.

## Description

As automation becomes more and more prevalent, the need to manage the security environment programmaticaly increases. On z/OS that means managing a security product like the IBM Resource Access Control Facility(RACF). RACF is the primary facility for managing identity, authority, and access control for z/OS. There are more than 50 callable services with assembler interfaces that are part of the RACF API. The complete set of interfaces can be found at:

<http://publibz.boulder.ibm.com/epubs/pdf/ich2d112.pdf>

 While there are a number of languages that can be used to manage RACF, (from low level lnaguages like Assembler to higher level languages like REXX), the need to have it in a language that is used to manage other platforms is paramount. The pyRACF project is focused on making the RACF management tasks available to Python programmers. This will make it easier to manage RACF from management tools like Ansible and Tekton.

## Getting Started

### Dependencies

* z/OS 2.4 and higher.
* R_SecMgtOper (IRRSMO00): Security Management Operations.
* The appropriate RACF authorizations. Detail can be found at: <https://www.ibm.com/docs/en/zos/2.3.0?topic=operations-racf-authorization>

### Installing

Build the c code with:

```shell
cd common && ./build.sh && cd ..
```

Put the resulting dll in a directory of your libpath or include the directory that contains the dll in your libpath.
Make sure that the python code is in a directory defined in your PYTHONPATH or extend your PYTHONPATH to point to the directory containing pyracf python code.

### Executing program

import the pyracf.py package and issue the appropriate python calls. This will grow over time. In the samples directory you will find examples of user, group, and resource profile management. Additionally there is more information in the [index.md](./docs/index.md) file.

## Help

Questions, comments, and bugs can be discussed on the #pyracf channel in the IBMZ community

## Authors

* Leonard Carcaramo: lcarcaramo@ibm.com
* Elijah Swift: Elijah.Swift@ibm.com
* Joseph Bostian: jbostian@us.ibm.com
* Melissa Chodziutko: mchodziutko@ibm.com

## Version History

* 0.9 Initial release with IRRSmo00
