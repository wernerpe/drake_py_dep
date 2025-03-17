load("@rules_python//python:defs.bzl", "py_test")
load("@pip//:requirements.bzl", "requirement")

py_test(
    name = "test_drake_imports",
    srcs = ["test_drake_imports.py"],
    deps = [
        requirement("drake"),
        requirement("numpy"),
    ],
)