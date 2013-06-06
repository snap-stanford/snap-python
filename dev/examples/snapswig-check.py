#!/usr/bin/python
# test-bfsdfs.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Performs mini unit tests for the following functions:
#     - gviz (graph visualization, using Gnuplot)
#     - bfsfdfs (Breadth First Search)

import sys
sys.path.append("../swig-r")
import snap as Snap

import os
import unittest

def GVizTest(NNodes, NEdges):
  
  Graph = Snap.GenRndGnm(NNodes, NEdges, 1)
  FName = "test.png"
  Snap.DrawGViz(Graph, 1, Snap.TStr(FName),
                        Snap.TStr("Snap Ringo Dot"), 1)
  
  return os.path.exists(FName)

def BfsDfsTest(NNodes, NEdges):
  Graph = Snap.GenRndGnm(NNodes, NEdges, 1)
  
  Snap.GetBfsTree(Graph, False, False, 1)
  
  G2 = Snap.GetBfsTree(Graph, False, False, 1)
  
  return G2

class GVizTests(unittest.TestCase):
  
  def testOne(self):
    NNodes, NEdges = (15, 25)
    self.failUnless(GVizTest(NNodes, NEdges))
  
  def testTwo(self):
    NNodes, NEdges = (8242, 12424)
    G = BfsDfsTest(NNodes, NEdges)
    self.assertEqual(NNodes == G.GetNodes(), NEdges == G.GetEdges())

def main():
  unittest.main()

if __name__ == "__main__":
  main()
                      
                      
