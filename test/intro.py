from snap import *

def intro():

    # create a graph PNGraph
    G1 = TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    print "G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges())

    # create a directed random graph on 100 nodes and 1k edges
    G2 = GenRndGnm(PNGraph, 100, 1000)
    print "G2: Nodes %d, Edges %d" % (G2.GetNodes(), G2.GetEdges())

    # traverse the nodes
    for NI in G2.Nodes():
        print "node id %d with out-degree %d and in-degree %d" % (
            NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    # traverse the edges
    for EI in G2.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    # traverse the edges by nodes
    for NI in G2.Nodes():
        for Id in NI.GetOutEdges():
            print "edge (%d %d)" % (NI.GetId(), Id)

    # generate a network using Forest Fire model
    G3 = GenForestFire(1000, 0.35, 0.35)
    print "G3: Nodes %d, Edges %d" % (G3.GetNodes(), G3.GetEdges())

    # save and load binary
    FOut = TFOut("test.graph")
    G3.Save(FOut)
    FOut.Flush()
    FIn = TFIn("test.graph")
    G4 = TNGraph.Load(FIn)
    print "G4: Nodes %d, Edges %d" % (G4.GetNodes(), G4.GetEdges())

    # save and load from a text file
    SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")
    G5 = LoadEdgeList(PNGraph, "test.txt", 0, 1)
    print "G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges())

    # generate a network using Forest Fire model
    G6 = GenForestFire(1000, 0.35, 0.35)
    print "G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges())
    # convert to undirected graph
    G7 = ConvertGraph(PUNGraph,G6)
    print "G7: Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges())
    # get largest weakly connected component of G
    WccG = GetMxWcc(G6)
    # get a subgraph induced on nodes {0,1,2,3,4,5}
    SubG = GetSubGraph(G6, TIntV.GetV(0,1,2,3,4))
    # get 3-core of G
    Core3 = GetKCore(G6, 3)
    # delete nodes of out degree 10 and in degree 5
    DelDegKNodes(G6, 10, 5)
    print "G6a: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges())

    # generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
    G8 = GenPrefAttach(1000, 3)
    print "G8: Nodes %d, Edges %d" % (G8.GetNodes(), G8.GetEdges())
    # vector of pairs of integers (size, count)
    CntV = TIntPrV()
    # get distribution of connected components (component size, count)
    GetWccSzCnt(G8, CntV)
    # get degree distribution pairs (degree, count)
    GetOutDegCnt(G8, CntV)
    # vector of floats
    EigV = TFltV()
    # get first eigenvector of graph adjacency matrix
    GetEigVec(G8, EigV)
    # get diameter of G8
    GetBfsFullDiam(G8, 100)
    # count the number of triads in G8, get the clustering coefficient of G8
    GetTriads(G8)
    GetClustCf(G8)

if __name__ == '__main__':
    intro()

