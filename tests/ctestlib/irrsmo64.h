#include <string.h>
#include <stdio.h>

#ifndef _irrsmo64_test
#define _irrsmo64_test

#define REQUEST_XML_BASIC_SIZE 220
#define RESULT_XML_BASIC_SIZE 1252

#define REQUEST_XML_TEST_SIZE 214
#define RESULT_XML_SIZE 2328
#define PARTIAL_XML_SIZE 201


typedef struct
{
    unsigned char running_userid_length;
    char running_userid[8];
} running_userid_t;

void IRRSMO64(
    char work_area[1024],
    unsigned int alet_saf_rc,
    unsigned int * saf_rc,
    unsigned int alet_racf_rc,
    unsigned int * racf_rc,
    unsigned int alet_racf_rsn,
    unsigned int * racf_rsn,
    unsigned int num_parms,
    unsigned int fn,
    unsigned int irrsmo00_options,
    unsigned int request_xml_length,
    char * request_xml,
    unsigned char request_handle[64],
    running_userid_t userid,
    unsigned int acee,
    unsigned int * result_len,
    char * result_buffer);

#endif