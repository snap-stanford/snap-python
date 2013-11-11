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

        # Undirected Graph
        expected_results = [False, -1]
        results = snap.IsTree(self.UnDirTree)
        self.assertEqual(expected_results, results)

        # Network
        expected_results = [True, 0]
        results = snap.IsTree(self.NetTree)
        self.assertEqual(expected_results, results)

    def test_GetTreeRootNId(self):
        # Directed Graph
        root_id = snap.GetTreeRootNId(self.DirTree)
        self.assertEqual(0, root_id)

        # Undirected Graph
        root_id = snap.GetTreeRootNId(self.UnDirTree)
        self.assertEqual(-1, root_id)

        # Network
        root_id = snap.GetTreeRootNId(self.NetTree)
        self.assertEqual(0, root_id)

    def test_GetBfsTree(self):
        # Directed Graph
        pass

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

    def test_GetEigenVectorCentr(self):
        # Undirected Graph
        EigenVec = snap.TIntFltH()
        snap.GetEigenVectorCentr(self.UnDirGraphStar, EigenVec)
        for item in EigenVec:
            self.assertTrue(0 < item.GetDat())

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
            self.assertEqual(value, item.GetDat())
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, item.GetDat())

        # Undirected Graph
        NIdHubH = snap.TIntFltH()
        NIdAuthH = snap.TIntFltH()
        snap.GetHits(self.UnDirGraphFull, NIdHubH, NIdAuthH)
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, item.GetDat())
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, item.GetDat())

        # Network
        NIdHubH = snap.TIntFltH()
        NIdAuthH = snap.TIntFltH()
        snap.GetHits(self.NetFull, NIdHubH, NIdAuthH)
        value = NIdHubH.GetDat(0)
        for item in NIdHubH:
            self.assertEqual(value, item.GetDat())
        value = NIdAuthH.GetDat(0)
        for item in NIdAuthH:
            self.assertEqual(value, item.GetDat())

    def test_GetBiConSzCnt(self):
        # Undirected Graph
        szCntV = snap.TIntPrV()
        snap.GetBiConSzCnt(self.UnDirGraphFull, szCntV)
        for item in szCntV:
            self.assertEqual(item.GetVal1(), self.num_nodes)
            self.assertEqual(item.GetVal2(), 1)

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

if __name__ == '__main__':
  unittest.main()
