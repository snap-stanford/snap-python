import os
import sys
import time

sys.path.append("../swig")

import snap

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <graph_file>"
        sys.exit(1)

    gname = sys.argv[1]

    tname = snap.TStr(gname)

    t1 = time.time()
    print time.ctime(t1)

    Graph = snap.LoadEdgeList_PNGraph(tname, 0, 1)
    t2 = time.time()
    print "%s loadg %.2fs" % (time.ctime(t2), t2-t1)

    # count the nodes
    NCount = 0
    NI = Graph.BegNI()
    while NI < Graph.EndNI():
        NCount += 1
        NI.Next()
    t3 = time.time()
    print "%s nodei %.2fs" % (time.ctime(t3), t3-t2)

    # count the edges
    ECount = 0;
    EI = Graph.BegEI()
    while EI < Graph.EndEI():
        ECount += 1
        EI.Next()
    t4 = time.time()
    print "%s edgei %.2fs" % (time.ctime(t4), t4-t3)

    print "nodes %d, edges %d" % (NCount, ECount)
    time.sleep(60)


