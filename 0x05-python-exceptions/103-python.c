#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t i;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++) {
            printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        }
    } else {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_GET_SIZE(p);
        const char *str = PyBytes_AsString(p);
        Py_ssize_t i;

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);

        if (size > 10) {
            size = 10;
        }
        printf("  first %ld bytes: ", size);
        for (i = 0; i < size; i++) {
            printf("%02hhx", str[i]);
            if (i < size - 1) {
                printf(" ");
            }
        }
        printf("\n");
    } else {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  value: %s\n", PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
    } else {
        fprintf(stderr, "  [ERROR] Invalid Float Object\n");
    }
}
