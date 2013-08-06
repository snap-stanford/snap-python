import random
import sys
sys.path.append("../swig")
from snap import *

def PrintGStats(s, Graph):
    '''
    Print graph statistics
    '''

    print "graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no")

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

    print 1
    Graph.Clr()
    print "4nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    print 2
    NNodes = 12345
    NEdges = 123456
    FName = "test.graph"

    #Graph = TNEANet()
    #print "5type %s" % (type(Graph))

    print 3
    t = Graph.Empty()

    print 4
    # create the nodes
    for i in range(0, NNodes):
        Graph.AddNode(i)

    print 5
    t = Graph.Empty()
    n = Graph.GetNodes()
    
    print 6
    # create random edges
    NCount = NEdges
    while NCount > 0:
        x = int(random.random() * NNodes)
        y = int(random.random() * NNodes)
        # skip the loops in this test
        if x != y  and  not Graph.IsEdge(x,y):
            n = Graph.AddEdge(x, y)
            NCount -= 1

    print 7
    PrintGStats("ManipulateNodesEdges:Graph1", Graph)

    # get all the nodes
    NCount = 0
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        NCount += 1
        NI.Next()

    # get all the edges for all the nodes
    ECount1 = 0
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        ECount1 += NI.GetOutDeg()
        NI.Next()

    ECount1 = ECount1 / 2

    # get all the edges directly
    ECount2 = 0
    EI = Graph.BegEI()
    while EI < Graph.EndEI():
        ECount2 += 1
        EI.Next()

    print "graph ManipulateNodesEdges:Graph2, nodes %d, edges1 %d, edges2 %d"\
        % (NCount, ECount1, ECount2)

    # assignment
    Graph1 = Graph
    PrintGStats("ManipulateNodesEdges:Graph3", Graph1)

    # save the graph
    print "graph type = ", type(Graph)
    FOut = TFOut(TStr(FName))
    print 8
    Graph().Save(FOut)
    print 9
    FOut.Flush()
    print 10

    # load the graph
    FIn = TFIn(TStr(FName))
    Graph2 = TNEANet(FIn)
    PrintGStats("ManipulateNodesEdges:Graph4" , Graph2)

    # remove all the nodes and edges
    for i in range(0, NNodes):
        n = Graph.GetRndNId()
        Graph.DelNode(n)

    PrintGStats("ManipulateNodesEdges:Graph5" , Graph)
    
    Graph1.Clr()
    PrintGStats("ManipulateNodesEdges:Graph6" , Graph1)

def Main():

    Graph = TNEANet()
    print "6type %s" % (type(Graph))

    Graph = GenRndGnm(123, 1234)
    print "7type %s" % (type(Graph))

    for NI in Graph.Nodes():
        print NI.GetId()

    for EI in Graph.Edges():
        print EI.GetId()

    G1 = Graph()
    print "8type %s" % (type(G1))

    print "----- GenGraph -----"
    Graph = GenGraph(PNEANet)
    print "type %s" % (type(Graph))
    print "nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())

    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges(Graph)

if __name__ == '__main__':
    for i in range(0,10000):
        Main()

