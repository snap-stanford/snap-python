import os.path
import sys
from time import time
from socket import gethostname
import argparse
import json
from datetime import datetime

sys.path.append("../swig")
import snap as Snap

NUM_ITERATIONS = 1
PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Random, Small World, Pref, R-MAT
GRAPH_TYPES = ['rmat', 'rnd','pref','sw']
#GRAPH_TYPES = ['sw', 'pref', 'rnd', 'rmat']
DEGREE_TYPES = [0, 1]
DEFAULT_RANGE = '5-7'   # Exponent (e.g. 10^x to 10^y)

VERBOSE = False

AVG_DEG = 3
AVG_DEGREE_RANGE = range(2, 10)
SW_REWIRE_PROB = 0.1

HOSTNAME = gethostname()

# Where to build the table.
PUBLIC_DIR = 'public_html'
TABLE_FILE = os.path.join(PUBLIC_DIR, 'results_%s.html' %
                          datetime.now().strftime('%m%d-%H%m'))

# Where to read-in/generate the graph.

DATA_DIR = 'data'
RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%m'))

def write_stats(all_results):
  
  f = open(TABLE_FILE, 'w')
  
  f.write("<html>\n");
  
  f.write("<body>\n");
  f.write("<table border=1 id=\"datatab\" summary=\"Dataset statistics\">\n");
  
  f.write("<tr>");
  f.write("<th>Model</th>\n");
  f.write("<th>Type</th>\n");
  f.write("<th>Nodes</th>\n");
  f.write("<th>Edges</th>\n");
  f.write("<th>Gen Time (sec)</th>\n");
  f.write("<th>Run Time (sec)</th>\n");
  f.write("<th>Hostname</th>\n");
  f.write("</tr>\n");
  
  for results in all_results:
    f.write("<tr>\n");
    f.write("<td>%s</td>" % results['model']);
    f.write("<td>%s</td>" % results['type']);
    f.write("<td>%.3e</td>" % results['num_nodes']);
    f.write("<td>%.3e</td>" % results['num_edges']);
    f.write("<td>%.4f</td>" % results['time_generate']);
    f.write("<td>%.4f</td>" % results['time_elapsed']);
    f.write("<td>%s</td>" % results['hostname']);
    f.write("</tr>\n");
  
  f.write("</table>\n");
  
  f.write("</body>");
  f.write("</html>");
  
  f.close();

# --------------- Plotting ---------------
import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import sort,array,ones,linalg,column_stack,loadtxt,savetxt
from scipy import *
from scipy.optimize import leastsq
from scipy import linalg

def plot_2d(property):
  
  # Plot average degree on 2d-graph
  figure()
  for g in GRAPH_TYPES:
    
    fname = '%s/%s_%sdeg%d.txt' % (results_dir, Snap.GetAttributeAbbr(property),
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
    pname = '%s/plot2d_%s.png' % (results_dir, Snap.GetAttributeAbbr(property))
    print "Saving figure %s" % pname
    savefig(pname)


def plot_stats():
  
  pass


#end for loop - plot type

def main():
  
  global results_dir, verbose
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")
  
  parser.add_argument("-r", "--results_dir", help="results directory")
  
  args = parser.parse_args()
  
  verbose = args.verbose
  
  print "Hostname: %s" % HOSTNAME
  print "Range = 10^%s to 10^%s" % (args.range[0], args.range[-1])
  
  if not os.path.exists(RESULTS_DIR):
  os.makedirs(RESULTS_DIR)
  
  if not os.path.exists(PUBLIC_DIR):
  os.makedirs(PUBLIC_DIR)
  
  all_results = run_tests(args.num_iterations, int(args.range[0]), int(args.range[-1]))
  
  if verbose:
  print "Plotting results"
  plot_stats()
  
  if __name__ == "__main__":
  main()

                      
