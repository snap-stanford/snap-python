# printstat.py
# python printstat.py data/p2p-Gnutella08.txt p2p

import os
import sys

sys.path.insert(0,"../swig")

import snap

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] + " <graph_file> <header_text>"
        sys.exit(1)

    gname = sys.argv[1]
    header = sys.argv[2]

    tlabel = snap.TStr(os.path.splitext(gname)[0])
    theader = snap.TStr(header)

    g = snap.LoadEdgeList(snap.PNGraph, gname, 0, 1)
    snap.PrintGraphStatTable(g,tlabel,theader)
