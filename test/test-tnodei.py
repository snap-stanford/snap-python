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
            self.graph(G1)
            self.nodei(G1)

    def graph(self, G):
        # verify the number of nodes and edges
        self.assertEqual(self.nodes, G.GetNodes())
        self.assertEqual(self.edges, G.GetEdges())

        # test node iterator
        count = 0
        for NI in G.Nodes():
            count += 1
        self.assertEqual(self.nodes, count)

        # test edge iterator
        count = 0
        for EI in G.Edges():
            count += 1
        self.assertEqual(self.edges, count)

    def nodei(self, G):

        for NI in G.Nodes():
            # get out and in neighbors
            olist = [e for e in NI.GetOutEdges()]
            ilist = [e for e in NI.GetInEdges()]

            # test number of neighbors 
            self.assertEqual(NI.GetOutDeg(), len(olist))
            self.assertEqual(NI.GetInDeg(), len(ilist))

            # test neighbor access
            for i in xrange(0, NI.GetOutDeg()):
                self.assertEqual(olist[i], NI.GetOutNId(i))
            for i in xrange(0, NI.GetInDeg()):
                self.assertEqual(ilist[i], NI.GetInNId(i))

            # test neighbor validation
            for i in xrange(0,self.nodes):
                self.assertEqual(i in olist, NI.IsOutNId(i))
                self.assertEqual(i in ilist, NI.IsInNId(i))
                self.assertEqual((i in ilist) or (i in olist), NI.IsNbrNId(i))

if __name__ == '__main__':
    unittest.main()

