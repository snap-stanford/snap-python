import random
import sys

import snap

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

    Graph = snap.TNEANet.New()
    PrintGStats("DefaultConstructor:Graph", Graph)

def ManipulateNodesEdges():
    '''
    Test node, edge creation
    '''

    NNodes = 10000
    NEdges = 100000
    FName = "test.graph"

    Graph = snap.TNEANet.New()
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
    #FOut = TFOut(TStr(FName))
    FOut = snap.TFOut(FName)
    Graph.Save(FOut)
    FOut.Flush()

    # load the graph
    #FIn = TFIn(TStr(FName))
    FIn = snap.TFIn(FName)
    Graph2 = snap.TNEANet(FIn)
    PrintGStats("ManipulateNodesEdges:Graph4" , Graph2)

    # remove all the nodes and edges
    for i in range(0, NNodes):
        n = Graph.GetRndNId()
        Graph.DelNode(n)

    PrintGStats("ManipulateNodesEdges:Graph5" , Graph)
    
    Graph1.Clr()
    PrintGStats("ManipulateNodesEdges:Graph6" , Graph1)

def ManipulateAttributesId():
    '''
        Test node, edge attribute functionality using Ids
    '''

    NNodes = 1000
    NEdges = 1000
  
    Graph = snap.TNEANet.New()
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
    #attr1 = TStr("str")
    #attr2 = TStr("int")
    #attr3 = TStr("float")
    #attr4 = TStr("default")
    attr1 = "STR"
    attr2 = "INT"
    attr3 = "FLOAT"
    attr4 = "DEFAULT"
  
    # Test column int iterator for node 3, 50, 700, 900
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
           print "Attribute1: %s, Node: %i, Val: %d" % (attr2, NodeId, NI.GetDat())
           #print "Attribute: %s, Node: %i, Val: %d" % (attr2(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column flt iterator for node 3, 50, 700, 900
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
        if NI.GetDat() != snap.TFlt.Mn:
            print "Attribute2: %s, Node: %i, Val: %f" % (attr3, NodeId, NI.GetDat())
            #print "Attribute: %s, Node: %i, Val: %f" % (attr3(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column str iterator for node 3, 50, 700, 900
    #Graph.AddStrAttrDatN(10, TStr("abc"), attr1)
    #Graph.AddStrAttrDatN(20, TStr("def"), attr1)
    #Graph.AddStrAttrDatN(400, TStr("ghi"), attr1)
    Graph.AddStrAttrDatN(10, "abc", attr1)
    Graph.AddStrAttrDatN(20, "def", attr1)
    Graph.AddStrAttrDatN(400, "ghi", attr1)
    # this does not show since ""=null
    #Graph.AddStrAttrDatN(455, TStr(""), attr1)
    # TODO Graph.AddStrAttrDatN(455, "", attr1)
    NodeId = 0

    NI = Graph.BegNAStrI(attr1)
    NodeId = 0
    while NI < Graph.EndNAStrI(attr1):
        if NI.GetDat() != snap.TStr.GetNullStr():
            print "Attribute3: %s, Node: %i, Val: %s" % (attr1, NodeId, NI.GetDat())
            #print "Attribute: %s, Node: %i, Val: %s" % (attr1(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column iterator over many types (must skip default/deleted attr)
    NId = 55
    #Graph.AddStrAttrDatN(NId, TStr("aaa"), attr1)
    Graph.AddStrAttrDatN(NId, "aaa", attr1)
    Graph.AddIntAttrDatN(NId, 3*2, attr2)
    Graph.AddFltAttrDatN(NId, 3.41, attr3)
    #Graph.AddStrAttrDatN(80, TStr("dont appear"), attr4) # should not show up
    Graph.AddStrAttrDatN(80, "dont appear", attr4) # should not show up

    attr1idx = Graph.GetAttrIndN(attr1)
    attr2idx = Graph.GetAttrIndN(attr2)
    attr3idx = Graph.GetAttrIndN(attr3)
    attr4idx = Graph.GetAttrIndN(attr4)
    print "Node attribute indexes:  %s %d,   %s %d,   %s %d,   %s %d" % (
            attr1, attr1idx, attr2, attr2idx, attr3, attr3idx, attr4, attr4idx)

    print "NId attributes: %i, %s %d %.2f" % (
            NId,
            Graph.GetStrAttrDatN(NId, attr1),
            Graph.GetIntAttrDatN(NId, attr2),
            Graph.GetFltAttrDatN(NId, attr3))

    print "ind attributes: %i, %s %d %.2f" % (
            NId,
            Graph.GetStrAttrIndDatN(NId, attr1idx),
            Graph.GetIntAttrIndDatN(NId, attr2idx),
            Graph.GetFltAttrIndDatN(NId, attr3idx))

    NIdAttrName = snap.TStrV()
    NIdAttrValue = snap.TStrV()
    NIdIntAttrValue = snap.TIntV()
    NIdFltAttrValue = snap.TFltV()
    NIdStrAttrValue = snap.TStrV()

    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node1: %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.IntAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node11 (int): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.FltAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node12 (flt): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.StrAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node13 (str): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.IntAttrValueNI(NId, NIdIntAttrValue)
    AttrLen = NIdIntAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node14 (int): %i, Attr_Val: %d" % (NId, NIdIntAttrValue.GetI(i)())

    Graph.FltAttrValueNI(NId, NIdFltAttrValue)
    AttrLen = NIdFltAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node15 (flt): %i, Attr_Val: %.2f" % (NId, NIdFltAttrValue.GetI(i)())

    Graph.StrAttrValueNI(NId, NIdStrAttrValue)
    AttrLen = NIdStrAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node16 (str): %i, Attr_Val: %s" % (NId, NIdStrAttrValue.GetI(i)())

    print "DeletedN: %i, Attr: %s, %s" % (NId, attr1, Graph.IsAttrDeletedN(NId, attr1))
    print "DeletedN: %i, Attr: %s, %s" % (NId, attr2, Graph.IsAttrDeletedN(NId, attr2))
    print "DeletedN: %i, Attr: %s, %s" % (NId, attr3, Graph.IsAttrDeletedN(NId, attr3))
    print "DeletedN: %i, Attr: %s, %s" % (NId, attr4, Graph.IsAttrDeletedN(NId, attr4))
    print "DeletedN (str): %i, Attr: %s, %s" % (NId, attr1, Graph.IsStrAttrDeletedN(NId, attr1))
    print "DeletedN (int): %i, Attr: %s, %s" % (NId, attr2, Graph.IsIntAttrDeletedN(NId, attr2))
    print "DeletedN (flt): %i, Attr: %s, %s" % (NId, attr3, Graph.IsFltAttrDeletedN(NId, attr3))
    print "DeletedN (str): %i, Attr: %s, %s" % (NId, attr4, Graph.IsStrAttrDeletedN(NId, attr4))
    print "DeletedN (int): %i, Attr: %s, %s" % (NId, attr4, Graph.IsIntAttrDeletedN(NId, attr4))
    print "DeletedN (flt): %i, Attr: %s, %s" % (NId, attr4, Graph.IsFltAttrDeletedN(NId, attr4))

    Graph.DelAttrDatN(NId, attr2)
    print "DeletedN: %i, Attr: %s, %s" % (NId, attr2, Graph.IsAttrDeletedN(NId, attr2))
    print "DeletedN (int): %i, Attr: %s, %s" % (NId, attr2, Graph.IsIntAttrDeletedN(NId, attr2))

    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node2 (no int): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.AddIntAttrDatN(NId, 3*2, attr2)
    Graph.DelAttrN(attr1)
    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node3 (no str): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.AttrValueNI(NId, NIdAttrValue)
    AttrLen = NIdAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node4 (no str): %i, Attr_Val: %s" % (NId, NIdAttrValue.GetI(i)())

    for i in range(NNodes):
        Graph.AddIntAttrDatN(i, 70, attr2)

    total = 0
    NI = Graph.BegNAIntI(attr2)
    while NI < Graph.EndNAIntI(attr2):
        total += NI.GetDat()
        NI.Next()

    print "Average: %i (should be 70)" % (total/NNodes)
    if total/NNodes != 70:
        print "*** Error1"

    # Test column iterator for edge
    Graph.AddIntAttrDatE(3, 3*2, attr2)
    Graph.AddIntAttrDatE(55, 55*2, attr2)
    Graph.AddIntAttrDatE(705, 705*2, attr2)
    Graph.AddIntAttrDatE(905, 905*2, attr2)
    EdgeId = 0
    EI = Graph.BegEAIntI(attr2)
    while EI < Graph.EndEAIntI(attr2):
        if EI.GetDat() != snap.TInt.Mn:
            print "E Attribute1: %s, Edge: %i, Val: %i" % (
                attr2, EdgeId, EI.GetDat())
            #% (attr2(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column flt iterator for edge
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
            print "E Attribute2: %s, Edge: %i, Val: %f" % (
                attr3, EdgeId, EI.GetDat())
            #(attr3(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column str iterator for edge
    #Graph.AddStrAttrDatE(10, TStr("abc"), attr1)
    #Graph.AddStrAttrDatE(20, TStr("def"), attr1)
    #Graph.AddStrAttrDatE(400, TStr("ghi"), attr1)
    Graph.AddStrAttrDatE(10, "abc", attr1)
    Graph.AddStrAttrDatE(20, "def", attr1)
    Graph.AddStrAttrDatE(400, "ghi", attr1)
    # this does not show since ""=null
    #Graph.AddStrAttrDatE(455, TStr(""), attr1)
    # TODO Graph.AddStrAttrDatE(455, "", attr1)
    EdgeId = 0
    EI = Graph.BegEAStrI(attr1)
    while EI < Graph.EndEAStrI(attr1):
        if EI.GetDat() != snap.TStr.GetNullStr():
            print "E Attribute3: %s, Edge: %i, Val: %s" % (
                attr1, EdgeId, EI.GetDat())
            #(attr1(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column iterator over many types (must skip default/deleted attr)
    EId = 55
    #Graph.AddStrAttrDatE(EId, TStr("aaa"), attr1)
    Graph.AddStrAttrDatE(EId, "aaa", attr1)
    Graph.AddIntAttrDatE(EId, 3*2, attr2)
    Graph.AddFltAttrDatE(EId, 3.41, attr3)
    #Graph.AddStrAttrDatE(80, TStr("dont appear"), attr4) # should not show up
    Graph.AddStrAttrDatE(80, "dont appear", attr4) # should not show up

    attr1idx = Graph.GetAttrIndE(attr1)
    attr2idx = Graph.GetAttrIndE(attr2)
    attr3idx = Graph.GetAttrIndE(attr3)
    attr4idx = Graph.GetAttrIndE(attr4)
    print "Edge attribute indexes:  %s %d,   %s %d,   %s %d,   %s %d" % (
            attr1, attr1idx, attr2, attr2idx, attr3, attr3idx, attr4, attr4idx)

    print "EId attributes: %i, %s %d %.2f" % (
            EId,
            Graph.GetStrAttrDatE(EId, attr1),
            Graph.GetIntAttrDatE(EId, attr2),
            Graph.GetFltAttrDatE(EId, attr3))

    print "ind attributes: %i, %s %d %.2f" % (
            EId,
            Graph.GetStrAttrIndDatE(EId, attr1idx),
            Graph.GetIntAttrIndDatE(EId, attr2idx),
            Graph.GetFltAttrIndDatE(EId, attr3idx))

    EIdAttrName = snap.TStrV()
    EIdAttrValue = snap.TStrV()
    EIdIntAttrValue = snap.TIntV()
    EIdFltAttrValue = snap.TFltV()
    EIdStrAttrValue = snap.TStrV()

    EdgeId = 0
    EI = Graph.BegEAIntI(attr2)
    while EI < Graph.EndEAIntI(attr2):
        if EI.GetDat() != snap.TInt.Mn:
            print "E Attribute1: %s, Edge: %i, Val: %i" % (
                attr2, EdgeId, EI.GetDat())
            #% (attr2(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    Graph.AttrValueEI(EId, EIdAttrValue)
    AttrLen = EIdAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge4 (no str): %i, Attr_Val: %s" % (EId, EIdAttrValue.GetI(i)())

    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge1: %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.IntAttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge11 (int): %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.FltAttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge12 (flt): %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.StrAttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge13 (str): %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.IntAttrValueEI(EId, EIdIntAttrValue)
    AttrLen = EIdIntAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge14 (int): %i, Attr_Val: %d" % (EId, EIdIntAttrValue.GetI(i)())

    Graph.FltAttrValueEI(EId, EIdFltAttrValue)
    AttrLen = EIdFltAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge15 (flt): %i, Attr_Val: %.2f" % (EId, EIdFltAttrValue.GetI(i)())

    Graph.StrAttrValueEI(EId, EIdStrAttrValue)
    AttrLen = EIdStrAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge16 (str): %i, Attr_Val: %s" % (EId, EIdStrAttrValue.GetI(i)())

    print "DeletedE: %i, Attr: %s, %s" % (EId, attr1, Graph.IsAttrDeletedE(EId, attr1))
    print "DeletedE: %i, Attr: %s, %s" % (EId, attr2, Graph.IsAttrDeletedE(EId, attr2))
    print "DeletedE: %i, Attr: %s, %s" % (EId, attr3, Graph.IsAttrDeletedE(EId, attr3))
    print "DeletedE: %i, Attr: %s, %s" % (EId, attr4, Graph.IsAttrDeletedE(EId, attr4))
    print "DeletedE (str): %i, Attr: %s, %s" % (EId, attr1, Graph.IsStrAttrDeletedE(EId, attr1))
    print "DeletedE (int): %i, Attr: %s, %s" % (EId, attr2, Graph.IsIntAttrDeletedE(EId, attr2))
    print "DeletedE (flt): %i, Attr: %s, %s" % (EId, attr3, Graph.IsFltAttrDeletedE(EId, attr3))
    print "DeletedE (str): %i, Attr: %s, %s" % (EId, attr4, Graph.IsStrAttrDeletedE(EId, attr4))
    print "DeletedE (int): %i, Attr: %s, %s" % (EId, attr4, Graph.IsIntAttrDeletedE(EId, attr4))
    print "DeletedE (flt): %i, Attr: %s, %s" % (EId, attr4, Graph.IsFltAttrDeletedE(EId, attr4))

    Graph.DelAttrDatE(EId, attr2)
    print "DeletedE: %i, Attr: %s, %s" % (EId, attr2, Graph.IsAttrDeletedE(EId, attr2))
    print "DeletedE (int): %i, Attr: %s, %s" % (EId, attr2, Graph.IsIntAttrDeletedE(EId, attr2))

    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge2 (no int): %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.AddIntAttrDatE(EId, 3*2, attr2)
    Graph.DelAttrE(attr1)
    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge3 (no str): %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.AttrValueEI(EId, EIdAttrValue)
    AttrLen = EIdAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge4 (no str): %i, Attr_Val: %s" % (EId, EIdAttrValue.GetI(i)())

    for i in range(NEdges):
        Graph.AddIntAttrDatE(i, 70, attr2)

    total = 0
    EI = Graph.BegNAIntI(attr2)
    while EI < Graph.EndNAIntI(attr2):
        total += EI.GetDat()
        EI.Next()

    print "Average: %i (should be 70)" % (total/NEdges)
    if total/NNodes != 70:
        print "*** Error2"
  
    Graph.Clr()

def ManipulateAttributesIter():
    '''
        Test node, edge attribute functionality using iterators
    '''

    NNodes = 1000
    NEdges = 1000
  
    Graph = snap.TNEANet.New()
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
    #attr1 = TStr("str")
    #attr2 = TStr("int")
    #attr3 = TStr("float")
    #attr4 = TStr("default")
    attr1 = "STR"
    attr2 = "INT"
    attr3 = "FLOAT"
    attr4 = "DEFAULT"
  
    # Test column int iterator for node 3, 50, 700, 900
    # Check if we can set defaults to 0 fordata.
    Graph.AddIntAttrN(attr2, 0)
    NI3 = Graph.GetNI(3)
    NI50 = Graph.GetNI(50)
    NI700 = Graph.GetNI(700)
    NI900 = Graph.GetNI(900)
    Graph.AddIntAttrDatN(NI3, 3*2, attr2)
    Graph.AddIntAttrDatN(NI50, 50*2, attr2)
    Graph.AddIntAttrDatN(NI700, 700*2, attr2)
    Graph.AddIntAttrDatN(NI900, 900*2, attr2)
        
    print "Added attributes"
        
    NodeId = 0
    NI = Graph.BegNAIntI(attr2)
    while NI < Graph.EndNAIntI(attr2):
        if NI.GetDat() != 0:
           print "Attribute1: %s, Node: %i, Val: %d" % (attr2, NodeId, NI.GetDat())
           #print "Attribute: %s, Node: %i, Val: %d" % (attr2(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column flt iterator for node 3, 50, 700, 900
    NI5 = Graph.GetNI(5)
    NI50 = Graph.GetNI(50)
    NI300 = Graph.GetNI(300)
    NI653 = Graph.GetNI(653)
    Graph.AddFltAttrDatN(NI5, 3.41, attr3)
    Graph.AddFltAttrDatN(NI50, 2.718, attr3)
    Graph.AddFltAttrDatN(NI300, 150.0, attr3)
    Graph.AddFltAttrDatN(NI653, 653, attr3)

    NodeId = 0
    NCount = 0
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        NCount += 1
        NI.Next()

    NI = Graph.BegNAFltI(attr3)
    NodeId = 0
    while NI < Graph.EndNAFltI(attr3):
        if NI.GetDat() != snap.TFlt.Mn:
            print "Attribute2: %s, Node: %i, Val: %f" % (attr3, NodeId, NI.GetDat())
            #print "Attribute: %s, Node: %i, Val: %f" % (attr3(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column str iterator for node 3, 50, 700, 900
    NI10 = Graph.GetNI(10)
    NI20 = Graph.GetNI(20)
    NI400 = Graph.GetNI(400)
    #Graph.AddStrAttrDatN(10, TStr("abc"), attr1)
    #Graph.AddStrAttrDatN(20, TStr("def"), attr1)
    #Graph.AddStrAttrDatN(400, TStr("ghi"), attr1)
    Graph.AddStrAttrDatN(NI10, "abc", attr1)
    Graph.AddStrAttrDatN(NI20, "def", attr1)
    Graph.AddStrAttrDatN(NI400, "ghi", attr1)
    # this does not show since ""=null
    #Graph.AddStrAttrDatN(455, TStr(""), attr1)
    # TODO Graph.AddStrAttrDatN(455, "", attr1)
    NodeId = 0

    NI = Graph.BegNAStrI(attr1)
    NodeId = 0
    while NI < Graph.EndNAStrI(attr1):
        if NI.GetDat() != snap.TStr.GetNullStr():
            print "Attribute3: %s, Node: %i, Val: %s" % (attr1, NodeId, NI.GetDat())
            #print "Attribute: %s, Node: %i, Val: %s" % (attr1(), NodeId, NI.GetDat())
        NodeId += 1
        NI.Next()

    # Test column iterator over many types (must skip default/deleted attr)
    NId = 55
    NI55 = Graph.GetNI(55)
    NI80 = Graph.GetNI(80)
    #Graph.AddStrAttrDatN(NId, TStr("aaa"), attr1)
    Graph.AddStrAttrDatN(NI55, "aaa", attr1)
    Graph.AddIntAttrDatN(NI55, 3*2, attr2)
    Graph.AddFltAttrDatN(NI55, 3.41, attr3)
    #Graph.AddStrAttrDatN(80, TStr("dont appear"), attr4) # should not show up
    Graph.AddStrAttrDatN(NI80, "dont appear", attr4) # should not show up

    attr1idx = Graph.GetAttrIndN(attr1)
    attr2idx = Graph.GetAttrIndN(attr2)
    attr3idx = Graph.GetAttrIndN(attr3)
    attr4idx = Graph.GetAttrIndN(attr4)
    print "Node attribute indexes:  %s %d,   %s %d,   %s %d,   %s %d" % (
            attr1, attr1idx, attr2, attr2idx, attr3, attr3idx, attr4, attr4idx)

    NI = Graph.GetNI(NId)
    print "NI  attributes: %i, %s %d %.2f" % (
            NI.GetId(),
            Graph.GetStrAttrDatN(NI, attr1),
            Graph.GetIntAttrDatN(NI, attr2),
            Graph.GetFltAttrDatN(NI, attr3))

    print "ind attributes: %i, %s %d %.2f" % (
            NI.GetId(),
            Graph.GetStrAttrIndDatN(NI, attr1idx),
            Graph.GetIntAttrIndDatN(NI, attr2idx),
            Graph.GetFltAttrIndDatN(NI, attr3idx))

    NIdAttrName = snap.TStrV()
    NIdAttrValue = snap.TStrV()
    NIdIntAttrValue = snap.TIntV()
    NIdFltAttrValue = snap.TFltV()
    NIdStrAttrValue = snap.TStrV()

    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node1: %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    NIdAttrName = snap.TStrV()
    Graph.IntAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node11 (int): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    NIdAttrName = snap.TStrV()
    Graph.FltAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node12 (flt): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    NIdAttrName = snap.TStrV()
    Graph.StrAttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node13 (str): %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.IntAttrValueNI(NId, NIdIntAttrValue)
    AttrLen = NIdIntAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node14 (int): %i, Attr_Val: %d" % (NId, NIdIntAttrValue.GetI(i)())

    Graph.FltAttrValueNI(NId, NIdFltAttrValue)
    AttrLen = NIdFltAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node15 (flt): %i, Attr_Val: %.2f" % (NId, NIdFltAttrValue.GetI(i)())

    Graph.StrAttrValueNI(NId, NIdStrAttrValue)
    AttrLen = NIdStrAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node16 (str): %i, Attr_Val: %s" % (NId, NIdStrAttrValue.GetI(i)())

    Graph.DelAttrDatN(NId, attr2)
    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node2 (no int) : %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.AddIntAttrDatN(NId, 3*2, attr2)
    Graph.DelAttrN(attr1)
    Graph.AttrNameNI(NId, NIdAttrName)
    AttrLen = NIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Node3 (no str) : %i, Attr: %s" % (NId, NIdAttrName.GetI(i)())

    Graph.AttrValueNI(NId, NIdAttrValue)
    AttrLen = NIdAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Node4 (no str) : %i, Attr_Val: %s" % (NId, NIdAttrValue.GetI(i)())

    for i in range(NNodes):
        Graph.AddIntAttrDatN(i, 70, attr2)

    total = 0
    NI = Graph.BegNAIntI(attr2)
    while NI < Graph.EndNAIntI(attr2):
        total += NI.GetDat()
        NI.Next()

    print "Average: %i (should be 70)" % (total/NNodes)
    if total/NNodes != 70:
        print "*** Error3"

    # Test column iterator for edge
    EI3 = Graph.GetEI(3)
    EI55 = Graph.GetEI(55)
    EI705 = Graph.GetEI(705)
    EI905 = Graph.GetEI(905)
    Graph.AddIntAttrDatE(EI3, 3*2, attr2)
    Graph.AddIntAttrDatE(EI55, 55*2, attr2)
    Graph.AddIntAttrDatE(EI705, 705*2, attr2)
    Graph.AddIntAttrDatE(EI905, 905*2, attr2)
    EdgeId = 0
    EI = Graph.BegEAIntI(attr2)
    while EI < Graph.EndEAIntI(attr2):
        if EI.GetDat() != snap.TInt.Mn:
            print "E Attribute1: %s, Edge: %i, Val: %i" % (
                attr2, EdgeId, EI.GetDat())
            #% (attr2(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column flt iterator for edge
    Graph.AddFltAttrE(attr3, 0.00)
    EI5 = Graph.GetEI(5)
    EI50 = Graph.GetEI(50)
    EI300 = Graph.GetEI(300)
    EI653 = Graph.GetEI(653)
    Graph.AddFltAttrDatE(EI5, 4.41, attr3)
    Graph.AddFltAttrDatE(EI50, 3.718, attr3)
    Graph.AddFltAttrDatE(EI300, 151.0, attr3)
    Graph.AddFltAttrDatE(EI653, 654, attr3)
    EdgeId = 0
    EI = Graph.BegEAFltI(attr3)
    while EI < Graph.EndEAFltI(attr3):
        # Check if defaults are set to 0.
        if EI.GetDat() != 0:
            print "E Attribute2: %s, Edge: %i, Val: %f" % (
                attr3, EdgeId, EI.GetDat())
            #(attr3(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column str iterator for edge
    #Graph.AddStrAttrDatE(10, TStr("abc"), attr1)
    #Graph.AddStrAttrDatE(20, TStr("def"), attr1)
    #Graph.AddStrAttrDatE(400, TStr("ghi"), attr1)
    EI10 = Graph.GetEI(10)
    EI20 = Graph.GetEI(20)
    EI400 = Graph.GetEI(400)
    Graph.AddStrAttrDatE(EI10, "abc", attr1)
    Graph.AddStrAttrDatE(EI20, "def", attr1)
    Graph.AddStrAttrDatE(EI400, "ghi", attr1)
    # this does not show since ""=null
    #Graph.AddStrAttrDatE(455, TStr(""), attr1)
    # TODO Graph.AddStrAttrDatE(455, "", attr1)
    EdgeId = 0
    EI = Graph.BegEAStrI(attr1)
    while EI < Graph.EndEAStrI(attr1):
        if EI.GetDat() != snap.TStr.GetNullStr():
            print "E Attribute3: %s, Edge: %i, Val: %s" % (
                attr1, EdgeId, EI.GetDat())
            #(attr1(), EdgeId, EI.GetDat())
        EdgeId += 1
        EI.Next()

    # Test column iterator over many types (must skip default/deleted attr)
    EId = 55
    EI55 = Graph.GetEI(55)
    EI80 = Graph.GetEI(80)
    #Graph.AddStrAttrDatE(EId, TStr("aaa"), attr1)
    Graph.AddStrAttrDatE(EI55, "aaa", attr1)
    Graph.AddIntAttrDatE(EI55, 3*2, attr2)
    Graph.AddFltAttrDatE(EI55, 3.41, attr3)
    #Graph.AddStrAttrDatE(80, TStr("dont appear"), attr4) # should not show up
    Graph.AddStrAttrDatE(EI80, "dont appear", attr4) # should not show up

    attr1idx = Graph.GetAttrIndE(attr1)
    attr2idx = Graph.GetAttrIndE(attr2)
    attr3idx = Graph.GetAttrIndE(attr3)
    attr4idx = Graph.GetAttrIndE(attr4)
    print "Edge attribute indexes:  %s %d,   %s %d,   %s %d,   %s %d" % (
            attr1, attr1idx, attr2, attr2idx, attr3, attr3idx, attr4, attr4idx)

    EI = Graph.GetEI(EId)
    print "EI  attributes: %i, %s %d %.2f" % (
            EI.GetId(),
            Graph.GetStrAttrDatE(EI, attr1),
            Graph.GetIntAttrDatE(EI, attr2),
            Graph.GetFltAttrDatE(EI, attr3))

    print "ind attributes: %i, %s %d %.2f" % (
            EI.GetId(),
            Graph.GetStrAttrIndDatE(EI, attr1idx),
            Graph.GetIntAttrIndDatE(EI, attr2idx),
            Graph.GetFltAttrIndDatE(EI, attr3idx))

    EIdAttrName = snap.TStrV()
    EIdAttrValue = snap.TStrV()

    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge1: %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.DelAttrDatE(EId, attr2)
    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge2 (no int) : %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.AddIntAttrDatE(EId, 3*2, attr2)
    Graph.DelAttrE(attr1)
    Graph.AttrNameEI(EId, EIdAttrName)
    AttrLen = EIdAttrName.Len()
    for i in range(AttrLen):
        print "Vertical Edge3 (no str) : %i, Attr: %s" % (EId, EIdAttrName.GetI(i)())

    Graph.AttrValueEI(EId, EIdAttrValue)
    AttrLen = EIdAttrValue.Len()
    for i in range(AttrLen):
        print "Vertical Edge4 (no str) : %i, Attr_Val: %s" % (EId, EIdAttrValue.GetI(i)())

    for i in range(NEdges):
        Graph.AddIntAttrDatE(i, 70, attr2)

    total = 0
    EI = Graph.BegNAIntI(attr2)
    while EI < Graph.EndNAIntI(attr2):
        total += EI.GetDat()
        EI.Next()

    print "Average: %i (should be 70)" % (total/NEdges)
    if total/NNodes != 70:
        print "*** Error4"
  
    Graph.Clr()

if __name__ == '__main__':
    print "----- DefaultConstructor -----"
    DefaultConstructor()
    print "----- ManipulateNodesEdges -----"
    ManipulateNodesEdges()
    print "----- ManipulateAttributesId -----"
    ManipulateAttributesId()
    print "----- ManipulateAttributesIter -----"
    ManipulateAttributesIter()

