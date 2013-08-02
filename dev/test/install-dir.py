#!/usr/bin/env python

"""
print out the Python install directory
"""

import inspect
import os
import sys

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

print "install-prefix", user_install

