import os
import sys
import time
from socket import gethostname

sys.path.append("../swig")

import snap as Snap

MIN_NODES_EXPONENT = 1
MAX_NODES_EXPONENT = 4
NUM_ITERATIONS = 4
PLOT_TYPES = Snap.PlotMx  # Max of 7
GRAPH_TYPES = (0, 3, 4)
HOSTNAME = gethostname().split('.')[0]
#GRAPH_TYPES = 5

RESULTS_DIR = "results-%s" % HOSTNAME
#RESULTS_DIR = "results-%s" % time.strftime("%m-%d-%H%M.%S")

def calc_stats():
  
  from random import randrange
  
  for g in GRAPH_TYPES:
    
    for e in range(MIN_NODES_EXPONENT,MAX_NODES_EXPONENT+1):
        
        # Random number of nodes of degree i
        NNodes = randrange(10**e,10**(e+1))
        
        # Random number of edges (from 1-3x nodes)
        NEdges = randrange(NNodes, NNodes*3)
        
        print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
        
        # Repeat for all graph types
        for j in range(PLOT_TYPES):
          t = Snap.GetStats(NNodes, NEdges, j, g)
          f = open('%s/%s-%s.txt' % (RESULTS_DIR, Snap.GetGraphAbbr(g),
                                     Snap.GetAttributeAbbr(j)), 'a+')
          f.write("%d %d %.5f\n" % (NNodes, NEdges, t))
    
    # For each characteristic:
    # Write out test data to same file (linear fit using matlab?)
    # NNodes NEdges Time
    
  print "-"*75

# run tests on infolab machines
# get processor speed (and memory)
# sysctl -a | grep hw.cpufrequency

def plot_stats():
  
  from numpy import sort,array,ones,linalg,column_stack,loadtxt
  import matplotlib
  matplotlib.use('Agg')
  from pylab import plot,show,xlabel,ylabel,savefig,title,figure,legend

#  xi = arange(0,9)
#  A = array([ xi, ones(9)])

  for type in range(PLOT_TYPES):
    figure()
    
    for g in GRAPH_TYPES:
    
      fname = '%s/%s-%s.txt' % (RESULTS_DIR, Snap.GetGraphAbbr(g),
                                Snap.GetAttributeAbbr(type))
      print "Plotting '%s'" % fname
      A = loadtxt(fname)
      A = sort(A,0)
      Y = A[:,-1]     # Last column
      X = A[:,:-1]    # Columns 0-(n-1)
      
  #    print "Y = ", Y, "X = ", X
      # Add column of 1's for intercept
      X = column_stack([X, ones(len(X))])

      # Fit using least-squares
      w = linalg.lstsq(X,Y)[0] # obtaining the parameters
      print "N = %d" % len(X)
      print "coefficients = ", w
      
      # Plot the line
      line = w[0]*X[:,0] + w[1]*X[:,1] + w[2] # get regression line
      plot(X[:,0], Y,'o', label=Snap.GetGraphDesc(g))
      plot(X[:,0], line, label="%s-fit" % Snap.GetGraphDesc(g))
      legend()
      xlabel('Num Nodes')
      ylabel('time (2.6 GHz)')
      title('%s run time (%s)' % (Snap.GetAttributeDesc(type), HOSTNAME))
      
    pname = '%s/plot_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(type))
    print "Saving figure %s" % pname
  
  #end for - graph type
    savefig(pname)

    coeff_file = open('%s/coeff.txt' % RESULTS_DIR, 'w+')
    coeff_file.write('%d %.4f %.4f %.4f\n' % (type, w[0], w[1], w[2]))

if __name__ == '__main__':
  
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

  for n in range(NUM_ITERATIONS):

#    calc_stats()
    # Update plots every 5 iterations
    if (n+1) % 2 == 0:
      print "Iteration %d of %d:" % (n+1, NUM_ITERATIONS)
      plot_stats()

