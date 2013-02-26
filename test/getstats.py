import os
import sys

sys.path.append("../swig")

import snap as Snap

import time
#RESULTS_DIR = "data"
RESULTS_DIR = "results-%s" % time.strftime("%m-%d-%H%M.%S")

MAX_NODES_EXPONENT = 2
NUM_ITERATIONS = 3
PLOT_TYPES = 2

def calc_stats():
  
  from random import randrange
  
  for e in range(1,MAX_NODES_EXPONENT):
    for n in range(NUM_ITERATIONS):
      
      # Random number of nodes of degree i
      NNodes = randrange(10**e,10**(e+1))
      
      # Random number of edges (from 1-3x nodes)
      NEdges = randrange(NNodes, NNodes*3)
      
      print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
      
      # Repeat for all graph types
      for j in range(PLOT_TYPES):
        t = Snap.GetStats_PNGraph(NNodes, NEdges, j, 0)
        print "t = %.3fs" % t
        f = open('%s/%s.txt' % (RESULTS_DIR, Snap.GetAbbrev(j)), 'a+')
        f.write("%d %d %.5f\n" % (NNodes, NEdges, t))
    
    # For each characteristic:
    # Write out test data to same file (linear fit using matlab?)
    # NNodes NEdges Time
    
    print "-"*75

# run tests on infolab machines
# get processor speed (and memory)
# sysctl -a | grep hw.cpufrequency

def plot_stats():
  
  from numpy import arange,array,ones,linalg,column_stack,loadtxt
  from pylab import plot,show,xlabel,ylabel,savefig,title

  xi = arange(0,9)
  A = array([ xi, ones(9)])

  for type in range(PLOT_TYPES):    
    fname = '%s/%s.txt' % (RESULTS_DIR, Snap.GetAbbrev(type))
    print "Loading '%s'" % fname
    print open(fname,'r').read()
    A = loadtxt(fname)
    Y = A[:,-1]     # Last column
    X = A[:,:-1]    # Columns 0-(n-1)
    
    print "Y = ", Y
    
    print "X = ", X
    # Add column of 1's for intercept
    X = column_stack([X, ones(len(X))])
    
    w = linalg.lstsq(X,Y)[0] # obtaining the parameters
    
    # plotting the line
    line = w[0]*X[:,0] + w[1]*X[:,1] + w[2] # get regression line
    plot(X[:,0],line,'r-',X[:,0],Y,'o')
    xlabel('Num Nodes')
    ylabel('time (2.6 GHz)')
    title('%s Runtime' % Snap.GetDesc(type))
    savefig('%s/plot_%s.png' % (RESULTS_DIR, Snap.GetAbbrev(type)))
    
    #  show()
    coeff_file = open('%s/coeff.txt' % RESULTS_DIR, 'w+')
    coeff_file.write('%d %.4f %.4f %.4f\n' % (type, w[0], w[1], w[2]))

if __name__ == '__main__':
  
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)
  
  calc_stats()
  plot_stats()

