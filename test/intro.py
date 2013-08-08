from snap import *

if __name__ == '__main__':

    # create a graph PNGraph
    Graph = TNGraph.New()
    Graph.AddNode(1)
    Graph.AddNode(5)
    Graph.AddNode(32)
    Graph.AddEdge(1,5)
    Graph.AddEdge(5,1)
    Graph.AddEdge(5,32)
    print "Graph: Nodes %d, Edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    # create a directed random graph on 100 nodes and 1k edges
    Graph = GenRndGnm(PNGraph, 100, 1000)
    print "Graph: Nodes %d, Edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    # traverse the nodes
    for NI in Graph.Nodes():
        print "node id %d with out-degree %d and in-degree %d" % (
            NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    # traverse the edges
    for EI in Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    # traverse the edges by nodes
    for NI in Graph.Nodes():
        for e in range(0, NI.GetOutDeg()):
            print "edge (%d %d)" % (NI.GetId(), NI.GetOutNId(e))

    # generate a network using Forest Fire model
    G = GenForestFire(1000, 0.35, 0.35)
    print "G: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())

    # save and load binary
    FOut = TFOut(TStr("test.graph"))
    G.Save(FOut)
    FOut.Flush()
    FIn = TFIn(TStr("test.graph"))
    G2 = TNGraph.Load(FIn)
    print "G2: Nodes %d, Edges %d" % (G2.GetNodes(), G2.GetEdges())

    # save and load from a text file
    SaveEdgeList(G2, TStr("test.txt"), TStr("Save as tab-separated list of edges"))
    G3 = LoadEdgeList(PNGraph, TStr("test.txt"), 0, 1)
    print "G3: Nodes %d, Edges %d" % (G3.GetNodes(), G3.GetEdges())

    # generate a network using Forest Fire model
    G = GenForestFire(1000, 0.35, 0.35)
    # convert to undirected graph
    # TODO UG = ConvertGraph(G,PUNGraph)
    # get largest weakly connected component of G
    WccG = GetMxWcc(G)
    # get a subgraph induced on nodes {0,1,2,3,4,5}
    SubG = GetSubGraph(G, TIntV.GetV(TInt(0),TInt(1),TInt(2),TInt(3),TInt(4)))
    # get 3-core of G
    # TODO Core3 = GetKCore(G, TInt(3))
    # delete nodes of degree 10
    # TODO DelDegKNodes(G, TInt(10))

    # generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
    G = GenPrefAttach(1000, 3)
    # get distribution of connected components (component size, count)
    # TODO TVec<TPair<TInt, TInt> > CntV    # vector of pairs of integers (size, count)
    # TODO GetWccSzCnt(G, CntV)    # get degree distribution pairs (degree, count)
    # TODO GetOutDegCnt(G, CntV)   # get first eigenvector of graph adjacency matrix
    # TODO EigV = TFltV()          # vector of floats
    # TODO GetEigVec(G, EigV)
    # get diameter of G
    # TODO GetBfsFullDiam(G)
    # count the number of triads in G, get the clustering coefficient of G
    # TODO GetTriads(G)
    # TODO GetClustCf(G)

