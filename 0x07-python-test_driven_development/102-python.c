#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints Python string information
 * @p: Python object
 */

void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("[.] string object info\n");
	printf("  type: %s\n", p->ob_type->tp_name);
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));

	const char *s = PyUnicode_AsUTF8(p);
	printf("  value: %s\n", s);
}
