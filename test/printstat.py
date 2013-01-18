import os
import sys

sys.path.append("../swig")

import snap

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] + " <graph_file> <header_text>"
        sys.exit(1)

    gname = sys.argv[1]
    header = sys.argv[2]

    tname = snap.TStr(gname)
    tlabel = snap.TStr(os.path.splitext(gname)[0])
    theader = snap.TStr(header)

    g = snap.LoadEdgeList_PNGraph(tname, 0, 1)
    snap.PrintGraphStatTable_PNGraph(g,tlabel,theader)
