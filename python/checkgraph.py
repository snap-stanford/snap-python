import os
import sys
import time

sys.path.append("../swig")

import snap as Snap

#RESULTS_DIR = "results-%s" % time.strftime("%m-%d-%H%M.%S")

def check_good(Graph):
  
  print "%.3f valid nodes" % Snap

if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " <graph_file>"
    sys.exit(1)
  
  gname = sys.argv[1]
  
  tname = Snap.TStr(gname)

  print "Loading graph %s" % gname
  G = Snap.LoadEdgeList_PNGraph(tname, 0, 1)

  for degree in range(1,10):
    good = Snap.PercentDegree_PNGraph(G, degree)
    print "Percent with at least degree %d: %.3f" % (good, degree)

  print "Percent in Max Weakly Conn Comp: %.3f" % \
    Snap.PercentMxWcc_PNGraph(G)

  print "Percent in Max Strongly Conn Comp: %.3f" % \
    Snap.PercentMxScc_PNGraph(G)