#include <Python.h>

#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>

#pragma linkage(IRRSMO64, OS)

typedef struct
{
    unsigned char running_userid_length;
    char running_userid[8];
} running_userid_t;

// This function changes any null character not preceded by '>' to a blank character.
// This is a workaround for an issue where profile data embedded in response xml
// returned by IRROSMO00 sometimes includes null characters instead of properly
// encoded text, which causes the returned xml to be truncated.
void null_byte_fix(char *str, unsigned int length)
{
    for (int i = 1; i < length; i++)
    {
        if (str[i] == 0)
        {
            if (str[i - 1] == 0x6E)
            {
                return;
            }
            else
            {
                str[i] = 0x40;
            }
        }
    }
}

static PyObject *call_irrsmo00(PyObject *self, PyObject *args, PyObject *kwargs)
{
    const char *request_xml;
    const unsigned int request_xml_length;
    const unsigned int response_buffer_size;
    const unsigned int irrsmo00_options;
    const char *running_userid;
    const uint8_t running_userid_length;

    static char *kwlist[] = {
        "request_xml",
        "request_xml_length",
        "response_buffer_size",
        "irrsmo00_options",
        "running_userid",
        "running_userid_length",
        NULL};

    if (
        !PyArg_ParseTupleAndKeywords(
            args,
            kwargs,
            "y|IIIyb",
            kwlist,
            &request_xml,
            &request_xml_length,
            &response_buffer_size,
            &irrsmo00_options,
            &running_userid,
            &running_userid_length))
    {
        return NULL;
    }

    char work_area[1024];
    char req_handle[64] = {0};
    running_userid_t running_userid_struct = {running_userid_length, {0}};
    unsigned int alet = 0;
    unsigned int acee = 0;
    unsigned char response_buffer[response_buffer_size];
    memset(response_buffer, 0, response_buffer_size);
    unsigned int saf_rc = 0;
    unsigned int racf_rc = 0;
    unsigned int racf_rsn = 0;
    unsigned int num_parms = 17;
    unsigned int fn = 1; 

    strncpy(
        running_userid_struct.running_userid, 
        running_userid, 
        running_userid_struct.running_userid_length);

    IRRSMO64(
        work_area,
        alet,
        &saf_rc,
        alet,
        &racf_rc,
        alet,
        &racf_rsn,
        num_parms,
        fn,
        irrsmo00_options,
        request_xml_length,
        request_xml,
        req_handle,
        running_userid_struct,
        acee,
        response_buffer_size,
        response_buffer);

    null_byte_fix(response_buffer, response_buffer_size);

    return Py_BuildValue("y*BBB", rsp, saf_rc, racf_rc, racf_rsn);
}

static char call_irrsmo00_docs[] =
    "call_irrsmo00(\n"
    "    request_xml: bytes,\n"
    "    request_xml_length: uint,\n"
    "    response_buffer_size: uint,\n"
    "    irrsmo00_options: uint,\n"
    "    running_userid: bytes,\n"
    "    running_userid_length: uint,\n"
    ") -> List[bytes,int,int,int]:\n"
    "# Returns an XML response string and return and reason "
    "codes from the IRRSMO00 RACF Callable Service.\n";

static PyMethodDef cpyracf_methods[] = {
    {"call_irrsmo00", (PyCFunction)call_irrsmo00,
     METH_VARARGS | METH_KEYWORDS, call_irrsmo00_docs},
    {NULL}};

static struct PyModuleDef cpyracf_module_def =
    {
        PyModuleDef_HEAD_INIT,
        "cpyracf",
        "C code that enables pyRACF to call the IRRSMO00 RACF callable service.\n",
        -1,
        cpyracf_methods};

PyMODINIT_FUNC PyInit_cpyracf(void)
{
    Py_Initialize();
    return PyModule_Create(&cpyracf_module_def);
}
