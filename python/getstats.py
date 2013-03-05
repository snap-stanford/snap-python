import os
import sys
import time
from socket import gethostname
import os, platform, subprocess, re

sys.path.append("../swig")

import snap as Snap

MIN_NODES_EXPONENT = 1
MAX_NODES_EXPONENT = 5
NUM_ITERATIONS = 10
PLOT_TYPES = [1]   # Max of 8
GRAPH_TYPES = [4]    # Just RMAT for now
HOSTNAME = gethostname().split('.')[0]
AVG_DEG = 3
#GRAPH_TYPES = 5

RESULTS_DIR = "results-%s" % HOSTNAME
#RESULTS_DIR = "results-%s" % time.strftime("%m-%d-%H%M.%S")

#def get_processor_name():
#  
#  os_string = sys.platform
#  
#  if 'win' in os_string:
#    return platform.processor()
#  elif 'darwin' in os_string:
#    import os
#    os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
#    command = "sysctl -n machdep.cpu.brand_string"
#    brand = subprocess.check_output(command).strip()
#    command = "sysctl -n hw.cpufrequency"
#    speed = float(subprocess.check_output(command).strip()) / 10**9
#    return "%s %.2f" % (brand, speed)
#  elif 'linux' in os_string:
#    command = "cat /proc/cpuinfo"
#    all_info = subprocess.check_output(command, shell=True).strip()
#    for line in allInfo.split("\n"):
#      if "model name" in line:
#        return re.sub( ".*model name.*:", "", line,1)
#  else:
#    return "unknown"

def calc_stats():
  
  from random import randrange
  
  for g in GRAPH_TYPES:
    
    for e in range(MIN_NODES_EXPONENT,MAX_NODES_EXPONENT+1):
        
        # Random number of nodes of degree i
        NNodes = randrange(10**e,10**(e+1))
        
        # Random number of edges (from 1-3x nodes)
#        NEdges = randrange(NNodes, NNodes*3)
        NEdges = NNodes*AVG_DEG
      
        print "NNodes=%.2e, %.2e" % (NNodes, NEdges)
        
        # Repeat for all graph types
        for j in PLOT_TYPES:
          t = Snap.GetStats(NNodes, NEdges, j, g)
          f = open('%s/%s-%s.txt' % (RESULTS_DIR, Snap.GetGraphAbbr(g),
                                     Snap.GetAttributeAbbr(j)), 'a+')
          f.write("%d %d %.5f\n" % (NNodes, NEdges, t))
    
    # For each characteristic:
    # Write out test data to same file (linear fit using matlab?)
    # NNodes NEdges Time
    
  print "-"*75

# run tests on infolab machines
# run simple calibration program, then provide estimate

import matplotlib
matplotlib.use('Agg')

from pylab import plot,loglog,show,xlabel,ylabel,savefig,title,figure,legend,grid
from numpy import sort,array,ones,linalg,column_stack,loadtxt
from scipy import *
from scipy import optimize

  
##########
# Fitting the data -- Least Squares Method
##########
def poly_fit(Xdata, Ydata, label):
  
  X = Xdata
  Y = Ydata

  # define our (line) fitting function
  fitfunc = lambda p, x: p[0] + p[1] * x
  #  errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  pinit = [1.0, 1.0]
  pfinal,covar,infodict,mesg,ier = \
      optimize.leastsq(errfunc, pinit, args=(X, Y), full_output=1)
  
  print "pfinal = ", pfinal
  print "covar: \n", covar
  
  ss_err=(infodict['fvec']**2).sum()
  ss_tot=((Y-X.mean())**2).sum()
  rsquared=1-(ss_err/ss_tot)
  print "Poly: rsquared = ", rsquared
  
  index = pfinal[1]
  amp = 10.0**pfinal[0]
  
  indexErr = sqrt( covar[0][0] )
  ampErr = sqrt( covar[1][1] ) * amp
  plot(X, Y, 'o', label=label)
  
  grid(True)
  Y_fit = fitfunc(pfinal,X)
  plot(X, Y_fit, '-', label=("%s-poly" % label))

def powerlaw_fit(Xdata, Ydata, label):
# Power-law fitting is best done by first converting
# to a linear equation and then fitting to a straight line.
#
#  y = a * x^b
#  log(y) = log(a) + b*log(x)
#

#  X = log10(Xdata)
  X = Xdata
#  Y = log10(Ydata)
  Y = Ydata
#  logyerr = yerr / ydata

  # define our (line) fitting function
  fitfunc = lambda p, x: p[0] + p[1] * x
#  errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  pinit = [1.0, -1.0]
  pfinal,covar,infodict,mesg,ier = optimize.leastsq( \
                    errfunc, pinit, args=(X, Y), full_output=1)

  print "pfinal = ", pfinal
  print "covar = ", covar
  
  ss_err=(infodict['fvec']**2).sum()
  ss_tot=((Y-X.mean())**2).sum()
  rsquared=1-(ss_err/ss_tot)
  print "rsquared = ", rsquared

  index = pfinal[1]
  amp = 10.0**pfinal[0]

  indexErr = sqrt( covar[0][0] )
  ampErr = sqrt( covar[1][1] ) * amp
  loglog(X, Y, 'o', label=label)
  
  grid(True)
  Y_fit = fitfunc(pfinal,X)
  plot(Xdata, Y_fit, '-', label=("%s-power" % label))

#def func(x, a, b, c):
#  return a * numpy.exp(-b * x) + c

def plot_stats():
  
  for type in PLOT_TYPES:
    
    figure()
    for g in GRAPH_TYPES:
    
      fname = '%s/%s-%s.txt' % (RESULTS_DIR, Snap.GetGraphAbbr(g),
                                Snap.GetAttributeAbbr(type))
      print "Plotting '%s'" % fname
      A = loadtxt(fname)
      A = sort(A,0)
      Y = A[:,-1]     # Last column
      X = A[:,:-1]    # Columns 0-(n-1)
      
      # Add column of 1's for intercept
      X = column_stack([X, ones(len(X))])

      # Fit using least-squares
#      logX = log10(X)
#      logY = log10(Y)
#      w = linalg.lstsq(logX,logY)[0] # obtaining the parameters
#      print "N = %d" % len(X)
#      print "coefficients = ", w
#      # Plot the least-squares line
#      Y_fit = w[0]*logX[:,0] + w[1]*logX[:,1] + w[2] # get regression line
      
      # Fit using Levenburg-Marquardt algorithm through leastsq
#      p0 = scipy.array([1,1,1])
#      coeffs, matcov = curve_fit(func, X[:,0], Y, p0)
#      Y_fit = func(x, coeffs[0], coeffs[1], coeffs[2])

#      powerlaw_fit(X[:,0], Y, "%s-fit" % Snap.GetGraphDesc(g))
      poly_fit(X[:,0], Y, "%s" % Snap.GetGraphDesc(g))

      
#      loglog(X[:,0], Y,'o', label=Snap.GetGraphDesc(g))
#      loglog(X[:,0], Y_fit, label="%s-fit" % Snap.GetGraphDesc(g))
      legend(loc='lower right')
      xlabel('Num Nodes (d_avg = %.1f)' % AVG_DEG)
      ylabel('time')
      
      title('%s run time (%s)' % (Snap.GetAttributeDesc(type), HOSTNAME))

    #end for loop - graph type
  
    pname = '%s/plot_%s.png' % (RESULTS_DIR, Snap.GetAttributeAbbr(type))
    print "Saving figure %s" % pname
  
    savefig(pname)

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
#    if (n+1) % 2 == 0:
#      print "Iteration %d of %d:" % (n+1, NUM_ITERATIONS)
#      plot_stats()

  plot_stats()



