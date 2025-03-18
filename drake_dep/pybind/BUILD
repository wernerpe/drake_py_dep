load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

pybind_extension(
    name = "foo_binding",
    srcs = ["foo_binding.cpp"],
    copts = [
        "-Idrake_dep/src",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//drake_dep/src:foo",
    ],
)