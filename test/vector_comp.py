#!/usr/bin/python
# vector_comp.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Randomly generates Python types
#     - Compares conversion of Python types to SNAP types:
#           1. Python instantiation of SNAP type
#           2. Passing Python objects to SWIG C++ and convertion to SNAP type

import sys
sys.path.append("../swig")
import snap as Snap
import timeit
import cProfile

# Python conversion of Python list to SNAP vector
def PyListToTIntV(pylist):
  
  v = Snap.TIntV()
  for i in pylist:
    v.Add(i)

  return v

# C++ conversion of Python list to SNAP vector
def SwigPyList(pylist):
  v = Snap.PyToTIntV(pylist)
  return v

def main():
  
  n = 10**6

  pylist = range(n)

  # Basic verification that both methods have the same effect.
  #v1 = PyListToTIntV(pylist)
  #assert v1.Len() == n

  #v2 = SwigPyList(pylist)
  #assert v2.Len() == n
  #assert v1 == v2     # Doesn't appear to check
  #print "Converted %d values\n" % v2.Len()
  
  setup = """\
import snap as Snap 
from __main__ import PyListToTIntV, SwigPyList
pylist = range(%d)
""" % n

  print "Method 1: Python-to-SNAP conversion:"
  print "-" * 50
  s1 = "v1 = PyListToTIntV(pylist)"
#  print timeit.timeit(setup=setup, stmt=s1, number=5)/5.0
  cProfile.run(setup + s1)
 
  print "Method 2: Python-to-SNAP conversion:"
  print "-" * 50

  s2 = "v2 = SwigPyList(pylist)"
#  print timeit.timeit(setup=setup, stmt=s2, number=5)/5.0
  cProfile.run(setup + s2)

if __name__ == "__main__":
  main()
                      
                      
