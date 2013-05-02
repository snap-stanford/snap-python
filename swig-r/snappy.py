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

def FIn(FName):

  return TFIn(TStr(FName))

def FOut(FName):
  
  return TFOut(TStr(FName))

def Load(FName):
  """
    Opens graph file and returns graph.
  """
    
  f = TFIn(TStr(FName))
  return Load(f)


def Save(Graph, FName):
  """
    Saves graph file.
  """
  
  FOut = FOut(FName)
  Graph.__ref__().Save(FOut)   # Save as TUNGraph or TNGraph
  FOut.Flush()