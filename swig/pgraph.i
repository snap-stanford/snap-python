// pgraph.i
// Templates for SNAP

%pythoncode %{
def GenGraph(gtype):
    '''
    Test node, edge creation
    '''

    NNodes = 12345
    NEdges = 123456

    if gtype == PNEANet:
        # PNEANet
        Graph = GenRndGnm(NNodes, NEdges)
        print "1type %s" % (type(Graph))
        print "1nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    if gtype == PUNGraph:
        # PUNGraph
        Graph = GenRndGnm_PUNGraph(NNodes, NEdges)
        print "2type %s" % (type(Graph))
        print "2nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    if gtype == PNGraph:
        # PNGraph
        #Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        Graph = GenRndGnm_PNGraph(NNodes, NEdges)
        print "3type %s" % (type(Graph))
        print "3nodes %d, edges %d" % (Graph.GetNodes(), Graph.GetEdges())
        return Graph

    return None

def Nodes(self):
    NI = self.BegNI()
    while NI < self.EndNI():
        yield NI
        NI.Next()

def Edges(self):
    EI = self.BegEI()
    while EI < self.EndEI():
        yield EI
        EI.Next()

def Clr(self):
    print "Python Clr"
    self().Clr()

def Save(self):
    self().Save()

PNEANet.Nodes = Nodes
PNEANet.Edges = Edges
PNEANet.Clr = Clr
PNEANet.Save = Save

       
%}

