import os
import sys
import time
from random import randrange, choice
from socket import gethostname

sys.path.append("../swig")

import snap as Snap

MIN_NODES_EXPONENT = 2
MAX_NODES_EXPONENT = 4
NUM_ITERATIONS = 5
PROPERTY_TYPES = [1]   # Max of 8
GRAPH_TYPES = [4]    # Just RMAT for now
DEGREE_TYPES = [0, 1]

HOSTNAME = gethostname().split('.')[0]
AVG_DEG = 3
AVG_DEGREE_RANGE = range(2, 10)
#GRAPH_TYPES = 5

RESULTS_DIR = "results-%s" % HOSTNAME
#RESULTS_DIR = "results-%s" % time.strftime("%m-%d-%H%M.%S")

def calc_stats():
  
  for g in GRAPH_TYPES:
    
    for e in range(MIN_NODES_EXPONENT,MAX_NODES_EXPONENT+1):
        
        # Random number of nodes of degree i
        NNodes = randrange(10**e,10**(e+1))
      
        for avg in DEGREE_TYPES:
        
          if avg:
            # Use average degree
            NEdges = NNodes*AVG_DEG
          
          else:
            # Random number of edges (from 1-3x nodes)
            NEdges = NNodes * choice(AVG_DEGREE_RANGE)

          fname = "%s%s" % (Snap.GetGraphAbbr(g), 'deg%d' % AVG_DEG if avg else '')

          print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
          
          # Repeat for all graph types
          for j in PROPERTY_TYPES:
            t = Snap.GetStats(NNodes, NEdges, j, g)
            f = open('%s/%s_%s.txt' % (RESULTS_DIR, fname,
                                       Snap.GetAttributeAbbr(j)), 'a+')
            f.write("%d %d %.5f\n" % (NNodes, NEdges, t))
  
    # For each characteristic:
    # Write out test data to same file (linear fit using matlab?)
    # NNodes NEdges Time
    
  print "-"*75

import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import sort,array,ones,linalg,column_stack,loadtxt,savetxt
from scipy import *
from scipy.optimize import leastsq
from scipy import linalg

import pdb
  
##########
# Fitting the data -- Least Squares Method
##########
def plot_fit(Xdata, Ydata, labelstr, fit_type):
  
  print "Fitting %s" % labelstr
  X1 = Xdata[:,0]  # Nodes
  X2 = Xdata[:,1]  # Edges
  Y = Ydata

  if fit_type == "poly":
    # define our (line) fitting function
    fitfunc = lambda p, x1, x2: (p[0] + p[1] * x1 + p[2] * x2)
    pinit = [1.0 for i in range(3)]
  
  if fit_type == "exp":
    # define our (line) fitting function
    Y = log(Y)
    fitfunc = lambda p, x1, x2: (p[0] + p[1] * x1 + p[3] * x2)
    pinit = [1.0 for i in range(5)]
                                 
  if fit_type == "log":
    # define our (line) fitting function
    fitfunc = lambda p, x1, x2: (p[0] + p[1] * log10(x1) + p[2] * log10(x2))
    pinit = [1.0 for i in range(3)]

  #  errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
  errfunc = lambda p, y, x1, x2: (y - fitfunc(p, x1, x2))

  pfinal,covar,infodict,mesg,ier = \
      leastsq(errfunc, pinit, args=(Y, X1, X2), full_output=1)
  
  print "pfinal = ", pfinal
#  print "covar: \n", covar
#  print "infodict['fvec']: ", infodict['fvec']

  ss_err=(infodict['fvec']**2).sum()
  ss_tot=((Y-Y.mean())**2).sum()
  rsquared=1-(ss_err/ss_tot)
  print "%s: rsquared = %.3f" % (fit_type, rsquared)

  labelstr = "%s (r2=%.3f)" % (fit_type, rsquared)  
  plot(X1, errfunc(pfinal, Y, X1, X2), '.', label=labelstr)

#  index = pfinal[1]
#  amp = 10.0**pfinal[0]
#  
#  indexErr = sqrt( covar[0][0] )
#  ampErr = sqrt( covar[1][1] ) * amp
#  plot(X, Y, 'o', label=label)
#  
#  Y_fit = fitfunc(pfinal,X)
#  plot(X, fitfunc(pfinal, X1, X2), '-', label=("%s-poly fit" % label))
#  plot(X, Y_fit, '-', label=("%s" % label))
#  plot(X, fitfunc(pfinal, X1, X2), '-', label=("%s-poly fit" % label))

#def func(x, a, b, c):
#  return a * numpy.exp(-b * x) + c

def plot_stats():
  
  for type in PROPERTY_TYPES:
    
    for g in GRAPH_TYPES:
    
      for avg in DEGREE_TYPES:
        fname = '%s/%s%s_%s.txt' % (RESULTS_DIR, Snap.GetGraphAbbr(g),
                                    'deg%d' % AVG_DEG if avg else '',
                                    Snap.GetAttributeAbbr(type))
        
        A = loadtxt(fname)
        A = sort(A,0)
        Y = A[:,-1]     # Last column
        X = A[:,:-1]    # Columns 0-(n-1)
  #      savetxt(fname+'_sorted.txt', A)
      
        if avg:

          figure()
          loglog(X[:,0], Y,'o', label=Snap.GetGraphDesc(g))
          legend(loc='lower right')
          xlabel('Num Nodes (d_avg = %.1f)' % AVG_DEG)
          ylabel('time')
          title('%s runtime (avg degree = %d)' % (Snap.GetGraphDesc(g), AVG_DEG))
          pname = '%s/plot_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(type))
          print "Saving figure %s" % pname
          savefig(pname)

        else:
          # Random average degree
          
          # Plot 3d
          import mpl_toolkits.mplot3d.axes3d as p3
          fig3d = figure()
          ax = fig3d.add_subplot(111, projection='3d')
          Nodes = X[:,0]
          Edges = X[:,1]
          ax.scatter(Nodes,Edges,Y)
          ax.set_xlabel('# of nodes', fontsize=9)
          ax.set_ylabel('# of edges', fontsize=9)
          ax.set_zlabel('Run time %s' % Snap.GetAttributeAbbr(type), fontsize=9)
          ax.auto_scale_xyz([0, max(Nodes)], [0, max(Edges)], [0, max(Y)])
          pname = '%s/plot3d%s_%s.png' % (RESULTS_DIR, 'deg%d' % AVG_DEG if avg else '',
                                          Snap.GetAttributeAbbr(type))
          print "Saving figure %s" % pname
          fig3d.savefig(pname)

          # Plot residuals with multiple fitting types
          figure()
          plot_fit(X, Y, "%s" % Snap.GetGraphDesc(g), 'poly')
          plot_fit(X, Y, "%s" % Snap.GetGraphDesc(g), 'exp')
          plot_fit(X, Y, "%s" % Snap.GetGraphDesc(g), 'log')
          
          title('%s Residuals' % Snap.GetAttributeDesc(type))
          xscale('log')
          grid(True)
          xlabel('Num Nodes')
          ylabel('Residuals')
          legend()
          pname = '%s/residuals%s_%s.png' % (RESULTS_DIR,'deg%d' % AVG_DEG if avg else '',
                                             Snap.GetAttributeAbbr(type))
          print "Saving figure %s" % pname
          savefig(pname)



    #end for loop - graph type
  
#    pname = '%s/plot_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(type))
#    print "Saving figure %s" % pname
#    savefig(pname)

#    coeff_file = open('%s/coeff.txt' % RESULTS_DIR, 'w+')
#    coeff_file.write('%d %.4f %.4f %.4f\n' % (type, w[0], w[1], w[2]))

  #end for loop - plot type

if __name__ == '__main__':
  
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)
  
#  for n in range(NUM_ITERATIONS):
#
#    calc_stats()
#    
#    # Update plots every 5 iterations
#    if (n+1) % 5 == 0:
#      print "Iteration %d of %d:" % (n+1, NUM_ITERATIONS)
#      plot_stats()

  plot_stats()



