import unittest

import snap

class SnapPythonTest(unittest.TestCase):

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

if __name__ == '__main__':
  unittest.main()
