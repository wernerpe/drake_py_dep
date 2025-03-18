#include <pybind11/pybind11.h>

#include "foo.h"

namespace py = pybind11;

PYBIND11_MODULE(foo_binding, m) {
    m.doc() = "pybind11 foo bindings";
    m.def("foo", &foo, py::arg("x1"), py::arg("x2"), "add two vectors");
}