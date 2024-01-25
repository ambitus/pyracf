#define PY_SSIZE_T_CLEAN
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

// This function changes any null character not preceded by '>' to a space character.
// This is a workaround for an issue where profile data embedded in response xml
// returned by IRROSMO00 sometimes includes null characters instead of properly
// encoded text, which causes the returned xml to be truncated.
void null_byte_fix(char *str, unsigned int length)
{
    for (int i = 1; i < length; i++)
    {
        if (str[i] == 0)
        {
            if (str[i - 1] == 0x6E)     // 0xfE is a '>' character in IBM-1047
            {
                return;
            }
            else
            {
                str[i] = 0x40;          // 0x40 is a space character in IBM-1047
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

    // https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue
    //
    // According to the Python 3 C API documentation:
    //      When memory buffers are passed as parameters to supply data to 
    //      build objects, as for the s and s# formats, the required data is 
    //      copied. Buffers provided by the caller are never referenced by 
    //      the objects created by Py_BuildValue(). In other words, if your 
    //      code invokes malloc() and passes the allocated memory to 
    //      Py_BuildValue(), your code is responsible for calling free() for 
    //      that memory once Py_BuildValue() returns.
    //
    //      y# (bytes) [const char *, Py_ssize_t]
    //          This converts a C string and its lengths to a Python object. 
    //          If the C string pointer is NULL, None is returned.
    //
    //      https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue
    //
    // So, given that 'response_buffer' is a stack allocated buffer
    // and that Python creates a copy of the buffer, which Python's
    // garbage collection should be responsible for, we do not need
    // to do any memory mangement here. 'response_buffer' will simply
    // just be popped off the stack when this function returns.
    //
    // Also, according to the Python3 C documentation 'y#' should be 
    // just giving us a copy copy of exactly what is in the buffer,
    // without attempting to do any transformations to the data.
    // The following GeesForGeeks article futher confirms that we are
    // going to get a bytes object that is completely unmanipulated.
    // https://www.geeksforgeeks.org/c-strings-conversion-to-python/
    //
    // In this case, all post processing of the data is handled on
    // the Python side.

    return Py_BuildValue(
        "y#BBB", 
        response_buffer, 
        response_buffer_size, 
        saf_rc, 
        racf_rc, 
        racf_rsn);
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
