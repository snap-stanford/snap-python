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

        # Grid
        self.DirGrid = snap.GenGrid(snap.PNGraph, 3, 3, False)
        self.UnDirGrid = snap.GenGrid(snap.PUNGraph, 3, 3)
        self.NetGrid = snap.GenGrid(snap.PNEANet, 3, 3, False)

    #### Helper Functions for Tests ####

    def checkPlotHash(self, gen_file, exp_hash):
        self.assertTrue(os.path.isfile(gen_file))
        f = open(gen_file,'r')
        lines = f.readlines()
        f.close()
        # remove comments, since these include time
        newlines = []
        for line in lines:
            if len(line) > 0  and  line[0] == "#":
                continue
            newlines.append(line)
        # remove carriage return, which is included on Windows
        newcontent = str("".join(newlines).replace("\r","")).encode("utf-8")
        act_hash = hashlib.md5(newcontent).hexdigest()
        self.assertEqual(exp_hash, act_hash)

    def getFileHash(self, fname):
        f = open(fname, 'r')
        content = f.read()
        f.close()
        newcontent = str(content.replace("\r","")).encode("utf-8")
        test_hash = hashlib.md5(newcontent).hexdigest()
        return test_hash

    def checkPrintInfoOutput(self, filename, params):
        count = 0
        with open(filename) as f:
            for line in f:
                if count == 0:
                    firstLine = line.split(':')
                    self.assertEqual(params[count], firstLine[0])
                else:
                    result = re.findall('[0-9]+', line)
                    self.assertEqual(params[count], result[0])
                count += 1

    #### Tests ####
    
    def test_GenFull(self):
        # Directed Graph
        Graph_swig = snap.GenFull(snap.PNGraph, 5)
        Graph = snap.GenFull(snap.TNGraph, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenFull(snap.PUNGraph, 5)
        Graph = snap.GenFull(snap.TUNGraph, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenFull(snap.PNEANet, 5)
        Graph = snap.GenFull(snap.TNEANet, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenCircle(self):
        # Directed Graph
        Graph_swig = snap.GenCircle(snap.PNGraph, 10, 2)
        Graph = snap.GenCircle(snap.TNGraph, 10, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenCircle(snap.PUNGraph, 10, 2)
        Graph = snap.GenCircle(snap.TUNGraph, 10, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenCircle(snap.PNEANet, 10, 2)
        Graph = snap.GenCircle(snap.TNEANet, 10, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenGrid(self):
        # Directed Graph
        Graph_swig = snap.GenGrid(snap.PNGraph, 2, 2)
        Graph = snap.GenGrid(snap.TNGraph, 2, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenGrid(snap.PUNGraph, 2, 2)
        Graph = snap.GenGrid(snap.TUNGraph, 2, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenGrid(snap.PNEANet, 2, 2)
        Graph = snap.GenGrid(snap.TNEANet, 2, 2)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenStar(self):
        # Directed Graph
        Graph_swig = snap.GenStar(snap.PNGraph, 5)
        Graph = snap.GenStar(snap.TNGraph, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenStar(snap.PUNGraph, 5)
        Graph = snap.GenStar(snap.TUNGraph, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenStar(snap.PNEANet, 5)
        Graph = snap.GenStar(snap.TNEANet, 5)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenTree(self):
        # Directed Graph
        Graph_swig = snap.GenTree(snap.PNGraph, 3, 3)
        Graph = snap.GenTree(snap.TNGraph, 3, 3)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenTree(snap.PUNGraph, 3, 3)
        Graph = snap.GenTree(snap.TUNGraph, 3, 3)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenTree(snap.PNEANet, 3, 3)
        Graph = snap.GenTree(snap.TNEANet, 3, 3)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenRndGnm(self):
        # Directed Graph
        Graph_swig = snap.GenRndGnm(snap.PNGraph, 100, 1000)
        Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
        Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        Graph = snap.GenRndGnm(snap.TNEANet, 100, 1000)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_GenBaraHierar(self):
        # Directed Graph
        Graph_swig = snap.GenBaraHierar(snap.PNGraph, 3, True)
        Graph = snap.GenBaraHierar(snap.TNGraph, 3, True)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Undirected Graph
        Graph_swig = snap.GenBaraHierar(snap.PUNGraph, 3, True)
        Graph = snap.GenBaraHierar(snap.TUNGraph, 3, True)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

        # Network
        Graph_swig = snap.GenBaraHierar(snap.PNEANet, 3, True)
        Graph = snap.GenBaraHierar(snap.TNEANet, 3, True)
        self.assertEqual(Graph_swig.GetNodes(), Graph.GetNodes())
        self.assertEqual(Graph_swig.GetEdges(), Graph.GetEdges())

    def test_CntInDegNodes(self):
        # Directed graph
        num_nodes = self.DirGraphFull.CntInDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntInDegNodes(self.DirGraphFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntInDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntInDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Network
        num_nodes = self.NetFull.CntInDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntInDegNodes(self.NetFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

    def test_CntOutDegNodes(self):
        # Directed Graph
        num_nodes = self.DirGraphFull.CntOutDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntOutDegNodes(self.DirGraphFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntOutDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntOutDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Network
        num_nodes = self.NetFull.CntOutDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntOutDegNodes(self.NetFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

    def test_CntDegNodes(self):
        # Directed Graph - it will have twice the edges as the undirected graph
        num_nodes = self.DirGraphFull.CntDegNodes(2*(self.num_nodes-1))
        num_nodes_swig = snap.CntDegNodes(self.DirGraphFull, 2*(self.num_nodes-1))
        self.assertEqual(num_nodes, num_nodes_swig)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntDegNodes(self.num_nodes-1)
        num_nodes_swig = snap.CntDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Network
        num_nodes = self.NetFull.CntDegNodes(2*(self.num_nodes-1))
        num_nodes_swig = snap.CntDegNodes(self.NetFull, 2*(self.num_nodes-1))
        self.assertEqual(num_nodes, num_nodes_swig)

    def test_CntNonZNodes(self):
        # Directed Graph
        num_nodes = self.DirGraphFull.CntNonZNodes()
        num_nodes_swig = snap.CntNonZNodes(self.DirGraphFull)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntNonZNodes()
        num_nodes_swig = snap.CntNonZNodes(self.UnDirGraphFull)
        self.assertEqual(num_nodes, num_nodes_swig)

        # Network
        num_nodes = self.NetFull.CntNonZNodes()
        num_nodes_swig = snap.CntNonZNodes(self.NetFull)
        self.assertEqual(num_nodes, num_nodes_swig)

    def test_GetMxDegNId(self):
        # Directed Graph
        max_id = self.DirGraphStar.GetMxDegNId()
        max_id_swig = snap.GetMxDegNId(self.DirGraphStar)
        self.assertEqual(max_id, max_id_swig)

        # Undirected Graph
        max_id = self.UnDirGraphStar.GetMxDegNId()
        max_id_swig = snap.GetMxDegNId(self.UnDirGraphStar)
        self.assertEqual(max_id, max_id_swig)

        # Network
        max_id = self.NetStar.GetMxDegNId()
        max_id_swig = snap.GetMxDegNId(self.NetStar)
        self.assertEqual(max_id, max_id_swig)

    def test_GetMxInDegNId(self):
        # Directed Graph
        # node with id 0 is the only node with in-degree 0
        max_id = self.DirGrid.GetMxInDegNId()
        max_id_swig = snap.GetMxInDegNId(self.DirGrid)
        self.assertEqual(max_id, max_id_swig)

        # Undirected Graph
        max_id = self.UnDirGrid.GetMxInDegNId()
        max_id_swig = snap.GetMxInDegNId(self.UnDirGrid)
        self.assertEqual(max_id, max_id_swig)

        # Network
        # node with id 0 is the only node with in-degree 0
        max_id = self.NetGrid.GetMxInDegNId()
        max_id_swig = snap.GetMxInDegNId(self.NetGrid)
        self.assertEqual(max_id, max_id_swig)

    def test_GetMxOutDegNId(self):
        # Directed Graph
        max_id = self.DirGraphStar.GetMxOutDegNId()
        max_id_swig = snap.GetMxOutDegNId(self.DirGraphStar)
        self.assertEqual(max_id, max_id_swig)

        # Undirected Graph
        max_id = self.UnDirGraphStar.GetMxOutDegNId()
        max_id_swig = snap.GetMxOutDegNId(self.UnDirGraphStar)
        self.assertEqual(max_id, max_id_swig)

        # Network
        max_id = self.NetStar.GetMxOutDegNId()
        max_id_swig = snap.GetMxOutDegNId(self.NetStar)
        self.assertEqual(max_id, max_id_swig)

    def test_GetInDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetInDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetInDegCnt(self.DirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetInDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetInDegCnt(self.UnDirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Network
        DegToCntV = self.NetFull.GetInDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetInDegCnt(self.NetFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

    def test_GetOutDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetOutDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetOutDegCnt(self.DirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetOutDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetOutDegCnt(self.UnDirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Network
        DegToCntV = self.NetFull.GetOutDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetOutDegCnt(self.NetFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

    def test_GetDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetDegCnt(self.DirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetDegCnt(self.UnDirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Network
        DegToCntV = self.NetFull.GetDegCnt()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetDegCnt(self.NetFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

    def test_GetNodeInDegV(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetNodeInDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeInDegV(self.DirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetNodeInDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeInDegV(self.UnDirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Network
        DegToCntV = self.NetFull.GetNodeInDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeInDegV(self.NetFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

    def test_GetNodeOutDegV(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetNodeOutDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeOutDegV(self.DirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetNodeOutDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeOutDegV(self.UnDirGraphFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

        # Network
        DegToCntV = self.NetFull.GetNodeOutDegV()
        DegToCntV_swig = snap.TIntPrV()
        snap.GetNodeOutDegV(self.NetFull, DegToCntV_swig)
        self.assertEqual(DegToCntV, DegToCntV_swig)

    def test_GetDegSeqV(self):
        # Directed Graph
        V = self.DirGraphFull.GetDegSeqV(Dir = False)
        V_swig = snap.TIntV()
        snap.GetDegSeqV(self.DirGraphFull, V_swig)
        self.assertEqual(V, V_swig)

        # Undirected Graph
        V = self.UnDirGraphFull.GetDegSeqV(Dir = False)
        V_swig = snap.TIntV()
        snap.GetDegSeqV(self.UnDirGraphFull, V_swig)
        self.assertEqual(V, V_swig)

        # Network
        V = self.NetFull.GetDegSeqV(Dir = False)
        V_swig = snap.TIntV()
        snap.GetDegSeqV(self.NetFull, V_swig)
        self.assertEqual(V, V_swig)

    def test_GetDegSeqV2(self):
        # Directed Graph
        V, V2 = self.DirGraphFull.GetDegSeqV(Dir = True)
        V_swig = snap.TIntV()
        V2_swig = snap.TIntV()
        snap.GetDegSeqV(self.DirGraphFull, V_swig, V2_swig)
        self.assertEqual(V, V_swig)
        self.assertEqual(V2, V2_swig)

        # Undirected Graph
        V, V2 = self.UnDirGraphFull.GetDegSeqV(Dir = True)
        V_swig = snap.TIntV()
        V2_swig = snap.TIntV()
        snap.GetDegSeqV(self.UnDirGraphFull, V_swig, V2_swig)
        self.assertEqual(V, V_swig)
        self.assertEqual(V2, V2_swig)

        # Network
        V, V2 = self.NetFull.GetDegSeqV(Dir = True)
        V_swig = snap.TIntV()
        V2_swig = snap.TIntV()
        snap.GetDegSeqV(self.NetFull, V_swig, V2_swig)
        self.assertEqual(V, V_swig)
        self.assertEqual(V2, V2_swig)

    def test_CntUniqUndirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqUndirEdges()
        num_edges_swig = snap.CntUniqUndirEdges(self.DirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqUndirEdges()
        num_edges_swig = snap.CntUniqUndirEdges(self.UnDirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Network
        num_edges = self.NetFull.CntUniqUndirEdges()
        num_edges_swig = snap.CntUniqUndirEdges(self.NetFull)
        self.assertEqual(num_edges, num_edges_swig)

    def test_CntUniqDirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqDirEdges()
        num_edges_swig = snap.CntUniqDirEdges(self.DirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqDirEdges()
        num_edges_swig = snap.CntUniqDirEdges(self.UnDirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Network
        num_edges = self.NetFull.CntUniqDirEdges()
        num_edges_swig = snap.CntUniqDirEdges(self.NetFull)
        self.assertEqual(num_edges, num_edges_swig)

    def test_CntUniqBiDirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqBiDirEdges()
        num_edges_swig = snap.CntUniqBiDirEdges(self.DirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqBiDirEdges()
        num_edges_swig = snap.CntUniqBiDirEdges(self.UnDirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Network
        num_edges = self.NetFull.CntUniqBiDirEdges()
        num_edges_swig = snap.CntUniqBiDirEdges(self.NetFull)
        self.assertEqual(num_edges, num_edges_swig)

    def test_CntSelfEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntSelfEdges()
        num_edges_swig = snap.CntSelfEdges(self.DirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Undirected Graph
        num_edges = self.UnDirGraphFull.CntSelfEdges()
        num_edges_swig = snap.CntSelfEdges(self.UnDirGraphFull)
        self.assertEqual(num_edges, num_edges_swig)

        # Network
        num_edges = self.NetFull.CntSelfEdges()
        num_edges_swig = snap.CntSelfEdges(self.NetFull)
        self.assertEqual(num_edges, num_edges_swig)

    def test_GetUnDir(self):
        # Directed Graph
        New_Graph = self.DirGraphStar.GetUnDir()
        New_Graph_swig = snap.GetUnDir(self.DirGraphStar)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = self.UnDirGraphStar.GetUnDir()
        New_Graph_swig = snap.GetUnDir(self.UnDirGraphStar)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = self.NetStar.GetUnDir()
        New_Graph_swig = snap.GetUnDir(self.NetStar)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_MakeUnDir(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphStar)
        New_Graph.MakeUnDir()
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphStar)
        snap.MakeUnDir(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphStar)
        New_Graph.MakeUnDir()
        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphStar)
        snap.MakeUnDir(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetStar)
        New_Graph.MakeUnDir()
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetStar)
        snap.MakeUnDir(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_AddSelfEdges(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphFull)
        New_Graph.AddSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphFull)
        snap.AddSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphFull)
        New_Graph.AddSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphFull)
        snap.AddSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetFull)
        New_Graph.AddSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetFull)
        snap.AddSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_DelSelfEdges(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphSelfEdge)
        New_Graph.DelSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphSelfEdge)
        snap.DelSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphSelfEdge)
        New_Graph.DelSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphSelfEdge)
        snap.DelSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetSelfEdge)
        New_Graph.DelSelfEdges()
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetSelfEdge)
        snap.DelSelfEdges(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_DelNodes(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphFull)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphFull)
        DelNodes_swig = snap.TIntV()
        DelNodes_swig.Add(0)
        snap.DelNodes(New_Graph_swig, DelNodes_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphFull)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphFull)
        DelNodes_swig = snap.TIntV()
        DelNodes_swig.Add(0)
        snap.DelNodes(New_Graph_swig, DelNodes_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetFull)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetFull)
        DelNodes_swig = snap.TIntV()
        DelNodes_swig.Add(0)
        snap.DelNodes(New_Graph_swig, DelNodes_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_DelZeroDegNodes(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphZeroDegree)
        New_Graph.DelZeroDegNodes()
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphZeroDegree)
        snap.DelZeroDegNodes(New_Graph_swig)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphZeroDegree)
        New_Graph.DelZeroDegNodes()
        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphZeroDegree)
        New_Graph_swig.DelZeroDegNodes()
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetZeroDegree)
        New_Graph.DelZeroDegNodes()
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetZeroDegree)
        New_Graph_swig.DelZeroDegNodes()
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_DelDegKNodes(self):
        # Directed Graph
        New_Graph = snap.ConvertGraph(snap.PNGraph, self.DirGraphZeroDegree)
        New_Graph.DelDegKNodes(0,0)
        New_Graph_swig = snap.ConvertGraph(snap.PNGraph, self.DirGraphZeroDegree)
        snap.DelDegKNodes(New_Graph_swig,0,0)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        New_Graph = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphZeroDegree)
        New_Graph.DelDegKNodes(0,0)

        New_Graph_swig = snap.ConvertGraph(snap.PUNGraph, self.UnDirGraphZeroDegree)
        snap.DelDegKNodes(New_Graph_swig,0,0)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        New_Graph = snap.ConvertGraph(snap.PNEANet, self.NetZeroDegree)
        New_Graph.DelDegKNodes(0,0)
        New_Graph_swig = snap.ConvertGraph(snap.PNEANet, self.NetZeroDegree)
        snap.DelDegKNodes(New_Graph_swig,0,0)
        for node,node_swig in zip(New_Graph.Nodes(), New_Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(New_Graph.Edges(), New_Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_IsTree(self):
        # Directed Graph
        results = self.DirTree.IsTree()
        results_swig = snap.IsTree(self.DirTree)
        self.assertEqual(results, results_swig)

        # Network
        results = self.NetTree.IsTree()
        results_swig = snap.IsTree(self.NetTree)
        self.assertEqual(results, results_swig)

    def test_GetTreeRootNId(self):
        # Directed Graph
        root_id = self.DirTree.GetTreeRootNId()
        root_id_swig = snap.GetTreeRootNId(self.DirTree)
        self.assertEqual(root_id, root_id_swig)

        # Network
        root_id = self.NetTree.GetTreeRootNId()
        root_id_swig = snap.GetTreeRootNId(self.NetTree)
        self.assertEqual(root_id, root_id_swig)

    def test_GetBfsTree(self):
        start_node = 0
        follow_out = True
        follow_in = False

        # Directed Graph
        BfsTree = self.DirGraphFull.GetBfsTree(start_node, follow_out, follow_in)
        BfsTree_swig = snap.GetBfsTree(self.DirGraphFull, start_node, follow_out, follow_in)
        for node,node_swig in zip(BfsTree.Nodes(), BfsTree_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(BfsTree.Edges(), BfsTree_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        BfsTree = self.UnDirGraphFull.GetBfsTree(start_node, follow_out, follow_in)
        BfsTree_swig = snap.GetBfsTree(self.UnDirGraphFull, start_node, follow_out, follow_in)
        for node,node_swig in zip(BfsTree.Nodes(), BfsTree_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(BfsTree.Edges(), BfsTree_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        BfsTree = self.NetFull.GetBfsTree(start_node, follow_out, follow_in)
        BfsTree_swig = snap.GetBfsTree(self.NetFull, start_node, follow_out, follow_in)
        for node,node_swig in zip(BfsTree.Nodes(), BfsTree_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(BfsTree.Edges(), BfsTree_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetSubTreeSz(self):
        # Directed Graph
        results = self.DirTree.GetSubTreeSz(0, True, True)
        results_swig = snap.GetSubTreeSz(self.DirTree, 0, True, True)
        self.assertEqual(results, results_swig)

        # Undirected Graph
        results = self.UnDirTree.GetSubTreeSz(0, True, True)
        results_swig = snap.GetSubTreeSz(self.UnDirTree, 0, True, True)
        self.assertEqual(results, results_swig)

        # Network
        results = self.NetTree.GetSubTreeSz(0, True, True)
        results_swig = snap.GetSubTreeSz(self.NetTree, 0, True, True)
        self.assertEqual(results, results_swig)

    def test_GetNodesAtHop(self):
        # Directed Graph
        num_nodes, NodeVec = self.DirGraphStar.GetNodesAtHop(0, 1, True)
        NodeVec_swig = snap.TIntV()
        num_nodes_swig = snap.GetNodesAtHop(self.DirGraphStar, 0, 1, NodeVec_swig, True)
        self.assertEqual(num_nodes, num_nodes_swig)
        self.assertEqual(NodeVec, NodeVec_swig)

        # Undirected Graph
        num_nodes, NodeVec = self.UnDirGraphStar.GetNodesAtHop(0, 1, True)
        NodeVec_swig = snap.TIntV()
        num_nodes_swig = snap.GetNodesAtHop(self.UnDirGraphStar, 0, 1, NodeVec_swig, False)
        self.assertEqual(num_nodes, num_nodes_swig)
        self.assertEqual(NodeVec, NodeVec_swig)

        # Network
        num_nodes, NodeVec = self.NetStar.GetNodesAtHop(0, 1, True)
        NodeVec_swig = snap.TIntV()
        num_nodes_swig = snap.GetNodesAtHop(self.NetStar, 0, 1, NodeVec_swig, True)
        self.assertEqual(num_nodes, num_nodes_swig)
        self.assertEqual(NodeVec, NodeVec_swig)

    def test_GetNodesAtHops(self):
        # Directed Graph
        num_hops, HopVec = self.DirGraphStar.GetNodesAtHops(0, True)
        HopVec_swig = snap.TIntPrV()
        num_hops_swig = snap.GetNodesAtHops(self.DirGraphStar, 0, HopVec_swig, True)
        self.assertEqual(num_hops, num_hops_swig)
        self.assertEqual(HopVec, HopVec_swig)

        # Undirected Graph
        num_hops, HopVec = self.UnDirGraphStar.GetNodesAtHops(0, False)
        HopVec_swig = snap.TIntPrV()
        num_hops_swig = snap.GetNodesAtHops(self.UnDirGraphStar, 0, HopVec_swig, False)
        self.assertEqual(num_hops, num_hops_swig)
        self.assertEqual(HopVec, HopVec_swig)

        # Network
        num_hops, HopVec = self.NetStar.GetNodesAtHops(0, False)
        HopVec_swig = snap.TIntPrV()
        num_hops_swig = snap.GetNodesAtHops(self.NetStar, 0, HopVec_swig, True)
        self.assertEqual(num_hops, num_hops_swig)
        self.assertEqual(HopVec, HopVec_swig)

    def test_GetDegreeCentr(self):
        # Undirected Graph
        degree_center = self.UnDirGraphStar.GetDegreeCentr(0)
        degree_center_swig = snap.GetDegreeCentr(self.UnDirGraphStar, 0)
        self.assertEqual(degree_center, degree_center_swig)

    def test_GetFarnessCentr(self):
        # Undirected Graph
        farness_center = self.UnDirGraphStar.GetFarnessCentr(0)
        farness_center_swig = snap.GetFarnessCentr(self.UnDirGraphStar, 0)
        self.assertEqual(farness_center, farness_center_swig)

        # Directed Graph
        farness_center = self.DirGraphStar.GetFarnessCentr(0)
        farness_center_swig = snap.GetFarnessCentr(self.DirGraphStar, 0)
        self.assertEqual(farness_center, farness_center_swig)

        # Network
        farness_center = self.NetStar.GetFarnessCentr(0)
        farness_center_swig = snap.GetFarnessCentr(self.NetStar, 0)
        self.assertEqual(farness_center, farness_center_swig)

    def test_GetClosenessCentr(self):
        # Undirected Graph
        closeness_center = self.UnDirGraphStar.GetClosenessCentr(0)
        closeness_center_swig = snap.GetClosenessCentr(self.UnDirGraphStar, 0)
        self.assertEqual(closeness_center, closeness_center_swig)

        # Directed Graph
        closeness_center = self.DirGraphStar.GetClosenessCentr(0)
        closeness_center_swig = snap.GetClosenessCentr(self.DirGraphStar, 0)
        self.assertEqual(closeness_center, closeness_center_swig)

        # Network
        closeness_center = self.NetStar.GetClosenessCentr(0)
        closeness_center_swig = snap.GetClosenessCentr(self.NetStar, 0)
        self.assertEqual(closeness_center, closeness_center_swig)

    def test_GetEigenVectorCentr(self):
        # Undirected Graph
        EigenVec = self.UnDirGraphStar.GetEigenVectorCentr()
        EigenVec_swig = snap.TIntFltH()
        snap.GetEigenVectorCentr(self.UnDirGraphStar, EigenVec_swig)
        self.assertEqual(EigenVec, EigenVec_swig)

    def test_GetNodeEcc(self):
        # Directed Graph
        node_ecc = self.DirGraphStar.GetNodeEcc(0, True)
        node_ecc_swig = snap.GetNodeEcc(self.DirGraphStar, 0, True)
        self.assertEqual(node_ecc, node_ecc_swig)

        # Undirected Graph
        node_ecc = self.UnDirGraphStar.GetNodeEcc(0, True)
        node_ecc_swig = snap.GetNodeEcc(self.UnDirGraphStar, 0, False)
        self.assertEqual(node_ecc, node_ecc_swig)

        # Network
        node_ecc = self.NetStar.GetNodeEcc(0, True)
        node_ecc_swig = snap.GetNodeEcc(self.NetStar, 0, True)
        self.assertEqual(node_ecc, node_ecc_swig)

    def test_GetHits(self):
        # Directed Graph
        NIdHubH, NIdAuthH = self.DirGraphFull.GetHits()
        NIdHubH_swig = snap.TIntFltH()
        NIdAuthH_swig = snap.TIntFltH()
        snap.GetHits(self.DirGraphFull, NIdHubH_swig, NIdAuthH_swig)
        self.assertEqual(NIdHubH, NIdHubH_swig)
        self.assertEqual(NIdAuthH, NIdAuthH_swig)

        # Undirected Graph
        NIdHubH, NIdAuthH = self.UnDirGraphFull.GetHits()
        NIdHubH_swig = snap.TIntFltH()
        NIdAuthH_swig = snap.TIntFltH()
        snap.GetHits(self.UnDirGraphFull, NIdHubH_swig, NIdAuthH_swig)
        self.assertEqual(NIdHubH, NIdHubH_swig)
        self.assertEqual(NIdAuthH, NIdAuthH_swig)

        # Network
        NIdHubH, NIdAuthH = self.NetFull.GetHits()
        NIdHubH_swig = snap.TIntFltH()
        NIdAuthH_swig = snap.TIntFltH()
        snap.GetHits(self.NetFull, NIdHubH_swig, NIdAuthH_swig)
        self.assertEqual(NIdHubH, NIdHubH_swig)
        self.assertEqual(NIdAuthH, NIdAuthH_swig)

    def test_CommunityGirvanNewman(self):
        Graph = snap.GenPrefAttach(100, 10)
        act_val, Vec = Graph.CommunityGirvanNewman()
        Vec_swig = snap.TCnComV()
        act_val_swig = snap.CommunityGirvanNewman(Graph, Vec_swig)
        self.assertEqual(act_val, act_val_swig)
        self.assertEqual(Vec, Vec_swig)

    def test_CommunityCNM(self):
        gnutellaUndir = snap.ConvertGraph(snap.PUNGraph, self.gnutella)
        modularity, Vcc = gnutellaUndir.CommunityCNM()
        Vcc_swig = snap.TCnComV()
        modularity_swig = snap.CommunityCNM(gnutellaUndir, Vcc_swig)
        self.assertEqual(modularity, modularity_swig)
        self.assertEqual(Vcc, Vcc_swig)

    def test_GetModularity(self):
        V = [0,1,2,3,4]
        V_swig = snap.TIntV()
        for i in range(5):
            V_swig.Add(i)

        # Directed Graph
        val = self.DirGraphFull.GetModularity(V)
        val_swig = snap.GetModularity(self.DirGraphFull, V_swig)
        self.assertEqual(val, val_swig)

        # Undirected Graph
        val = self.UnDirGraphFull.GetModularity(V)
        val_swig = snap.GetModularity(self.UnDirGraphFull, V_swig)
        self.assertEqual(val, val_swig)

        # Network
        val = self.NetFull.GetModularity(V)
        val_swig = snap.GetModularity(self.NetFull, V_swig)
        self.assertEqual(val, val_swig)

    def test_GetEdgesInOut(self):
        V = [0]
        V_swig = snap.TIntV()
        V_swig.Add(0)

        # Directed Graph
        result = self.DirGraphFull.GetEdgesInOut(V)
        result_swig = snap.GetEdgesInOut(self.DirGraphFull, V_swig)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        result = self.UnDirGraphFull.GetEdgesInOut(V)
        result_swig = snap.GetEdgesInOut(self.UnDirGraphFull, V_swig)
        self.assertEqual(result, result_swig)

        # Network
        result = self.NetFull.GetEdgesInOut(V)
        result_swig = snap.GetEdgesInOut(self.NetFull, V_swig)
        self.assertEqual(result, result_swig)

    def test_GetBiConSzCnt(self):
        # Undirected Graph
        szCntV = self.UnDirGraphFull.GetBiConSzCnt()
        szCntV_swig = snap.TIntPrV()
        snap.GetBiConSzCnt(self.UnDirGraphFull, szCntV_swig)
        self.assertEqual(szCntV, szCntV_swig)

    def test_GetBiCon(self):
        # Undirected Graph
        CnComs = self.UnDirGraphFull.GetBiCon()
        CnComs_swig = snap.TCnComV()
        snap.GetBiCon(self.UnDirGraphFull, CnComs_swig)
        self.assertEqual(CnComs, CnComs_swig)

    def test_GetEdgeBridges(self):
        # Undirected Graph
        edges = self.UnDirGraphStar.GetEdgeBridges()
        edges_swig = snap.TIntPrV()
        snap.GetEdgeBridges(self.UnDirGraphStar, edges_swig)
        self.assertEqual(edges, edges_swig)

    def test_Get1CnCom(self):
        # Undirected Graph
        components = self.UnDirGraphStar.Get1CnCom()
        components_swig = snap.TCnComV()
        snap.Get1CnCom(self.UnDirGraphStar, components_swig)
        self.assertEqual(components, components_swig)

    def test_GetMxBiCon(self):
        # Directed Graph
        Graph = self.DirGraphFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.DirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        Graph = self.UnDirGraphFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.UnDirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        Graph = self.NetFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.NetFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetNodeWcc(self):
        # Directed Graph
        component = self.DirGraphStar.GetNodeWcc(1)
        component_swig = snap.TIntV()
        snap.GetNodeWcc(self.DirGraphStar, 1, component_swig)
        self.assertEqual(component, component_swig)

        # Undirected Graph
        component = self.UnDirGraphStar.GetNodeWcc(1)
        component_swig = snap.TIntV()
        snap.GetNodeWcc(self.UnDirGraphStar, 1, component_swig)
        self.assertEqual(component, component_swig)

        # Network
        component = self.NetStar.GetNodeWcc(1)
        component_swig = snap.TIntV()
        snap.GetNodeWcc(self.NetStar, 1, component_swig)
        self.assertEqual(component, component_swig)

    def test_isConnected(self):
        # Directed Graph
        result = self.DirGraphStar.IsConnected()
        result_swig = snap.IsConnected(self.DirGraphStar)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        result = self.UnDirGraphStar.IsConnected()
        result_swig = snap.IsConnected(self.UnDirGraphStar)
        self.assertEqual(result, result_swig)

        # Network
        result = self.NetStar.IsConnected()
        result_swig = snap.IsConnected(self.NetStar)
        self.assertEqual(result, result_swig)

    def test_isWeaklyConn(self):
        # Directed Graph
        result = self.DirGraphStar.IsWeaklyConn()
        result_swig = snap.IsWeaklyConn(self.DirGraphStar)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        result = self.UnDirGraphStar.IsWeaklyConn()
        result_swig = snap.IsWeaklyConn(self.UnDirGraphStar)
        self.assertEqual(result, result_swig)

        # Network
        result = self.NetStar.IsWeaklyConn()
        result_swig = snap.IsWeaklyConn(self.NetStar)
        self.assertEqual(result, result_swig)

    def test_GetWccSzCnt(self):
        # Directed Graph
        counts = self.DirGraphStar.GetWccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetWccSzCnt(self.DirGraphStar, counts_swig)
        self.assertEqual(counts, counts_swig)

        # Undirected Graph
        counts = self.UnDirGraphStar.GetWccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetWccSzCnt(self.UnDirGraphStar, counts_swig)
        self.assertEqual(counts, counts_swig)

        # Network
        counts = self.NetStar.GetWccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetWccSzCnt(self.NetStar, counts_swig)
        self.assertEqual(counts, counts_swig)

    def test_GetWccs(self):
        # Directed Graph
        components = self.DirGraphStar.GetWccs()
        components_swig = snap.TCnComV()
        snap.GetWccs(self.DirGraphStar, components_swig)
        self.assertEqual(components, components_swig)

        # Undirected Graph
        components = self.UnDirGraphStar.GetWccs()
        components_swig = snap.TCnComV()
        snap.GetWccs(self.UnDirGraphStar, components_swig)
        self.assertEqual(components, components_swig)

        # Network
        components = self.UnDirGraphStar.GetWccs()
        components_swig = snap.TCnComV()
        snap.GetWccs(self.NetStar, components_swig)
        self.assertEqual(components, components_swig)

    def test_GetSccSzCnt(self):
         # Directed Graph
        counts = self.DirGraphFull.GetSccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetSccSzCnt(self.DirGraphFull, counts_swig)
        self.assertEqual(counts, counts_swig)

        # Undirected Graph
        counts = self.UnDirGraphFull.GetSccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetSccSzCnt(self.UnDirGraphFull, counts_swig)
        self.assertEqual(counts, counts_swig)

        # Network
        counts = self.NetFull.GetSccSzCnt()
        counts_swig = snap.TIntPrV()
        snap.GetSccSzCnt(self.NetFull, counts_swig)
        self.assertEqual(counts, counts_swig)

    def test_GetSccs(self):
        # Directed Graph
        components = self.DirGraphFull.GetSccs()
        components_swig = snap.TCnComV()
        snap.GetSccs(self.DirGraphFull, components_swig)
        self.assertEqual(components, components_swig)

        # Undirected Graph
        components = self.UnDirGraphFull.GetSccs()
        components_swig = snap.TCnComV()
        snap.GetSccs(self.UnDirGraphFull, components_swig)
        self.assertEqual(components, components_swig)

        # Network
        components = self.NetFull.GetSccs()
        components_swig = snap.TCnComV()
        snap.GetSccs(self.NetFull, components_swig)
        self.assertEqual(components, components_swig)

    def test_GetMxWccSz(self):
        # Directed Graph
        size = self.DirGraphStar.GetMxWccSz()
        size_swig = snap.GetMxWccSz(self.DirGraphStar)
        self.assertEqual(size, size_swig)

        # Undirected Graph
        size = self.UnDirGraphStar.GetMxWccSz()
        size_swig = snap.GetMxWccSz(self.UnDirGraphStar)
        self.assertEqual(size, size_swig)

        # Network
        size = self.NetStar.GetMxWccSz()
        size_swig = snap.GetMxWccSz(self.NetStar)
        self.assertEqual(size, size_swig)

    def test_GetMxSccSz(self):
        # Directed Graph
        size = self.DirGraphStar.GetMxSccSz()
        size_swig = snap.GetMxSccSz(self.DirGraphStar)
        self.assertEqual(size, size_swig)

        # Undirected Graph
        size = self.UnDirGraphStar.GetMxSccSz()
        size_swig = snap.GetMxSccSz(self.UnDirGraphStar)
        self.assertEqual(size, size_swig)

        # Network
        size = self.NetStar.GetMxSccSz()
        size_swig = snap.GetMxSccSz(self.NetStar)
        self.assertEqual(size, size_swig)

    def test_GetMxWcc(self):
        # Directed Graph
        Graph = self.DirGraphStar.GetMxWcc()
        Graph_swig = snap.GetMxWcc(self.DirGraphStar)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        Graph = self.UnDirGraphStar.GetMxWcc()
        Graph_swig = snap.GetMxWcc(self.UnDirGraphStar)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        Graph = self.NetStar.GetMxWcc()
        Graph_swig = snap.GetMxWcc(self.NetStar)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetMxScc(self):
        # Directed Graph
        Graph = self.DirGraphFull.GetMxScc()
        Graph_swig = snap.GetMxScc(self.DirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        Graph = self.UnDirGraphFull.GetMxScc()
        Graph_swig = snap.GetMxScc(self.UnDirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        Graph = self.NetFull.GetMxScc()
        Graph_swig = snap.GetMxScc(self.NetFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetMxBiCon(self):
        # Directed Graph
        Graph = self.DirGraphFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.DirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        Graph = self.UnDirGraphFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.UnDirGraphFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        Graph = self.NetFull.GetMxBiCon()
        Graph_swig = snap.GetMxBiCon(self.NetFull)
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_PrintInfo(self):
        self.DirGraphFull.PrintInfo("description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '90', '0', '0', '0', '10'])
        os.remove('test.txt')

        self.UnDirGraphFull.PrintInfo("description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '45', '0', '0', '0', '10'])
        os.remove('test.txt')

        self.NetFull.PrintInfo("description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '90', '0', '0', '0', '10'])
        os.remove('test.txt')
        
    def test_GetKCoreNodes(self):
        # Directed Graph
        result, CoreN = self.DirGraphStar.GetKCoreNodes()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreNodes(self.DirGraphStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

        # Undirected Graph
        result, CoreN = self.UnDirGraphStar.GetKCoreNodes()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreNodes(self.UnDirGraphStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

        # Network
        result, CoreN = self.NetStar.GetKCoreNodes()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreNodes(self.NetStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

    def test_GetKCoreEdges(self):
        # Directed Graph
        result, CoreN = self.DirGraphStar.GetKCoreEdges()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreEdges(self.DirGraphStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

        # Undirected Graph
        result, CoreN = self.UnDirGraphStar.GetKCoreEdges()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreEdges(self.UnDirGraphStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

        # Network
        result, CoreN = self.NetStar.GetKCoreEdges()
        CoreN_swig = snap.TIntPrV()
        result_swig = snap.GetKCoreEdges(self.NetStar, CoreN_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(CoreN, CoreN_swig)

    def test_GenRewire(self):
        Rewired = self.UnDirRand.GenRewire()
        Rewired_swig = snap.GenRewire(self.UnDirRand)
        for node in Rewired.Nodes():
            for nodeR in Rewired_swig.Nodes():
                if node.GetId() == nodeR.GetId():
                    self.assertEqual(node.GetOutDeg()+node.GetInDeg(), nodeR.GetOutDeg()+nodeR.GetInDeg())

    def test_SaveEdgeList(self):
        # Directed Graph
        fname = "mygraph.txt"
        self.DirGraphFull.SaveEdgeList(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveEdgeList(self.DirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Undirected Graph
        fname = "mygraph.txt"
        self.UnDirGraphFull.SaveEdgeList(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Directed Graph
        fname = "mygraph.txt"
        self.NetFull.SaveEdgeList(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveEdgeList(self.NetFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

    def test_SaveMatlabSparseMtx(self):
        # Directed Graph
        fname = "mygraph.txt"
        self.DirGraphFull.SaveMatlabSparseMtx(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveMatlabSparseMtx(self.DirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Undirected Graph
        fname = "mygraph.txt"
        self.UnDirGraphFull.SaveMatlabSparseMtx(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveMatlabSparseMtx(self.UnDirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Directed Graph
        fname = "mygraph.txt"
        self.NetFull.SaveMatlabSparseMtx(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveMatlabSparseMtx(self.NetFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

    def test_GetSngVals(self):
        SngVals = 4
        SngValV = self.DirGraphFull.GetSngVals(SngVals)
        SngValV_swig = snap.TFltV()
        snap.GetSngVals(self.DirGraphFull, SngVals, SngValV_swig)
        self.assertEqual(SngValV, SngValV_swig)

    def test_GetEigVals(self):
        Graph = snap.GenStar(snap.PUNGraph, 50)
        NumEigVals = 2
        EigValV = Graph.GetEigVals(NumEigVals)
        EigValV_swig = snap.TFltV()
        snap.GetEigVals(Graph, NumEigVals, EigValV_swig)
        self.assertEqual(EigValV, EigValV_swig)

    def test_GetInvParticipRate(self):
        Graph = snap.TUNGraph.New()
        Graph.AddNode(1)
        Graph.AddNode(2)
        Graph.AddNode(3)
        Graph.AddNode(4)
        Graph.AddNode(5)
        Graph.AddNode(6)
        Graph.AddEdge(1, 2)
        Graph.AddEdge(2, 3)
        Graph.AddEdge(3, 5)
        Graph.AddEdge(4, 6)
        Graph.AddEdge(4, 1)

        EigValIprV = Graph.GetInvParticipRat(10, 1000)
        EigValIprV_swig = snap.TFltPrV()
        snap.GetInvParticipRat(Graph, 10, 1000, EigValIprV_swig)
        self.assertEqual(EigValIprV, EigValIprV_swig)

    def test_GetKCore(self):
        # Directed Graph
        k = self.num_nodes - 1
        KCore = self.DirGraphFull.GetKCore(k)
        KCore_swig = snap.GetKCore(self.DirGraphFull, k)
        for node,node_swig in zip(KCore.Nodes(), KCore_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(KCore.Edges(), KCore_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        k = self.num_nodes - 1
        KCore = self.UnDirGraphFull.GetKCore(k)
        KCore_swig = snap.GetKCore(self.UnDirGraphFull, k)
        for node,node_swig in zip(KCore.Nodes(), KCore_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(KCore.Edges(), KCore_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        k = self.num_nodes - 1
        KCore = self.NetFull.GetKCore(k)
        KCore_swig = snap.GetKCore(self.NetFull, k)
        for node,node_swig in zip(KCore.Nodes(), KCore_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(KCore.Edges(), KCore_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_PlotEigValRank(self):
        Graph = snap.GenStar(snap.PUNGraph, 20)
        NumEigVals = 2
        fname = 'test'
        desc = 'test'
        plt = 'eigVal.' + fname + '.plt'
        png = 'eigVal.' + fname + '.png'
        tab = 'eigVal.' + fname + '.tab'

        Graph.PlotEigValRank(NumEigVals, fname, desc)
        self.checkPlotHash(plt, 'c6ed3d548e47a32ab81b9d93fd5210fa')
        os.remove(plt)
        #self.checkPlotHash(png, '88e8150cca4d8b102e69e48f4f75bbc8')
        os.remove(png)
        self.checkPlotHash(tab, '74c9e40a9c5254c36f3808524f42b3d8')
        os.remove(tab)

    def test_PlotEigValDistr(self):
        Graph = snap.GenStar(snap.PUNGraph, 20)
        NumEigVals = 2
        fname = 'test'
        desc = 'test'
        plt = 'eigDistr.' + fname + '.plt'
        png = 'eigDistr.' + fname + '.png'
        tab = 'eigDistr.' + fname + '.tab'

        Graph.PlotEigValDistr(NumEigVals, fname, desc)
        self.checkPlotHash(plt, 'b22f6198cf212c27756b1edb4bed3508')
        os.remove(plt)
        #self.checkPlotHash(png, 'a620e5ca09dd447b4229850227678056')
        os.remove(png)
        self.checkPlotHash(tab, 'e6af369e84c82eea2fc1ae422d64f171')
        os.remove(tab)

    def test_PlotInvParticipRat(self):
        Graph = self.UnDirGraphStar
        NumEigVals = 3
        TimeLimit = 5
        fname = 'test'
        desc = 'test'
        plt = 'eigIPR.' + fname + '.plt'
        png = 'eigIPR.' + fname + '.png'
        tab = 'eigIPR.' + fname + '.tab'

        Graph.PlotInvParticipRat(NumEigVals, TimeLimit, fname, desc)
        self.checkPlotHash(plt, '87de319e252341f359c6cf92aa9b7090')
        os.remove(plt)
        #self.checkPlotHash(png, 'b518c4e4a1b0af4de529961986198127')
        os.remove(png)
        self.checkPlotHash(tab, '303939e032d64c7f1e3d201a3bb3629e')
        os.remove(tab)

    def test_PlotSngValRank(self):
        Graph = self.DirGraphFull
        SngVals = 3
        fname = 'test'
        desc = 'test'
        plt = 'sngVal.' + fname + '.plt'
        png = 'sngVal.' + fname + '.png'
        tab = 'sngVal.' + fname + '.tab'

        Graph.PlotSngValRank(SngVals, fname, desc)
        self.checkPlotHash(plt, '3d94b5107efd76abb478b18995447c2c')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4d688e2e38f3a7df07067ee1c92ab64')
        os.remove(png)
        self.checkPlotHash(tab, 'bc0edcc3dd69677930bb37316e3bdddf')
        os.remove(tab)

    def test_PlotSngValDistr(self):
        Graph = self.DirGraphFull
        SngVals = 3
        fname = 'test'
        desc = 'test'
        plt = 'sngDistr.' + fname + '.plt'
        png = 'sngDistr.' + fname + '.png'
        tab = 'sngDistr.' + fname + '.tab'

        Graph.PlotSngValDistr(SngVals, fname, desc)
        self.checkPlotHash(plt, '3c3dde0ffb43838943dcc5983baa5aa3')
        os.remove(plt)
        #self.checkPlotHash(png, '61a7195efc4864225c38f389e89c641e')
        os.remove(png)
        self.checkPlotHash(tab, '8683dabf0f9d787609dc1be1867f31a5')
        os.remove(tab)

    def test_PlotInDegDistr(self):
        fname = 'test'
        desc = 'test'
        plt = 'inDeg.' + fname + '.plt'
        png = 'inDeg.' + fname + '.png'
        tab = 'inDeg.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotInDegDistr(fname, desc)

        self.checkPlotHash(plt, '7f08086973d30d356eaa2e695e1a6fff')
        os.remove(plt)
        #self.checkPlotHash(png, '3a7a729d393a0ba37d455c67dacd8510')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotInDegDistr(fname, desc)

        self.checkPlotHash(plt, '9469cef95ca7701898d9da53fd83d3cf')
        os.remove(plt)
        #self.checkPlotHash(png, '3a7a729d393a0ba37d455c67dacd8510')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotInDegDistr(fname, desc)

        self.checkPlotHash(plt, '7f08086973d30d356eaa2e695e1a6fff')
        os.remove(plt)
        #self.checkPlotHash(png, '3a7a729d393a0ba37d455c67dacd8510')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

    def test_PlotOutDegDistr(self):
        fname = 'test'
        desc = 'test'
        plt = 'outDeg.' + fname + '.plt'
        png = 'outDeg.' + fname + '.png'
        tab = 'outDeg.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        snap.PlotOutDegDistr(Graph, fname, desc)

        self.checkPlotHash(plt, 'c0e03b616e4dc61331efb11d6ed6d3f6')
        os.remove(plt)
        #self.checkPlotHash(png, '03a7e7d530235143bf3a0ad09df30d5d')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotOutDegDistr(fname, desc)

        self.checkPlotHash(plt, '893e4d32769a7235bade506f4558559a')
        os.remove(plt)
        #self.checkPlotHash(png, '03a7e7d530235143bf3a0ad09df30d5d')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotOutDegDistr(fname, desc)

        self.checkPlotHash(plt, 'c0e03b616e4dc61331efb11d6ed6d3f6')
        os.remove(plt)
        #self.checkPlotHash(png, '03a7e7d530235143bf3a0ad09df30d5d')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

    def test_PlotWccDistr(self):
        fname = 'test'
        desc = 'test'
        plt = 'wcc.' + fname + '.plt'
        png = 'wcc.' + fname + '.png'
        tab = 'wcc.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotWccDistr(fname, desc)

        self.checkPlotHash(plt, '376654f801519f5a89519c020cd0cecf')
        os.remove(plt)
        #self.checkPlotHash(png, '3092ffd346709cbb0fb1210e39314c4c')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotWccDistr(fname, desc)

        self.checkPlotHash(plt, '25f0e2f9efd05b483bd3498de485b525')
        os.remove(plt)
        #self.checkPlotHash(png, '3092ffd346709cbb0fb1210e39314c4c')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotWccDistr(fname, desc)

        self.checkPlotHash(plt, '376654f801519f5a89519c020cd0cecf')
        os.remove(plt)
        #self.checkPlotHash(png, '3092ffd346709cbb0fb1210e39314c4c')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

    def test_PlotSccDistr(self):
        fname = 'test'
        desc = 'test'
        plt = 'scc.' + fname + '.plt'
        png = 'scc.' + fname + '.png'
        tab = 'scc.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotSccDistr(fname, desc)

        self.checkPlotHash(plt, 'f92d2c3b97156ff049ce64aaeada099c')
        os.remove(plt)
        #self.checkPlotHash(png, '91fb4493d7a2e9fef7fc998607a94649')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotSccDistr(fname, desc)

        self.checkPlotHash(plt, '09bc574ab814ec9bd0fc5865529f513b')
        os.remove(plt)
        #self.checkPlotHash(png, '91fb4493d7a2e9fef7fc998607a94649')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotSccDistr(fname, desc)

        self.checkPlotHash(plt, 'f92d2c3b97156ff049ce64aaeada099c')
        os.remove(plt)
        #self.checkPlotHash(png, '91fb4493d7a2e9fef7fc998607a94649')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

    def test_PlotClustCf(self):
        fname = 'test'
        desc = 'test'
        plt = 'ccf.' + fname + '.plt'
        png = 'ccf.' + fname + '.png'
        tab = 'ccf.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotClustCf(fname, desc)

        self.checkPlotHash(plt, 'd3e9c7ce6e1c5792a663bd0ee1abeb04')
        os.remove(plt)
        #self.checkPlotHash(png, '634a0518b0ee9db6c712ade205e089a2')
        os.remove(png)
        self.checkPlotHash(tab, '5e08cd594354ee12d733c98ffbb888c4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotClustCf(fname, desc)

        self.checkPlotHash(plt, 'f2d1d9456515a92700e922d213a82084')
        os.remove(plt)
        #self.checkPlotHash(png, '634a0518b0ee9db6c712ade205e089a2')
        os.remove(png)
        self.checkPlotHash(tab, '0350d2154b877f0ae9415ea4d7e07f07')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotClustCf(fname, desc)

        self.checkPlotHash(plt, 'd3e9c7ce6e1c5792a663bd0ee1abeb04')
        os.remove(plt)
        #self.checkPlotHash(png, '634a0518b0ee9db6c712ade205e089a2')
        os.remove(png)
        self.checkPlotHash(tab, '5e08cd594354ee12d733c98ffbb888c4')
        os.remove(tab)

    def test_PlotHops(self):
        fname = 'test'
        desc = 'test'
        plt = 'hop.' + fname + '.plt'
        png = 'hop.' + fname + '.png'
        tab = 'hop.' + fname + '.tab'
        NApprox = 1024

        # Directed Graph
        Graph = self.DirGraphFull
        isDir = True
        Graph.PlotHops(fname, desc, isDir, NApprox)

        self.assertTrue(os.path.isfile(plt))
        os.remove(plt)
        #self.checkPlotHash(png, '7558cfcb4b34e02fdda090fe2ebdeb03')
        os.remove(png)
        self.assertTrue(os.path.isfile(tab))
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        isDir = False
        Graph.PlotHops(fname, desc, isDir, NApprox)

        self.assertTrue(os.path.isfile(plt))
        os.remove(plt)
        #self.checkPlotHash(png, '7558cfcb4b34e02fdda090fe2ebdeb03')
        os.remove(png)
        self.assertTrue(os.path.isfile(tab))
        os.remove(tab)

        # Network
        Graph = self.NetFull
        isDir = True
        Graph.PlotHops(fname, desc, isDir, NApprox)

        self.assertTrue(os.path.isfile(plt))
        os.remove(plt)
        #self.checkPlotHash(png, '7558cfcb4b34e02fdda090fe2ebdeb03')
        os.remove(png)
        self.assertTrue(os.path.isfile(tab))
        os.remove(tab)

    def test_PlotShortPathDistr(self):
        fname = 'test'
        desc = 'test'
        plt = 'diam.' + fname + '.plt'
        png = 'diam.' + fname + '.png'
        tab = 'diam.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotShortPathDistr(fname, desc)

        self.checkPlotHash(plt, 'dbd3b8f4b0c82637c204173997625600')
        os.remove(plt)
        #self.checkPlotHash(png, 'ceaaab603196866102afa52042d33b15')
        os.remove(png)
        self.checkPlotHash(tab, '9b31a3d74e08ba09fb560dd2cfbf8e59')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotShortPathDistr(fname, desc)

        self.checkPlotHash(plt, 'b0e6ad4b3419c43ec4f4bac9ab9d74c7')
        os.remove(plt)
        #self.checkPlotHash(png, 'ceaaab603196866102afa52042d33b15')
        os.remove(png)
        self.checkPlotHash(tab, '9b31a3d74e08ba09fb560dd2cfbf8e59')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotShortPathDistr(fname, desc)

        self.checkPlotHash(plt, 'dbd3b8f4b0c82637c204173997625600')
        os.remove(plt)
        #self.checkPlotHash(png, 'ceaaab603196866102afa52042d33b15')
        os.remove(png)
        self.checkPlotHash(tab, '9b31a3d74e08ba09fb560dd2cfbf8e59')
        os.remove(tab)

    def test_PlotKCoreNodes(self):
        fname = 'test'
        desc = 'test'
        plt = 'coreNodes.' + fname + '.plt'
        png = 'coreNodes.' + fname + '.png'
        tab = 'coreNodes.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotKCoreNodes(fname, desc)

        self.checkPlotHash(plt, '8b47f5a7082e940e5b1a49f7a19bac1a')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4ffb2358ff82930b8832cbe1d5d3ecd')
        os.remove(png)
        self.checkPlotHash(tab, '1b1750d5304a4f2fbb19ab8919be8e27')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotKCoreNodes(fname, desc)

        self.checkPlotHash(plt, 'fd660ab9df8f84231ca61e6ad74b5a9f')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4ffb2358ff82930b8832cbe1d5d3ecd')
        os.remove(png)
        self.checkPlotHash(tab, '6a1db7740949f594b7cc3917ec65f4d9')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotKCoreNodes(fname, desc)

        self.checkPlotHash(plt, '8b47f5a7082e940e5b1a49f7a19bac1a')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4ffb2358ff82930b8832cbe1d5d3ecd')
        os.remove(png)
        self.checkPlotHash(tab, '1b1750d5304a4f2fbb19ab8919be8e27')
        os.remove(tab)

    def test_PlotKCoreEdges(self):
        fname = 'test'
        desc = 'test'
        plt = 'coreEdges.' + fname + '.plt'
        png = 'coreEdges.' + fname + '.png'
        tab = 'coreEdges.' + fname + '.tab'

        # Directed Graph
        Graph = self.DirGraphFull
        Graph.PlotKCoreEdges(fname, desc)

        self.checkPlotHash(plt, 'b2bcd1cbfadfa7280727163c0fc85854')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '7c22771f72c0bbe0c5ac5fa7c97928eb')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        Graph.PlotKCoreEdges(fname, desc)

        self.checkPlotHash(plt, 'ce0a125f61e5e00e58c639afa434b012')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '13f4612f2cec666a421b39d18ae7afb6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        Graph.PlotKCoreEdges(fname, desc)

        self.checkPlotHash(plt, 'b2bcd1cbfadfa7280727163c0fc85854')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '7c22771f72c0bbe0c5ac5fa7c97928eb')
        os.remove(tab)

    def test_GetESubGraph(self):
        EIdV = []
        for edge in self.NetStar.Edges():
            EIdV.append(edge.GetId())
        ESubGraph = self.NetStar.GetESubGraph(EIdV)
        EIdV_swig = snap.TIntV()
        for edge in self.NetStar.Edges():
            EIdV_swig.Add(edge.GetId())
        ESubGraph_swig = snap.GetESubGraph(self.NetStar, EIdV_swig)
        for node,node_swig in zip(ESubGraph.Nodes(), ESubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(ESubGraph.Edges(), ESubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_ConvertGraph(self):
        # Directed to Undirected
        UnDirStar = self.DirGraphStar.ConvertGraph(snap.PUNGraph)
        UnDirStar_swig = snap.ConvertGraph(snap.PUNGraph, self.DirGraphStar)
        for node,node_swig in zip(UnDirStar.Nodes(), UnDirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(UnDirStar.Edges(), UnDirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Directed to Network
        NetStar = self.DirGraphStar.ConvertGraph(snap.PNEANet)
        NetStar_swig = snap.ConvertGraph(snap.PNEANet, self.DirGraphStar)
        for node,node_swig in zip(NetStar.Nodes(), NetStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(NetStar.Edges(), NetStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected to Directed
        DirStar = self.UnDirGraphStar.ConvertGraph(snap.PNGraph)
        DirStar_swig = snap.ConvertGraph(snap.PNGraph, self.UnDirGraphStar)
        for node,node_swig in zip(DirStar.Nodes(), DirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(DirStar.Edges(), DirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected to Network
        NetStar = self.UnDirGraphStar.ConvertGraph(snap.PNEANet)
        NetStar_swig = snap.ConvertGraph(snap.PNEANet, self.UnDirGraphStar)
        for node,node_swig in zip(NetStar.Nodes(), NetStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(NetStar.Edges(), NetStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network to Undirected
        UnDirStar = self.NetStar.ConvertGraph(snap.PUNGraph)
        UnDirStar_swig = snap.ConvertGraph(snap.PUNGraph, self.NetStar)
        for node,node_swig in zip(UnDirStar.Nodes(), UnDirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(UnDirStar.Edges(), UnDirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network to Directed
        DirStar = self.NetStar.ConvertGraph(snap.PNGraph)
        DirStar_swig = snap.ConvertGraph(snap.PNGraph, self.NetStar)
        for node,node_swig in zip(DirStar.Nodes(), DirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(DirStar.Edges(), DirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_ConvertSubGraph(self):
        ListNodes = []
        for x in range(self.num_nodes):
            ListNodes.append(x)
        ListNodes_swig = snap.TIntV()
        for x in range(self.num_nodes):
            ListNodes_swig.Add(x)

        # Directed to Undirected
        UnDirStar = self.DirGraphStar.ConvertSubGraph(snap.PUNGraph, ListNodes)
        UnDirStar_swig = snap.ConvertSubGraph(snap.PUNGraph, self.DirGraphStar, ListNodes_swig)
        for node,node_swig in zip(UnDirStar.Nodes(), UnDirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(UnDirStar.Edges(), UnDirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Directed to Network
        NetStar = self.DirGraphStar.ConvertSubGraph(snap.PNEANet, ListNodes)
        NetStar_swig = snap.ConvertSubGraph(snap.PNEANet, self.DirGraphStar, ListNodes_swig)
        for node,node_swig in zip(NetStar.Nodes(), NetStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(NetStar.Edges(), NetStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected to Directed
        DirStar = self.UnDirGraphStar.ConvertSubGraph(snap.PNGraph, ListNodes)
        DirStar_swig = snap.ConvertSubGraph(snap.PNGraph, self.UnDirGraphStar, ListNodes_swig)
        for node,node_swig in zip(DirStar.Nodes(), DirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(DirStar.Edges(), DirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected to Network
        NetStar = self.UnDirGraphStar.ConvertSubGraph(snap.PNEANet, ListNodes)
        NetStar_swig = snap.ConvertSubGraph(snap.PNEANet, self.UnDirGraphStar, ListNodes_swig)
        for node,node_swig in zip(NetStar.Nodes(), NetStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(NetStar.Edges(), NetStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network to Undirected
        UnDirStar = self.NetStar.ConvertSubGraph(snap.PUNGraph, ListNodes)
        UnDirStar_swig = snap.ConvertSubGraph(snap.PUNGraph, self.NetStar, ListNodes_swig)
        for node,node_swig in zip(UnDirStar.Nodes(), UnDirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(UnDirStar.Edges(), UnDirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network to Directed
        DirStar = self.NetStar.ConvertSubGraph(snap.PNGraph, ListNodes)
        DirStar_swig = snap.ConvertSubGraph(snap.PNGraph, self.NetStar, ListNodes_swig)
        for node,node_swig in zip(DirStar.Nodes(), DirStar_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(DirStar.Edges(), DirStar_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetRndSubGraph(self):
        exp_nodes = 10

        # Directed Graph
        Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
        subGraph = Graph.GetRndSubGraph(exp_nodes)
        self.assertEqual(exp_nodes, subGraph.GetNodes())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(Graph.IsNode(edge.GetSrcNId()))
            self.assertTrue(Graph.IsNode(edge.GetDstNId()))

        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
        subGraph = Graph.GetRndSubGraph(exp_nodes)
        self.assertEqual(exp_nodes, subGraph.GetNodes())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(Graph.IsNode(edge.GetSrcNId()))
            self.assertTrue(Graph.IsNode(edge.GetDstNId()))

        # Directed Graph
        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        subGraph = Graph.GetRndSubGraph(exp_nodes)
        self.assertEqual(exp_nodes, subGraph.GetNodes())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(Graph.IsNode(edge.GetSrcNId()))
            self.assertTrue(Graph.IsNode(edge.GetDstNId()))

    def test_GetRndESubGraph(self):
        exp_edges = 10

        # Directed Graph
        Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
        subGraph = Graph.GetRndESubGraph(exp_edges)
        self.assertEqual(exp_edges, subGraph.GetEdges())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
            self.assertTrue(node.GetInDeg() + node.GetOutDeg() > 0)
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        subGraph = Graph.GetRndESubGraph(exp_edges)
        self.assertEqual(exp_edges, subGraph.GetEdges())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
            self.assertTrue(node.GetInDeg() + node.GetOutDeg() > 0)
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetTriadEdges(self):
        # Directed Graph
        act_triad_edges = self.DirGraphFull.GetTriadEdges()
        act_triad_edges_swig = snap.GetTriadEdges(self.DirGraphFull)
        self.assertEqual(act_triad_edges, act_triad_edges_swig)

        # Unirected Graph
        act_triad_edges = self.UnDirGraphFull.GetTriadEdges()
        act_triad_edges_swig = snap.GetTriadEdges(self.UnDirGraphFull)
        self.assertEqual(act_triad_edges, act_triad_edges_swig)

        # Network
        act_triad_edges = self.NetFull.GetTriadEdges()
        act_triad_edges_swig = snap.GetTriadEdges(self.NetFull)
        self.assertEqual(act_triad_edges, act_triad_edges_swig)

    def test_GetTriadParticip(self):
        f = math.factorial
        exp_num_tri = f(self.num_nodes-1)/f(2)/f(self.num_nodes-3)

        # Directed Graph
        TriadCntV = self.DirGraphFull.GetTriadParticip()
        TriadCntV_swig = snap.TIntPrV()
        snap.GetTriadParticip(self.DirGraphFull, TriadCntV_swig)
        self.assertEqual(TriadCntV, TriadCntV_swig)

        # Undirected Graph
        TriadCntV = self.UnDirGraphFull.GetTriadParticip()
        TriadCntV_swig = snap.TIntPrV()
        snap.GetTriadParticip(self.UnDirGraphFull, TriadCntV_swig)

        # Network
        TriadCntV = self.NetFull.GetTriadParticip()
        TriadCntV_swig = snap.TIntPrV()
        snap.GetTriadParticip(self.NetFull, TriadCntV_swig)

    def test_CntEdgesToSet(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        val = G.CntEdgesToSet(0, set())
        TS_swig = snap.TIntSet()
        val_swig = snap.CntEdgesToSet(G, 0, TS_swig)
        self.assertEqual(val, val_swig)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        val = G.CntEdgesToSet(0, set())
        TS_swig = snap.TIntSet()
        val_swig = snap.CntEdgesToSet(G, 0, TS_swig)
        self.assertEqual(val, val_swig)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        val = G.CntEdgesToSet(0, set())
        TS_swig = snap.TIntSet()
        val_swig = snap.CntEdgesToSet(G, 0, TS_swig)
        self.assertEqual(val, val_swig)

    def test_GetAnfNode(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SrcNId = 0
        DistNbrsV = Graph.GetAnfNode(SrcNId, 3, False, 8192)
        SrcNId_swig = 0
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId_swig, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SrcNId = 0
        DistNbrsV = Graph.GetAnfNode(SrcNId, 3, False, 8192)
        SrcNId_swig = 0
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId_swig, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SrcNId = 0
        DistNbrsV = Graph.GetAnfNode(SrcNId, 3, False, 8192)
        SrcNId_swig = 0
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId_swig, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

    def test_GetAnfGraph(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        DistNbrsV = Graph.GetAnfGraph(3, False, 8192)
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        DistNbrsV = Graph.GetAnfGraph(3, False, 8192)
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        DistNbrsV = Graph.GetAnfGraph(3, False, 8192)
        DistNbrsV_swig = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV_swig, 3, False, 8192)
        self.assertEqual(DistNbrsV, DistNbrsV_swig)

    def test_GetAnfEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        result_swig = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertAlmostEqual(result, result_swig, places=2)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        result_swig = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertAlmostEqual(result, result_swig, places=2)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        result_swig = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertAlmostEqual(result, result_swig, places=2)

    def test_GetAnfEffDiam2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetAnfEffDiam()
        result_swig = snap.GetAnfEffDiam(Graph)
        self.assertAlmostEqual(result, result_swig, places=2)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetAnfEffDiam()
        result_swig = snap.GetAnfEffDiam(Graph)
        self.assertAlmostEqual(result, result_swig, places=2)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetAnfEffDiam()
        result_swig = snap.GetAnfEffDiam(Graph)
        self.assertAlmostEqual(result, result_swig, places=2)

    def test_GetShortPath(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetShortPath(0, 1)
        result_swig = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetShortPath(0, 1)
        result_swig = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetShortPath(0, 1)
        result_swig = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(result, result_swig)

    def test_GetShortPath2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result, H = Graph.GetShortPathAll(0)
        H_swig = snap.TIntH()
        result_swig = snap.GetShortPath(Graph, 0, H_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(H, H_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result, H = Graph.GetShortPathAll(0)
        H_swig = snap.TIntH()
        result_swig = snap.GetShortPath(Graph, 0, H_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(H, H_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result, H = Graph.GetShortPathAll(0)
        H_swig = snap.TIntH()
        result_swig = snap.GetShortPath(Graph, 0, H_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(H, H_swig)

    def test_GetBfsFullDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetBfsFullDiam(10)
        result_swig = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetBfsFullDiam(10)
        result_swig = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetBfsFullDiam(10)
        result_swig = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(result, result_swig)

    def test_GetBfsEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetBfsEffDiam(10)
        result_swig = snap.GetBfsEffDiam(Graph, 10)
        self.assertAlmostEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetBfsEffDiam(10)
        result_swig = snap.GetBfsEffDiam(Graph, 10)
        self.assertEqual(result, result_swig)
        self.assertAlmostEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetBfsEffDiam(10)
        result_swig = snap.GetBfsEffDiam(Graph, 10)
        self.assertAlmostEqual(result, result_swig)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        PyList = [1, 4, 9, 16, 25, 36]
        result = Graph.GetBfsEffDiam(Num, PyList, True)
        result_swig = snap.GetBfsEffDiam(Graph, Num, List, True)
        self.assertAlmostEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        PyList = [1, 4, 9, 16, 25, 36]
        result = Graph.GetBfsEffDiam(Num, PyList, False)
        result_swig = snap.GetBfsEffDiam(Graph, Num, List, False)
        self.assertAlmostEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        PyList = [1, 4, 9, 16, 25, 36]
        result = Graph.GetBfsEffDiam(Num, PyList, True)
        result_swig = snap.GetBfsEffDiam(Graph, Num, List, True)
        self.assertAlmostEqual(result, result_swig)

    def test_GetBfsEffDiamAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        result = Graph.GetBfsEffDiamAll(Num, True)
        result_swig = snap.GetBfsEffDiamAll(Graph, Num, True)
        self.assertAlmostEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        result = Graph.GetBfsEffDiamAll(Num, False)
        result_swig = snap.GetBfsEffDiamAll(Graph, Num, False)
        self.assertAlmostEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        result = Graph.GetBfsEffDiamAll(Num, True)
        result_swig = snap.GetBfsEffDiamAll(Graph, Num, True)
        self.assertAlmostEqual(result, result_swig)

    def test_GetBetweennessCentr(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        Nodes_swig = snap.TIntFltH()
        Edges_swig = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes_swig, Edges_swig, 1.0)
        self.assertEqual(Nodes, Nodes_swig)
        self.assertEqual(Edges, Edges_swig)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        Nodes_swig = snap.TIntFltH()
        Edges_swig = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes_swig, Edges_swig, 1.0)
        self.assertEqual(Nodes, Nodes_swig)
        self.assertEqual(Edges, Edges_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        Nodes_swig = snap.TIntFltH()
        Edges_swig = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes_swig, Edges_swig, 1.0)
        self.assertEqual(Nodes, Nodes_swig)
        self.assertEqual(Edges, Edges_swig)

    def test_GetArtPoints(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        V = Graph.GetArtPoints()
        V_swig = snap.TIntV()
        snap.GetArtPoints(Graph, V_swig)
        self.assertEqual(V, V_swig)

    def test_GenConfModel(self):
        # Undirected Graph
        DegSeqV = [0]
        Graph = snap.GenConfModel(DegSeqV)
        DegSeqV_swig = snap.TIntV()
        DegSeqV_swig.Add(0)
        Graph_swig = snap.GenConfModel(DegSeqV_swig)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())

    def test_GetCmnNbrs(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        result_swig = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        result_swig = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        result_swig = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, result_swig)

    def test_GetCmnNbrs1(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        V_swig = snap.TIntV()
        result_swig = snap.GetCmnNbrs(Graph, 0, 1, V_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        V_swig = snap.TIntV()
        result_swig = snap.GetCmnNbrs(Graph, 0, 1, V_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        V_swig = snap.TIntV()
        result_swig = snap.GetCmnNbrs(Graph, 0, 1, V_swig)
        self.assertEqual(result, result_swig)
        self.assertEqual(V, V_swig)

    def test_GetNodeTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetNodeTriads(0)
        result_swig = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetNodeTriads(0)
        result_swig = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetNodeTriads(0)
        result_swig = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, result_swig)

    def test_GetNodeTriadsSet(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSet = set()
        for NbrIdx in range(4):
            GroupSet.add(NI.GetOutNId(NbrIdx))
        result = Graph.GetNodeTriadsSet(NId, GroupSet)
        GroupSet_swig = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet_swig.AddKey(NI.GetOutNId(NbrIdx))
        result_swig = snap.GetNodeTriads(Graph, NId, GroupSet_swig)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSetPy = set()
        for NbrIdx in range(4):
            GroupSetPy.add(NI.GetOutNId(NbrIdx))
        result = Graph.GetNodeTriadsSet(NId, GroupSetPy)
        GroupSet_swig = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet_swig.AddKey(NI.GetOutNId(NbrIdx))
        result_swig = snap.GetNodeTriads(Graph, NId, GroupSet_swig)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSetPy = set()
        for NbrIdx in range(4):
            GroupSetPy.add(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = Graph.GetNodeTriadsSet(NId, GroupSetPy)
        GroupSet_swig = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet_swig.AddKey(NI.GetOutNId(NbrIdx))
        result_swig = snap.GetNodeTriads(Graph, NId, GroupSet_swig)
        self.assertEqual(result, result_swig)

    def test_GetNodeTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        result = Graph.GetNodeTriadsAll(10)
        result_swig = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        result = Graph.GetNodeTriadsAll(10)
        result_swig = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        result = Graph.GetNodeTriadsAll(10)
        result_swig = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, result_swig)

    def test_GetTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetTriads()
        result_swig = snap.GetTriads(Graph)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetTriads()
        result_swig = snap.GetTriads(Graph)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetTriads()
        result_swig = snap.GetTriads(Graph)
        self.assertEqual(result, result_swig)

    def test_GetTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        result = Graph.GetTriadsAll()
        result_swig = snap.GetTriadsAll(Graph)
        self.assertEqual(result, result_swig)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        result = Graph.GetTriadsAll()
        result_swig = snap.GetTriadsAll(Graph)
        self.assertEqual(result, result_swig)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        result = Graph.GetTriadsAll()
        result_swig = snap.GetTriadsAll(Graph)
        self.assertEqual(result, result_swig)

    def test_GetClustCf(self):

        # testing GetClustCf(Graph, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        result = DirGraph.GetClustCf()
        result_swig = snap.GetClustCf(DirGraph)
        self.assertAlmostEqual(result, result_swig)

        # Undirected Graph
        result = UnGraph.GetClustCf()
        result_swig = snap.GetClustCf(UnGraph)
        self.assertAlmostEqual(result, result_swig)

        # Network
        result = MultiGraph.GetClustCf()
        result_swig = snap.GetClustCf(MultiGraph)
        self.assertAlmostEqual(result, result_swig)

        # parameter = 0

        result = DirGraph.GetClustCf(False, 0)
        result_swig = snap.GetClustCf(DirGraph, 0)
        self.assertAlmostEqual(result, result_swig)

        result = UnGraph.GetClustCf(False, 0)
        result_swig = snap.GetClustCf(UnGraph, 0)
        self.assertAlmostEqual(result, result_swig)

        result = MultiGraph.GetClustCf(False, 0)
        result_swig = snap.GetClustCf(MultiGraph, 0)
        self.assertAlmostEqual(result, result_swig)

        # parameter > 0

        result = DirGraph.GetClustCf(False, 3)
        result_swig = snap.GetClustCf(DirGraph, 3)
        self.assertAlmostEqual(result, result_swig)

        result = UnGraph.GetClustCf(False, 3)
        result_swig = snap.GetClustCf(UnGraph, 3)
        self.assertAlmostEqual(result, result_swig)

        result = MultiGraph.GetClustCf(False, 3)
        result_swig = snap.GetClustCf(MultiGraph, 3)
        self.assertAlmostEqual(result, result_swig)

    def test_GetClustCf2(self):

        # testing GetClustCf(Graph, DegToCCfV, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        result, V = DirGraph.GetClustCf(True)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(DirGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # Undirected Graph
        result, V = UnGraph.GetClustCf(True)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(UnGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # Network
        result, V = MultiGraph.GetClustCf(True)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(MultiGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # parameter = 0

        result, V = DirGraph.GetClustCf(True, 0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(DirGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = UnGraph.GetClustCf(True, 0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(UnGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = MultiGraph.GetClustCf(True, 0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(MultiGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # parameter > 0

        result, V = DirGraph.GetClustCf(True, 3)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(DirGraph, V_swig, 3)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = UnGraph.GetClustCf(True, 3)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(UnGraph, V_swig, 3)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = MultiGraph.GetClustCf(True, 3)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCf(MultiGraph, V_swig, 3)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

    def test_GetClustCfAll(self):

        DirGraph = snap.GenFull(snap.PNGraph, 100)
        UnGraph = snap.GenFull(snap.PUNGraph, 100)
        MultiGraph = snap.GenFull(snap.PNEANet, 100)

        # no parameter

        result, V = DirGraph.GetClustCfAll()
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(DirGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = UnGraph.GetClustCfAll()
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(UnGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = MultiGraph.GetClustCfAll()
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(MultiGraph, V_swig)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # parameter = 0

        result, V = DirGraph.GetClustCfAll(0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(DirGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = UnGraph.GetClustCfAll(0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(UnGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = MultiGraph.GetClustCfAll(0)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(MultiGraph, V_swig, 0)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        # parameter > 0

        result, V = DirGraph.GetClustCfAll(5)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(DirGraph, V_swig, 5)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = UnGraph.GetClustCfAll(5)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(UnGraph, V_swig, 5)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

        result, V = MultiGraph.GetClustCfAll(5)
        V_swig = snap.TFltPrV()
        result_swig = snap.GetClustCfAll(MultiGraph, V_swig, 5)
        self.assertAlmostEqual(result, result_swig)
        self.assertEqual(V, V_swig)

    def test_GetLen2Paths(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        result_swig = Graph.GetLen2Paths(0, 1, False)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result_swig, result)

        result_swig, NV_swig = Graph.GetLen2Paths(0, 1, True)
        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(result_swig, result)
        self.assertEqual(NV_swig.Len(), NV_swig.Len())

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        result_swig = Graph.GetLen2Paths(0, 1, False)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result_swig, result)

        result_swig, NV_swig = Graph.GetLen2Paths(0, 1, True)
        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(result_swig, result)
        self.assertEqual(NV_swig.Len(), NV_swig.Len())

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        result_swig = Graph.GetLen2Paths(0, 1, False)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result_swig, result)

        result_swig, NV_swig = Graph.GetLen2Paths(0, 1, True)
        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(result_swig, result)
        self.assertEqual(NV_swig.Len(), NV_swig.Len())

    def test_SavePajek(self):
        fname = "mygraph.txt"
        # Directed Graph
        self.DirGraphFull.SavePajek(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.DirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Undirected Graph
        self.UnDirGraphFull.SavePajek(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.UnDirGraphFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

        # Directed Graph
        self.NetFull.SavePajek(fname)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.NetFull, fname)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash, test_hash_swig)

    def test_SavePajek2(self):
        fname = "mygraph.txt"
        NIdColorH_swig = snap.TIntStrH()
        NIdColorH = {}
        for i in range(self.num_nodes):
            NIdColorH_swig[i] = "red"
            NIdColorH[i] = "red"
        # Directed Graph
        self.DirGraphFull.SavePajek(fname, NIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Undirected Graph
        self.UnDirGraphFull.SavePajek(fname, NIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Directed Graph
        self.NetFull.SavePajek(fname, NIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.NetFull, fname, NIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

    def test_SavePajek3(self):
        fname = "mygraph.txt"
        NIdColorH_swig = snap.TIntStrH()
        NIdColorH = {}
        for i in range(self.num_nodes):
            NIdColorH_swig[i] = "red"
            NIdColorH[i] = "red"
        NIdLabelH_swig = snap.TIntStrH()
        NIdLabelH = {}
        for i in range(100):
            NIdLabelH_swig[i] = str(i)
            NIdLabelH[i] = str(i)
        # Directed Graph
        self.DirGraphFull.SavePajek(fname, NIdColorH, NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH_swig, NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)
        
        # Undirected Graph
        self.UnDirGraphFull.SavePajek(fname, NIdColorH, NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH_swig, NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Directed Graph
        self.NetFull.SavePajek(fname, NIdColorH, NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.NetFull, fname, NIdColorH_swig, NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

    def test_SavePajek4(self):
        fname = "mygraph.txt"
        NIdColorH_swig = snap.TIntStrH()
        NIdColorH = {}
        for i in range(self.num_nodes):
            NIdColorH_swig[i] = "red"
            NIdColorH[i] = "red"
        NIdLabelH_swig = snap.TIntStrH()
        NIdLabelH = {}
        for i in range(100):
            NIdLabelH_swig[i] = str(i)
            NIdLabelH[i] = str(i)
        EIdColorH_swig = snap.TIntStrH()
        EIdColorH = {}
        for i in range(1000):
            EIdColorH_swig[i] = "black"
            EIdColorH[i] = "black"
        # Directed Graph
        self.DirGraphFull.SavePajek(fname, NIdColorH, NIdLabelH, EIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH_swig, NIdLabelH_swig, EIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)
        
        # Undirected Graph
        self.UnDirGraphFull.SavePajek(fname, NIdColorH, NIdLabelH, EIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH_swig, NIdLabelH_swig, EIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Directed Graph
        self.NetFull.SavePajek(fname, NIdColorH, NIdLabelH, EIdColorH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SavePajek(self.NetFull, fname, NIdColorH_swig, NIdLabelH_swig, EIdColorH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

    def test_SaveGViz(self):
        fname = "mygraph.dot"
        NIdColorH = snap.TIntStrH()
        NIdColor_dict = {}
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
            NIdColor_dict[i] = "red"
        # Directed Graph
        snap.SaveGViz(self.DirGraphFull, fname, "text", True, NIdColorH)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.DirGraphFull.SaveGVizColor(fname, "text", True, NIdColor_dict)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Undirected Graph
        snap.SaveGViz(self.UnDirGraphFull, fname, "text", True, NIdColorH)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.UnDirGraphFull.SaveGVizColor(fname, "text", True, NIdColor_dict)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Directed Graph
        snap.SaveGViz(self.NetFull, fname, "text", True, NIdColorH)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.NetFull.SaveGVizColor(fname, "text", True, NIdColor_dict)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

    def test_SaveGViz2(self):
        fname = "mygraph.dot"
        NIdLabelH_swig = snap.TIntStrH()
        NIdLabelH = {}
        for i in range(self.num_nodes):
            NIdLabelH_swig[i] = str(i)
            NIdLabelH[i] = str(i)
        # Directed Graph
        self.DirGraphFull.SaveGViz(fname, "text", NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveGViz(self.DirGraphFull, fname, "text", NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Undirected Graph
        self.UnDirGraphFull.SaveGViz(fname, "text", NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveGViz(self.UnDirGraphFull, fname, "text", NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

        # Directed Graph
        self.NetFull.SaveGViz(fname, "text", NIdLabelH)
        test_hash = self.getFileHash(fname)
        os.remove(fname)
        snap.SaveGViz(self.NetFull, fname, "text", NIdLabelH_swig)
        test_hash_swig = self.getFileHash(fname)
        os.remove(fname)
        self.assertEqual(test_hash_swig, test_hash)

    def test_LoadEdgeList(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TNGraph, fname, 0, 1)
        Graph_swig = snap.LoadEdgeList(snap.PNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TUNGraph, fname, 0, 1)
        Graph_swig = snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TNEANet, fname, 0, 1)
        Graph_swig = snap.LoadEdgeList(snap.PNEANet, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

    def test_LoadEdgeList2(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TNGraph, fname, 0, 1, '\t')
        Graph_swig = snap.LoadEdgeList(snap.PNGraph, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TUNGraph, fname, 0, 1, '\t')
        Graph_swig = snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.TNEANet, fname, 0, 1, '\t')
        Graph_swig = snap.LoadEdgeList(snap.PNEANet, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

    def test_LoadEdgeListStr(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.TNGraph, fname, 0, 1, True)
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadEdgeListStr(snap.PNGraph, fname, 0, 1, mapping_swig)
        self.assertEqual(mapping.Len(), mapping_swig.Len())
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.TUNGraph, fname, 0, 1, True)
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadEdgeListStr(snap.PUNGraph, fname, 0, 1, mapping_swig)
        self.assertEqual(mapping.Len(), mapping_swig.Len())
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.TNEANet, fname, 0, 1, True)
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadEdgeListStr(snap.PNEANet, fname, 0, 1, mapping_swig)
        self.assertEqual(mapping.Len(), mapping_swig.Len())
        for node,node_swig in zip(Graph.Nodes(), Graph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(Graph.Edges(), Graph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())
        os.remove(fname)


    def test_LoadConnList(self):
        fname = "mygraph.txt"
        output = open(fname, "w")
        output.write('0 1 2\n')
        output.write('1 2 0\n')
        output.write('2 0 1\n')
        output.close()

        # Directed Graph
        Graph_swig = snap.LoadConnList(snap.PNGraph, fname)
        Graph = snap.LoadConnList(snap.TNGraph, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())

        # Undirected Graph
        Graph_swig = snap.LoadConnList(snap.PUNGraph, fname)
        Graph = snap.LoadConnList(snap.TUNGraph, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())

        # Network
        Graph_swig = snap.LoadConnList(snap.PNEANet, fname)
        Graph = snap.LoadConnList(snap.TNEANet, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        os.remove(fname)

    def test_LoadConnListStr(self):
        fname = "mygraph.txt"
        output = open(fname, "w")
        output.write('0 1 2\n')
        output.write('1 2 0\n')
        output.write('2 0 1\n')
        output.close()

        # Directed Graph
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadConnListStr(snap.PNGraph, fname, mapping_swig)
        Graph, mapping = snap.LoadConnListStr(snap.TNGraph, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        self.assertEqual(mapping.Len(), mapping_swig.Len())

        # Undirected Graph
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadConnListStr(snap.PUNGraph, fname, mapping_swig)
        Graph, mapping = snap.LoadConnListStr(snap.TUNGraph, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        self.assertEqual(mapping.Len(), mapping_swig.Len())

        # Network
        mapping_swig = snap.TStrIntSH()
        Graph_swig = snap.LoadConnListStr(snap.PNEANet, fname, mapping_swig)
        Graph, mapping = snap.LoadConnListStr(snap.TNEANet, fname)
        self.assertEqual(Graph.GetNodes(), Graph_swig.GetNodes())
        self.assertEqual(Graph.GetEdges(), Graph_swig.GetEdges())
        self.assertEqual(mapping.Len(), mapping_swig.Len())
        os.remove(fname)

    def test_LoadPajek(self):
        fname = "example.paj"
        output = open(fname, "w")
        output.write('*Vertices      9\n')
        output.write('1 "1"    0.3034    0.7561\n')
        output.write('2 "2"    0.4565    0.6039\n')
        output.write('3 "3"    0.4887    0.8188\n')
        output.write('*Arcs\n')
        output.write('*Edges\n')
        output.write('    1      2       1\n')
        output.write('    1      3       1\n')
        output.write('    2      3       1\n')
        output.close()

        # Directed Graph
        Graph = snap.LoadPajek(snap.TNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        # Undirected Graph
        Graph = snap.LoadPajek(snap.TUNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        # Network
        Graph = snap.LoadPajek(snap.TNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        os.remove(fname)

    def test_GetSngVec(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        LeftSV, RightSV = Graph.GetLeadSngVec()
        LeftSV_swig = snap.TFltV()
        RightSV_swig = snap.TFltV()
        snap.GetSngVec(Graph, LeftSV_swig, RightSV_swig)
        for i,i_swig in zip(LeftSV, LeftSV_swig):
            self.assertAlmostEqual(i, i_swig)
        for i,i_swig in zip(RightSV, RightSV_swig):
            self.assertAlmostEqual(i, i_swig)

        SngValV, LeftSVV, RightSVV = Graph.GetSngVecs(5)
        SngValV_swig = snap.TFltV()
        LeftSVV_swig = snap.TFltVFltV()
        RightSVV_swig = snap.TFltVFltV()
        snap.GetSngVec(Graph, 5, SngValV_swig, LeftSVV_swig, RightSVV_swig)
        for i,i_swig in zip(SngValV, SngValV_swig):
            self.assertAlmostEqual(i, i_swig)
        for i,i_swig in zip(LeftSVV, LeftSVV_swig):
            self.assertAlmostEqual(i, i_swig)
        for i,i_swig in zip(RightSVV, RightSVV_swig):
            self.assertAlmostEqual(i, i_swig)

    def test_GetLeadEigVec(self):
        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
        EigV = Graph.GetLeadEigVec()
        self.assertEqual(EigV.Len(), 100)

    def test_GetEigVecs(self):
        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
        EigVal, EigVV = Graph.GetEigVecs(10)
        self.assertEqual(EigVal.Len(), 10)
        for V in EigVV:
            self.assertEqual(V.Len(), 100)

    def test_DrawGViz(self):
        # Directed Graph
        fname = "mygraph.png"
        snap.DrawGViz(self.DirGraphFull, snap.gvlDot, fname, "graph 1")
        self.assertTrue(os.path.isfile(fname))
        self.assertTrue(os.stat(fname).st_size > 50000)
        exp_hash = '7ac8bcf157f7d916be78a09faaf13f23'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        fname = "mygraph.png"
        snap.DrawGViz(self.UnDirGraphFull, snap.gvlDot, fname, "graph 1")
        self.assertTrue(os.path.isfile(fname))
        self.assertTrue(os.stat(fname).st_size > 50000)
        exp_hash = '734899b11f197b88d14d771b18011d85'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Network
        fname = "mygraph.png"
        snap.DrawGViz(self.NetFull, snap.gvlDot, fname, "graph 1")
        self.assertTrue(os.path.isfile(fname))
        self.assertTrue(os.stat(fname).st_size > 50000)
        exp_hash = '7ac8bcf157f7d916be78a09faaf13f23'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_DrawGViz2(self):

        # Directed Graph
        fname = "mygraph.png"
        labels = snap.TIntStrH()
        for NI in self.DirGraphFull.Nodes():
            labels[NI.GetId()] = str(NI.GetId())
        snap.DrawGViz(self.DirGraphFull, snap.gvlDot, fname, "graph 1", labels)
        self.assertTrue(os.stat(fname).st_size > 50000)
        self.assertTrue(os.path.isfile(fname))
        exp_hash = 'd0fa3688dd5d9c5599222270be49805e'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        fname = "mygraph.png"
        labels = snap.TIntStrH()
        for NI in self.UnDirGraphFull.Nodes():
            labels[NI.GetId()] = str(NI.GetId())
        snap.DrawGViz(self.UnDirGraphFull, snap.gvlDot, fname, "graph 1", labels)
        self.assertTrue(os.path.isfile(fname))
        self.assertTrue(os.stat(fname).st_size > 50000)
        exp_hash = '191c86413fd43f23bf1c5ce4a9972863'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Network
        fname = "mygraph.png"
        labels = snap.TIntStrH()
        for NI in self.NetFull.Nodes():
            labels[NI.GetId()] = str(NI.GetId())
        snap.DrawGViz(self.NetFull, snap.gvlDot, fname, "graph 1", labels)
        self.assertTrue(os.path.isfile(fname))
        self.assertTrue(os.stat(fname).st_size > 50000)
        exp_hash = 'd0fa3688dd5d9c5599222270be49805e'
        f = open(fname, 'rb')
        test_hash = hashlib.md5(f.read()).hexdigest()
        f.close()
        # OP RS 2014/05/13, disabled since it is not portable
        #self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_GetSubGraph(self):
        V = []
        for i in range(5):
            V.append(i)
        V_swig = snap.TIntV()
        for i in range(5):
            V_swig.Add(i)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SubGraph = Graph.GetSubGraph(V)
        SubGraph_swig = snap.GetSubGraph(Graph, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        SubGraph = Graph.GetSubGraphRenumber(V)
        SubGraph_swig = snap.GetSubGraphRenumber(Graph, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SubGraph = Graph.GetSubGraph(V)
        SubGraph_swig = snap.GetSubGraph(Graph, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        SubGraph = Graph.GetSubGraphRenumber(V)
        SubGraph_swig = snap.GetSubGraphRenumber(Graph, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SubGraph = Graph.GetSubGraph(V)
        SubGraph_swig = snap.GetSubGraph(Graph, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

    def test_GetNodeClustCf(self):
        # Directed Graph
        H = self.DirGraphFull.GetNodeClustCfAll()
        H_swig = snap.TIntFltH()
        snap.GetNodeClustCf(self.DirGraphFull, H_swig)
        self.assertEqual(H, H_swig)

        # Undirected Graph
        H = self.UnDirGraphFull.GetNodeClustCfAll()
        H_swig = snap.TIntFltH()
        snap.GetNodeClustCf(self.UnDirGraphFull, H_swig)
        self.assertEqual(H, H_swig)

        # Network
        H = self.NetFull.GetNodeClustCfAll()
        H_swig = snap.TIntFltH()
        snap.GetNodeClustCf(self.NetFull, H_swig)
        self.assertEqual(H, H_swig)

    def test_ConvertESubGraph(self):
        V = []
        for i in range(10):
            V.append(i+1)
        V_swig = snap.TIntV()
        for i in range(10):
            V_swig.Add(i+1)

        # Directed Graph
        SubGraph = self.NetFull.ConvertESubGraph(snap.PNGraph, V)
        SubGraph_swig = snap.ConvertESubGraph(snap.PNGraph, self.NetFull, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Undirected Graph
        SubGraph = self.NetFull.ConvertESubGraph(snap.PUNGraph, V)
        SubGraph_swig = snap.ConvertESubGraph(snap.PUNGraph, self.NetFull, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())

        # Network
        SubGraph = self.NetFull.ConvertESubGraph(snap.PNEANet, V)
        SubGraph_swig = snap.ConvertESubGraph(snap.PNEANet, self.NetFull, V_swig)
        for node,node_swig in zip(SubGraph.Nodes(), SubGraph_swig.Nodes()):
            self.assertEqual(node.GetId(), node_swig.GetId())
        for edge,edge_swig in zip(SubGraph.Edges(), SubGraph_swig.Edges()):
            self.assertEqual(edge.GetSrcNId(), edge_swig.GetSrcNId())
            self.assertEqual(edge.GetDstNId(), edge_swig.GetDstNId())


if __name__ == '__main__':
  unittest.main()

