"""
setup.py file for SNAP (Stanford Network Analysis Platform) Python
    Linux version, generated on CentOS, tested on Ubuntu as well
"""
import os
import shutil
import subprocess

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


SNAPPY_VERSION = "5.1.0.dev0"


class SwigExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class SwigBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        subprocess.check_call(['make'])

        if not os.path.exists(extdir):
            os.makedirs(extdir)

        shutil.copy('swig/_snap.so', extdir)
        shutil.copy('swig/snap.py', extdir)


with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='snap-stanford',
    version=SNAPPY_VERSION,
    author="snap.stanford.edu",
    description="SNAP (Stanford Network Analysis Platform) Python",
    long_description=LONG_DESCRIPTION,
    url="http://snap.stanford.edu",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    zip_safe=False,
    cmdclass=dict(build_ext=SwigBuild),
    ext_modules=[SwigExtension('snap._snap2')],
)
