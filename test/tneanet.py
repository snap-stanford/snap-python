import random
import sys
from snap import *

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

    Graph = TNEANet.New()
    PrintGStats("DefaultConstructor:Graph", Graph)

def ManipulateNodesEdges():
    '''
    Test node, edge creation
    '''

    NNodes = 10000
    NEdges = 100000
    FName = "test.graph"

    Graph = TNEANet.New()
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

    print "graph ManipulateNodesEdges:Graph2, nodes %d, edges1 %d, edges2 %d"\
        % (NCount, ECount1, ECount2)

    # assignment
    Graph1 = Graph
    PrintGStats("ManipulateNodesEdges:Graph3", Graph1)

    # save the graph
    print "graph type = ", type(Graph)
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

def ManipulateNodeEdgeAttributes():
  '''
    Test node attribute functionality
  '''

  NNodes = 1000
  NEdges = 1000
  
  Graph = TNEANet.New()
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
    if x != y  and not Graph.IsEdge(x,y):
      n = Graph.AddEdge(x, y)
    NCount -= 1

  print "Added nodes"

  # create attributes and fill all nodes
  attr1 = TStr("str")
  attr2 = TStr("int")
  attr3 = TStr("float")
  attr4 = TStr("default")
  
  # Test verticaliterator for node 3, 50, 700, 900
  # Check if we can set defaults to 0 fordata.
  Graph.AddIntAttrN(attr2, 0)
  Graph.AddIntAttrDatN(3, 3*2, attr2)
  Graph.AddIntAttrDatN(50, 50*2, attr2)
  Graph.AddIntAttrDatN(700, 700*2, attr2)
  Graph.AddIntAttrDatN(900, 900*2, attr2)
        
  print "Added attributes"
        
  NodeId = 0
  NI = Graph.BegNAIntI(attr2)
  while NI < Graph.EndNAIntI(attr2):
    if NI.GetDat() != 0:
      print "Attribute: %s, Node: %i, Val: %d" % (attr2(), NodeId, NI.GetDat())
    NodeId += 1
    NI.Next()

  # Test vertical flt iterator for node 3, 50, 700, 900
  Graph.AddFltAttrDatN(5, 3.41, attr3)
  Graph.AddFltAttrDatN(50, 2.718, attr3)
  Graph.AddFltAttrDatN(300, 150.0, attr3)
        
  Graph.AddFltAttrDatN(653, 653, attr3)
  NodeId = 0
  NCount = 0
  NI = Graph.BegNI()
  while NI < Graph.EndNI():
    NCount += 1
    NI.Next()
        
  NI = Graph.BegNAFltI(attr3)
  NodeId = 0
  while NI < Graph.EndNAFltI(attr3):
    if NI.GetDat() != TFlt.Mn:
      print "Attribute: %s, Node: %i, Val: %f" % (attr3(), NodeId, NI.GetDat())
    NodeId += 1
    NI.Next()

  # Test vertical str iterator for node 3, 50, 700, 900
  Graph.AddStrAttrDatN(10, TStr("abc"), attr1)
  Graph.AddStrAttrDatN(20, TStr("def"), attr1)
  Graph.AddStrAttrDatN(400, TStr("ghi"), attr1)
  # this does not show since ""=null
  Graph.AddStrAttrDatN(455, TStr(""), attr1)
  NodeId = 0

  NI = Graph.BegNAStrI(attr1)
  NodeId = 0
  while NI < Graph.EndNAStrI(attr1):
    if NI.GetDat() != TStr.GetNullStr():
      print "Attribute: %s, Node: %i, Val: %s" % (attr1(), NodeId, NI.GetDat())
    NodeId += 1
    NI.Next()

  # Test vertical iterator over many types (must skip default/deleted attr)
  NId = 55
  Graph.AddStrAttrDatN(NId, TStr("aaa"), attr1)
  Graph.AddIntAttrDatN(NId, 3*2, attr2)
  Graph.AddFltAttrDatN(NId, 3.41, attr3)
  Graph.AddStrAttrDatN(80, TStr("dont appear"), attr4) # should not show up
  NIdAttrName = TStrV()
  Graph.AttrNameNI(NId, NIdAttrName)
  AttrLen = NIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Node: %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

  Graph.DelAttrDatN(NId, attr2)
  Graph.AttrNameNI(NId, NIdAttrName)
  AttrLen = NIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Node (no int) : %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

  Graph.AddIntAttrDatN(NId, 3*2, attr2)
  Graph.DelAttrN(attr1)
  Graph.AttrNameNI(NId, NIdAttrName)
  AttrLen = NIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Node (no str) : %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

  NIdAttrValue = TStrV()
  Graph.AttrValueNI(NId, NIdAttrValue)
  AttrLen = NIdAttrValue.Len()
  for i in range(AttrLen):
    print "Vertical Node (no str) : %i, Attr_Val: %s" % (NId, NIdAttrName.GetI(i)())

  for i in range(NNodes):
    Graph.AddIntAttrDatN(i, 70, attr2)

  total = 0
  NI = Graph.BegNAIntI(attr2)
  while NI < Graph.EndNAIntI(attr2):
    total += NI.GetDat()
    NI.Next()

  print "Average: %i (should be 70)" % (total/NNodes)

  # Test verticaliterator for edge
  Graph.AddIntAttrDatE(3, 3*2, attr2)
  Graph.AddIntAttrDatE(55, 55*2, attr2)
  Graph.AddIntAttrDatE(705, 705*2, attr2)
  Graph.AddIntAttrDatE(905, 905*2, attr2)
  EdgeId = 0
  EI = Graph.BegEAIntI(attr2)
  while EI < Graph.EndEAIntI(attr2):
    if EI.GetDat() != TInt.Mn:
      print "E Attribute: %s, Edge: %i, Val: %i"\
        % (attr2(), EdgeId, EI.GetDat())
    EdgeId += 1
    EI.Next()

  # Test vertical flt iterator for edge
  Graph.AddFltAttrE(attr3, 0.00)
  Graph.AddFltAttrDatE(5, 4.41, attr3)
  Graph.AddFltAttrDatE(50, 3.718, attr3)
  Graph.AddFltAttrDatE(300, 151.0, attr3)
  Graph.AddFltAttrDatE(653, 654, attr3)
  EdgeId = 0
  EI = Graph.BegEAFltI(attr3)
  while EI < Graph.EndEAFltI(attr3):
    # Check if defaults are set to 0.
    if EI.GetDat() != 0:
      print "E Attribute: %s, Edge: %i, Val: %f" % \
        (attr3(), EdgeId, EI.GetDat())
    EdgeId += 1
    EI.Next()

  # Test vertical str iterator for edge
  Graph.AddStrAttrDatE(10, TStr("abc"), attr1)
  Graph.AddStrAttrDatE(20, TStr("def"), attr1)
  Graph.AddStrAttrDatE(400, TStr("ghi"), attr1)
  # this does not show since ""=null
  Graph.AddStrAttrDatE(455, TStr(""), attr1)
  EdgeId = 0
  EI = Graph.BegEAStrI(attr1)
  while EI < Graph.EndEAStrI(attr1):
    if EI.GetDat() != TStr.GetNullStr():
      print "E Attribute: %s, Edge: %i, Val: %s" %\
        (attr1(), EdgeId, EI.GetDat())
    EdgeId += 1
    EI.Next()

  # Test vertical iterator over many types (must skip default/deleted attr)
  EId = 55
  Graph.AddStrAttrDatE(EId, TStr("aaa"), attr1)
  Graph.AddIntAttrDatE(EId, 3*2, attr2)
  Graph.AddFltAttrDatE(EId, 3.41, attr3)
  Graph.AddStrAttrDatE(80, TStr("dont appear"), attr4) # should not show up
  EIdAttrName = TStrV()
#  Graph.AttrNameEI(EId, EIdAttrName)
  AttrLen = EIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Edge: %i, Attr: %s" % (EId, EIdAttrName.GetI(i))

  Graph.DelAttrDatE(EId, attr2)
#  Graph.AttrNameEI(EId, EIdAttrName)
  AttrLen = EIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Edge (no int) : %i, Attr: %s" % (EId, EIdAttrName.GetI(i))

  Graph.AddIntAttrDatE(EId, 3*2, attr2)
  Graph.DelAttrE(attr1)
#  Graph.AttrNameEI(EId, EIdAttrName)
  AttrLen = EIdAttrName.Len()
  for i in range(AttrLen):
    print "Vertical Edge (no str) : %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

  EIdAttrValue = TStrV()
  #Graph.AttrValueEI(TInt(EId), EIdAttrValue)
  Graph.AttrValueEI(EId, EIdAttrValue)
  AttrLen = EIdAttrValue.Len()
  for i in range(AttrLen):
    print "Vertical Edge (no str) : %i, Attr_Val: %s" % (EId, EIdAttrValue.GetI(i)())

  for i in range(NEdges):
    Graph.AddIntAttrDatE(i, 70, attr2)

  total = 0
  EI = Graph.BegNAIntI(attr2)
  while EI < Graph.EndNAIntI(attr2):
    total += EI.GetDat()
    EI.Next()

  print "Average: %i (should be 70)" % (total/NEdges)
  
  Graph.Clr()

if __name__ == '__main__':
    print "----- DefaultConstructor -----"
    DefaultConstructor()
    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges()
    print "----- ManipulateNodesEdgesAttributes -----"
    ManipulateNodeEdgeAttributes()

