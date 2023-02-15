# Choosing IRRSM000 as the RACF interface

## Status

Accepted

## Context

There are multiple documented ways to interface with RACF. Choosing the right one is important to the success of the project. The team experimented with multiple options before choosing the solution. Here we will describe an option and why it was not used ultimately

### TSOCMD infrastructure

The easiest way to solve this would be to issue TSO commands from the python environment. We could do this a number of ways. Initially the use of the existing TSOCMD structure was the most straightforward.

#### Rejected because

The problem with this approach is that the data passed back and fourth had to fit into buffers that were 255 characters or less. This is problematic since the data we were passing back and fourth could be sizable. Ultimately we rejected this solution because of this.

### TSO Command from IKJEFT01

Instead of using TSOCMD, we could open a separate TSO address space and issue the command there. This would solve the buffer issue and we could handle as much data as we needed to.

#### Rejected Beause

We abandoned this when we realized it would mean that we would have to write the data to a file in the TSO address space then deal with it back in the calling world. This would mean that potentially sensitive data would be in files even temporarily. This is a security exposure. Aditionally it would mean we would have to spin up a new address space to solve the problem and it seemed unnecessarily expensive.

### Use the Assembler function IRRSEQ001

The team spent a fair amount of time on this one. The assembler macro is readily available, it would not cost much to deal with everything from a resource perspective. It was tricky to deal with because the interface is in 31 bit assembler and Python runs in 64 bit. Solving this meant marshalling the data multiple times, from Python 64 bit to 64 Bit C code to 64 bit Assembler code to 31 bit Assembler code. This required a fair amount of data manipulation gymnsatics but it was fast and lightwieght on resources.

#### Rejected Because

While we could make this interface function, it required authorization to do even the most basic things and would cause the identity runing the code to have way to much power to do even simple things. Additionally code would have to be linked together in supervisor state which again makes this problematic

### Decision

Use the IRRSM000 (AKA R_SecMgtOper) interface. This XML based interface was built for the purpose of managing RACF without all of the authorization headaches that are associated with IRRSEQ001. Additionally, mashalling and demashalling the data becomes a breeze as we are really just parsing XML data into JSON and vice versa. This makes the solution easier to understand and manage. Information about IRRSM00 can be found here: <https://www.ibm.com/docs/en/zos/2.3.0?topic=descriptions-r-secmgtoper-irrsmo00-security-management-operations>

## Consequences

Using IRRSM000 allows the team to provide a python solution with minimal overhead. It also creates a solution that is simple to follow and lends itself to simple updates. Since this solution should work with any SAF security product, it shoule not need much modification to support the broadcom security tools TOP SECRET or ACF2.
