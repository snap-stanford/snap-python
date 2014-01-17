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

