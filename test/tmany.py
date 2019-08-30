import random
import sys
sys.path.append("../swig")
from snap import *

def PrintGStats(s, Graph):
    '''
    Print graph statistics
    '''

    print("graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no"))

def GenGraph1(gtype):
    '''
    Test node, edge creation
    '''

    NNodes = 12345
    NEdges = 123456

    if gtype == PNEANet:
        # PNEANet
        Graph = GenRndGnm(NNodes, NEdges)
        print("type %s" % (type(Graph)))
        print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))
        return Graph

    if gtype == PUNGraph:
        # PUNGraph
        Graph = GenRndGnm_PUNGraph(NNodes, NEdges)
        print("type %s" % (type(Graph)))
        print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))
        return Graph

    if gtype == PNGraph:
        # PNGraph
        #Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        print("type %s" % (type(Graph)))
        print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))
        return Graph

    return None

def ManipulateNodesEdges():
    '''
    Test node, edge creation
    '''

    NNodes = 12345
    NEdges = 123456

    FName = "test.graph"

    Graph = TNEANet()
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

    print("graph ManipulateNodesEdges:Graph2, nodes %d, edges1 %d, edges2 %d"\
        % (NCount, ECount1, ECount2))

    # assignment
    Graph1 = Graph
    PrintGStats("ManipulateNodesEdges:Graph3", Graph1)

    # save the graph
    print("graph type = ", type(Graph))
    FOut = TFOut(TStr(FName))
    Graph.Save(FOut)
    FOut.Flush()

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

if __name__ == '__main__':

    print("type 1", PNEANet)
    p = PNEANet
    print("type 2", p)
    if p == PNEANet:
        print("true  snap.PNEANet")
    else:
        print("false snap.PNEANet")
    if p == PNGraph:
        print("true  snap.PGraph")
    else:
        print("false snap.PGraph")

    print("type 1", PNGraph)
    p = PNGraph
    print("type 2", p)
    if p == PNEANet:
        print("true  snap.PNEANet")
    else:
        print("false snap.PNEANet")
    if p == PNGraph:
        print("true  snap.PGraph")
    else:
        print("false snap.PGraph")

    print("----- GenGraph -----")
    Graph = GenGraph(PNEANet)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    Graph = GenGraph(PUNGraph)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    Graph = GenGraph(PNGraph)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    Graph = GenGraph1(PNEANet)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    Graph = GenGraph1(PUNGraph)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    Graph = GenGraph1(PNGraph)
    print("type %s" % (type(Graph)))
    print("nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges()))

    #print("----- ManipulateNodesEdges -----")
    #ManipulateNodesEdges()

