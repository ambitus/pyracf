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

static PyObject* pyracf_call_irrsmo00(PyObject* self, PyObject* args, PyObject *kwargs) {
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

static char pyracf_call_irrsmo00_docs[] =
   "pyracf_call_irrsmo00(input_xml: bytes, xml_len: uint, opts: uint): Returns XML response from RACF Callable Service IRRSMO00.\n";

static PyMethodDef pyracf_call_irrsmo00_methods[] = {
   {"pyracf_call_irrsmo00", (PyCFunction)pyracf_call_irrsmo00,
      METH_VARARGS | METH_KEYWORDS, pyracf_call_irrsmo00_docs},
      {NULL}
};

static struct PyModuleDef pyracf_call_irrsmo00_module_def =
{
        PyModuleDef_HEAD_INIT,
        "pyracf_call_irrsmo00", 
        "usage: pyracf_call_irrsmo00(input_xml: bytes, xml_len: uint, opts: uint) -> resp: bytes \n",
        -1,
        pyracf_call_irrsmo00_methods
};

PyMODINIT_FUNC PyInit_pyracf_call_irrsmo00(void)
{
        Py_Initialize();
        return PyModule_Create(&pyracf_call_irrsmo00_module_def);
}
