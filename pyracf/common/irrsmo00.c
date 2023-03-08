#include <unistd.h>
#include <signal.h>
#include <stdio.h>

#define BUFFER_SIZE (100000)

typedef struct {
        unsigned char len;
        char str[8];
} VarStr_T;

#pragma linkage(IRRSMO64, OS)

#pragma export(call_irrsmo00)

char * call_irrsmo00(char input_xml[BUFFER_SIZE],unsigned int xml_len, unsigned int input_opts) {

    char work_area[1024];
    char req_handle[64] = { 0 };
    VarStr_T userid = { 0, {0}};
    unsigned int alet = 0;
    unsigned int acee = 0;
    char rsp[BUFFER_SIZE+1];
    memset(rsp, 0, BUFFER_SIZE);
    unsigned int saf_rc=0, racf_rc=0, racf_rsn=0;
    unsigned int num_parms=17, fn=1, opts = input_opts, rsp_len = sizeof(rsp)-1;

    IRRSMO64(
        work_area, 
        alet, 
        saf_rc, 
        alet, 
        racf_rc, 
        alet, 
        racf_rsn, 
        num_parms, 
        fn, 
        opts, 
        xml_len, 
        input_xml, 
        req_handle, 
        userid, 
        acee, 
        rsp_len, 
        rsp
    );

    FILE* dump_file = fopen("irrsmo00.dump", "wb+");
    fwrite(rsp, 1, BUFFER_SIZE, dump_file);
    fclose(dump_file);

    return rsp;
}