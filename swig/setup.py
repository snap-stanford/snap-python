#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

import inspect
import os
import sys

from distutils.core import setup, Extension

snap_module = Extension(
    '_snap',
    sources = ['snap_wrap.cxx'],
    define_macros = [("__STDC_LIMIT_MACROS", None)],
    include_dirs = ["../../", "../../../../snap/snap-core", "../../../../snap/glib-core"],
    extra_compile_args = ["-std=c++98", "-O3", "-shared"],
    extra_objects = ['Snap.o'],
    libraries = ["rt"],
    )

# get the installation directory

# get the system Python directory
sys_install = os.path.join(
            os.path.dirname(inspect.getfile(inspect)),
            "site-packages")

# check for an alternative Python user directory
user_install = sys_install
for p in sys.path:
    n = p.find("site-packages")
    if n > 0:
        user_install = os.path.join(p[:n],"site-packages")
        break

setup (name = 'snap',
    py_modules = ["snap"],
    #ext_modules = [snap_module],
    data_files = [(user_install, ["_snap.so"])],
    version = '0.1',
    author      = "snap.stanford.edu",
    description = """SNAP (Stanford Network Analysis Platform) Python""",
    )

