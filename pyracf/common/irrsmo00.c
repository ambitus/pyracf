#include <Python.h>

#include <unistd.h>
#include <signal.h>
#include <stdio.h>

#define BUFFER_SIZE (100000)

#pragma linkage(IRRSMO64, OS)

typedef struct {
        unsigned char len;
        char str[8];
} VarStr_T;

static PyObject* call_irrsmo00(PyObject* self, PyObject* args, PyObject *kwargs) {
   const unsigned int xml_len;
   const unsigned int input_opts;
   const char *input_xml;

   static char *kwlist[] = {"xml_str", "xml_len", "opts", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "y|II", kwlist, &input_xml, &xml_len, &input_opts)) {
        return NULL;
    }


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

   return Py_BuildValue("y", rsp);
}

static char call_irrsmo00_docs[] =
   "call_irrsmo00(input_xml: bytes, xml_len: uint, opts: uint): Returns an XML response from the IRRSMO00 RACF Callable Service.\n";

static PyMethodDef cpyracf_methods[] = {
   {"call_irrsmo00", (PyCFunction)call_irrsmo00,
      METH_VARARGS | METH_KEYWORDS, call_irrsmo00_docs},
      {NULL}
};

static struct PyModuleDef cpyracf_module_def =
{
        PyModuleDef_HEAD_INIT,
        "cpyracf", 
        "C code that enables pyRACF to call the IRRSMO00 RACF callable service.\n",
        -1,
        cpyracf_methods
};

PyMODINIT_FUNC PyInit_cpyracf(void)
{
        Py_Initialize();
        return PyModule_Create(&cpyracf_module_def);
}
