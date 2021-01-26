#include <Python.h>

#if PY_MAJOR_VERSION >= 3
#define PY3VER
#endif

static PyObject* hello(PyObject* self, PyObject* args) {
    printf("Hello World\n");
    return Py_None;
}

static PyMethodDef helloMethods[] = {
    { "helloworld", hello, METH_NOARGS, "Prints Hello World" },
    { NULL, NULL, 0, NULL }
};

#ifdef PY3VER

static struct PyModuleDef hellotest = {
    PyModuleDef_HEAD_INIT,
    "hellotest",
    "Hello Test Module",
    -1,
    helloMethods
};

PyMODINIT_FUNC PyInit_hellotest(void) {
    return PyModule_Create(&hellotest);
}

#else

// module initializer for python2
PyMODINIT_FUNC inithellotest() {
    Py_InitModule3("hellotest", helloMethods, "Hello Test Module");
}

#endif


