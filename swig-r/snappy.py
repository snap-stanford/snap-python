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

import os
import sys
import unittest

sys.path.append("../swig-r")

from snap import *

# Pass snap type through
def AddIntAttrN(attr, defaultValue=0):

  TNEANet.AddIntAttrN(TStr(attr), defaultValue)

TNEANet.AddIntAttrN = AddIntAttrN


def FIn(FName):

  return TFIn(TStr(FName))

def FOut(FName):
  
  return TFOut(TStr(FName))

def Load(FName):
  """
    Opens graph file and returns graph.
  """
  
  print "In load of snappy"
  f = TFIn(TStr(FName))
  return snap.Load(f)


def Save(Graph, FName):
  """
    Saves graph file (as directed, undirected or multi-edge).
  """
  
  FOut = FOut(FName)
  Graph.__ref__().Save(FOut)
  FOut.Flush()

# Convert from Python vector to Snap int

def GetWccs(G, V):

  G = snap.PNGraph() 