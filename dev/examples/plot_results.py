import os.path
import sys
from socket import gethostname
import argparse
from datetime import datetime

sys.path.append("../swig")
import snap
from glob import glob

NUM_ITERATIONS = 1
PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS
DEFAULT_TYPES = "rmat,rand_ngraph,rand_neanet,rand_negraph"      #   Comma separated

# Random, Small World, Pref, R-MAT
# Graph types:
# 'rand_ungraph' - random undirected
# 'rand_ngraph' - random directed
# 'rmat' - R-MAT
# 'pref' - preferential attachment
# 'sw' - small world

DEGREE_TYPES = [0, 1]
DEFAULT_RANGE = '5-7'   # Exponent (e.g. 10^x to 10^y)
DEFAULT_NODES_MIN = 10**5

VERBOSE = False
DEFAULT_TIME_MIN = 0.0

AVG_DEG = 3
AVG_DEGREE_RANGE = range(2, 10)
SW_REWIRE_PROB = 0.1

HOSTNAME = gethostname()

# Where to build the table.
PUBLIC_DIR = 'public_html'
TABLE_FILE = os.path.join(PUBLIC_DIR, 'result_table_%s.html' %
                          datetime.now().strftime('%m%d-%H%M'))

# Where to read-in/generate the graph.

RESULTS_DIR = 'results'
RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%M'))

def parse_file(f, results):

  import csv
  print "Parsing %s" % f

  with open(f, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      result = {}
      result["hostname"] = row[0]
      result["model"] = row[1]
      result["type"] = row[2]
      result["num_nodes"] = int(row[3])
      result["num_edges"] = int(row[4])
      result["start_time"] = row[5]
      result["time_generate"] = float(row[6])
      result["time_elapsed"] = float(row[7])
 
      results.append(result)

def write_stats(results):
  
  f = open(TABLE_FILE, 'w')
  
  f.write("<html>\n");
  
  f.write("<body>\n");
  f.write("<table border=1 id=\"datatab\" summary=\"Dataset statistics\">\n");
  
  f.write("<tr>");
  f.write("<th>Hostname</th>\n");
  f.write("<th>Model</th>\n");
  f.write("<th>Type</th>\n");
  f.write("<th>Nodes</th>\n");
  f.write("<th>Edges</th>\n");
  f.write("<th>Start Time</th>\n");
  f.write("<th>Gen Time (sec)</th>\n");
  f.write("<th>Run Time (sec)</th>\n");
  f.write("</tr>\n");

  for result in results:

      for model in graph_types:
        
        if result['time_elapsed'] > time_min \
          and model in result['model'] and \
          result['num_nodes'] >= DEFAULT_NODES_MIN:
          
          f.write("<tr>\n");
          f.write("<td>%s</td>" % result['hostname']);
          f.write("<td>%s</td>" % result['model']);
          f.write("<td>%s</td>" % result['type']);
          f.write("<td>%.3e</td>" % result['num_nodes']);
          f.write("<td>%.3e</td>" % result['num_edges']);
          f.write("<td>%s</td>" % result['start_time']);
          f.write("<td>%.4f</td>" % result['time_generate']);
          f.write("<td>%.4f</td>" % result['time_elapsed']);
          f.write("</tr>\n");

  f.write("</table>\n");
  
  f.write("</body>");
  f.write("</html>");
  if verbose:
    print "Writing to file ", TABLE_FILE
          
  f.close();

# --------------- Plotting ---------------
import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import sort,array,ones,linalg,column_stack,loadtxt,savetxt

def plot_2d(property):
  
  # Plot average degree on 2d-graph
  figure()
  for g in GRAPH_TYPES:
    
    fname = '%s/%s_%sdeg%d.txt' % (results_dir, snap.GetAttributeAbbr(property),
                                   snap.GetGraphAbbr(g), AVG_DEG)
    A = loadtxt(fname)
    A = sort(A,0)
    Y = A[:,-1]     # Last column
    X = A[:,:-1]    # Columns 0-(n-1)
    
    loglog(X[:,0], Y, 'o', label=snap.GetGraphDesc(g))
    
    legend(loc='lower right')
    xlabel('Num Nodes (d_avg = %.1f)' % AVG_DEG)
    ylabel('time')
    title('%s runtime (avg degree = %d)' % (snap.GetAttributeDesc(property), AVG_DEG))
    pname = '%s/plot2d_%s.png' % (results_dir, snap.GetAttributeAbbr(property))
    print "Saving figure %s" % pname
    savefig(pname)

def main():
  
  global results_dir, verbose, time_min, graph_types
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")
  
  parser.add_argument("-d", "--results_dir", help="results directory",
                      default=RESULTS_DIR)
  
  parser.add_argument("-m", "--time_min", type=float,
                      default=DEFAULT_TIME_MIN,
                      help="time minimum threshold")
  
  parser.add_argument("-t", "--graph_types", default=DEFAULT_TYPES,
                      help='''
                        Graph types, comma separated.
                        Available: rand_ungraph, rand_ngraph, rand_neanet rmat, 
                        pref, sw''')
  
  args = parser.parse_args()
  
  verbose = args.verbose
  graph_types = args.graph_types.split(",")
  
  print "Hostname: %s" % HOSTNAME
  
  time_min = args.time_min
  
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)
  
  if not os.path.exists(PUBLIC_DIR):
    os.makedirs(PUBLIC_DIR)

  if verbose:
    print "Reading results %s" % args.results_dir
  
  results = []
  for f in glob("%s/result*.txt" % args.results_dir):
    print "Parsing %s" % f
    parse_file(f, results)

  write_stats(results)
  
if __name__ == "__main__":
  main()

