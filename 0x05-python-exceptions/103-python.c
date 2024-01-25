#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyListObject\n");
        return;
    }

    size = PyObject_Length(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->ob_base.ob_size);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    }
}


void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
        return;
    }

    size = PyObject_Length(p);
    printf("[.] Bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: ");
    for (i = 0; i < size; i++) {
        unsigned char byte = ((unsigned char *)PyBytes_AsString(p))[i];
        printf("%02x", byte);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}


void print_python_float(PyObject *p) {
    double value;

    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyFloatObject\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] Float object info\n");
    printf("  value: %f\n", value);
}
