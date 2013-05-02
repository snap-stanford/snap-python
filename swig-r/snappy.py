#!/usr/bin/python
# snappy.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Wraps SNAP functions to make it easier to implement
#     - User-friendly SNAP framework, which allows basic Python primitives.
#
# Note: Uses Python format when possible (lower-case 'open'), SNAP-otherise.

import sys
import os
import unittest

from snap import *

def FIn(fname):

  return TFIn(TStr(FName))

def FOut(fname):
  
  return TFOut(TStr(FName))

def Load(fname):
  """
    Opens graph file and returns graph.
  """
    
  f = TFIn(TStr(FName))
  return Load(f)
