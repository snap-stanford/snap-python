#
#   build a graph and calculate various graph properties

import os
import snap
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: %s <file> <column1> <column2>" % (sys.argv[0])
        sys.exit(1)

    fname = sys.argv[1]
    col1 = int(sys.argv[2]) - 1
    col2 = int(sys.argv[3]) - 1

    G = snap.LoadEdgeList(snap.PNGraph, fname, col1, col2)
    print "\ngraph nodes %d, edges %d" % (G.GetNodes(), G.GetEdges())

    WccV = snap.TIntPrV()
    snap.GetWccSzCnt(G, WccV)

    print "\n# of connected component sizes", WccV.Len()
    for comp in WccV:
        print "size %d, number of components %d" % (comp.GetVal1(), comp.GetVal2())

    MxWcc = snap.GetMxWcc(G)
    print "\nmax wcc nodes %d, edges %d" % (MxWcc.GetNodes(), MxWcc.GetEdges())

    InDegCntV = snap.TIntPrV()
    snap.GetInDegCnt(G, InDegCntV)

    print "\n# of different in-degrees", InDegCntV.Len()
    for item in InDegCntV:
        print "%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1())

    OutDegCntV = snap.TIntPrV()
    snap.GetOutDegCnt(G, OutDegCntV)

    print "\n# of different out-degrees", OutDegCntV.Len()
    for item in OutDegCntV:
        print "%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1())

    PRankH = snap.TIntFltH()
    snap.GetPageRank(G, PRankH)
    #for item in PRankH:
    #    print item, PRankH[item]

    slist = sorted(PRankH, key = lambda key: float(PRankH[key]), reverse = True)
    print "\ntop 10 experts by PageRank"
    for item in slist[:10]:
            print item,PRankH[item]

    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(G, NIdHubH, NIdAuthH)
    slist = sorted(NIdAuthH, key = lambda key: float(NIdAuthH[key]), reverse = True)
    print "\ntop 10 experts by Hits"
    for item in slist[:10]:
        print item, NIdAuthH[item]

    slist = sorted(NIdHubH, key = lambda key: float(NIdHubH[key]), reverse = True)
    print "\ntop 10 learners by Hits"
    for item in slist[:10]:
        print item, NIdHubH[item]

