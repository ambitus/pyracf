#!/bin/bash

set -e

c89 -c -D_XOPEN_SOURCE_EXTENDED -Wc,lp64,langlvl\(extended\),STACKPROTECT\(ALL\)  -I../../safCommon -I irrsmo00.so irrsmo00.c
c89 -Wl,"DLL,LP64,XPLINK" -o irrsmo00.dll irrsmo00.o