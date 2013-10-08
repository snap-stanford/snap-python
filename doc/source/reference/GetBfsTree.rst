GetBfsTree
'''''''''''''''
.. note::

    This page is a draft and under revision.



Function Definition

.. function:: GetBfsTree:: PNGraph GetBfsTree(PGraph, startNodeId, followOut, followIn)

Returns a directed Breadth-First-Search tree rooted at startNodeId.
Links are such that parent points to its child.
Tree is created by following in-links
(parameter FollowIn = true) and/or out-links (parameter FollowOut = true).

Parameters

- PGraph
    Instance of graph.

- startNodeId
    Id of the root node of BST.

- followOut
    Boolean suggesting if the graph should be constructed by following the outward links.

- followIn
    Boolean suggesting if the graph should be constructed by following inward links.

References of Programming Constructs

class        :class:`snap.PGraph`

function     :func:`New`

test_using_directed_graph.py::

    import snap

    class BfsTreeDirectedGraphTest:
        def __init__(self):
            g = snap.PNGraph.New()
            for i in range(5):
                g.AddNode(i)
            g.AddEdge(0, 1)
            g.AddEdge(1, 2)
            g.AddEdge(1, 3)
            g.AddEdge(2, 4)
            self.g = g

        def createBfsFollowingOutLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, False)
            expected_mapping = {1: [2, 3], 2: [4]}
            self.verify(bfs_graph, expected_mapping, 3)

        def createBfsFollowingInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, True)
            expected_mapping = {1: [0]}
            self.verify(bfs_graph, expected_mapping, 1)

        def createBfsFollowingOutAndInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, True)
            expected_mapping = {1: [0,2,3], 2:[4]}
            self.verify(bfs_graph, expected_mapping, 4)

        def createBfsFollowingNoLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, False)
            expected_mapping = {}
            self.verify(bfs_graph, expected_mapping, 0)

        def verify(self, bfs_graph, expected_mapping, expected_edge_count):
            assert len(list(bfs_graph.Edges())) == expected_edge_count
            for edge in bfs_graph.Edges():
                assert edge.GetDstNId() in expected_mapping.get(edge.GetSrcNId())

    if __name__ == '__main__':
        test = BfsTreeDirectedGraphTest()
        test.createBfsFollowingOutLinks()
        test.createBfsFollowingInLinks()
        test.createBfsFollowingNoLinks()
        test.createBfsFollowingOutAndInLinks()

test_using_undirected_graph.py::

    import snap

    class BfsTreeUndirectedGraphTest:
        def __init__(self):
            g = snap.PUNGraph.New()
            for i in range(5):
                g.AddNode(i)
            g.AddEdge(0, 1)
            g.AddEdge(1, 2)
            g.AddEdge(1, 3)
            g.AddEdge(2, 4)
            self.g = g

        def createBfsFollowingOutLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, False)
            expected_mapping = {1: [0,2,3], 2:[4]}
            self.verify(bfs_graph, expected_mapping, 4)
        def createBfsFollowingInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, True)
            expected_mapping = {1: [0,2,3], 2:[4]}
            self.verify(bfs_graph, expected_mapping, 4)

        def createBfsFollowingOutAndInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, True)
            expected_mapping = {1: [0,2,3], 2:[4]}
            self.verify(bfs_graph, expected_mapping, 4)

        def createBfsFollowingNoLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, False)
            expected_mapping = {}
            self.verify(bfs_graph, expected_mapping, 0)

        def verify(self, bfs_graph, expected_mapping, expected_edge_count):
            assert len(list(bfs_graph.Edges())) == expected_edge_count
            for edge in bfs_graph.Edges():
                assert edge.GetDstNId() in expected_mapping.get(edge.GetSrcNId())

    if __name__ == '__main__':
        test = BfsTreeUndirectedGraphTest()
        test.createBfsFollowingOutLinks()
        test.createBfsFollowingInLinks()
        test.createBfsFollowingNoLinks()
        test.createBfsFollowingOutAndInLinks()


test_using_tneanet_graph.py::

    import snap

    class BfsTreeTNEAnetTest:
        def __init__(self):
            g = snap.TNEANet.New()
            for i in range(5):
                g.AddNode(i)
            g.AddEdge(0, 1)
            g.AddEdge(1, 2)
            g.AddEdge(1, 3)
            g.AddEdge(2, 4)
            self.g = g

        def createBfsFollowingOutLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, False)
            expected_mapping = {1: [2, 3], 2: [4]}
            self.verify(bfs_graph, expected_mapping, 3)

        def createBfsFollowingInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, True)
            expected_mapping = {1: [0]}
            self.verify(bfs_graph, expected_mapping, 1)

        def createBfsFollowingOutAndInLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, True, True)
            expected_mapping = {1: [0,2,3], 2:[4]}
            self.verify(bfs_graph, expected_mapping, 4)

        def createBfsFollowingNoLinks(self):
            bfs_graph = snap.GetBfsTree(self.g, 1, False, False)
            expected_mapping = {}
            self.verify(bfs_graph, expected_mapping, 0)

        def verify(self, bfs_graph, expected_mapping, expected_edge_count):
            assert len(list(bfs_graph.Edges())) == expected_edge_count
            for edge in bfs_graph.Edges():
                assert edge.GetDstNId() in expected_mapping.get(edge.GetSrcNId())

    if __name__ == '__main__':
        test = BfsTreeTNEAnetTest()
        test.createBfsFollowingOutLinks()
        test.createBfsFollowingInLinks()
        test.createBfsFollowingNoLinks()
        test.createBfsFollowingOutAndInLinks()

