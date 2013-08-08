import random
import sys
sys.path.append("../swig")
from snap import *

def PrintGStats(s, Graph, nodes, edges, empty):
    '''
    Print graph statistics
    '''

    print "%s graph %s, nodes %d (%d), edges %d (%d), empty %s (%s)" % (
        type(Graph), s, Graph.GetNodes(), nodes, Graph.GetEdges(), edges,
        Graph.Empty(), empty)

    if Graph.GetNodes() != nodes:
        print "*** Error: %d %d, incorrect number of nodes" % (
            Graph.GetNodes(), nodes)
        sys.exit(1)

    if Graph.GetEdges() != edges:
        print "*** Error: %d %d, incorrect number of edges" % (
            Graph.GetEdges(), edges)
        sys.exit(1)

    if Graph.Empty() != empty:
        print "*** Error: %s %s, incorrect empty test" % (
            Graph.Empty(), empty)
        sys.exit(1)

def GenGraph1(gtype):
    '''
    Test node, edge creation
    '''

    NNodes = 12345
    NEdges = 123456

    if gtype == PNEANet:
        # PNEANet
        Graph = GenRndGnm(NNodes, NEdges)
        print "type %s" % (type(Graph))
        print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    if gtype == PUNGraph:
        # PUNGraph
        Graph = GenRndGnm_PUNGraph(NNodes, NEdges)
        print "type %s" % (type(Graph))
        print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    if gtype == PNGraph:
        # PNGraph
        #Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        print "type %s" % (type(Graph))
        print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    return None

def ManipulateNodesEdges(Graph):
    '''
    Test node, edge creation
    '''

    print "4type %s" % (type(Graph))
    print "4nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    Graph.Clr()
    print "5nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    NNodes = 12345
    NEdges = 123456
    FName = "test.graph"

    #Graph = TNEANet()
    #print "5type %s" % (type(Graph))

    t = Graph.Empty()

    # create the nodes
    for i in range(0, NNodes):
        Graph.AddNode(i)

    t = Graph.Empty()
    n = Graph.GetNodes()
    
    # create random edges
    NCount = NEdges
    while NCount > 0:
        x = int(random.random() * NNodes)
        y = int(random.random() * NNodes)
        # skip the loops in this test
        if x != y  and  not Graph.IsEdge(x,y):
            n = Graph.AddEdge(x, y)
            NCount -= 1

    PrintGStats("ManipulateNodesEdges:Graph1", Graph, NNodes, NEdges, False)

    # get all the nodes
    NCount = 0
    for NI in Graph.Nodes():
        NCount += 1

    # get all the edges for all the nodes
    ECount1 = 0
    for NI in Graph.Nodes():
        ECount1 += NI.GetOutDeg()

    ECount1 = ECount1 / 2

    # get all the edges directly
    ECount2 = 0
    for EI in Graph.Edges():
        ECount2 += 1

    print "graph ManipulateNodesEdges:Graph2, nodes %d, edges1 %d, edges2 %d (%d)"\
        % (NCount, ECount1, ECount2, ECount1*2)

    # assignment
    Graph1 = Graph
    PrintGStats("ManipulateNodesEdges:Graph3", Graph1, NNodes, NEdges, False)

    # save the graph
    print "graph type = ", type(Graph)
    FOut = TFOut(TStr(FName))
    Graph.Save(FOut)
    FOut.Flush()

    # load the graph
    FIn = TFIn(TStr(FName))
    if type(Graph) == PNEANet:
        Graph2 = TNEANet(FIn)
    elif type(Graph) == PUNGraph:
        Graph2 = TUNGraph(FIn)
    elif type(Graph) == PNGraph:
        Graph2 = TNGraph(FIn)
    PrintGStats("ManipulateNodesEdges:Graph4" , Graph2, NNodes, NEdges, False)

    # remove all the nodes and edges
    for i in range(0, NNodes):
        n = Graph.GetRndNId()
        Graph.DelNode(n)

    PrintGStats("ManipulateNodesEdges:Graph5" , Graph, 0, 0, True)
    
    Graph1.Clr()
    PrintGStats("ManipulateNodesEdges:Graph6" , Graph1, 0, 0, True)

def NewGraph():

    print "----- New TUNGraph -----"
    Graph = TUNGraph.New()
    #Graph = PUNGraph.New()
    print "6type %s" % (type(Graph))
    print "connected", IsConnected(Graph)
    #print "connected", IsConnected_PNEANet(Graph)
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 0, 0, True)

    Graph = GenRndGnm(PUNGraph, 23, 234)
    print "type %s" % (type(Graph))
    print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
    print "connected", IsConnected(Graph)
    print "connected", IsConnected_PUNGraph(Graph)
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 23, 234, False)
    for NI in Graph.Nodes():
        print NI.GetId()
    for EI in Graph.Edges():
        print EI.GetId()

def Main():

    print "----- PNEANet -----"
    Graph = TNEANet.New()
    #Graph = PNEANet.New()
    print "6type %s" % (type(Graph))
    print "connected", IsConnected(Graph)
    #print "connected", IsConnected_PNEANet(Graph)
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 0, 0, True)

    Graph = GenRndGnm(PNEANet, 23, 234)
    print "type %s" % (type(Graph))
    print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
    print "connected", IsConnected(Graph)
    print "connected", IsConnected_PNEANet(Graph)
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 23, 234, False)
    for NI in Graph.Nodes():
        print NI.GetId()
    for EI in Graph.Edges():
        print EI.GetId()

    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges(Graph)

    print "----- PUNGraph -----"
    Graph = TUNGraph.New()
    print "6type %s" % (type(Graph))
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 0, 0, True)

    Graph = GenRndGnm(PUNGraph, 34, 345)
    print "type %s" % (type(Graph))
    print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 34, 345, False)
    for NI in Graph.Nodes():
        print NI.GetId()
    for EI in Graph.Edges():
        print EI.GetId()

    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges(Graph)

    print "----- PNGraph -----"
    Graph = TNGraph.New()
    print "6type %s" % (type(Graph))
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 0, 0, True)

    Graph = GenRndGnm(PNGraph, 45, 456)
    print "type %s" % (type(Graph))
    print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
    PrintGStats("ManipulateNodesEdges:Graph" , Graph, 45, 456, False)
    for NI in Graph.Nodes():
        print NI.GetId()
    for EI in Graph.Edges():
        print EI.GetId()

    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges(Graph)

if __name__ == '__main__':
    NewGraph()
    Main()

