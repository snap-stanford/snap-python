#
#   clique percolation method for community detection
#

import sys

import snap

def cmp(gname, size):
    G = snap.LoadEdgeList(snap.PUNGraph, gname, 0, 1)
    print "G: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())

    Communities = snap.TIntIntVV()
    snap.TCliqueOverlap_GetCPMCommunities(G, size, Communities)

    print "---------------"
    for C in Communities:
        for I in C:
            print I
        print "---------------"

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] + " <graph_file> <size>"
        sys.exit(1)

    gname = sys.argv[1]
    size = int(sys.argv[2])

    cmp(gname, size)

