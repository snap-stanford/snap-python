import os
import sys

sys.path.append("../swig")

import snap as Snap
from random import randrange

DATA_DIR = "data"
MAX_NODES_EXP = 8
NUM_ITERATIONS = 10
PLOT_TYPES = 7

if __name__ == '__main__':

  for i in range(1,MAX_NODES_EXP):
    for n in range(NUM_ITERATIONS):
      NNodes = randrange(10**i,10**(i+1))
      NEdges = randrange(NNodes, NNodes*3)
      print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
      for j in range(PLOT_TYPES):
        t = Snap.GetStats_PNGraph(NNodes, NEdges, j)
        print "t = %.3fs" % t
        f = open('%s/data%s.txt' % (DATA_DIR, Snap.GetAbbrev(j)), 'a+')
        f.write("%d %d %.5f\n" % (NNodes, NEdges, t))
    
        # For each characteristic:
        # Write out test data to same file (linear fit using matlab?)
        # NNodes NEdges Time
  
    print "-"*75

# run tests on infolab machines
# get processor speed (and memory)
# sysctl -a | grep hw.cpufrequency