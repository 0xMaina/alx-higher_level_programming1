#include <Python.h>
/**
 * print_python_list_info - print info about python lists
 * @p: python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
int length, mem, i;
PyObject *ob;
length = Py_SIZE(p);
mem = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", length);
printf("[*] Allocated = %d\n", mem);
for (i = 0; i < length; i++)
{
printf("Element %d: ", i);
ob = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(ob)->tp_name);
}
}
