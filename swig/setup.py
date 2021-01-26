"""
setup.py file for SNAP (Stanford Network Analysis Platform) Python
"""
import os
import platform
import shutil

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

import distutils.dir_util

SNAPPY_VERSION = '6.0.0'

class SwigExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class PkgBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        if not os.path.exists(extdir):
            os.makedirs(extdir)

        snap_obj = '_snap.so'
        if platform.uname()[0].find('Windows') == 0:
            snap_obj = '_snap.pyd'

        # SWIG generated SNAP .py
        shutil.copy('snap.py', extdir)
        # compiled SNAP object library
        shutil.copy(snap_obj, extdir)

        # __init__ to import snapx as a module
        shutil.copy('snap/__init__.py', extdir)
        # snapx implementation
        distutils.dir_util.copy_tree(
                        '../snapx/snapx', os.path.join(extdir, 'snapx'))

with open('../README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='snap-stanford',
    version=SNAPPY_VERSION,
    author="snap.stanford.edu",
    description="SNAP (Stanford Network Analysis Platform) Python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="http://snap.stanford.edu",
    license="3-clause BSD, http://snap.stanford.edu/snap/license.html",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering"
    ],
    zip_safe=False,
    cmdclass=dict(build_ext=PkgBuild),
    ext_modules=[SwigExtension('snap.')],
)

