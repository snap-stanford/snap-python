import sys
from numpy import arange,array,ones,linalg,column_stack,loadtxt
from pylab import plot,show,xlabel,ylabel,savefig,title

xi = arange(0,9)
A = array([ xi, ones(9)])
# linearly generated sequence

sys.path.append("../swig")

import snap as Snap

PLOT_TYPES = 7
DATA_DIR = "data"

for type in range(PLOT_TYPES):
  f = open('%s/data%s.txt' % (DATA_DIR, Snap.GetAbbrev(type)), 'r')
  print f.read()

  # y = column 1
  # x = column 0
  A = loadtxt('data/dataDD.txt')
  Y = A[:,-1]
  X = A[:,:-1]

  # Add column of 1's for intercept
  X = column_stack([X, ones(len(X))])

  w = linalg.lstsq(X,Y)[0] # obtaining the parameters

  # plotting the line
  line = w[0]*X[:,0] + w[1]*X[:,1] + w[2] # regression line
  plot(X[:,0],line,'r-',X[:,0],Y,'o')
  xlabel('Num Nodes')
  ylabel('time (2.6 GHz)')
  title('%s Runtime' % Snap.GetDesc(type))
  savefig('%s/plot_%s.eps' % (DATA_DIR, Snap.GetAbbrev(type)))
  
#  show()
  
  coeff_file = open('%s/coeff.txt' % DATA_DIR, 'w+')
  coeff_file.write('%d %.4f %.4f %.4f\n' % (type, w[0], w[1], w[2]))
