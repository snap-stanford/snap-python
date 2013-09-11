import random
import unittest

import snap

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.nodes = 100
        self.edges = 1000

        # list graph types to test
        self.gtypes = [ snap.PUNGraph, snap.PNGraph, snap.PNEANet ]

    def test_graph(self):
        for gtype in self.gtypes:
            # create the graph
            G1 = snap.GenRndGnm(gtype, self.nodes, self.edges)
            self.ioproc(G1)

    def ioproc(self, G1):
        # save the graph in binary
        FOut = snap.TFOut("test.graph")
        G1.Save(FOut)
        FOut.Flush()

        # load the graph in binary
        FIn = snap.TFIn("test.graph")
        if type(G1) == snap.PUNGraph:
            G2 = snap.TUNGraph.Load(FIn)
        elif type(G1) == snap.PNGraph:
            G2 = snap.TNGraph.Load(FIn)
        elif type(G1) == snap.PNEANet:
            G2 = snap.TNEANet.Load(FIn)

        self.compare(G1, G2)

        # save the graph in text
        snap.SaveEdgeList(G2, "test.txt", "Save as tab-separated list of edges")

        # load the graph in text
        G3 = snap.LoadEdgeList(type(G1), "test.txt", 0, 1)

        self.compare(G1, G3)

    def compare(self, G1, G2):
        # test the number of nodes and edges
        self.assertEqual(G1.GetNodes(), G2.GetNodes())
        self.assertEqual(G1.GetEdges(), G2.GetEdges())

        # test the number nodes
        g1nodes = [ NI.GetId() for NI in G1.Nodes() ]
        g2nodes = [ NI.GetId() for NI in G2.Nodes() ]
        self.assertEqual(len(g1nodes), len(g2nodes))

        g1nodes.sort()
        g2nodes.sort()

        for p in zip(g1nodes, g2nodes):
            # test node ids
            self.assertEqual(p[0], p[1])

            # test out-neighbors
            NI1 = G1.GetNI(p[0])
            g1nbrs = [ e for e in NI1.GetOutEdges() ]
            NI2 = G2.GetNI(p[1])
            g2nbrs = [ e for e in NI2.GetOutEdges() ]

            g1nbrs.sort()
            g2nbrs.sort()

            for p1 in zip(g1nbrs, g2nbrs):
                self.assertEqual(p1[0], p1[1])

            # test in-neighbors
            NI1 = G1.GetNI(p[0])
            g1nbrs = [ e for e in NI1.GetInEdges() ]
            NI2 = G2.GetNI(p[1])
            g2nbrs = [ e for e in NI2.GetInEdges() ]

            g1nbrs.sort()
            g2nbrs.sort()

            for p1 in zip(g1nbrs, g2nbrs):
                self.assertEqual(p1[0], p1[1])

if __name__ == '__main__':
    unittest.main()

