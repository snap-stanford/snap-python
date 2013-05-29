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


from darray import *
# Turn a Python list into a C double array
def createfromlist(l):
  d = new_darray(len(l))
  for i in range(0,len(l)):
    darray_set(d,i,l[i])
  return d

# Print out some elements of an array
def printelements(a, first, last):
  for i in range(first,last):
    print darray_get(a,i)


from snap import *
import snap

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
  G = snap.TN
  GetWccs_PNGraph(