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

        # Petersen graph
        Graph = snap.TUNGraph.New()
        for i in range(10):
            Graph.AddNode(i)
        for i in range(5):
            Graph.AddEdge(i,(i+1) % 5)
        for i in range(5):
            Graph.AddEdge(i + 5,(i+2) % 5 + 5)
        for i in range(5):
            Graph.AddEdge(i,i + 5)
        self.UPetersen = Graph
        snap.DrawGViz(self.UPetersen, snap.gvlDot, "upetersen.png", "petersen 1")

        # directed Petersen graph
        Graph = snap.TNGraph.New()
        for i in range(10):
            Graph.AddNode(i)
        for i in range(5):
            Graph.AddEdge(i,(i+1) % 5)
        for i in range(5):
            Graph.AddEdge(i + 5,(i+2) % 5 + 5)
        for i in range(5):
            Graph.AddEdge(i,i + 5)
        self.DPetersen = Graph
        snap.DrawGViz(self.DPetersen, snap.gvlDot, "dpetersen.png", "petersen 2")

        # directed Petersen network
        self.NPetersen = self.DPetersen.ConvertGraph(snap.TNEANet)
        snap.DrawGViz(self.NPetersen, snap.gvlDot, "npetersen.png", "petersen 3")

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

    # Avery Vector tests
    def test_vec_append(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)

        vector = snap.TIntV()
        vector.append(1)
        self.assertEqual(vector, new_vec)

    def test_vec_extend(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)
        new_vec.Add(2)
        new_vec.Add(3)

        # Vector to extend by
        extend_vec = snap.TIntV()
        extend_vec.Add(2)
        extend_vec.Add(3)

        # Extend operation
        vector = snap.TIntV()
        vector.Add(1)
        vector.extend(extend_vec)

        self.assertEqual(vector, new_vec)

    def test_vec_clear(self):
        # Vector to test against
        new_vec = snap.TIntV()

        # Adding to and clearing vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.clear()

        self.assertEqual(vector, new_vec)

    def test_vec_insert(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)
        new_vec.Add(2)
        new_vec.Add(3)

        # Attempting insert on self.vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(3)
        vector.insert(1, 2)

        self.assertEqual(vector, new_vec)

    def test_vec_remove(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)

        # Attempting insert on vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        vector.remove(2)

        self.assertEqual(vector, new_vec)

    def test_vec_index(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        index = vector.index(2)

        self.assertEqual(index, 1)

    def test_vec_count(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(1)
        vector.Add(1)
        num_ones = vector.count(1)

        self.assertEqual(num_ones, 3)

    def test_vec_pop(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        popped = vector.pop(1)

        self.assertEqual(popped, 2)

    def test_vec_reverse(self):
        # Vector to compare
        new_vec = snap.TIntV()
        new_vec.Add(2)
        new_vec.Add(1)

        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        vector.reverse()

        self.assertEqual(vector, new_vec)

    def test_vec_sort(self):
        # Vector to compare
        new_vec = snap.TIntV()
        new_vec.Add(1)
        new_vec.Add(2)
        new_vec.Add(3)

        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(3)
        vector.Add(2)
        vector.sort(asc=True)

        self.assertEqual(vector, new_vec)

    def test_vec_copy(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        new_vec = vector.copy()

        self.assertEqual(vector, new_vec)

    def test_vec_max(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(5)
        vector.Add(2)

        maximum = max(vector)

        self.assertEqual(maximum, 5)

    def test_vec_min(self):
        vector = snap.TIntV()
        vector.Add(2)
        vector.Add(1)
        vector.Add(5)

        minimum = min(vector)

        self.assertEqual(minimum, 1)

    # Avery Hash Table Tests
    def test_hash_clear(self):
        new_ht = snap.TIntH()

        ht = snap.TIntH()
        ht[1] = 2
        ht.clear()

        self.assertEqual(ht, new_ht)

    def test_hash_copy(self):
        ht = snap.TIntH()
        ht[1] = 2
        new_ht = ht.copy()

        self.assertEqual(ht, new_ht)

    def test_hash_get(self):
        ht = snap.TIntH()
        ht[1] = 2
        value = ht.get(1)

        self.assertEqual(value, 2)

    def test_hash_items(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        items = [(1, 2), (3, 4)]
        ht_items = ht.items()

        self.assertEqual(items, ht_items)

    def test_hash_keys(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        keys = [1, 3]
        ht_keys = ht.keys()

        self.assertEqual(keys, ht_keys)

    def test_hash_pop(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        popped = 2
        ht_popped = ht.pop(1)

        self.assertEqual(popped, ht_popped)

    def test_hash_setdefault(self):
        new_ht = snap.TIntH()
        new_ht[1] = 2
        new_ht[3] = 4

        ht = snap.TIntH()
        ht[1] = 2
        default_val = ht.setdefault(3, 4)

        self.assertEqual(ht, new_ht)
        self.assertEqual(default_val, 4)

    def test_hash_update(self):
        new_ht = snap.TIntH()
        new_ht[1] = 2
        new_ht[3] = 5

        ht = snap.TIntH()
        ht[3] = 4
        ht.update(new_ht)

        final_ht = snap.TIntH()
        final_ht[1] = 2
        final_ht[3] = 5

        self.assertEqual(ht, final_ht)

    def test_hash_values(self):
        expected_values = [2, 4]

        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        values = ht.values()

        self.assertEqual(expected_values, values)


    def test_CntInDegNodes(self):
        # Directed graph
        num_nodes = snap.CntInDegNodes(self.DirGraphFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

        # Undirected Graph
        num_nodes = snap.CntInDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

        # Network
        num_nodes = snap.CntInDegNodes(self.NetFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

    def test_CntOutDegNodes(self):
        # Directed Graph
        num_nodes = snap.CntOutDegNodes(self.DirGraphFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

        # Undirected Graph
        num_nodes = snap.CntOutDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

        # Network
        num_nodes = snap.CntOutDegNodes(self.NetFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

    def test_CntDegNodes(self):
        # Directed Graph - it will have twice the edges as the undirected graph
        num_nodes = snap.CntDegNodes(self.DirGraphFull, 2*(self.num_nodes-1))
        self.assertEqual(self.num_nodes, num_nodes)

        # Undirected Graph
        num_nodes = snap.CntDegNodes(self.UnDirGraphFull, self.num_nodes-1)
        self.assertEqual(self.num_nodes, num_nodes)

        # Network
        num_nodes = snap.CntDegNodes(self.NetFull, 2*(self.num_nodes-1))
        self.assertEqual(self.num_nodes, num_nodes)

    def test_CntNonZNodes(self):
        # Directed Graph
        num_nodes = snap.CntNonZNodes(self.DirGraphFull)
        self.assertEqual(self.num_nodes, num_nodes)

        # Undirected Graph
        num_nodes = snap.CntNonZNodes(self.UnDirGraphFull)
        self.assertEqual(self.num_nodes, num_nodes)

        # Network
        num_nodes = snap.CntNonZNodes(self.NetFull)
        self.assertEqual(self.num_nodes, num_nodes)

    def test_GetMxDegNId(self):
        # Directed Graph
        max_id = snap.GetMxDegNId(self.DirGraphStar)
        self.assertEqual(0, max_id)

        # Undirected Graph
        max_id = snap.GetMxDegNId(self.UnDirGraphStar)
        self.assertEqual(0, max_id)

        # Network
        max_id = snap.GetMxDegNId(self.NetStar)
        self.assertEqual(0, max_id)

    def test_GetMxInDegNId(self):
        # Directed Graph
        max_id = snap.GetMxInDegNId(self.DirGraphStar)
        # node with id 0 is the only node with in-degree 0
        self.assertNotEqual(0, max_id)

        # Undirected Graph
        max_id = snap.GetMxInDegNId(self.UnDirGraphStar)
        self.assertEqual(0, max_id)

        # Network
        max_id = snap.GetMxInDegNId(self.NetStar)
        # node with id 0 is the only node with in-degree 0
        self.assertNotEqual(0, max_id)

    def test_GetMxOutDegNId(self):
        # Directed Graph
        max_id = snap.GetMxOutDegNId(self.DirGraphStar)
        self.assertEqual(0, max_id)

        # Undirected Graph
        max_id = snap.GetMxOutDegNId(self.UnDirGraphStar)
        self.assertEqual(0, max_id)

        # Network
        max_id = snap.GetMxOutDegNId(self.NetStar)
        self.assertEqual(0, max_id)

    def test_GetInDegCnt(self):
        # Directed Graph
        DegToCntV = snap.TIntPrV()
        snap.GetInDegCnt(self.DirGraphFull, DegToCntV)
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Undirected Graph
        DegToCntV = snap.TIntPrV()
        snap.GetInDegCnt(self.UnDirGraphFull, DegToCntV)
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = snap.TIntPrV()
        snap.GetInDegCnt(self.NetFull, DegToCntV)
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetOutDegCnt(self):
        # Directed Graph
        DegToCntV = snap.TIntPrV()
        snap.GetOutDegCnt(self.DirGraphFull, DegToCntV)
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Undirected Graph
        DegToCntV = snap.TIntPrV()
        snap.GetOutDegCnt(self.UnDirGraphFull, DegToCntV)
        # There should be only one entry (num_nodes -1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = snap.TIntPrV()
        snap.GetOutDegCnt(self.NetFull, DegToCntV)
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetDegCnt(self):
        # Directed Graph
        DegToCntV = snap.TIntPrV()
        snap.GetDegCnt(self.DirGraphFull, DegToCntV)
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(2*(self.num_nodes-1), item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Undirected Graph
        DegToCntV = snap.TIntPrV()
        snap.GetDegCnt(self.UnDirGraphFull, DegToCntV)
        # There should be only one entry (num_nodes-1, num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal1())
            self.assertEqual(self.num_nodes, item.GetVal2())

        # Network
        DegToCntV = snap.TIntPrV()
        snap.GetDegCnt(self.NetFull, DegToCntV)
        # There should be only one entry (2*(num_nodes-1), num_nodes) in DegToCntV
        for item in DegToCntV:
            self.assertEqual(self.num_nodes, item.GetVal2())

    def test_GetNodeInDegV(self):
        # Directed Graph
        DegToCntV = snap.TIntPrV()
        snap.GetNodeInDegV(self.DirGraphFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Undirected Graph
        DegToCntV = snap.TIntPrV()
        snap.GetNodeInDegV(self.UnDirGraphFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Network
        DegToCntV = snap.TIntPrV()
        snap.GetNodeInDegV(self.NetFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

    def test_GetNodeOutDegV(self):
        # Directed Graph
        DegToCntV = snap.TIntPrV()
        snap.GetNodeOutDegV(self.DirGraphFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Undirected Graph
        DegToCntV = snap.TIntPrV()
        snap.GetNodeOutDegV(self.UnDirGraphFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

        # Network
        DegToCntV = snap.TIntPrV()
        snap.GetNodeOutDegV(self.NetFull, DegToCntV)
        for item in DegToCntV:
            self.assertEqual(self.num_nodes-1, item.GetVal2())

    def test_CntUniqUndirEdges(self):
        # Directed Graph
        num_edges = snap.CntUniqUndirEdges(self.DirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Unidrected Graph
        num_edges = snap.CntUniqUndirEdges(self.UnDirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Network
        num_edges = snap.CntUniqUndirEdges(self.NetFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

    def test_CntUniqDirEdges(self):
        # Directed Graph
        num_edges = snap.CntUniqDirEdges(self.DirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

        # Unidrected Graph
        num_edges = snap.CntUniqDirEdges(self.UnDirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

        # Network
        num_edges = snap.CntUniqDirEdges(self.NetFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1), num_edges)

    def test_CntUniqBiDirEdges(self):
        # Directed Graph
        num_edges = snap.CntUniqBiDirEdges(self.DirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Unidrected Graph
        num_edges = snap.CntUniqBiDirEdges(self.UnDirGraphFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

        # Network
        num_edges = snap.CntUniqBiDirEdges(self.NetFull)
        self.assertEqual(self.num_nodes * (self.num_nodes - 1)/2, num_edges)

    def test_CntSelfEdges(self):
        # Directed Graph
        num_edges = snap.CntSelfEdges(self.DirGraphFull)
        self.assertEqual(0, num_edges)

        # Undirected Graph
        num_edges = snap.CntSelfEdges(self.UnDirGraphFull)
        self.assertEqual(0, num_edges)

        # Network
        num_edges = snap.CntSelfEdges(self.NetFull)
        self.assertEqual(0, num_edges)

    def test_GetUnDir(self):
        # Directed Graph
        New_Graph = snap.GetUnDir(self.DirGraphStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Undirected Graph
        New_Graph = snap.GetUnDir(self.UnDirGraphStar)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Network
        New_Graph = snap.GetUnDir(self.NetStar)
        for node in self.NetStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

    def test_MakeUnDir(self):
        # Directed Graph
        New_Graph = self.DirGraphStar
        snap.MakeUnDir(New_Graph)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Undirected Graph
        New_Graph = self.UnDirGraphStar
        snap.MakeUnDir(New_Graph)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

        # Network
        New_Graph = self.NetStar
        snap.MakeUnDir(New_Graph)
        for node in self.NetStar.Nodes():
            self.assertTrue(New_Graph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(New_Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(New_Graph.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))

    def test_AddSelfEdges(self):
        # Directed Graph
        Graph_Copy = self.DirGraphFull
        snap.AddSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertTrue(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

        # Undirected Graph
        Graph_Copy = self.UnDirGraphFull
        snap.AddSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertTrue(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

        # Network
        Graph_Copy = self.NetFull
        snap.AddSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertTrue(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

    def test_DelSelfEdges(self):
        # Directed Graph
        Graph_Copy = self.DirGraphSelfEdge
        snap.DelSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertFalse(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

        # Undirected Graph
        Graph_Copy = self.UnDirGraphSelfEdge
        snap.DelSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertFalse(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

        # Network
        Graph_Copy = self.NetSelfEdge
        snap.DelSelfEdges(Graph_Copy)
        for node in Graph_Copy.Nodes():
            self.assertFalse(Graph_Copy.IsEdge(node.GetId(), node.GetId()))

    def test_DelNodes(self):
        # Directed Graph
        Graph_Copy = self.DirGraphFull
        DelNodes = snap.TIntV()
        DelNodes.Add(0)
        snap.DelNodes(Graph_Copy, DelNodes)
        for node in DelNodes:
            self.assertFalse(Graph_Copy.IsNode(node))

        # Undirected Graph
        Graph_Copy = self.UnDirGraphFull
        DelNodes = snap.TIntV()
        DelNodes.Add(0)
        snap.DelNodes(Graph_Copy, DelNodes)
        for node in DelNodes:
            self.assertFalse(Graph_Copy.IsNode(node))

        # Network
        Graph_Copy = self.NetFull
        DelNodes = snap.TIntV()
        DelNodes.Add(0)
        snap.DelNodes(Graph_Copy, DelNodes)
        for node in DelNodes:
            self.assertFalse(Graph_Copy.IsNode(node))

    def test_DelZeroDegNodes(self):
        # Directed Graph
        snap.DelZeroDegNodes(self.DirGraphZeroDegree)
        for NI in self.DirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Undirected Graph
        snap.DelZeroDegNodes(self.UnDirGraphZeroDegree)
        for NI in self.UnDirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Network
        snap.DelZeroDegNodes(self.NetZeroDegree)
        for NI in self.NetZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

    def test_DelDegKNodes(self):
        # Directed Graph
        snap.DelDegKNodes(self.DirGraphZeroDegree, 0, 0)
        for NI in self.DirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Undirected Graph
        snap.DelDegKNodes(self.UnDirGraphZeroDegree, 0, 0)
        for NI in self.UnDirGraphZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

        # Network
        snap.DelDegKNodes(self.NetZeroDegree, 0, 0)
        for NI in self.NetZeroDegree.Nodes():
            self.assertNotEqual(0, NI.GetOutDeg() + NI.GetInDeg())

    def test_IsTree(self):
        # Directed Graph
        expected_results = [True, 0]
        results = snap.IsTree(self.DirTree)
        self.assertEqual(expected_results, results)

        # Network
        expected_results = [True, 0]
        results = snap.IsTree(self.NetTree)
        self.assertEqual(expected_results, results)

    def test_GetTreeRootNId(self):
        # Directed Graph
        root_id = snap.GetTreeRootNId(self.DirTree)
        self.assertEqual(0, root_id)

        # Network
        root_id = snap.GetTreeRootNId(self.NetTree)
        self.assertEqual(0, root_id)

    def test_GetBfsTree(self):
        start_node = 0
        follow_out = True
        follow_in = False

        # Directed Graph
        BfsTree = snap.GetBfsTree(self.DirGraphFull, start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

        # Undirected Graph
        BfsTree = snap.GetBfsTree(self.UnDirGraphFull, start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

        # Network
        BfsTree = snap.GetBfsTree(self.NetFull, start_node, follow_out, follow_in)
        self.assertEqual(self.num_nodes - 1, BfsTree.GetEdges())
        for end_node in range(1, self.num_nodes-1):
            self.assertTrue(BfsTree.IsEdge(start_node, end_node))

    def test_GetSubTreeSz(self):
        # Directed Graph
        results = snap.GetSubTreeSz(self.DirTree, 0, True, True)
        exp_results = [40, 40, 3]
        self.assertEqual(exp_results, results)

        # Undirected Graph
        results = snap.GetSubTreeSz(self.UnDirTree, 0, True, True)
        exp_results = [40, 40, 3]
        self.assertEqual(exp_results, results)

        # Network
        results = snap.GetSubTreeSz(self.NetTree, 0, True, True)
        exp_results = [40, 40, 3]
        self.assertEqual(exp_results, results)

    def test_GetNodesAtHop(self):
        # Directed Graph
        NodeVec = snap.TIntV()
        num_nodes = snap.GetNodesAtHop(self.DirGraphStar, 0, 1, NodeVec, True)
        self.assertEqual(self.num_nodes-1, num_nodes)

        # Undirected Graph
        NodeVec = snap.TIntV()
        num_nodes = snap.GetNodesAtHop(self.UnDirGraphStar, 0, 1, NodeVec, False)
        self.assertEqual(self.num_nodes-1, num_nodes)

        # Network
        NodeVec = snap.TIntV()
        num_nodes = snap.GetNodesAtHop(self.NetStar, 0, 1, NodeVec, True)
        self.assertEqual(self.num_nodes-1, num_nodes)

    def test_GetNodesAtHops(self):
        # Directed Graph
        HopVec = snap.TIntPrV()
        num_hops = snap.GetNodesAtHops(self.DirGraphStar, 0, HopVec, True)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())

        # Undirected Graph
        HopVec = snap.TIntPrV()
        num_hops = snap.GetNodesAtHops(self.UnDirGraphStar, 0, HopVec, False)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())

        # Network
        HopVec = snap.TIntPrV()
        num_hops = snap.GetNodesAtHops(self.NetStar, 0, HopVec, True)
        self.assertEqual(2, num_hops)
        for pair in HopVec:
            if pair.Val1() == 0:
                self.assertEqual(1, pair.Val2())
            else:
                self.assertEqual(1, pair.Val1())
                self.assertEqual(self.num_nodes-1, pair.Val2())

    def test_GetDegreeCentr(self):
        # Undirected Graph
        degree_center = snap.GetDegreeCentr(self.UnDirGraphStar, 0)
        self.assertEqual(1, degree_center)

    def test_GetFarnessCentr(self):
        # Undirected Graph
        farness_center = snap.GetFarnessCentr(self.UnDirGraphStar, 0)
        self.assertEqual(1, farness_center)

        # Directed Graph
        farness_center = snap.GetFarnessCentr(self.DirGraphStar, 0)
        self.assertEqual(1, farness_center)

        # Network
        farness_center = snap.GetFarnessCentr(self.NetStar, 0)
        self.assertEqual(1, farness_center)

    def test_GetClosenessCentr(self):
        # Undirected Graph
        closeness_center = snap.GetClosenessCentr(self.UnDirGraphStar, 0)
        self.assertEqual(1, closeness_center)

        # Directed Graph
        closeness_center = snap.GetClosenessCentr(self.DirGraphStar, 0)
        self.assertEqual(1, closeness_center)

        # Network
        closeness_center = snap.GetClosenessCentr(self.NetStar, 0)
        self.assertEqual(1, closeness_center)

    def test_GetEigenVectorCentr(self):
        # Undirected Graph
        EigenVec = snap.TIntFltH()
        snap.GetEigenVectorCentr(self.UnDirGraphStar, EigenVec)
        for item in EigenVec:
            self.assertTrue(0 < EigenVec[item])

    def test_GetNodeEcc(self):
        # Directed Graph
        node_ecc = snap.GetNodeEcc(self.DirGraphStar, 0, True)
        self.assertEqual(1, node_ecc)

        # Undirected Graph
        node_ecc = snap.GetNodeEcc(self.UnDirGraphStar, 0, False)
        self.assertEqual(1, node_ecc)

        # Network
        node_ecc = snap.GetNodeEcc(self.NetStar, 0, True)
        self.assertEqual(1, node_ecc)

    def test_GetHits(self):
        # Directed Graph
        NIdHubH = snap.TIntFltH()
        NIdAuthH = snap.TIntFltH()
        snap.GetHits(self.DirGraphFull, NIdHubH, NIdAuthH)
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

        # Undirected Graph
        NIdHubH = snap.TIntFltH()
        NIdAuthH = snap.TIntFltH()
        snap.GetHits(self.UnDirGraphFull, NIdHubH, NIdAuthH)
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

        # Network
        NIdHubH = snap.TIntFltH()
        NIdAuthH = snap.TIntFltH()
        snap.GetHits(self.NetFull, NIdHubH, NIdAuthH)
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, NIdHubH[item])
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, NIdAuthH[item])

    def test_CommunityGirvanNewman(self):
        Rnd = snap.TRnd(42)
        Graph = snap.GenPrefAttach(100, 10, Rnd)
        exp_val = 0.00963802805072646
        Vec = snap.TCnComV()
        act_val = snap.CommunityGirvanNewman(Graph, Vec)
        self.assertAlmostEqual(exp_val, act_val)

    def test_CommunityCNM(self):
        gnutellaUndir = snap.ConvertGraph(snap.PUNGraph, self.gnutella)
        Vcc = snap.TCnComV()
        modularity = snap.CommunityCNM(gnutellaUndir, Vcc)
        self.assertAlmostEqual(0.4647213330572384, modularity)

    def test_GetModularity(self):
        V = snap.TIntV()
        for i in range(5):
            V.Add(i)

        val = snap.GetModularity(self.DirGraphFull, V)
        self.assertAlmostEqual(0.04861111111111111, val)

        val = snap.GetModularity(self.UnDirGraphFull, V)
        self.assertAlmostEqual(-0.027777777777777776, val)

        val = snap.GetModularity(self.NetFull, V)
        self.assertAlmostEqual(0.04861111111111111, val)

    def test_GetEdgesInOut(self):
        V = snap.TIntV()
        V.Add(0)

        # Directed Graph
        result = snap.GetEdgesInOut(self.DirGraphFull, V)
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

        # Undirected Graph
        result = snap.GetEdgesInOut(self.UnDirGraphFull, V)
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

        # Network
        result = snap.GetEdgesInOut(self.NetFull, V)
        exp_results = [0, 9]
        self.assertEqual(exp_results, result)

    def test_GetBiConSzCnt(self):
        # Undirected Graph
        szCntV = snap.TIntPrV()
        snap.GetBiConSzCnt(self.UnDirGraphFull, szCntV)
        for item in szCntV:
            self.assertEqual(item.GetVal1(), self.num_nodes)
            self.assertEqual(item.GetVal2(), 1)

    def test_GetBiCon(self):
        # Undirected Graph
        CnComs = snap.TCnComV()
        snap.GetBiCon(self.UnDirGraphFull, CnComs)
        nodeId = 0
        for CnCom in CnComs:
            for node in CnCom:
              self.assertEqual(nodeId, node)
              nodeId += 1

    def test_GetEdgeBridges(self):
        # Undirected Graph
        edges = snap.TIntPrV()
        snap.GetEdgeBridges(self.UnDirGraphStar, edges)
        count = 0
        for edge in edges:
            self.assertEqual(0, edge.GetVal1())
            self.assertNotEqual(0, edge.GetVal2())
            count+=1
        self.assertEqual(9, count)

    def test_Get1CnCom(self):
        # Undirected Graph
        components = snap.TCnComV()
        snap.Get1CnCom(self.UnDirGraphStar, components)
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
        Graph = snap.GetMxBiCon(self.DirGraphFull)
        self.assertEqual(self.DirGraphFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.DirGraphFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(self.DirGraphFull), type(Graph))

        # Undirected Graph
        Graph = snap.GetMxBiCon(self.UnDirGraphFull)
        self.assertEqual(self.UnDirGraphFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.UnDirGraphFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(self.UnDirGraphFull), type(Graph))

        # Network
        Graph = snap.GetMxBiCon(self.NetFull)
        self.assertEqual(self.NetFull.GetNodes(), Graph.GetNodes())
        self.assertEqual(self.NetFull.GetEdges(), Graph.GetEdges())
        self.assertEqual(type(Graph), type(self.NetFull))

    def test_GetNodeWcc(self):
        # Directed Graph
        component = snap.TIntV()
        snap.GetNodeWcc(self.DirGraphStar, 1, component)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

        # Undirected Graph
        component = snap.TIntV()
        snap.GetNodeWcc(self.UnDirGraphStar, 1, component)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

        # Network
        component = snap.TIntV()
        snap.GetNodeWcc(self.NetStar, 1, component)
        sumNodes = 0
        for node in component:
            sumNodes += node
        self.assertEqual((self.num_nodes - 1) * self.num_nodes / 2, sumNodes)

    def test_isConnected(self):
        # Directed Graph
        self.assertTrue(snap.IsConnected(self.DirGraphStar))

        # Undirected Graph
        self.assertTrue(snap.IsConnected(self.UnDirGraphStar))

        # Network
        self.assertTrue(snap.IsConnected(self.NetStar))

    def test_isWeaklyConn(self):
        # Directed Graph
        self.assertTrue(snap.IsWeaklyConn(self.DirGraphStar))

        # Undirected Graph
        self.assertTrue(snap.IsWeaklyConn(self.UnDirGraphStar))

        # Network
        self.assertTrue(snap.IsWeaklyConn(self.NetStar))

    def test_GetWccSzCnt(self):
        # Directed Graph
        counts = snap.TIntPrV()
        snap.GetWccSzCnt(self.DirGraphStar, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Undirected Graph
        counts = snap.TIntPrV()
        snap.GetWccSzCnt(self.UnDirGraphStar, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Network
        counts = snap.TIntPrV()
        snap.GetWccSzCnt(self.NetStar, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

    def test_GetWccs(self):
        # Directed Graph
        components = snap.TCnComV()
        snap.GetWccs(self.DirGraphStar, components)
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Undirected Graph
        components = snap.TCnComV()
        snap.GetWccs(self.UnDirGraphStar, components)
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Network
        components = snap.TCnComV()
        snap.GetWccs(self.NetStar, components)
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
        counts = snap.TIntPrV()
        snap.GetSccSzCnt(self.DirGraphFull, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Undirected Graph
        counts = snap.TIntPrV()
        snap.GetSccSzCnt(self.UnDirGraphFull, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

        # Network
        counts = snap.TIntPrV()
        snap.GetSccSzCnt(self.NetFull, counts)
        for pair in counts:
            self.assertEqual(self.num_nodes, pair.GetVal1())
            self.assertEqual(1, pair.GetVal2())

    def test_GetSccs(self):
        # Directed Graph
        components = snap.TCnComV()
        snap.GetSccs(self.DirGraphFull, components)
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Undirected Graph
        components = snap.TCnComV()
        snap.GetSccs(self.UnDirGraphFull, components)
        num_comp = 0
        comp_size = 0
        for comp in components:
            num_comp += 1
            for node in comp:
                comp_size += 1
        self.assertEqual(1, num_comp)
        self.assertEqual(self.num_nodes, comp_size)

        # Network
        components = snap.TCnComV()
        snap.GetSccs(self.NetFull, components)
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
        sz = snap.GetMxWccSz(self.DirGraphStar)
        self.assertEqual(1, sz)

        # Undirected Graph
        sz = snap.GetMxWccSz(self.UnDirGraphStar)
        self.assertEqual(1, sz)

        # Network
        sz = snap.GetMxWccSz(self.NetStar)
        self.assertEqual(1, sz)

    def test_GetMxSccSz(self):
        # Directed Graph
        sz = snap.GetMxSccSz(self.DirGraphStar)
        self.assertEqual(1.0/self.num_nodes, sz)

        # Undirected Graph
        sz = snap.GetMxSccSz(self.UnDirGraphStar)
        self.assertEqual(1, sz)

        # Network
        sz = snap.GetMxSccSz(self.NetStar)
        self.assertEqual(1.0/self.num_nodes, sz)

    def test_GetMxWcc(self):
        # Directed Graph
        subgraph = snap.GetMxWcc(self.DirGraphStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = snap.GetMxWcc(self.UnDirGraphStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = snap.GetMxWcc(self.NetStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetMxScc(self):
        # Directed Graph
        subgraph = snap.GetMxScc(self.DirGraphFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = snap.GetMxScc(self.UnDirGraphFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = snap.GetMxScc(self.NetFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetMxBiCon(self):
        # Directed Graph
        subgraph = snap.GetMxBiCon(self.DirGraphFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Undirected Graph
        subgraph = snap.GetMxBiCon(self.UnDirGraphFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        subgraph = snap.GetMxBiCon(self.NetFull)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(subgraph.IsNode(node.GetId()))
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(subgraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_PrintInfo(self):
        snap.PrintInfo(self.DirGraphFull, "description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '90', '0', '0', '0', '10'])
        os.remove('test.txt')

        snap.PrintInfo(self.UnDirGraphFull, "description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '45', '0', '0', '0', '10'])
        os.remove('test.txt')

        snap.PrintInfo(self.NetFull, "description", "test.txt")
        self.checkPrintInfoOutput("test.txt", ["description", '10', '90', '0', '0', '0', '10'])
        os.remove('test.txt')

    def test_GetKCoreNodes(self):
        # Directed Graph
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreNodes(self.DirGraphStar, CoreN)
        self.assertEqual(2, result)

        # Undirected Graph
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreNodes(self.UnDirGraphStar, CoreN)
        self.assertEqual(2, result)

        # Network
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreNodes(self.NetStar, CoreN)
        self.assertEqual(2, result)

    def test_GetKCoreEdges(self):
        # Directed Graph
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreEdges(self.DirGraphStar, CoreN)
        self.assertEqual(2, result)

        # Undirected Graph
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreEdges(self.UnDirGraphStar, CoreN)
        self.assertEqual(2, result)

        # Network
        CoreN = snap.TIntPrV()
        result = snap.GetKCoreEdges(self.NetStar, CoreN)
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
        SngValV = snap.TFltV()
        snap.GetSngVals(self.DirGraphFull, SngVals, SngValV)
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
        EigValV = snap.TFltV()
        snap.GetEigVals(Graph, NumEigVals, EigValV)
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
        EigValIprV = snap.TFltPrV()
        snap.GetInvParticipRat(Graph, 10, 1000, EigValIprV)
        count = 0
        for x in EigValIprV:
            self.assertAlmostEqual(expected[count][0], x.GetVal1(), 5)
            self.assertAlmostEqual(expected[count][1], x.GetVal2(), 5)
            count += 1

    def test_GetKCore(self):
        # Directed Graph
        k = self.num_nodes - 1
        KCore = snap.GetKCore(self.DirGraphFull, k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

        # Undirected Graph
        k = self.num_nodes - 1
        KCore = snap.GetKCore(self.UnDirGraphFull, k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

        # Network
        k = self.num_nodes - 1
        KCore = snap.GetKCore(self.NetFull, k)
        self.assertEqual(self.num_nodes, KCore.GetNodes())

    def test_PlotEigValRank(self):
        Graph = snap.GenStar(snap.PUNGraph, 20)
        NumEigVals = 2
        fname = 'test'
        desc = 'test'
        plt = 'eigVal.' + fname + '.plt'
        png = 'eigVal.' + fname + '.png'
        tab = 'eigVal.' + fname + '.tab'
        snap.PlotEigValRank(Graph, NumEigVals, fname, desc)

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
        snap.PlotEigValDistr(Graph, NumEigVals, fname, desc)

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
        snap.PlotInvParticipRat(Graph, NumEigVals, TimeLimit, fname, desc)

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
        snap.PlotSngValRank(Graph, SngVals, fname, desc)

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
        snap.PlotSngValDistr(Graph, SngVals, fname, desc)

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
        snap.PlotInDegDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '7f08086973d30d356eaa2e695e1a6fff')
        os.remove(plt)
        #self.checkPlotHash(png, '3a7a729d393a0ba37d455c67dacd8510')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotInDegDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '9469cef95ca7701898d9da53fd83d3cf')
        os.remove(plt)
        #self.checkPlotHash(png, '3a7a729d393a0ba37d455c67dacd8510')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotInDegDistr(Graph, fname, desc)

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
        snap.PlotOutDegDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '893e4d32769a7235bade506f4558559a')
        os.remove(plt)
        #self.checkPlotHash(png, '03a7e7d530235143bf3a0ad09df30d5d')
        os.remove(png)
        self.checkPlotHash(tab, 'b3fd1f8e8d03274bc4c6b7d63dda8ac6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotOutDegDistr(Graph, fname, desc)

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
        snap.PlotWccDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '376654f801519f5a89519c020cd0cecf')
        os.remove(plt)
        #self.checkPlotHash(png, '3092ffd346709cbb0fb1210e39314c4c')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotWccDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '25f0e2f9efd05b483bd3498de485b525')
        os.remove(plt)
        #self.checkPlotHash(png, '3092ffd346709cbb0fb1210e39314c4c')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotWccDistr(Graph, fname, desc)

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
        snap.PlotSccDistr(Graph, fname, desc)

        self.checkPlotHash(plt, 'f92d2c3b97156ff049ce64aaeada099c')
        os.remove(plt)
        #self.checkPlotHash(png, '91fb4493d7a2e9fef7fc998607a94649')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotSccDistr(Graph, fname, desc)

        self.checkPlotHash(plt, '09bc574ab814ec9bd0fc5865529f513b')
        os.remove(plt)
        #self.checkPlotHash(png, '91fb4493d7a2e9fef7fc998607a94649')
        os.remove(png)
        self.checkPlotHash(tab, 'ead5104c0c23279add2652356fe836e4')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotSccDistr(Graph, fname, desc)

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
        snap.PlotClustCf(Graph, fname, desc)

        self.checkPlotHash(plt, 'd3e9c7ce6e1c5792a663bd0ee1abeb04')
        os.remove(plt)
        #self.checkPlotHash(png, '634a0518b0ee9db6c712ade205e089a2')
        os.remove(png)
        self.checkPlotHash(tab, '5e08cd594354ee12d733c98ffbb888c4')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotClustCf(Graph, fname, desc)

        self.checkPlotHash(plt, 'f2d1d9456515a92700e922d213a82084')
        os.remove(plt)
        #self.checkPlotHash(png, '634a0518b0ee9db6c712ade205e089a2')
        os.remove(png)
        self.checkPlotHash(tab, '0350d2154b877f0ae9415ea4d7e07f07')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotClustCf(Graph, fname, desc)

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
        snap.PlotHops(Graph, fname, desc, isDir, NApprox)

        self.assertTrue(os.path.isfile(plt))
        os.remove(plt)
        #self.checkPlotHash(png, '7558cfcb4b34e02fdda090fe2ebdeb03')
        os.remove(png)
        self.assertTrue(os.path.isfile(tab))
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        isDir = False
        snap.PlotHops(Graph, fname, desc, isDir, NApprox)

        self.assertTrue(os.path.isfile(plt))
        os.remove(plt)
        #self.checkPlotHash(png, '7558cfcb4b34e02fdda090fe2ebdeb03')
        os.remove(png)
        self.assertTrue(os.path.isfile(tab))
        os.remove(tab)

        # Network
        Graph = self.NetFull
        isDir = True
        snap.PlotHops(Graph, fname, desc, isDir, NApprox)

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
        snap.PlotShortPathDistr(Graph, fname, desc)

        self.checkPlotHash(plt, 'dbd3b8f4b0c82637c204173997625600')
        os.remove(plt)
        #self.checkPlotHash(png, 'ceaaab603196866102afa52042d33b15')
        os.remove(png)
        self.checkPlotHash(tab, '9b31a3d74e08ba09fb560dd2cfbf8e59')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotShortPathDistr(Graph, fname, desc)

        self.checkPlotHash(plt, 'b0e6ad4b3419c43ec4f4bac9ab9d74c7')
        os.remove(plt)
        #self.checkPlotHash(png, 'ceaaab603196866102afa52042d33b15')
        os.remove(png)
        self.checkPlotHash(tab, '9b31a3d74e08ba09fb560dd2cfbf8e59')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotShortPathDistr(Graph, fname, desc)

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
        snap.PlotKCoreNodes(Graph, fname, desc)

        self.checkPlotHash(plt, '8b47f5a7082e940e5b1a49f7a19bac1a')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4ffb2358ff82930b8832cbe1d5d3ecd')
        os.remove(png)
        self.checkPlotHash(tab, '1b1750d5304a4f2fbb19ab8919be8e27')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotKCoreNodes(Graph, fname, desc)

        self.checkPlotHash(plt, 'fd660ab9df8f84231ca61e6ad74b5a9f')
        os.remove(plt)
        #self.checkPlotHash(png, 'c4ffb2358ff82930b8832cbe1d5d3ecd')
        os.remove(png)
        self.checkPlotHash(tab, '6a1db7740949f594b7cc3917ec65f4d9')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotKCoreNodes(Graph, fname, desc)

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
        snap.PlotKCoreEdges(Graph, fname, desc)

        self.checkPlotHash(plt, 'b2bcd1cbfadfa7280727163c0fc85854')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '7c22771f72c0bbe0c5ac5fa7c97928eb')
        os.remove(tab)

        # Undirected Graph
        Graph = self.UnDirGraphFull
        snap.PlotKCoreEdges(Graph, fname, desc)

        self.checkPlotHash(plt, 'ce0a125f61e5e00e58c639afa434b012')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '13f4612f2cec666a421b39d18ae7afb6')
        os.remove(tab)

        # Network
        Graph = self.NetFull
        snap.PlotKCoreEdges(Graph, fname, desc)

        self.checkPlotHash(plt, 'b2bcd1cbfadfa7280727163c0fc85854')
        os.remove(plt)
        #self.checkPlotHash(png, '6fab2c397c5b4ab0b740d4a5adf4171a')
        os.remove(png)
        self.checkPlotHash(tab, '7c22771f72c0bbe0c5ac5fa7c97928eb')
        os.remove(tab)

    def test_GetESubGraph(self):
        EIdV = snap.TIntV()
        for edge in self.NetStar.Edges():
            EIdV.Add(edge.GetId())
        ESubGraph = snap.GetESubGraph(self.NetStar, EIdV)
        for node in self.NetStar.Nodes():
            self.assertTrue(ESubGraph.IsNode(node.GetId()))
        for edge in self.NetStar.Edges():
            self.assertTrue(ESubGraph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_ConvertGraph(self):
        # Directed to Undirected
        UnDirStar = snap.ConvertGraph(snap.PUNGraph, self.DirGraphStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Directed to Network
        NetStar = snap.ConvertGraph(snap.PNEANet, self.DirGraphStar)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(NetStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Undirected to Directed
        DirStar = snap.ConvertGraph(snap.PNGraph, self.UnDirGraphStar)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(DirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(DirStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Undirected to Network
        NetStar = snap.ConvertGraph(snap.PNEANet, self.UnDirGraphStar)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(NetStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(NetStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Network to Undirected
        UnDirStar = snap.ConvertGraph(snap.PUNGraph, self.NetStar)
        for node in self.NetStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.NetStar.GetEdges())

        # Network to Directed
        DirStar = snap.ConvertGraph(snap.PNGraph, self.NetStar)
        for node in self.NetStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(DirStar.GetEdges(), self.NetStar.GetEdges())

    def test_ConvertSubGraph(self):
        ListNodes = snap.TIntV()
        for x in range(self.num_nodes):
            ListNodes.Add(x)

        # Directed to Undirected
        UnDirStar = snap.ConvertSubGraph(snap.PUNGraph, self.DirGraphStar, ListNodes)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Directed to Network
        NetStar = snap.ConvertSubGraph(snap.PNEANet, self.DirGraphStar, ListNodes)
        for node in self.DirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.DirGraphStar.GetNodes())
        for edge in self.DirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
        self.assertEqual(NetStar.GetEdges(), self.DirGraphStar.GetEdges())

        # Undirected to Directed
        DirStar = snap.ConvertSubGraph(snap.PNGraph, self.UnDirGraphStar, ListNodes)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(DirStar.IsNode(node.GetId()))
        self.assertEqual(DirStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(DirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(DirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(DirStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Undirected to Network
        NetStar = snap.ConvertSubGraph(snap.PNEANet, self.UnDirGraphStar, ListNodes)
        for node in self.UnDirGraphStar.Nodes():
            self.assertTrue(NetStar.IsNode(node.GetId()))
        self.assertEqual(NetStar.GetNodes(), self.UnDirGraphStar.GetNodes())
        for edge in self.UnDirGraphStar.Edges():
            self.assertTrue(NetStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(NetStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(NetStar.GetEdges(), self.UnDirGraphStar.GetEdges()*2)

        # Network to Undirected
        UnDirStar = snap.ConvertSubGraph(snap.PUNGraph, self.NetStar, ListNodes)
        for node in self.NetStar.Nodes():
            self.assertTrue(UnDirStar.IsNode(node.GetId()))
        self.assertEqual(UnDirStar.GetNodes(), self.NetStar.GetNodes())
        for edge in self.NetStar.Edges():
            self.assertTrue(UnDirStar.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(UnDirStar.IsEdge(edge.GetDstNId(), edge.GetSrcNId()))
        self.assertEqual(UnDirStar.GetEdges(), self.NetStar.GetEdges())

        # Network to Directed
        DirStar = snap.ConvertSubGraph(snap.PNGraph, self.NetStar, ListNodes)
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
        subGraph = snap.GetRndSubGraph(Graph, exp_nodes)
        self.assertEqual(exp_nodes, subGraph.GetNodes())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(Graph.IsNode(edge.GetSrcNId()))
            self.assertTrue(Graph.IsNode(edge.GetDstNId()))

        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
        subGraph = snap.GetRndSubGraph(Graph, exp_nodes)
        self.assertEqual(exp_nodes, subGraph.GetNodes())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))
            self.assertTrue(Graph.IsNode(edge.GetSrcNId()))
            self.assertTrue(Graph.IsNode(edge.GetDstNId()))

        # Directed Graph
        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        subGraph = snap.GetRndSubGraph(Graph, exp_nodes)
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
        subGraph = snap.GetRndESubGraph(Graph, exp_edges)
        self.assertEqual(exp_edges, subGraph.GetEdges())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
            self.assertTrue(node.GetInDeg() + node.GetOutDeg() > 0)
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

        # Network
        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
        subGraph = snap.GetRndESubGraph(Graph, exp_edges)
        self.assertEqual(exp_edges, subGraph.GetEdges())
        for node in subGraph.Nodes():
            self.assertTrue(Graph.IsNode(node.GetId()))
            self.assertTrue(node.GetInDeg() + node.GetOutDeg() > 0)
        for edge in subGraph.Edges():
            self.assertTrue(Graph.IsEdge(edge.GetSrcNId(), edge.GetDstNId()))

    def test_GetTriadEdges(self):
        # Directed Graph
        exp_triad_edges = self.DirGraphFull.GetEdges()
        act_triad_edges = snap.GetTriadEdges(self.DirGraphFull)
        self.assertEqual(exp_triad_edges, act_triad_edges)

        # Unirected Graph
        exp_triad_edges = self.UnDirGraphFull.GetEdges()
        act_triad_edges = snap.GetTriadEdges(self.UnDirGraphFull)
        self.assertEqual(exp_triad_edges, act_triad_edges)

        # Network
        exp_triad_edges = self.NetFull.GetEdges()
        act_triad_edges = snap.GetTriadEdges(self.NetFull)
        self.assertEqual(exp_triad_edges, act_triad_edges)

    def test_GetTriadParticip(self):
        f = math.factorial
        exp_num_tri = f(self.num_nodes-1)/f(2)/f(self.num_nodes-3)

        # Directed Graph
        TriadCntV = snap.TIntPrV()
        snap.GetTriadParticip(self.DirGraphFull, TriadCntV)
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

        # Undirected Graph
        TriadCntV = snap.TIntPrV()
        snap.GetTriadParticip(self.UnDirGraphFull, TriadCntV)
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

        # Network
        TriadCntV = snap.TIntPrV()
        snap.GetTriadParticip(self.NetFull, TriadCntV)
        for pair in TriadCntV:
            self.assertEqual(exp_num_tri, pair.Val1())
            self.assertEqual(self.num_nodes, pair.Val2)

    def test_CntEdgesToSet(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        TS = snap.TIntSet()
        val = snap.CntEdgesToSet(G, 0, TS)
        self.assertEqual(0, val)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        TS = snap.TIntSet()
        val = snap.CntEdgesToSet(G, 0, TS)
        self.assertEqual(0, val)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        TS = snap.TIntSet()
        val = snap.CntEdgesToSet(G, 0, TS)
        self.assertEqual(0, val)

    def test_GetDegSeqV(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        V = snap.TIntV()
        snap.GetDegSeqV(G, V)
        for i in V:
            self.assertEqual(18, i)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        V = snap.TIntV()
        snap.GetDegSeqV(G, V)
        for i in V:
            self.assertEqual(9, i)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        V = snap.TIntV()
        snap.GetDegSeqV(G, V)
        for i in V:
            self.assertEqual(18, i)

    def test_GetDegSeqV2(self):
        # Directed Graph
        G = snap.GenFull(snap.PNGraph, 10)
        V = snap.TIntV()
        V2 = snap.TIntV()
        snap.GetDegSeqV(G, V, V2)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

        # Undirected Graph
        G = snap.GenFull(snap.PUNGraph, 10)
        V = snap.TIntV()
        V2 = snap.TIntV()
        snap.GetDegSeqV(G, V, V2)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

        # Network
        G = snap.GenFull(snap.PNEANet, 10)
        V = snap.TIntV()
        V2 = snap.TIntV()
        snap.GetDegSeqV(G, V, V2)
        for i in V:
            self.assertEqual(9, i)
        for i in V2:
            self.assertEqual(9, i)

    def test_GetAnf(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SrcNId = 0
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, SrcNId, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

    def test_GetAnf2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        DistNbrsV = snap.TIntFltKdV()
        snap.GetAnf(Graph, DistNbrsV, 3, False, 8192)
        self.assertEqual(3, DistNbrsV.Len())

    def test_GetAnfEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertTrue(result >= 0)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertTrue(result >= 0)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetAnfEffDiam(Graph, True, 0.9, 1024)
        self.assertTrue(result >= 0)

    def test_GetAnfEffDiam2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetAnfEffDiam(Graph)
        self.assertTrue(result >= 0)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetAnfEffDiam(Graph)
        self.assertTrue(result >= 0)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetAnfEffDiam(Graph)
        self.assertTrue(result >= 0)

    def test_GetShortPath(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetShortPath(Graph, 0, 1)
        self.assertEqual(1, result)

    def test_GetShortPath2(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        H = snap.TIntH()
        result = snap.GetShortPath(Graph, 0, H)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        H = snap.TIntH()
        result = snap.GetShortPath(Graph, 0, H)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        H = snap.TIntH()
        result = snap.GetShortPath(Graph, 0, H)
        self.assertEqual(1, result)

    def test_GetBfsFullDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(1, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(1, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetBfsFullDiam(Graph, 10)
        self.assertEqual(1, result)

    def test_GetBfsEffDiam(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetBfsEffDiam(Graph, 10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetBfsEffDiam(Graph, 10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetBfsEffDiam(Graph, 10)
        self.assertAlmostEqual(0.88888888888888888888, result)

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = snap.GetBfsEffDiam(Graph, Num, List, True)
        self.assertEqual(expected_result, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = snap.GetBfsEffDiam(Graph, Num, List, False)
        self.assertEqual(expected_result, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
        expected_result = [0.88, 0.88, 1]
        result = snap.GetBfsEffDiam(Graph, Num, List, True)
        self.assertEqual(expected_result, result)

    def test_GetBfsEffDiamAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        Num = 50
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = snap.GetBfsEffDiamAll(Graph, Num, True)
        self.assertEqual(expected_result, result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        Num = 75
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = snap.GetBfsEffDiamAll(Graph, Num, False)
        self.assertEqual(expected_result, result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        Num = 33
        expected_result = [0.89898989898989901,
                            0.89898989898989901, 1, 0.98999999999999999]
        result = snap.GetBfsEffDiamAll(Graph, Num, True)
        self.assertEqual(expected_result, result)

    def test_GetBetweennessCentr(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        Nodes = snap.TIntFltH()
        Edges = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        Nodes = snap.TIntFltH()
        Edges = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        Nodes = snap.TIntFltH()
        Edges = snap.TIntPrFltH()
        snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
        for node in Nodes:
            self.assertAlmostEqual(0, Nodes[node])
        for edge in Edges:
            self.assertAlmostEqual(2, Edges[edge])

    def test_GetArtPoints(self):
        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        V = snap.TIntV()
        snap.GetArtPoints(Graph, V)
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
        result = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, 8)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, 8)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetCmnNbrs(Graph, 0, 1)
        self.assertEqual(result, 8)

    def test_GetCmnNbrs1(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        V = snap.TIntV()
        result = snap.GetCmnNbrs(Graph, 0, 1, V)
        self.assertEqual(result, 8)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        V = snap.TIntV()
        result = snap.GetCmnNbrs(Graph, 0, 1, V)
        self.assertEqual(result, 8)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        V = snap.TIntV()
        result = snap.GetCmnNbrs(Graph, 0, 1, V)
        self.assertEqual(result, 8)

    def test_GetNodeTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, 36)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, 36)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetNodeTriads(Graph, 0)
        self.assertEqual(result, 36)

    def test_GetNodeTriadsSet(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSet = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet.AddKey(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = snap.GetNodeTriads(Graph, NId, GroupSet)
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSet = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet.AddKey(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = snap.GetNodeTriads(Graph, NId, GroupSet)
        self.assertEqual(result, expected_result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        for NI in Graph.Nodes():
            break
        NId = NI.GetId()
        GroupSet = snap.TIntSet()
        for NbrIdx in range(4):
            GroupSet.AddKey(NI.GetOutNId(NbrIdx))
        expected_result = [6, 6, 380, 4465]
        result = snap.GetNodeTriads(Graph, NId, GroupSet)
        self.assertEqual(result, expected_result)

    def test_GetNodeTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        expected_result = [4851, 4851, 0]
        result = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        expected_result = [4851, 4851, 0]
        result = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, expected_result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        expected_result = [4851, 4851, 0]
        result = snap.GetNodeTriadsAll(Graph, 10)
        self.assertEqual(result, expected_result)

    def test_GetTriads(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        result = snap.GetTriads(Graph)
        self.assertEqual(result, 120)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        result = snap.GetTriads(Graph)
        self.assertEqual(result, 120)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        result = snap.GetTriads(Graph)
        self.assertEqual(result, 120)

    def test_GetTriadsAll(self):
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 100)
        expected_result = [161700, 161700, 0]
        result = snap.GetTriadsAll(Graph)
        self.assertEqual(result, expected_result)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 100)
        expected_result = [161700, 161700, 0]
        result = snap.GetTriadsAll(Graph)
        self.assertEqual(result, expected_result)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 100)
        expected_result = [161700, 161700, 0]
        result = snap.GetTriadsAll(Graph)
        self.assertEqual(result, expected_result)

    def test_GetClustCf(self):

        # testing GetClustCf(Graph, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        result = snap.GetClustCf(DirGraph)
        self.assertAlmostEqual(result, 1.0)

        # Undirected Graph
        result = snap.GetClustCf(UnGraph)
        self.assertAlmostEqual(result, 1.0)

        # Network
        result = snap.GetClustCf(MultiGraph)
        self.assertAlmostEqual(result, 1.0)

        # parameter = 0

        result = snap.GetClustCf(DirGraph, 0)
        self.assertAlmostEqual(result, 0.0)

        result = snap.GetClustCf(UnGraph, 0)
        self.assertAlmostEqual(result, 0.0)

        result = snap.GetClustCf(MultiGraph, 0)
        self.assertAlmostEqual(result, 0.0)

        # parameter > 0

        result = snap.GetClustCf(DirGraph, 3)
        self.assertAlmostEqual(result, 1.0)

        result = snap.GetClustCf(UnGraph, 3)
        self.assertAlmostEqual(result, 1.0)

        result = snap.GetClustCf(MultiGraph, 3)
        self.assertAlmostEqual(result, 1.0)

    def test_GetClustCf2(self):

        # testing GetClustCf(Graph, DegToCCfV, SampleNodes=-1)

        DirGraph = snap.GenFull(snap.PNGraph, 10)
        UnGraph = snap.GenFull(snap.PUNGraph, 10)
        MultiGraph = snap.GenFull(snap.PNEANet, 10)

        # no parameters

        # Directed Graph
        V = snap.TFltPrV()
        result = snap.GetClustCf(DirGraph, V)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # Undirected Graph
        V = snap.TFltPrV()
        result = snap.GetClustCf(UnGraph, V)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # Network
        V = snap.TFltPrV()
        result = snap.GetClustCf(MultiGraph, V)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        # parameter = 0

        V = snap.TFltPrV()
        result = snap.GetClustCf(DirGraph, V, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        V = snap.TFltPrV()
        result = snap.GetClustCf(UnGraph, V, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        V = snap.TFltPrV()
        result = snap.GetClustCf(MultiGraph, V, 0)
        self.assertAlmostEqual(result, 0.0)
        self.assertEqual(V.Len(), 0)

        # parameter > 0

        V = snap.TFltPrV()
        result = snap.GetClustCf(DirGraph, V, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        V = snap.TFltPrV()
        result = snap.GetClustCf(UnGraph, V, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

        V = snap.TFltPrV()
        result = snap.GetClustCf(MultiGraph, V, 3)
        self.assertAlmostEqual(result, 1.0)
        self.assertEqual(V.Len(), 1)

    def test_GetClustCfAll(self):

        DirGraph = snap.GenFull(snap.PNGraph, 100)
        UnGraph = snap.GenFull(snap.PUNGraph, 100)
        MultiGraph = snap.GenFull(snap.PNEANet, 100)

        # no parameter

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(DirGraph, V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(UnGraph, V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(MultiGraph, V)
        expected_result = [1.0, 161700, 0]
        self.assertEqual(result, expected_result)

        # parameter = 0

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(DirGraph, V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(UnGraph, V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(MultiGraph, V, 0)
        expected_result = [0.0, 0, 0]
        self.assertEqual(result, expected_result)

        # parameter > 0

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(DirGraph, V, 5)
        expected_result = [1.0, 8085, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(UnGraph, V, 5)
        expected_result = [1.0, 8085, 0]
        self.assertEqual(result, expected_result)

        V = snap.TFltPrV()
        result = snap.GetClustCfAll(MultiGraph, V, 5)
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
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SaveGViz(self.DirGraphFull, fname, "text", True, NIdColorH)
        exp_hash = '64fe626fa482a0d45416824dc02d73a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SaveGViz(self.UnDirGraphFull, fname, "text", True, NIdColorH)
        exp_hash = 'd2185ec44f908e8d10da6c6319c900a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdColorH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdColorH[i] = "red"
        snap.SaveGViz(self.NetFull, fname, "text", True, NIdColorH)
        exp_hash = '64fe626fa482a0d45416824dc02d73a5'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

    def test_SaveGViz2(self):
        # Directed Graph
        fname = "mygraph.dot"
        NIdLabelH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdLabelH[i] = str(i)
        snap.SaveGViz(self.DirGraphFull, fname, "text", NIdLabelH)
        exp_hash = '260c9cfe1b5eac55a053ffcf418703e1'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Undirected Graph
        NIdLabelH = snap.TIntStrH()
        for i in range(self.num_nodes):
            NIdLabelH[i] = str(i)
        snap.SaveGViz(self.UnDirGraphFull, fname, "text", NIdLabelH)
        exp_hash = 'df04d8deed65d2a537a741e3ab3e251b'
        test_hash = self.getFileHash(fname)
        self.assertEqual(exp_hash, test_hash)
        os.remove(fname)

        # Directed Graph
        NIdLabelH = snap.TIntStrH()
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
        Graph = snap.LoadEdgeListStr(snap.PNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

        # Undirected Graph
        snap.SaveEdgeList(self.UnDirGraphFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeListStr(snap.PUNGraph, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes/2)
        os.remove(fname)

        # Directed Graph
        snap.SaveEdgeList(self.NetFull, fname)
        self.assertTrue(os.path.isfile(fname))
        Graph = snap.LoadEdgeListStr(snap.PNEANet, fname, 0, 1)
        self.assertEqual(Graph.GetNodes(), self.num_nodes)
        self.assertEqual(Graph.GetEdges(), (self.num_nodes-1)*self.num_nodes)
        os.remove(fname)

    def test_GetSngVec(self):
        # Directed Graph
        val = 0.316227766017
        Graph = snap.GenFull(snap.PNGraph, 10)
        LeftSV = snap.TFltV()
        RightSV = snap.TFltV()
        snap.GetSngVec(Graph, LeftSV, RightSV)
        for i in LeftSV:
            self.assertAlmostEqual(i, val)
        for i in RightSV:
            self.assertAlmostEqual(i, val)

        SngValV = snap.TFltV()
        LeftSVV = snap.TFltVFltV()
        RightSVV = snap.TFltVFltV()
        snap.GetSngVec(Graph, 5, SngValV, LeftSVV, RightSVV)
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

    def test_GetEigVec(self):
        # Undirected Graph
        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
        EigV = snap.TFltV()
        snap.GetEigVec(Graph, EigV)
        self.assertEqual(EigV.Len(), 100)

        EigVal = snap.TFltV()
        EigVV = snap.TFltVFltV()
        snap.GetEigVec(Graph, 10, EigVal, EigVV)
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
        V = snap.TIntV()
        for i in range(5):
            V.Add(i)
        # Directed Graph
        Graph = snap.GenFull(snap.PNGraph, 10)
        SubGraph = snap.GetSubGraph(Graph, V)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)

        SubGraph = snap.GetSubGraphRenumber(Graph, V)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)
        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Undirected Graph
        Graph = snap.GenFull(snap.PUNGraph, 10)
        SubGraph = snap.GetSubGraph(Graph, V)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4/2)

        SubGraph = snap.GetSubGraphRenumber(Graph, V)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4/2)
        # verify that NIds are in 0..N-1
        for NI in SubGraph.Nodes():
            self.assertEqual(NI.GetId() < SubGraph.GetNodes(), True)

        # Network
        Graph = snap.GenFull(snap.PNEANet, 10)
        SubGraph = snap.GetSubGraph(Graph, V)
        self.assertEqual(SubGraph.GetNodes(), 5)
        self.assertEqual(SubGraph.GetEdges(), 5 * 4)

    def test_GetNodeClustCf(self):
        # Directed Graph
        H = snap.TIntFltH()
        snap.GetNodeClustCf(self.DirGraphFull, H)
        for i in H:
            self.assertEqual(1.0, H[i])

        # Undirected Graph
        H = snap.TIntFltH()
        snap.GetNodeClustCf(self.UnDirGraphFull, H)
        for i in H:
            self.assertEqual(1.0, H[i])

        # Network
        H = snap.TIntFltH()
        snap.GetNodeClustCf(self.NetFull, H)
        for i in H:
            self.assertEqual(1.0, H[i])

    def test_ConvertESubGraph(self):
        V = snap.TIntV()
        for i in range(10):
            V.Add(i+1)
        # Directed Graph
        SubGraph = snap.ConvertESubGraph(snap.PNGraph, self.NetFull, V)
        self.assertEqual(SubGraph.GetEdges(), V.Len())

        # Undirected Graph
        SubGraph = snap.ConvertESubGraph(snap.PUNGraph, self.NetFull, V)
        self.assertEqual(SubGraph.GetEdges(), V.Len())

        # Network
        SubGraph = snap.ConvertESubGraph(snap.PNEANet, self.NetFull, V)
        self.assertEqual(SubGraph.GetEdges(), V.Len())

    def test_GetEgonet(self):

        # Undirected Graph
        for i in range(10):
            Egonet, edges = snap.GetEgonet(self.UPetersen, i)
            self.assertEqual(Egonet.GetNodes(), 4)
            self.assertEqual(Egonet.GetEdges(), 3)
            self.assertEqual(edges, 6)

        # Directed Graph
        for i in range(10):
            Egonet, ein, eout = snap.GetEgonet(self.DPetersen, i)
            self.assertEqual(Egonet.GetNodes(), 4)
            self.assertEqual(Egonet.GetEdges(), 3)
            if i < 5:
                self.assertEqual(ein, 2)
                self.assertEqual(eout, 4)
            else:
                self.assertEqual(ein, 4)
                self.assertEqual(eout, 2)

    def test_GetEgonetHop(self):

        # Undirected Graph
        for i in range(1,3):
            Egonet = snap.GetEgonetHop(self.UPetersen, 0, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 4)
                self.assertEqual(Egonet.GetEdges(), 3)
            else:
                self.assertEqual(Egonet.GetNodes(), 10)
                self.assertEqual(Egonet.GetEdges(), 15)

        # Directed Graph
        for i in range(1,3):
            Egonet = snap.GetEgonetHop(self.DPetersen, 1, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 4)
                self.assertEqual(Egonet.GetEdges(), 3)
            else:
                self.assertEqual(Egonet.GetNodes(), 10)
                self.assertEqual(Egonet.GetEdges(), 15)

        # Directed Network
        for i in range(1,3):
            Egonet = snap.GetEgonetHop(self.NPetersen, 2, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 4)
                self.assertEqual(Egonet.GetEdges(), 3)
            else:
                self.assertEqual(Egonet.GetNodes(), 10)
                self.assertEqual(Egonet.GetEdges(), 15)

    def test_GetInEgonetHop(self):

        # Undirected Graph
        for i in range(1,3):
            Egonet = snap.GetInEgonetHop(self.UPetersen, 3, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 4)
                self.assertEqual(Egonet.GetEdges(), 3)
            else:
                self.assertEqual(Egonet.GetNodes(), 10)
                self.assertEqual(Egonet.GetEdges(), 15)

        # Directed Graph
        for i in range(1,3):
            Egonet = snap.GetInEgonetHop(self.DPetersen, 4, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 2)
                self.assertEqual(Egonet.GetEdges(), 1)
            else:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)

        # Directed Network
        for i in range(1,3):
            Egonet = snap.GetInEgonetHop(self.NPetersen, 5, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)
            else:
                self.assertEqual(Egonet.GetNodes(), 6)
                self.assertEqual(Egonet.GetEdges(), 6)

    def test_GetOutEgonetHop(self):

        # Undirected Graph
        for i in range(1,3):
            Egonet = snap.GetOutEgonetHop(self.UPetersen, 6, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 4)
                self.assertEqual(Egonet.GetEdges(), 3)
            else:
                self.assertEqual(Egonet.GetNodes(), 10)
                self.assertEqual(Egonet.GetEdges(), 15)

        # Directed Graph
        for i in range(1,3):
            Egonet = snap.GetOutEgonetHop(self.DPetersen, 7, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 2)
                self.assertEqual(Egonet.GetEdges(), 1)
            else:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)

        # Directed Network
        for i in range(1,3):
            Egonet = snap.GetOutEgonetHop(self.NPetersen, 8, i)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 2)
                self.assertEqual(Egonet.GetEdges(), 1)
            else:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)

    def test_GetInEgonetSub(self):

        # Undirected Graph
        for i in range(1,3):
            Egonet = snap.GetInEgonetSub(self.UPetersen, 9, i, 2)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)
            else:
                self.assertEqual(Egonet.GetNodes(), 7)
                self.assertEqual(Egonet.GetEdges(), 8)

        # Directed Graph
        for i in range(1,3):
            Egonet = snap.GetInEgonetSub(self.DPetersen, 0, i, 2)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 2)
                self.assertEqual(Egonet.GetEdges(), 1)
            else:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)

        # Directed Network
        for i in range(1,3):
            Egonet = snap.GetInEgonetSub(self.NPetersen, 1, i, 2)
            if i == 1:
                self.assertEqual(Egonet.GetNodes(), 2)
                self.assertEqual(Egonet.GetEdges(), 1)
            else:
                self.assertEqual(Egonet.GetNodes(), 3)
                self.assertEqual(Egonet.GetEdges(), 2)

if __name__ == '__main__':
  unittest.main()

