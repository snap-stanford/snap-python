import os
import sys
import time

import snap

def SaveConnList(G, name):
    fout = open(name, "w")
    for NI in G.Nodes():
        l = []
        l.append(NI.GetId())
        for Id in NI.GetOutEdges():
            l.append(Id)

        l1 = list(map(lambda x: str(x), l))
        fout.write(" ".join(l1) + "\n")
    fout.close()

def printtime(tprev, note):
    t = time.time()
    lt = time.localtime(t)
    # get the time and add milliseconds
    s = time.strftime("%H:%M:%S", lt) + ("%.3f" % (t - int(t)))[1:]
    delta = "%9.3f" % (t - tprev)
    print(s, delta, note)

    return t

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <nodes> <degree>")
        sys.exit(1)

    nodes = int(sys.argv[1])
    degree = int(sys.argv[2])

    name = "test-%d-%d" % (nodes, degree)
    txtname = name + ".txt"
    adjname = name + "-adj" + ".txt"
    binname = name + ".bin"
    
    print("nodes", nodes)
    print("degree", degree)

    t = time.time()
    t = printtime(t, "generating the graph")

    G1 = snap.GenPrefAttach(nodes, degree)
    print("G1 nodes", G1.GetNodes())
    print("G1 edges", G1.GetEdges())

    t = printtime(t, "saving the graph to edge list")
    snap.SaveEdgeList(G1, txtname, "Save as tab-separated list of edges")

    t = printtime(t, "reading the graph from edge list")
    G2 = snap.LoadEdgeList(snap.PUNGraph, txtname, 0, 1)
    print("G2 nodes", G2.GetNodes())
    print("G2 edges", G2.GetEdges())

    t = printtime(t, "saving the graph to adjacency list")
    SaveConnList(G1, adjname)

    t = printtime(t, "reading the graph from adjacency list")
    G3 = snap.LoadConnList(snap.PUNGraph, adjname)
    print("G3 nodes", G3.GetNodes())
    print("G3 edges", G3.GetEdges())

    t = printtime(t, "saving the graph to binary")
    FOut = snap.TFOut(binname)
    G1.Save(FOut)
    FOut.Flush()

    t = printtime(t, "reading the graph from binary")
    FIn = snap.TFIn(binname)
    G4 = snap.TUNGraph.Load(FIn)
    print("G4 nodes", G4.GetNodes())
    print("G4 edges", G4.GetEdges())

    t = printtime(t, "reading the graph as table")
    context = snap.TTableContext()

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("SrcID", snap.atInt))
    schema.Add(snap.TStrTAttrPr("DstID", snap.atInt))

    T1 = snap.TTable.LoadSS(schema, txtname, context, "\t", snap.TBool(False))
    print("T1 rows", T1.GetNumRows())

    t = printtime(t, "converting table to graph")
    G5 = snap.ToGraph(snap.PUNGraph, T1, "SrcID", "DstID", snap.aaFirst)
    print("G5 nodes", G5.GetNodes())
    print("G5 edges", G5.GetEdges())

    printtime(t, "done")

