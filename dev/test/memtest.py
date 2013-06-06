import os
import sys

sys.path.append("../swig")

import snap

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <graph>"
        sys.exit(1)

    gname = sys.argv[1]
    tname = snap.TStr(gname)

    count = 0
    #l = []
    while 1:
        g = snap.LoadEdgeList_PNGraph(tname, 0, 1)
        #l.append(g)

        count += 1
        if count % 100 == 0:
            print count

        if count > 1000:
            break
