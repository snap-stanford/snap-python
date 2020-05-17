#include <Python.h>

static PyObject* hello(PyObject* self, PyObject* args) {
    printf("Hello World\n");
    return Py_None;
}

static PyMethodDef myMethods[] = {
    { "helloworld", hello, METH_NOARGS, "Prints Hello World" },
    { NULL, NULL, 0, NULL }
};


static struct PyModuleDef hellotest = {
    PyModuleDef_HEAD_INIT,
    "hellotest",
    "Hello Test Module",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_hellotest(void) {
    return PyModule_Create(&hellotest);
}


