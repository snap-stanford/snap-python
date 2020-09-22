# coding: utf-8
import hashlib
import math
import os
import re
import time
import unittest

import snap

PATH_TO_GNUTELLA = "data/p2p-Gnutella08.txt"

class SnapPythonTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.gnutella = snap.LoadEdgeList(snap.PNGraph, PATH_TO_GNUTELLA)
        super(SnapPythonTest, self).__init__(*args, **kwargs)

    def setUp(self):
        # Defaults for creating graphs
        self.num_nodes = 10

        # Full Graphs
        self.DirGraphFull = snap.GenFull(snap.PNGraph, self.num_nodes)
        self.UnDirGraphFull = snap.GenFull(snap.PUNGraph, self.num_nodes)
        self.NetFull = snap.GenFull(snap.PNEANet, self.num_nodes)

        # Star Graphs
        self.DirGraphStar = snap.GenStar(snap.PNGraph, self.num_nodes)
        self.UnDirGraphStar = snap.GenStar(snap.PUNGraph, self.num_nodes)
        self.NetStar = snap.GenStar(snap.PNEANet, self.num_nodes)

        # Graph With Self Edges
        self.DirGraphSelfEdge = snap.GenRndGnm(snap.PNGraph, 10, 20)
        self.DirGraphSelfEdge.AddEdge(0, 0)
        self.UnDirGraphSelfEdge = snap.GenRndGnm(snap.PUNGraph, 10, 20)
        self.UnDirGraphSelfEdge.AddEdge(0, 0)
        self.NetSelfEdge = snap.GenRndGnm(snap.PNEANet, 10, 20)
        self.NetSelfEdge.AddEdge(0, 0)

        # Graph With Multiple Zero-Degree Nodes
        self.DirGraphZeroDegree = snap.GenRndGnm(snap.PNGraph, 10, 1)
        self.UnDirGraphZeroDegree = snap.GenRndGnm(snap.PUNGraph, 10, 1)
        self.NetZeroDegree = snap.GenRndGnm(snap.PNEANet, 10, 1)

        # Trees
        self.DirTree = snap.GenTree(snap.PNGraph, 3, 3)
        self.UnDirTree = snap.GenTree(snap.PUNGraph, 3, 3)
        self.NetTree = snap.GenTree(snap.PNEANet, 3, 3)

        # Random
        self.DirRand = snap.GenRndGnm(snap.PNGraph, 10, 20)
        self.UnDirRand = snap.GenRndGnm(snap.PUNGraph, 10, 20)
        self.NetRand = snap.GenRndGnm(snap.PNEANet, 10, 20)





    # not at all sure how to test getitem, not in other
    def test_table_getitem(self):
        context = snap.TTableContext()

        schema = snap.Schema()

        schema.Add(snap.TStrTAttrPr("Col1", snap.atInt))
        schema.Add(snap.TStrTAttrPr("Col2", snap.atInt))
        schema.Add(snap.TStrTAttrPr("Col3", snap.atFlt))

        filename = "data/data-table.txt"
        grade_table = snap.TTable.LoadSS(schema, filename, context, "\t", snap.TBool(False))
        int_vec = snap.TIntV()
        int_vec.Add(0)
        int_vec.Add(1)
        int_vec.Add(2)
        int_vec.Add(3)
        int_vec.Add(4)
        # unsure about next line!
        col2_vec = grade_table[]
    # also passing on len for now since not obvious either.

    def test_table_merge(self):
        context = snap.TTableContext()

        schema = snap.Schema()

        schema.Add(snap.TStrTAttrPr("Col1", snap.atInt))
        schema.Add(snap.TStrTAttrPr("Col2", snap.atInt))
        schema.Add(snap.TStrTAttrPr("Col3", snap.atFlt))

        filename = "data/data-table.txt"
        grade_table = snap.TTable.LoadSS(schema, filename, context, "\t", snap.TBool(False))
        int_vec = snap.TIntV()
