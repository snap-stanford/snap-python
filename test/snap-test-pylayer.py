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
        
    def test_CntInDegNodes(self):
        # Directed graph
        num_nodes = self.DirGraphFull.CntInDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntInDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

        # Network
        num_nodes = self.NetFull.CntInDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

    def test_CntOutDegNodes(self):
        # Directed Graph
        num_nodes = self.DirGraphFull.CntOutDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntOutDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

        # Network
        num_nodes = self.NetFull.CntOutDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

    def test_CntDegNodes(self):
        # Directed Graph - it will have twice the edges as the undirected graph
        num_nodes = self.DirGraphFull.CntDegNodes(2*(self.num_nodes-1))
        self.assertEqual(num_nodes, self.num_nodes)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntDegNodes(self.num_nodes-1)
        self.assertEqual(num_nodes, self.num_nodes)

        # Network
        num_nodes = self.NetFull.CntDegNodes(2*(self.num_nodes-1))
        self.assertEqual(num_nodes, self.num_nodes)

    def test_CntNonZNodes(self):
        # Directed Graph
        num_nodes = self.DirGraphFull.CntNonZNodes()
        self.assertEqual(num_nodes, self.num_nodes)

        # Undirected Graph
        num_nodes = self.UnDirGraphFull.CntNonZNodes()
        self.assertEqual(num_nodes, self.num_nodes)

        # Network
        num_nodes = self.NetFull.CntNonZNodes()
        self.assertEqual(num_nodes, self.num_nodes)

    def test_GetMxDegNId(self):
        # Directed Graph
        max_id = self.DirGraphStar.GetMxDegNId()
        self.assertEqual(max_id, 0)

        # Undirected Graph
        max_id = self.UnDirGraphStar.GetMxDegNId()
        self.assertEqual(max_id, 0)

        # Network
        max_id = self.NetStar.GetMxDegNId()
        self.assertEqual(max_id, 0)

    def test_GetMxInDegNId(self):
        # Directed Graph
        # node with id 0 is the only node with in-degree 0
        max_id = self.DirGraphStar.GetMxInDegNId()
        self.assertNotEqual(max_id, 0)

        # Undirected Graph
        max_id = self.UnDirGraphStar.GetMxInDegNId()
        self.assertEqual(max_id, 0)

        # Network
        # node with id 0 is the only node with in-degree 0
        max_id = self.NetStar.GetMxInDegNId()
        self.assertNotEqual(max_id, 0)

    def test_GetMxOutDegNId(self):
        # Directed Graph
        max_id = self.DirGraphStar.GetMxOutDegNId()
        self.assertEqual(max_id, 0)

        # Undirected Graph
        max_id = self.UnDirGraphStar.GetMxOutDegNId()
        self.assertEqual(max_id, 0)

        # Network
        max_id = self.NetStar.GetMxOutDegNId()
        self.assertEqual(max_id, 0)

    def test_GetInDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetInDegCnt()
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())
        self.assertEqual(DegToCntV, DegToCntV)

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetInDegCnt()
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = self.NetFull.GetInDegCnt()
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetOutDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetOutDegCnt()
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetOutDegCnt()
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = self.NetFull.GetOutDegCnt()
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetDegCnt(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetDegCnt()
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(2*(self.num_nodes-1), item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetDegCnt()
        # There should be only one entry (num_nodes-1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = self.NetFull.GetDegCnt()
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetNodeInDegV(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetNodeInDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetNodeInDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Network
        DegToCntV = self.NetFull.GetNodeInDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

    def test_GetNodeOutDegV(self):
        # Directed Graph
        DegToCntV = self.DirGraphFull.GetNodeOutDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Undirected Graph
        DegToCntV = self.UnDirGraphFull.GetNodeOutDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Network
        DegToCntV = self.NetFull.GetNodeOutDegV()
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

    def test_GetDegSeqV(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        V = G.GetDegSeqV(Dir = False)
        for i in V:
            self.assertEqual(18, i)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        V = G.GetDegSeqV(Dir = False)
        snap.GetDegSeqV(G, V)
        for i in V:
            self.assertEqual(9, i)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        V = G.GetDegSeqV(Dir = False)
        for i in V:
            self.assertEqual(18, i)

    def test_GetDegSeqV2(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        V, V2 = G.GetDegSeqV(Dir = True)
        snap.GetDegSeqV(G, V, V2)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        V, V2 = G.GetDegSeqV(Dir = True)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        V_new, V2_new = G.GetDegSeqV(Dir = True)
        snap.GetDegSeqV(G, V, V2)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

    def test_CntUniqUndirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqUndirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqUndirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Network
        num_edges = self.NetFull.CntUniqUndirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

    def test_CntUniqDirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

        # Network
        num_edges = self.NetFull.CntUniqDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

    def test_CntUniqBiDirEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntUniqBiDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Unidrected Graph
        num_edges = self.UnDirGraphFull.CntUniqBiDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Network
        num_edges = self.NetFull.CntUniqBiDirEdges()
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

    def test_CntSelfEdges(self):
        # Directed Graph
        num_edges = self.DirGraphFull.CntSelfEdges()
        self.assertEqual(0, num_edges)

        # Undirected Graph
        num_edges = self.UnDirGraphFull.CntSelfEdges()
        self.assertEqual(0, num_edges)

        # Network
        num_edges = self.NetFull.CntSelfEdges()
        self.assertEqual(0, num_edges)

    def test_GetUnDir(self):
        # Directed Graph
        New_Graph = self.DirGraphStar.GetUnDir()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Undirected Graph
        New_Graph = self.UnDirGraphStar.GetUnDir()
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Network
        New_Graph = self.NetStar.GetUnDir()
        for node in self.NetStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

    def test_MakeUnDir(self):
        # Directed Graph
        New_Graph = snap.GenStar(snap.PNGraph, self.num_nodes)
        New_Graph.MakeUnDir()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Undirected Graph
        New_Graph = snap.GenStar(snap.PUNGraph, self.num_nodes)
        New_Graph.MakeUnDir()
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Network
        New_Graph = snap.GenStar(snap.PNEANet, self.num_nodes)
        New_Graph.MakeUnDir()
        for node in self.NetStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

    def test_AddSelfEdges(self):
        # Directed Graph
        New_Graph = snap.GenFull(snap.PNGraph, self.num_nodes)
        New_Graph.AddSelfEdges()
        for node in New_Graph.Nodes():
            self.assertTrue(New_Graph.IsEdge(node.GetId(), node.GetId()))

        # Undirected Graph
        New_Graph = snap.GenFull(snap.PUNGraph, self.num_nodes)
        New_Graph.AddSelfEdges()
        for node in New_Graph.Nodes():
            self.assertTrue(New_Graph.IsEdge(node.GetId(), node.GetId()))

        # Network
        New_Graph = snap.GenFull(snap.PNEANet, self.num_nodes)
        New_Graph.AddSelfEdges()
        for node in New_Graph.Nodes():
            self.assertTrue(New_Graph.IsEdge(node.GetId(), node.GetId()))

    def test_DelSelfEdges(self):
        # Directed Graph
        New_Graph = snap.GenRndGnm(snap.PNGraph, 10, 20)
        New_Graph.AddEdge(0, 0)
        New_Graph.DelSelfEdges()
        for node in New_Graph.Nodes():
            self.assertFalse(New_Graph.IsEdge(node.GetId(), node.GetId()))

        # Undirected Graph
        New_Graph = snap.GenRndGnm(snap.PUNGraph, 10, 20)
        New_Graph.AddEdge(0, 0)
        New_Graph.DelSelfEdges()
        for node in New_Graph.Nodes():
            self.assertFalse(New_Graph.IsEdge(node.GetId(), node.GetId()))

        # Network
        New_Graph = snap.GenRndGnm(snap.PNEANet, 10, 20)
        New_Graph.AddEdge(0, 0)
        New_Graph.DelSelfEdges()
        for node in New_Graph.Nodes():
            self.assertFalse(New_Graph.IsEdge(node.GetId(), node.GetId()))

    def test_DelNodes(self):
        # Directed Graph
        New_Graph = snap.GenFull(snap.PNGraph, self.num_nodes)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        for node in DelNodes:
            self.assertFalse(New_Graph.IsNode(node))

        # Undirected Graph
        New_Graph = snap.GenFull(snap.PUNGraph, self.num_nodes)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        for node in DelNodes:
            self.assertFalse(New_Graph.IsNode(node))

        # Network
        New_Graph = snap.GenFull(snap.PNEANet, self.num_nodes)
        DelNodes = [0]
        New_Graph.DelNodes(DelNodes)
        for node in DelNodes:
            self.assertFalse(New_Graph.IsNode(node))

    def test_DelZeroDegNodes(self):
        # Directed Graph
        New_Graph = snap.GenRndGnm(snap.PNGraph, 10, 1)
        New_Graph.DelZeroDegNodes()
        for NI in New_Graph.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())        

        # Undirected Graph
        New_Graph = snap.GenRndGnm(snap.PUNGraph, 10, 1)
        New_Graph.DelZeroDegNodes()
        for NI in New_Graph.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())    

        # Network
        New_Graph = snap.GenRndGnm(snap.PNEANet, 10, 1)
        New_Graph.DelZeroDegNodes()
        for NI in New_Graph.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())    

    def test_DelDegKNodes(self):
        # Directed Graph
        DirGraphZeroDegree = snap.GenRndGnm(snap.PNGraph, 10, 1)
        DirGraphZeroDegree.DelDegKNodes(0,0)
        for NI in DirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Undirected Graph
        UnDirGraphZeroDegree = snap.GenRndGnm(snap.PNGraph, 10, 1)
        UnDirGraphZeroDegree.DelDegKNodes(0,0)
        for NI in UnDirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Network
        NetZeroDegree = snap.GenRndGnm(snap.PNGraph, 10, 1)
        NetZeroDegree.DelDegKNodes(0,0)
        for NI in NetZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

    def test_IsTree(self):
        # Directed Graph
        expected_results = [True, 0]
        results = self.DirTree.IsTree()
        self.assertEqual(expected_results, results)

        # Network
        expected_results = [True, 0]
        results = self.NetTree.IsTree()
        self.assertEqual(expected_results, results)

    def test_GetTreeRootNId(self):
        # Directed Graph
        root_id = snap.GetTreeRootNId(self.DirTree)
        self.assertEqual(0, root_id)

        # Network
        root_id = self.NetTree.GetTreeRootNId()
        self.assertEqual(0, root_id)

    def test_GetBfsTree(self):
        start_node = 0
        follow_out = True
        follow_in = False

        # Directed Graph
        BfsTree = self.DirGraphFull.GetBfsTree(start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

        # Undirected Graph
        BfsTree = self.DirGraphFull.GetBfsTree(start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

        # Network
        BfsTree = self.NetFull.GetBfsTree(start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

    def test_GetSubTreeSz(self):
        # Directed Graph
        exp_results = [40, 40, 3]
        results = self.DirTree.GetSubTreeSz(0, True, True)
        self.assertEqual(exp_results, results)

        # Undirected Graph
        exp_results = [40, 40, 3]
        results = self.UnDirTree.GetSubTreeSz(0, True, True)
        self.assertEqual(exp_results, results)

        # Network
        exp_results = [40, 40, 3]
        results = self.NetTree.GetSubTreeSz(0, True, True)
        self.assertEqual(exp_results, results)

    def test_GetNodesAtHop(self):
        # Directed Graph
        num_nodes, NodeVec = self.DirGraphStar.GetNodesAtHop(0, 1, True)
        self.assertEqual(self.num_nodes-1, num_nodes)

        # Undirected Graph
        num_nodes, NodeVec = self.UnDirGraphStar.GetNodesAtHop(0, 1, True)
        self.assertEqual(self.num_nodes-1, num_nodes)

        # Network
        num_nodes, NodeVec = self.NetStar.GetNodesAtHop(0, 1, True)
        self.assertEqual(self.num_nodes-1, num_nodes)

    def test_GetNodesAtHops(self):
        # Directed Graph
        num_hops, HopVec = self.DirGraphStar.GetNodesAtHops(0, True)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())

        # Undirected Graph
        num_hops, HopVec = self.UnDirGraphStar.GetNodesAtHops(0, False)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())        

        # Network
        num_hops, HopVec = self.NetStar.GetNodesAtHops(0, False)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())

    def test_GetDegreeCentr(self):
        # Undirected Graph
        degree_center = self.UnDirGraphStar.GetDegreeCentr(0)
        self.assertEqual(1, degree_center)

    def test_GetFarnessCentr(self):
        # Undirected Graph
        farness_center = self.UnDirGraphStar.GetFarnessCentr(0)
        self.assertEqual(1, farness_center)

        # Directed Graph
        farness_center = self.DirGraphStar.GetFarnessCentr(0)
        self.assertEqual(1, farness_center)

        # Network
        farness_center = self.NetStar.GetFarnessCentr(0)
        self.assertEqual(1, farness_center)

    def test_GetClosenessCentr(self):
        # Undirected Graph
        closeness_center = self.UnDirGraphStar.GetClosenessCentr(0)
        self.assertEqual(1, closeness_center)

        # Directed Graph
        closeness_center = self.DirGraphStar.GetClosenessCentr(0)
        self.assertEqual(1, closeness_center)

        # Network
        closeness_center = self.NetStar.GetClosenessCentr(0)
        self.assertEqual(1, closeness_center)

    def test_GetEigenVectorCentr(self):
        # Undirected Graph
        EigenVec = self.UnDirGraphStar.GetEigenVectorCentr()
        for item in EigenVec:
            self.assertTrue(0 < EigenVec[item])

    def test_GetNodeEcc(self):
        # Directed Graph
        node_ecc = self.DirGraphStar.GetNodeEcc(0, True)
        self.assertEqual(1, node_ecc)

        # Undirected Graph
        node_ecc = self.UnDirGraphStar.GetNodeEcc(0, True)
        self.assertEqual(1, node_ecc)

        # Network
        node_ecc = self.NetStar.GetNodeEcc(0, True)
        self.assertEqual(1, node_ecc)

    def test_GetHits(self):
        # Directed Graph
        NIdHubH, NIdAuthH = self.DirGraphFull.GetHits()
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

        # Undirected Graph
        NIdHubH, NIdAuthH = self.UnDirGraphFull.GetHits()
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

        # Network
        NIdHubH, NIdAuthH = self.NetFull.GetHits()
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

    def test_CommunityGirvanNewman(self):
        exp_val = 0.010151451527112903
        Graph = snap.GenPrefAttach(100, 10)
        act_val, Vec = Graph.CommunityGirvanNewman()
        self.assertAlmostEqual(exp_val, act_val)        

    def test_CommunityCNM(self):
        gnutellaUndir = snap.ConvertGraph(snap.PUNGraph, self.gnutella)
        modularity, Vcc = gnutellaUndir.CommunityCNM()
        self.assertAlmostEqual(0.4647213330572384, modularity)

    def test_GetModularity(self):
        V = [0,1,2,3,4]

        # Directed Graph
        val = self.DirGraphFull.GetModularity(V)
        self.assertAlmostEqual(0.04861111111111111, val)

        # Undirected Graph
        val = self.UnDirGraphFull.GetModularity(V)
        self.assertAlmostEqual(-0.027777777777777776, val)

        # Network
        val = self.NetFull.GetModularity(V)
        self.assertAlmostEqual(0.04861111111111111, val)

    def test_GetEdgesInOut(self):
        # Directed Graph
        result = self.DirGraphFull.GetEdgesInOut([0])
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

        # Undirected Graph
        result = self.UnDirGraphFull.GetEdgesInOut([0])
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

        # Network
        result = self.NetFull.GetEdgesInOut([0])
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

    def test_GetBiConSzCnt(self):
        # Undirected Graph
        szCntV = self.UnDirGraphFull.GetBiConSzCnt()
        for item in szCntV:
            self.assertEqual(item.GetVal1(), self.num_nodes)
            self.assertEqual(item.GetVal2(), 1)

    def test_GetBiCon(self):
        # Undirected Graph
        CnComs = self.UnDirGraphFull.GetBiCon()
        nodeId = 0
        for CnCom in CnComs:
            for node in CnCom:
              self.assertEqual(nodeId, node)
              nodeId += 1 

    def test_GetEdgeBridges(self):
        # Undirected Graph
        edges = self.UnDirGraphStar.GetEdgeBridges()
        count = 0
        for edge in edges:
            self.assertEqual(0, edge.GetVal1())
            self.assertNotEqual(0, edge.GetVal2())
            count+=1
        self.assertEqual(9, count)

    def test_Get1CnCom(self):
        # Undirected Graph
        components = self.UnDirGraphStar.Get1CnCom()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes-1, comp_size)

    def test_GetMxBiCon(self):
        # Directed Graph
        Graph = self.DirGraphFull.GetMxBiCon()
        self.assertEqual(self.DirGraphFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.DirGraphFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(self.DirGraphFull), type(Graph))

        # Undirected Graph
        Graph = self.UnDirGraphFull.GetMxBiCon()
        self.assertEqual(self.UnDirGraphFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.UnDirGraphFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(self.UnDirGraphFull), type(Graph))

        # Network
        Graph = self.NetFull.GetMxBiCon()
        self.assertEqual(self.NetFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.NetFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(Graph), type(self.NetFull))

    def test_GetNodeWcc(self):
        # Directed Graph
        component = self.DirGraphStar.GetNodeWcc(1)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

        # Undirected Graph
        component = self.UnDirGraphStar.GetNodeWcc(1)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

        # Network
        component = self.NetStar.GetNodeWcc(1)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

    def test_isConnected(self):
        # Directed Graph
        self.assertTrue(self.DirGraphStar.IsConnected())

        # Undirected Graph
        self.assertTrue(self.UnDirGraphStar.IsConnected())

        # Network
        self.assertTrue(self.NetStar.IsConnected())

    def test_isWeaklyConn(self):
        # Directed Graph
        self.assertTrue(self.DirGraphStar.IsWeaklyConn())

        # Undirected Graph
        self.assertTrue(self.UnDirGraphStar.IsWeaklyConn())

        # Network
        self.assertTrue(self.NetStar.IsWeaklyConn())

    def test_GetWccSzCnt(self):
        # Directed Graph
        counts = self.DirGraphStar.GetWccSzCnt()
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Undirected Graph
        counts = self.UnDirGraphStar.GetWccSzCnt()
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Network
        counts = self.NetStar.GetWccSzCnt()
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

    def test_GetWccs(self):
        # Directed Graph
        components = self.DirGraphStar.GetWccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Undirected Graph
        components = self.UnDirGraphStar.GetWccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Network
        components = self.UnDirGraphStar.GetWccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

    def test_GetSccSzCnt(self):
         # Directed Graph
        counts = self.DirGraphFull.GetSccSzCnt()
        snap.GetSccSzCnt(self.DirGraphFull, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Undirected Graph
        counts = self.UnDirGraphFull.GetSccSzCnt()
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())
        # Network
        counts = self.NetFull.GetSccSzCnt()
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

    def test_GetSccs(self):
        # Directed Graph
        components = self.DirGraphFull.GetSccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Undirected Graph
        components = self.UnDirGraphFull.GetSccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Network
        components = self.NetFull.GetSccs()
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

    def test_GetMxWccSz(self):
        # Directed Graph
        sz = self.DirGraphStar.GetMxWccSz()
        self.assertEqual(1, sz)

        # Undirected Graph
        sz = self.UnDirGraphStar.GetMxWccSz()
        self.assertEqual(1, sz)

        # Network
        sz = self.NetStar.GetMxWccSz()
        self.assertEqual(1, sz)

    def test_GetMxSccSz(self):
        # Directed Graph
        sz = self.DirGraphStar.GetMxSccSz()
        self.assertEqual(1.0/self.num_nodes, sz)

        # Undirected Graph
        sz = self.UnDirGraphStar.GetMxSccSz()
        self.assertEqual(1, sz) 

        # Network
        sz = self.NetStar.GetMxSccSz()
        self.assertEqual(1.0/self.num_nodes, sz)

    def test_GetMxWcc(self):
        # Directed Graph
        subgraph = self.DirGraphStar.GetMxWcc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = self.UnDirGraphStar.GetMxWcc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = self.NetStar.GetMxWcc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetMxScc(self):
        # Directed Graph
        subgraph = self.DirGraphFull.GetMxScc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = self.UnDirGraphFull.GetMxScc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = self.NetFull.GetMxScc()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetMxBiCon(self):
        # Directed Graph
        subgraph = self.DirGraphFull.GetMxBiCon()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = self.UnDirGraphFull.GetMxBiCon()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = self.NetFull.GetMxBiCon()
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

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
        self.assertEqual(2, result)

        # Undirected Graph
        result, CoreN = self.UnDirGraphStar.GetKCoreNodes()
        self.assertEqual(2, result)

        # Network
        result, CoreN = self.NetStar.GetKCoreNodes()
        self.assertEqual(2, result)

    def test_GetKCoreEdges(self):
        # Directed Graph
        result, CoreN = self.DirGraphStar.GetKCoreEdges()
        self.assertEqual(2, result)

        # Undirected Graph
        result, CoreN = self.UnDirGraphStar.GetKCoreEdges()
        self.assertEqual(2, result)

        # Network
        result, CoreN = self.NetStar.GetKCoreEdges()
        self.assertEqual(2, result)

    def test_GenDegSeq(self):
        DegSeqV = snap.TIntV()
        DegSeqV.Add(3)
        DegSeqV.Add(2)
        DegSeqV.Add(1)
        DegSeqV.Add(1)
        DegSeqV.Add(1)
        Graph = snap.GenDegSeq(DegSeqV)
        count = 0
        for n in Graph.Nodes():
            count += 1
        self.assertEqual(5, count)
        count = [0, 0, 0, 0, 0]
        for node in Graph.Nodes():
            count[node.GetId()] = node.GetInDeg()
        self.assertEqual(3, count[0])
        self.assertEqual(2, count[1])
        self.assertEqual(1, count[2])
        self.assertEqual(1, count[3])
        self.assertEqual(1, count[4])

    def test_GenRewire(self):
        Rewired = snap.GenRewire(self.UnDirRand)
        for node in self.UnDirRand.Nodes():
            for nodeR in Rewired.Nodes():
                if node.GetId() == nodeR.GetId():
                    self.assertEqual(node.GetOutDeg()+node.GetInDeg(), nodeR.GetOutDeg()+nodeR.GetInDeg())

    def test_GenPrefAttach(self):
        Graph = snap.GenPrefAttach(100, 10)
        for node in Graph.Nodes():
            self.assertTrue(node.GetOutDeg() >= 10)
        self.assertEqual(100, Graph.GetNodes())

    def test_GenGeoPrefAttach(self):
        Graph = snap.GenGeoPrefAttach(100, 10, 0.25)
        for node in Graph.Nodes():
            self.assertTrue(node.GetOutDeg() + node.GetInDeg() >= 10)
        self.assertEqual(100, Graph.GetNodes())

    def test_GenForestFire(self):
        Graph = snap.GenForestFire(100, 0.5, 0.5)
        self.assertEqual(100, Graph.GetNodes())

    def test_GenRMat(self):
        Graph = snap.GenRMat(10, 20, 0.25, 0.25, 0.25)
        self.assertEqual(10, Graph.GetNodes())
        self.assertEqual(20, Graph.GetEdges())

    def test_GenRMatEpinions(self):
        Graph = snap.GenRMatEpinions()
        expected_nodes = 75888
        expected_edges = 508837
        self.assertEqual(expected_nodes, Graph.GetNodes())
        self.assertEqual(expected_edges, Graph.GetEdges())

    def test_GenStar(self):
        # Directed Graph
        Graph = self.DirGraphStar
        for node in Graph.Nodes():
            if node.GetId() == 0:
                self.assertEqual(self.num_nodes-1, node.GetOutDeg())
                self.assertEqual(0, node.GetInDeg())
            else:
                self.assertEqual(0, node.GetOutDeg())
                self.assertEqual(1, node.GetInDeg())

        # Undirected Graph
        Graph = self.UnDirGraphStar
        for node in Graph.Nodes():
            if node.GetId() == 0:
                self.assertEqual(self.num_nodes-1, node.GetOutDeg())
                self.assertEqual(self.num_nodes-1, node.GetInDeg())
            else:
                self.assertEqual(1, node.GetOutDeg())
                self.assertEqual(1, node.GetInDeg())

        # Network
        Graph = self.NetStar
        for node in Graph.Nodes():
            if node.GetId() == 0:
                self.assertEqual(self.num_nodes-1, node.GetOutDeg())
                self.assertEqual(0, node.GetInDeg())
            else:
                self.assertEqual(0, node.GetOutDeg())
                self.assertEqual(1, node.GetInDeg())

    def test_GenTree(self):
        # Directed Graph
        Graph = snap.GenTree(snap.PNGraph, 3, 3, True, False)
        for node in Graph.Nodes():
            self.assertTrue(node.GetDeg() == 4 or (node.GetDeg() == 3 and node.GetId() == 0) or node.GetDeg() == 1)

        # Undirected Graph
        Graph = snap.GenTree(snap.PUNGraph, 3, 3, False, False)
        for node in Graph.Nodes():
           self.assertTrue(node.GetDeg() == 4 or (node.GetDeg() == 3 and node.GetId() == 0) or node.GetDeg() == 1)

        # Network
        Graph = snap.GenTree(snap.PNEANet, 3, 3, True, False)
        for node in Graph.Nodes():
            self.assertTrue(node.GetDeg() == 4 or (node.GetDeg() == 3 and node.GetId() == 0) or node.GetDeg() == 1)

    def test_GenBaraHierar(self):
        expected_nodes = 625
        expected_edges = 1976

        # Directed Graph
        Graph = snap.GenBaraHierar(snap.PNGraph, 3, True)
        self.assertEqual(expected_nodes, Graph.GetNodes())
        self.assertEqual(expected_edges, Graph.GetEdges())

        # Directed Graph
        Graph = snap.GenBaraHierar(snap.PUNGraph, 3, True)
        self.assertEqual(expected_nodes, Graph.GetNodes())
        self.assertEqual(expected_edges, Graph.GetEdges())

        # Directed Graph
        Graph = snap.GenBaraHierar(snap.PNEANet, 3, True)
        self.assertEqual(expected_nodes, Graph.GetNodes())
        self.assertEqual(expected_edges, Graph.GetEdges())

    def test_LoadDyNet(self):
        Gout = snap.GenRndGnm(snap.PNGraph, 100, 1000)
        fname = "test.xml"
        with open(fname, "w") as f:
            f.write("<network>\n")

            for EI in Gout.Edges():
                src = EI.GetSrcNId()
                dst = EI.GetDstNId()
                f.write("\t<link source='" + str(src) + "' target='" + str(dst) + "'/> \n")

            f.write("</network>\n")

        Gin = snap.LoadDyNet(fname)

        self.assertTrue(Gin.GetNodes() == Gout.GetNodes())
        self.assertTrue(Gin.GetEdges() == Gout.GetEdges())
        os.remove(fname)

    def test_LoadConnList(self):
        fname = "test.txt"
        with open(fname, "w") as f:
            for i in range(10):
                line = str(i)
                for j in range(10):
                    if j != i:
                        line += " " + str(j)
                f.write(line + "\n")

        # Directed Graph
        Graph = snap.LoadConnList(snap.PNGraph, fname)
        for i in range(10):
            for j in range(10):
                if i != j:
                    self.assertTrue(Graph.IsEdge(i, j))
                else:
                    self.assertFalse(Graph.IsEdge(i, j))

        # Undirected Graph
        Graph = snap.LoadConnList(snap.PUNGraph, fname)
        for i in range(10):
            for j in range(10):
                if i != j:
                    self.assertTrue(Graph.IsEdge(i, j))
                else:
                    self.assertFalse(Graph.IsEdge(i, j))

        # Network
        Graph = snap.LoadConnList(snap.PNEANet, fname)
        for i in range(10):
            for j in range(10):
                if i != j:
                    self.assertTrue(Graph.IsEdge(i, j))
                else:
                    self.assertFalse(Graph.IsEdge(i, j))

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
        Graph = snap.LoadPajek(snap.PNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        # Undirected Graph
        Graph = snap.LoadPajek(snap.PUNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        # Network
        Graph = snap.LoadPajek(snap.PNGraph, fname)
        count = 1
        for node in Graph.Nodes():
            self.assertEqual(count, node.GetId())
            count += 1

        os.remove(fname)

    def test_SaveEdgeList(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        exp_hash = 'd26278f1b4d13aac3c22763f937a30d3'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        exp_hash = 'c767b54d9d1c607c791d895817b9b758'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        exp_hash = 'd26278f1b4d13aac3c22763f937a30d3'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SaveMatlabSparseMtx(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveMatlabSparseMtx(self.DirGraphFull, fname)
        exp_hash = 'a0e90dc5e7e3d9383a4af049d4dafee2'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        snap.SaveMatlabSparseMtx(self.UnDirGraphFull, fname)
        test_hash = self.getFileHash(fname)
        exp_hash = '28a9ccb0bf7c71de564fac9d071fb704'
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        snap.SaveMatlabSparseMtx(self.NetFull, fname)
        exp_hash = 'a0e90dc5e7e3d9383a4af049d4dafee2'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_GetSngVals(self):
        SngVals = 4
        SngValV = self.DirGraphFull.GetSngVals(SngVals)
        count = 0
        for item in SngValV:
            if count == 0:
                self.assertAlmostEqual(self.num_nodes-1, item)
            else:
                self.assertAlmostEqual(1, item)
            count += 1

    def test_GetEigVals(self):
        Graph = snap.GenStar(snap.PUNGraph, 50)
        NumEigVals = 2
        EigValV = Graph.GetEigVals(NumEigVals)
        count = 0
        for item in EigValV:
            if count == 0:
                self.assertAlmostEqual(7.0, item)
            else:
                self.assertAlmostEqual(-7.0, item)
            count += 1
        self.assertEqual(2, count)

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

        expected = [[-1.246980, 0.214286],[0.445042, 0.214286],[1.801938, 0.214286]]
        EigValIprV = Graph.GetInvParticipRat(10, 1000)
        count = 0
        for x in EigValIprV:
            self.assertAlmostEqual(expected[count][0], x.GetVal1(), 5)
            self.assertAlmostEqual(expected[count][1], x.GetVal2(), 5)
            count += 1

    def test_GetKCore(self):
        # Directed Graph
        k = self.num_nodes - 1
        KCore = self.DirGraphFull.GetKCore(k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

        # Undirected Graph
        k = self.num_nodes - 1
        KCore = self.UnDirGraphFull.GetKCore(k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

        # Network
        k = self.num_nodes - 1
        KCore = self.NetFull.GetKCore(k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

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
        for node in self.NetStar.Nodes():
            self.assertTrue(ESubGraph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(ESubGraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_ConvertGraph(self):
        # Directed to Undirected
        UnDirStar = self.DirGraphStar.ConvertGraph(snap.PUNGraph)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Directed to Network
        NetStar = self.DirGraphStar.ConvertGraph(snap.PNEANet)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(NetStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Undirected to Directed
        DirStar = self.UnDirGraphStar.ConvertGraph(snap.PNGraph)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(DirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(DirStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Undirected to Network
        NetStar = self.UnDirGraphStar.ConvertGraph(snap.PNEANet)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(NetStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(NetStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Network to Undirected
        UnDirStar = self.NetStar.ConvertGraph(snap.PUNGraph)
        for node in self.NetStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.NetStar.GetEdges())

        # Network to Directed
        DirStar = self.NetStar.ConvertGraph(snap.PNGraph)
        for node in self.NetStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(DirStar.GetEdges(), self.NetStar.GetEdges())

    def test_ConvertSubGraph(self):
        PyListNodes = []
        for x in range(self.num_nodes):
            PyListNodes.append(x)

        # Directed to Undirected
        UnDirStar = self.DirGraphStar.ConvertSubGraph(snap.PUNGraph, PyListNodes)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Directed to Network
        NetStar = self.DirGraphStar.ConvertSubGraph(snap.PNEANet, PyListNodes)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(NetStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Undirected to Directed
        DirStar = self.UnDirGraphStar.ConvertSubGraph(snap.PNGraph, PyListNodes)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(DirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(DirStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Undirected to Network
        NetStar = self.UnDirGraphStar.ConvertSubGraph(snap.PNEANet, PyListNodes)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(NetStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(NetStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Network to Undirected
        UnDirStar = self.NetStar.ConvertSubGraph(snap.PUNGraph, PyListNodes)
        for node in self.NetStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.NetStar.GetEdges())

        # Network to Directed
        DirStar = self.NetStar.ConvertSubGraph(snap.PNGraph, PyListNodes)
        for node in self.NetStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(DirStar.GetEdges(), self.NetStar.GetEdges())

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
        exp_triad_edges = self.DirGraphFull.GetEdges()
        act_triad_edges = self.DirGraphFull.GetTriadEdges()
        self.assertEqual(exp_triad_edges, act_triad_edges)

        # Unirected Graph
        exp_triad_edges = self.UnDirGraphFull.GetEdges()
        act_triad_edges = self.UnDirGraphFull.GetTriadEdges()
        self.assertEqual(exp_triad_edges, act_triad_edges)

        # Network
        exp_triad_edges = self.NetFull.GetEdges()
        act_triad_edges = self.NetFull.GetTriadEdges()
        self.assertEqual(exp_triad_edges, act_triad_edges)

    def test_GetTriadParticip(self):
        f = math.factorial
        exp_num_tri = f(self.num_nodes-1)/f(2)/f(self.num_nodes-3)

        # Directed Graph
        TriadCntV = self.DirGraphFull.GetTriadParticip()
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

        # Undirected Graph
        TriadCntV = self.UnDirGraphFull.GetTriadParticip()
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

        # Network
        TriadCntV = self.NetFull.GetTriadParticip()
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

    def test_CntEdgesToSet(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        val = G.CntEdgesToSet(0, set())
        self.assertEqual(0, val)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        val = G.CntEdgesToSet(0, set())
        self.assertEqual(0, val)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        val = G.CntEdgesToSet(0, set())
        self.assertEqual(0, val)

    def test_GetAnf(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

    def test_GetAnf2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        DistNbrsV = snap.TIntFltKdV()
        Graph.GetAnf(DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

    def test_GetAnfEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        self.assertTrue(result >= 0)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        self.assertTrue(result >= 0)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetAnfEffDiam(True, 0.9, 1024)
        self.assertTrue(result >= 0)

    def test_GetAnfEffDiam2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetAnfEffDiam()
        self.assertTrue(result >= 0)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetAnfEffDiam()
        self.assertTrue(result >= 0)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetAnfEffDiam()
        self.assertTrue(result >= 0)

    def test_GetShortPath(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetShortPath(0, 1)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetShortPath(0, 1)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetShortPath(0, 1)
        self.assertEqual(1, result)

    def test_GetShortPath2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result, H = Graph.GetShortPathAll(0)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result, H = Graph.GetShortPathAll(0)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result, H = Graph.GetShortPathAll(0)
        self.assertEqual(1, result)

    def test_GetBfsFullDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetBfsFullDiam(10)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetBfsFullDiam(10)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetBfsFullDiam(10)
        self.assertEqual(1, result)

    def test_GetBfsEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetBfsEffDiam(10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetBfsEffDiam(10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetBfsEffDiam(10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = Graph.GetBfsEffDiam(Num, List, True)
        self.assertEqual(expected_result, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = Graph.GetBfsEffDiam(Num, List, False)
        self.assertEqual(expected_result, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = Graph.GetBfsEffDiam(Num, List, True)
        self.assertEqual(expected_result, result)

    def test_GetBfsEffDiamAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = Graph.GetBfsEffDiamAll(Num, True)
        self.assertEqual(expected_result, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = Graph.GetBfsEffDiamAll(Num, False)
        self.assertEqual(expected_result, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = Graph.GetBfsEffDiamAll(Num, True)
        self.assertEqual(expected_result, result)

    def test_GetBetweennessCentr(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        Nodes, Edges = Graph.GetBetweennessCentr(1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

    def test_GetArtPoints(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        V = Graph.GetArtPoints()
        self.assertEqual(0, V.Len())

    def test_GenRndPowerLaw(self):
        # Undirected Graph
        Graph = snap.GenRndPowerLaw (9, 10)
        self.assertEqual(Graph.GetNodes(), 9)

    def test_GenConfModel(self):
        # Undirected Graph
        DegSeqV = snap.TIntV()
        DegSeqV.Add(0)
        Graph = snap.GenConfModel(DegSeqV)
        self.assertEqual(Graph.GetNodes(), 1)

    def test_GenConfModel1(self):
        # Undirected Graph
        GraphIn = snap.GenFull(snap.PUNGraph, 10)
        Graph = snap.GenConfModel(GraphIn)
        self.assertEqual(Graph.GetNodes(), 10)

    def test_GenSmallWorld(self):
        # Undirected Graph
        Graph = snap.GenSmallWorld(10, 3, 0, snap.TRnd())
        self.assertEqual(Graph.GetNodes(), 10)

    def test_GenCopyModel(self):
        # Directed Graph
        Graph = snap.GenCopyModel(20, 0.4, snap.TRnd())
        self.assertEqual(Graph.GetNodes(), 20)

    def test_GenGrid(self):
        # Directed Graph
        Graph = snap.GenGrid(snap.PNGraph, 2, 2)
        self.assertEqual(Graph.GetNodes(), 4)
        self.assertEqual(Graph.GetEdges(), 4)

        # Undirected Graph
        Graph = snap.GenGrid(snap.PUNGraph, 2, 2)
        self.assertEqual(Graph.GetNodes(), 4)
        self.assertEqual(Graph.GetEdges(), 4)

        # Network
        Graph = snap.GenGrid(snap.PNEANet, 2, 2)
        self.assertEqual(Graph.GetNodes(), 4)
        self.assertEqual(Graph.GetEdges(), 4)

    def test_GenFull(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 5)
        self.assertEqual(Graph.GetNodes(), 5)
        self.assertEqual(Graph.GetEdges(), 20)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 5)
        self.assertEqual(Graph.GetNodes(), 5)
        self.assertEqual(Graph.GetEdges(), 10)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 5)
        self.assertEqual(Graph.GetNodes(), 5)
        self.assertEqual(Graph.GetEdges(), 20)

    def test_GenRndGnm(self):
        # Directed Graph
        Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
        self.assertEqual(Graph.GetNodes(), 100)
        self.assertEqual(Graph.GetEdges(), 1000)

        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
        self.assertEqual(Graph.GetNodes(), 100)
        self.assertEqual(Graph.GetEdges(), 1000)

        # Network
        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        self.assertEqual(Graph.GetNodes(), 100)
        self.assertEqual(Graph.GetEdges(), 1000)

    def test_GetCmnNbrs(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        self.assertEqual(result, 8)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        self.assertEqual(result, 8)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetCmnNbrs(0, 1, False)
        self.assertEqual(result, 8)

    def test_GetCmnNbrs1(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        self.assertEqual(result, 8)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        self.assertEqual(result, 8)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result, V = Graph.GetCmnNbrs(0, 1, True)
        self.assertEqual(result, 8)

    def test_GetNodeTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetNodeTriads(0)
        self.assertEqual(result, 36)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetNodeTriads(0)
        self.assertEqual(result, 36)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetNodeTriads(0)
        self.assertEqual(result, 36)

    def test_GetNodeTriadsSet(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSetPy = set()
        for NbrIdx in range(4):
            GroupSetPy.add(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = Graph.GetNodeTriadsSet(NId, GroupSetPy)
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSetPy = set()
        for NbrIdx in range(4):
            GroupSetPy.add(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = Graph.GetNodeTriadsSet(NId, GroupSetPy)
        self.assertEqual(result, expected_result)

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
        self.assertEqual(result, expected_result)

    def test_GetNodeTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        expected_result = [4851, 4851, 0]
        result = Graph.GetNodeTriadsAll(10)
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        expected_result = [4851, 4851, 0]
        result = Graph.GetNodeTriadsAll(10)
        self.assertEqual(result, expected_result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        expected_result = [4851, 4851, 0]
        result = Graph.GetNodeTriadsAll(10)
        self.assertEqual(result, expected_result)

    def test_GetTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = Graph.GetTriads()
        self.assertEqual(result, 120)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = Graph.GetTriads()
        self.assertEqual(result, 120)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = Graph.GetTriads()
        self.assertEqual(result, 120)

    def test_GetTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        expected_result = [161700, 161700, 0]
        result = Graph.GetTriadsAll()
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        expected_result = [161700, 161700, 0]
        result = Graph.GetTriadsAll()
        self.assertEqual(result, expected_result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        expected_result = [161700, 161700, 0]
        result = Graph.GetTriadsAll()
        self.assertEqual(result, expected_result)

    def test_GetClustCf(self):

        # testing GetClustCf(Graph, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        result = DirGraph.GetClustCf()
        self.assertAlmostEqual(result, 1.0)

        # Undirected Graph
        result = UnGraph.GetClustCf()
        self.assertAlmostEqual(result, 1.0)

        # Network
        result = MultiGraph.GetClustCf()
        self.assertAlmostEqual(result, 1.0)

        # parameter = 0

        result = DirGraph.GetClustCf(False, 0)
        self.assertAlmostEqual(result, 0.0)

        result = UnGraph.GetClustCf(False, 0)
        self.assertAlmostEqual(result, 0.0)

        result = MultiGraph.GetClustCf(False, 0)
        self.assertAlmostEqual(result, 0.0)

        # parameter > 0

        result = DirGraph.GetClustCf(False, 3)
        self.assertAlmostEqual(result, 1.0)

        result = UnGraph.GetClustCf(False, 3)
        self.assertAlmostEqual(result, 1.0)

        result = MultiGraph.GetClustCf(False, 3)
        self.assertAlmostEqual(result, 1.0)

    def test_GetClustCf2(self):

        # testing GetClustCf(Graph, DegToCCfV, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        V = snap.TFltPrV()
        result, V = DirGraph.GetClustCf(True)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # Undirected Graph
        V = snap.TFltPrV()
        result, V = UnGraph.GetClustCf(True)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # Network
        V = snap.TFltPrV()
        result, V = MultiGraph.GetClustCf(True)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # parameter = 0

        V = snap.TFltPrV()
        result, V = DirGraph.GetClustCf(True, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        V = snap.TFltPrV()
        result, V = UnGraph.GetClustCf(True, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        V = snap.TFltPrV()
        result, V = MultiGraph.GetClustCf(True, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        # parameter > 0

        V = snap.TFltPrV()
        result, V = DirGraph.GetClustCf(True, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        V = snap.TFltPrV()
        result, V = UnGraph.GetClustCf(True, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        V = snap.TFltPrV()
        result, V = MultiGraph.GetClustCf(True, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

    def test_GetClustCfAll(self):

        DirGraph = snap.GenFull(snap.PNGraph, 100)
        UnGraph = snap.GenFull(snap.PUNGraph, 100)
        MultiGraph = snap.GenFull(snap.PNEANet, 100)

        # no parameter

        V = snap.TFltPrV()
        result = DirGraph.GetClustCfAll(V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = UnGraph.GetClustCfAll(V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = MultiGraph.GetClustCfAll(V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        # parameter = 0

        V = snap.TFltPrV()
        result = DirGraph.GetClustCfAll(V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = UnGraph.GetClustCfAll(V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = MultiGraph.GetClustCfAll(V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        # parameter > 0

        V = snap.TFltPrV()
        result = DirGraph.GetClustCfAll(V, 5)
        expected_result = [1.0, 8085, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = UnGraph.GetClustCfAll(V, 5)
        expected_result = [1.0, 8085, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = MultiGraph.GetClustCfAll(V, 5)
        expected_result = [1.0, 8085, 0]
        self.assertEqual(result, expected_result)

    def test_GetLen2Paths(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result, 98)

        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(NV.Len(), 98)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result, 98)

        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(result, 98)
        self.assertEqual(NV.Len(), 98)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        result = snap.GetLen2Paths(Graph, 0, 1)
        self.assertEqual(result, 98)
        self.assertEqual(result, 98)

        NV = snap.TIntV()
        result = snap.GetLen2Paths(Graph, 0, 1, NV)
        self.assertEqual(result, 98)
        self.assertEqual(NV.Len(), 98)

    def test_SavePajek(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SavePajek(self.DirGraphFull, fname)
        exp_hash = '9474d66aacad5a21ce366eb6b98eb157'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        snap.SavePajek(self.UnDirGraphFull, fname)
        exp_hash = '7552ace478ac1b2193a91f4d2707d45d'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        snap.SavePajek(self.NetFull, fname)
        exp_hash = '9474d66aacad5a21ce366eb6b98eb157'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SavePajek2(self):
        # Directed Graph
        fname = "mygraph.txt"
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH)
        exp_hash = '1d0c1618ae32a2e3e600e47d9540e2e4'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH)
        exp_hash = '7a63bc4bd44d9c078e50ba2a43fc484f'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SavePajek(self.NetFull, fname, NIdColorH)
        exp_hash = '1d0c1618ae32a2e3e600e47d9540e2e4'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SavePajek3(self):
        # Directed Graph
        fname = "mygraph.txt"
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH, NIdLabelH)
        exp_hash = '1d0c1618ae32a2e3e600e47d9540e2e4'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH, NIdLabelH)
        exp_hash = '7a63bc4bd44d9c078e50ba2a43fc484f'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        snap.SavePajek(self.NetFull, fname, NIdColorH, NIdLabelH)
        exp_hash = '1d0c1618ae32a2e3e600e47d9540e2e4'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SavePajek4(self):
        # Directed Graph
        fname = "mygraph.txt"
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        EIdColorH = snap.TIntStrH()
        for i in range(1000):
            EIdColorH[i] = "black"
        snap.SavePajek(self.DirGraphFull, fname, NIdColorH, NIdLabelH, EIdColorH)
        exp_hash = '1d0c1618ae32a2e3e600e47d9540e2e4'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        EIdColorH = snap.TIntStrH()
        for i in range(1000):
            EIdColorH[i] = "black"
        snap.SavePajek(self.UnDirGraphFull, fname, NIdColorH, NIdLabelH, EIdColorH)
        exp_hash = '7a63bc4bd44d9c078e50ba2a43fc484f'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        NIdLabelH = snap.TIntStrH()
        for i in range(100):
            NIdLabelH[i] = str(i)
        EIdColorH = snap.TIntStrH()
        for i in range(1000):
            EIdColorH[i] = "black"
        snap.SavePajek(self.NetFull, fname, NIdColorH, NIdLabelH, EIdColorH)
        exp_hash = '22acc46e0a1a57c4f74fbacac90ebd82'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SaveGViz(self):
        # Directed Graph
        fname = "mygraph.dot"
        NIdColor_dict = {}
        for i in range(self.num_nodes):
            NIdColor_dict[i] = "red"
        snap.SaveGVizColor(self.DirGraphFull, fname, "text", True, NIdColor_dict)
        exp_hash = '64fe626fa482a0d45416824dc02d73a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdColor_dict = {}
        for i in range(self.num_nodes):
            NIdColor_dict[i] = "red"
        snap.SaveGVizColor(self.UnDirGraphFull, fname, "text", True, NIdColor_dict)
        exp_hash = 'd2185ec44f908e8d10da6c6319c900a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdColor_dict = {}
        for i in range(self.num_nodes):
            NIdColor_dict[i] = "red"
        snap.SaveGVizColor(self.NetFull, fname, "text", True, NIdColor_dict)
        exp_hash = '64fe626fa482a0d45416824dc02d73a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SaveGViz2(self):
        # Directed Graph
        fname = "mygraph.dot"
        NIdLabelH = {}
        for i in range(self.num_nodes):
            NIdLabelH[i] = str(i)
        snap.SaveGViz(self.DirGraphFull, fname, "text", NIdLabelH)
        exp_hash = '260c9cfe1b5eac55a053ffcf418703e1'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdLabelH = {}
        for i in range(self.num_nodes):
            NIdLabelH[i] = str(i)
        snap.SaveGViz(self.UnDirGraphFull, fname, "text", NIdLabelH)
        exp_hash = 'df04d8deed65d2a537a741e3ab3e251b'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdLabelH = {}
        for i in range(self.num_nodes):
            NIdLabelH[i] = str(i)
        snap.SaveGViz(self.NetFull, fname, "text", NIdLabelH)
        exp_hash = '260c9cfe1b5eac55a053ffcf418703e1'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_LoadEdgeList(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes/2)
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PNEANet, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

    def test_LoadEdgeList2(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PNGraph, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes/2)
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeList(snap.PNEANet, fname, 0, 1, '\t')
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

    def test_LoadEdgeListStr(self):
        # Directed Graph
        fname = "mygraph.txt"
        snap.SaveEdgeList(self.DirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.PNGraph, fname, 0, 1, True)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.PUNGraph, fname, 0, 1, True)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes/2)
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph, mapping = snap.LoadEdgeListStr(snap.PNEANet, fname, 0, 1, True)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

    def test_GetSngVec(self):
        # Directed Graph
        val = 0.316227766017
        Graph = snap.GenFull(snap.PNGraph, 10)
        LeftSV, RightSV = Graph.GetLeadSngVec()
        for i in LeftSV:
            self.assertAlmostEqual(i, val)
        for i in RightSV:
            self.assertAlmostEqual(i, val)

        SngValV, LeftSVV, RightSVV = Graph.GetSngVecs(5)
        self.assertAlmostEqual(SngValV[0], 9.0)
        for i in range(1,10):
            self.assertAlmostEqual(SngValV[1], 1.0)

    def test_LoadConnList(self):
        fname = "mygraph.txt"
        output = open(fname, "w")
        output.write('0 1 2\n')
        output.write('1 2 0\n')
        output.write('2 0 1\n')
        output.close()

        # Directed Graph
        Graph = snap.LoadConnList(snap.PNGraph, fname)
        self.assertEqual(Graph.GetNodes(), 3)
        self.assertEqual(Graph.GetEdges(), 6)

        # Undirected Graph
        Graph = snap.LoadConnList(snap.PUNGraph, fname)
        self.assertEqual(Graph.GetNodes(), 3)
        self.assertEqual(Graph.GetEdges(), 3)

        # Network
        Graph = snap.LoadConnList(snap.PNEANet, fname)
        self.assertEqual(Graph.GetNodes(), 3)
        self.assertEqual(Graph.GetEdges(), 6)
        os.remove(fname)

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
        V_list = []
        for i in range(5):
            V_list.append(i)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SubGraph = Graph.GetSubGraph(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)

        SubGraph = Graph.GetSubGraphRenumber(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)
        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SubGraph = Graph.GetSubGraph(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4/2)

        SubGraph = Graph.GetSubGraphRenumber(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4/2)
        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SubGraph = Graph.GetSubGraph(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)

        SubGraph = Graph.GetSubGraph(V_list)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)
        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

    def test_GetNodeClustCf(self):
        # Directed Graph
        H = self.DirGraphFull.GetNodeClustCfAll()
        for i in H:
            self.assertEqual(1.0, H[i])

        # Undirected Graph
        H = self.UnDirGraphFull.GetNodeClustCfAll()
        for i in H:
            self.assertEqual(1.0, H[i])

        # Network
        H = self.NetFull.GetNodeClustCfAll()
        for i in H:
            self.assertEqual(1.0, H[i])

    def test_ConvertESubGraph(self):
        V_list = []
        for i in range(10):
            V_list.append(i+1)
        # Directed Graph
        SubGraph = self.NetFull.ConvertESubGraph(snap.PNGraph, V_list)
        self.assertEqual(SubGraph.GetEdges(), len(V_list))

        # Undirected Graph
        SubGraph = self.NetFull.ConvertESubGraph(snap.PUNGraph, V_list)
        self.assertEqual(SubGraph.GetEdges(), len(V_list))

        # Network
        SubGraph = self.NetFull.ConvertESubGraph(snap.PNEANet, V_list)
        self.assertEqual(SubGraph.GetEdges(), len(V_list))

if __name__ == '__main__':
  unittest.main()

