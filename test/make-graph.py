import sys

import snap

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <input_file>")
        sys.exit(1)

    fname = sys.argv[1]

    context = snap.TTableContext()

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("SrcNode", snap.atStr))
    schema.Add(snap.TStrTAttrPr("DstNode", snap.atStr))
    schema.Add(snap.TStrTAttrPr("EdgeType", snap.atStr))

    T1 = snap.TTable.LoadSS(schema, fname, context, "\t", snap.TBool(False))
    print("T1 #rows", T1.GetNumRows())

    G1 = snap.ToGraph(snap.PNGraph, T1, "SrcNode", "DstNode", snap.aaFirst)
    print("G1 #nodes", G1.GetNodes())
    print("G1 #edges", G1.GetEdges())

    G1.PrintInfo("Graph Statistics", "graph-stats.txt", False)

