import os
import sys
import time
from random import randrange, choice
from socket import gethostname

sys.path.append("../swig")

import snap as Snap

MIN_NODES_EXPONENT = 2
MAX_NODES_EXPONENT = 4
NUM_ITERATIONS = 10
PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS
GRAPH_TYPES = [0, 3, 4] # Small World, Pref, R-MAT
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
      
          print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
      
          fname = "%s%s" % (Snap.GetGraphAbbr(g), 'deg%d' % AVG_DEG if avg else '')
          # Repeat for all graph types
          for j in PROPERTY_TYPES:
            t = Snap.GetStats(NNodes, NEdges, j, g)
            f = open('%s/%s_%s.txt' % (RESULTS_DIR, Snap.GetAttributeAbbr(j),
                                       fname),
                     'a+')
            f.write("%d %d %.5f\n" % (NNodes, NEdges, t))

            f_all = open('%s/%s_all.txt' % (RESULTS_DIR,
                                            Snap.GetAttributeAbbr(j)),
                         'a+')
            f_all.write("%d %d %.5f\n" % (NNodes, NEdges, t))
  
    # For each characteristic:
    # Write out test data to same file (linear fit using matlab?)
    # NNodes NEdges Time
    
  print "-"*75


# --------------- Plotting ---------------
import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import sort,array,ones,linalg,column_stack,loadtxt,savetxt
from scipy import *
from scipy.optimize import leastsq
from scipy import linalg

import pdb
  
def plot_2d(property):
  
  # Plot average degree on 2d-graph
  figure()
  for g in GRAPH_TYPES:
    
    fname = '%s/%s_%sdeg%d.txt' % (RESULTS_DIR, Snap.GetAttributeAbbr(property),
                                   Snap.GetGraphAbbr(g), AVG_DEG)
    A = loadtxt(fname)
    A = sort(A,0)
    Y = A[:,-1]     # Last column
    X = A[:,:-1]    # Columns 0-(n-1)
    
    loglog(X[:,0], Y, 'o', label=Snap.GetGraphDesc(g))
    
    legend(loc='lower right')
    xlabel('Num Nodes (d_avg = %.1f)' % AVG_DEG)
    ylabel('time')
    title('%s runtime (avg degree = %d)' % (Snap.GetAttributeDesc(property), AVG_DEG))
    pname = '%s/plot2d_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(property))
    print "Saving figure %s" % pname
    savefig(pname)

# Plot using 3D-graph
def plot_3d(property):
  
  import mpl_toolkits.mplot3d.axes3d as p3
  fig3d = figure()
  ax = fig3d.add_subplot(111, projection='3d')
  
  for g in GRAPH_TYPES:
    fname = '%s/%s_%s.txt' % (RESULTS_DIR, Snap.GetAttributeAbbr(property),
                              Snap.GetGraphAbbr(g))
    
    A = loadtxt(fname)
    A = sort(A,0)
    Y = A[:,-1]     # Last column
    X = A[:,:-1]    # Columns 0-(n-1)
    #      savetxt(fname+'_sorted.txt', A)
    
    Nodes = X[:,0]
    Edges = X[:,1]
    ax.plot(Nodes,Edges,Y,'o',
           label="%s-%s" % (Snap.GetAttributeAbbr(property),
                            Snap.GetGraphAbbr(g)))
  
  ax.set_xlabel('# of nodes', fontsize=9)
  ax.set_ylabel('# of edges', fontsize=9)
  ax.set_zlabel('Run time %s (sec)' % Snap.GetAttributeAbbr(property),
                fontsize=9)
  ax.legend()

#  ax.set_xlim3d([0, 10**MAX_NODES_EXPONENT])
#  ax.set_ylim3d([0, 10**MAX_NODES_EXPONENT*AVG_DEGREE_RANGE[1]])
#  ax.set_zlim3d([0, max(Y)])
#  ax.set_xscale('log')
#  ax.w_xaxis.set_scale('log')
#  ax.w_yaxis.set_scale('log')
#  ax.set_zscale('log')
#  ax.auto_scale_xyz([0, max(Nodes)], [0, max(Edges)], [0, max(Y)])
#  ax.title("%s run time" % Snap.GetAttributeAbbr(property))
  pname = '%s/plot3d_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(property))
  print "Saving figure %s" % pname

  fig3d.savefig(pname)

# Fitting the data using given model and least squares
def plot_fit(Xdata, Ydata, labelstr, fit_type):
  
  X1 = Xdata[:,0]  # Nodes
  X2 = Xdata[:,1]  # Edges
  Y = Ydata
  
  best_r2 = 0
  
  if "poly" in fit_type:
    # Polynomial fit
    fitfunc = lambda p, x1, x2: (p[0] + p[1] * x1 + p[2] * x2 +
                                 p[3] * x1**2 + p[4] * x2**2)
    pinit = [1.0 for i in range(5)]
  
  if "exp" in fit_type:
    # Exponential fit
    Y = log(Y)
    fitfunc = lambda p, x1, x2: (p[0] + p[1] * x1 + p[3] * x2)
    pinit = [1.0 for i in range(5)]
  
  if "log" in fit_type:
    # Logarithmic fit
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
  
  labelstr = "%s (r2=%.3f)" % (fit_type, rsquared)
  plot(X1, errfunc(pfinal, Y, X1, X2), '.', label=labelstr)

  return (rsquared, pfinal)

# Calculate and Plot Residual Errors
def plot_residuals(property):

  # Calculate residuals for all graph types, and combined
  for g in GRAPH_TYPES + [-1]:
    
    figure()
    
    if g == -1:
      # All graphs
      fname = '%s/%s_all.txt' % (RESULTS_DIR, Snap.GetAttributeAbbr(property))

    else:
      fname = '%s/%s_%s.txt' % (RESULTS_DIR, Snap.GetAttributeAbbr(property),
                                Snap.GetGraphAbbr(g))
    
    A = loadtxt(fname)
    A = sort(A,0)
    Y = A[:,-1]     # Last column
    X = A[:,:-1]    # Columns 0-(n-1)
    #      savetxt(fname+'_sorted.txt', A)
    
    best_r2 = 0.0
    best_model = None
    p_best = None
    
    if g == -1:
      desc = 'all'
      abbr = 'all'
    else:
      desc = Snap.GetGraphDesc(g)
      abbr = Snap.GetGraphAbbr(g)

    print "Fitting %s for %s" % (Snap.GetAttributeDesc(property), desc)

    f = open('%s/coeff_%s.txt' %
             (RESULTS_DIR, Snap.GetAttributeDesc(property)), 'a+')

    for model in ['poly', 'exp', 'log']:
      # Plot residuals with multiple fitting types
      rsquared, pfinal = plot_fit(X, Y, desc, model)
          
      f.write("%s, model=%s r2=%.4f pfinal=%s\n" %
              (abbr, model, rsquared, pfinal))

      if (rsquared > best_r2):
        best_r2 = rsquared
        best_model = model
        p_best = pfinal
  
  
    title('Run-time approx. for %s (%s)' %
          (Snap.GetAttributeDesc(property).title(), desc))
    xscale('log')
    grid(True)
    xlabel('Number of Nodes')
    ylabel('Residual')
    legend()
    pname = '%s/residuals_%s_%s.png' % (RESULTS_DIR,
                                        Snap.GetAttributeAbbr(property),
                                        desc)
    print "Saving figure %s" % pname
    savefig(pname)
    print "Best model: %s, r2 = %.3f, pfinal: %s" % \
            (best_model, best_r2, repr(p_best))

def plot_stats():
  
  for type in PROPERTY_TYPES:
    
    plot_3d(type)

    plot_2d(type)

    plot_residuals(type)

    #end for loop - graph type

  #end for loop - plot type

if __name__ == '__main__':
  
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)
  
  for n in range(NUM_ITERATIONS):

    calc_stats()
    
    # Update plots every 5 iterations
    if (n+1) % 5 == 0:
      print "Iteration %d of %d:" % (n+1, NUM_ITERATIONS)
      plot_stats()

  plot_stats()



