import random
import sys

sys.path.append("../swig")

import snap as Snap

def PrintGStats(s, Graph):
    '''
    Print graph statistics
    '''

    print "graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no")

def DefaultConstructor():
    '''
    Test the default constructor
    '''

    Graph = Snap.TUNGraph()
    PrintGStats("DefaultConstructor:Graph",Graph)

def ManipulateNodesEdges():
    '''
    Test node, edge creation
    '''

    NNodes = 10000
    NEdges = 100000
    FName = "test.graph"

    Graph = Snap.TUNGraph()
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

    PrintGStats("ManipulateNodesEdges:Graph1",Graph)

    # get all the nodes
    NCount = 0
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        NCount += 1
        NI.Next()

    # get all the edges for all the nodes
    ECount1 = 0;
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        ECount1 += NI.GetOutDeg()
        NI.Next()

    ECount1 = ECount1 / 2

    # get all the edges directly
    ECount2 = 0;
    EI = Graph.BegEI()
    while EI < Graph.EndEI():
        ECount2 += 1
        EI.Next()

    print "graph ManipulateNodesEdges:Graph2, nodes %d, edges1 %d, edges2 %d" % (
        NCount, ECount1, ECount2)

    # assignment
    Graph1 = Graph;
    PrintGStats("ManipulateNodesEdges:Graph3",Graph1)

    # save the graph
    FOut = Snap.TFOut(Snap.TStr(FName))
    Graph.Save(FOut)
    FOut.Flush()

    # load the graph
    FIn = Snap.TFIn(Snap.TStr(FName))
    Graph2 = Snap.TUNGraph(FIn)
    PrintGStats("ManipulateNodesEdges:Graph4",Graph2)

    # remove all the nodes and edges
    for i in range(0, NNodes):
        n = Graph.GetRndNId()
        Graph.DelNode(n)

    PrintGStats("ManipulateNodesEdges:Graph5",Graph)
    
    Graph1.Clr()
    PrintGStats("ManipulateNodesEdges:Graph6",Graph1)

def GetSmallGraph():
    '''
    Test small graph
    '''

    Graph = Snap.TUNGraph()
    Graph.GetSmallGraph()
    PrintGStats("GetSmallGraph:Graph",Graph)

if __name__ == '__main__':
    print "----- DefaultConstructor -----"
    DefaultConstructor()
    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges()
    print "----- GetSmallGraph -----"
    GetSmallGraph()

