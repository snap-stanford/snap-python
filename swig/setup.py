#!/usr/bin/env python

"""
setup.py file for SNAP (Stanford Network Analysis Platform) Python
    Linux version, generated on CentOS, tested on Ubuntu as well
"""

import re
import inspect
import os
import platform
import sys

#from distutils.core import setup, Extension
#from setuptools import setup, Extension

import setuptools

# added pip flag
swpip = False

#
#   Snap.py version
#
snappy_version = "5.2.0"
def getdynpath():
    '''
    get the path for the Python dynamic library
    '''
 
    s = inspect.getfile(inspect)

    newpath = None
    if "conda" in s:
        pattern = re.compile('[\w\d]+conda[\s\S]+\/lib\/')
        found = pattern.search(s)
        if found:
            newpath = s[:found.end()] + "libpython2.7.dylib"
    elif "Cellar" in s:
        start = s.find("Python.framework")
        if start > 0:
            newpath = s[:start] + "Python.framework/Python"

    return newpath
    
# is this a dry run
narg = 1
dryrun = False
if len(sys.argv) > narg  and  sys.argv[narg] == "-n":
    dryrun = True
    narg += 1

# is this a distribution package build
swsdist = False
if len(sys.argv) > narg  and  sys.argv[narg] == "sdist":
    swsdist = True

# is this a wheel build
swwheel = False
if len(sys.argv) > narg  and  sys.argv[narg] == "bdist_wheel":
    swwheel = True
    
# added OS specific wheeling
bdist_wheel = None
if swwheel:
    try:
        from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
        class bdist_wheel(_bdist_wheel):
            def finalize_options(self):
                _bdist_wheel.finalize_options(self)
                self.root_is_pure = False
    except ImportError:
        pass

#
#   determine package parameters:
#       package version, python version, os version, architecture
#

# snap version
snap_version = "dev"
try:
    f = open("Version","r")
    content = f.read()
    f.close()
    w = content.split("-")
    snap_version = w[1].strip()
except:
    pass

# python version
python_version = "py" + str(sys.version_info[0]) + "." + str(sys.version_info[1])

# os version
uname = platform.uname()
os_version = "unknown-x.x"

swubuntu = False
if uname[0] == "Linux":
    try:
        f = open("/etc/centos-release","r")
        versionpos = 2
    except:
        try:
            f = open("/etc/redhat-release","r")
            versionpos = 2
        except:
            try:
                f = open("/etc/issue","r")
                versionpos = 1
            except:
                pass

    try:
        content = f.read()
        f.close()
        w = content.split(" ")
        os_version = (w[0] + w[versionpos]).lower()
        if w[0] == "Ubuntu":
            swubuntu = True
    except:
        pass
    user_os="POSIX :: Linux"

    obj_name = "_snap.so"

elif uname[0] == "Darwin":
    os.system("sw_vers -productVersion > OSX-Release")
    try:
        f = open("OSX-Release","r")
        content = f.read()
        f.close()
        os_version = "macosx" + content.strip()
    except:
        pass
    user_os="MacOS"
    obj_name = "_snap.so"

elif uname[0].find("CYGWIN") == 0:
    w = uname[0].rsplit("-",1)
    os_version = w[0].lower()
    obj_name   = "_snap.so"
    user_os    = "Microsoft :: Windows"

elif uname[0].find("Windows") == 0:
    os_version = "Win"
    obj_name   = "_snap.pyd"
    user_os    = "Microsoft :: Windows"

# architecture
arch = "i386"
# x86_64 on Linux, Mac OS X, i686 on Cygwin
if uname[4] == "x86_64"  or  uname[4] == "i686"  or  uname[4] == "AMD64":
    arch = "x64"

# the tarball package name
pkg_version = "-".join([snappy_version, snap_version,
		os_version, arch, python_version])
if swwheel:
   # pip requires that package names on different platforms are the same
   pkg_version = snappy_version

#
#   get the installation directory
#

# get the system Python directory
sys_install = os.path.join(
            os.path.dirname(inspect.getfile(inspect)),
            "site-packages")

instdir = "site-packages"
if swubuntu:
    instdir = "dist-packages"

# pip path relative to usr/local/ for mac and linux
if uname[0] == "Darwin":
    pip_install = os.path.join('lib/python', instdir)
elif uname[0] == "Linux":
    sysinfo = str(sys.version_info[0]) + '.' + str(sys.version_info[1])
    pip_install = os.path.join('lib/python', sysinfo, instdir)
else:
    pip_install = os.path.join('lib/python', instdir)

# check for an alternative Python user directory
user_install = sys_install
for p in sys.path:
    n = p.find(instdir)
    if n > 0:
        user_install = os.path.join(p[:n],instdir)
        break

# if Mac OS X, get a path for the Python dynamic library
dynlib_path = None
if uname[0] == "Darwin":
    dynlib_path = getdynpath()

if dryrun:
    print("snappy_version %s" % snappy_version)
    print("snap_version %s" % snap_version)
    print("os_version %s" % os_version)
    print("arch %s" % arch)
    print("python_version %s" % python_version)
    print("user_os %s" % user_os)
    print("swubuntu %s" % swubuntu)
    print("pkg_version %s" % pkg_version)
    print("obj_name %s" % obj_name)
    print("user_install %s" % user_install)
    print("sdist_flag %s" % swsdist)
    print("wheel_flag %s" % swwheel)
    print("pip_install %s" % pip_install)
    if dynlib_path:
        print("dynlib_path %s" % dynlib_path)
    sys.exit(0)
    
# switch to pip directory
if swpip:
    user_install = pip_install

# specify additional files for Mac OS X
files = []
if uname[0] == "Darwin"  and  swsdist:
    files = ["install_name_tool", "update_dynlib.sh"]

#
#   update the dynamic library path
#
if dynlib_path:
    cmd = "./update_dynlib.sh " + dynlib_path
    os.system(cmd)
    
with open("README.txt", "r") as fh:
    long_description = fh.read()

#
#   setup configuration
#
setuptools.setup(name = 'snap',
    py_modules  = ["snap"],
    #ext_modules = [snap_module],
    data_files  = [(user_install, [obj_name])], #user_install
    scripts     = files,
    version     = pkg_version,
    author      = "snap.stanford.edu",
    description = '""SNAP (Stanford Network Analysis Platform) Python""',
    long_description = long_description,
    #long_description_content_type = "text/plain",
    #url = "https://github.com/snap-stanford/snap-python",
    cmdclass = {'bdist_wheel': bdist_wheel},
    classifiers = [
        "Programming Language :: Python :: " + str(sys.version_info[0]),
        "Operating System :: " + user_os,
    ],
    )

