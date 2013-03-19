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

RESULTS_DIR = os.path.join('..','results')
PUBLIC_DIR = os.path.join(RESULTS_DIR, 'public_html')
TABLE_FILE = os.path.join(PUBLIC_DIR, 'results_%s.html' %
                          datetime.now().strftime('%m%d-%H%m'))
DATA_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
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
    f.write("<td>%.4f</td>" % results['gen_time']);
    f.write("<td>%.4f</td>" % results['run_time']);
    f.write("<td>%s</td>" % results['hostname']);
    f.write("</tr>\n");
  
  f.write("</table>\n");
  
  f.write("</body>");
  f.write("</html>");
  
  f.close();

# Run benchmark of tests
def benchmark_ngraph(results, NGraph):
    
  results['num_nodes'] = NGraph.GetNodes()
  results['num_edges'] = NGraph.GetEdges()
  
  for degree in range(0, 11):
    num = Snap.NodesGTEDegree_PNGraph(NGraph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PNGraph(NGraph)
  
  num = Snap.NodesGTEDegree_PNGraph(NGraph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = Snap.MxWccSz_PNGraph(NGraph) \
                                / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PNGraph(NGraph).GetNodes() \
                                / results['num_nodes']
  return results

def benchmark_ungraph(results, Graph):
  
  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0,11):
    num = Snap.NodesGTEDegree_PUNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PUNGraph(Graph)
  
  num = Snap.NodesGTEDegree_PUNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  results['max_wcc_percent'] = Snap.MxWccSz_PUNGraph(Graph) \
                                / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PUNGraph(NGraph).GetNodes() \
                                / results['num_nodes']
  results['run_time'] = time() - start_time
  
  # Calculate graph skew
  return results

def benchmark(results, Graph):
  
  print "Running results..."
  start_time = time()

  if results['type'] == 'directed'
    results = benchmark_ngraph(results, NGraph)
  if results['type'] == 'undirected'
    results = benchmark_ungraph(results, NGraph)
  else
    return none

  results['time_elapsed'] = time() - start_time


def run_tests(num_iterations=3, min_nodes_exponent=4, max_nodes_exponent=4):
  
  all_results = []
  
  print "Running results from %e to %e" % (min_nodes_exponent, max_nodes_exponent)

  import json
  for n in range(num_iterations):
    if verbose:
      print "Iteration: %d of %d" % (n+1, num_iterations)
    
    for e in range(min_nodes_exponent,max_nodes_exponent+1):
      
      for g in GRAPH_TYPES:
      
        # Random number of nodes of degree i
        NNodes = 10**e;
        
        for avg_deg in [10, 100]:
        
          NEdges = NNodes*avg_deg
  #      # load the graph
  #      FIn = Snap.TFIn(Snap.TStr(FName))
  #      Graph2 = Snap.TUNGraph()
  #      Graph2.Load(FIn)
  #      PrintGStats("ManipulateNodesEdges:Graph4",Graph2)
          FName = "%s_%d.graph" % (g, n)
          
          # Use SNAP to read from file FIn and FOut don't work
          Graph = None
          
  # TODO: TFIn is buggy, pass read-in for now
  #        if os.path.exists(FName):
  #          print "Reading from %s...." % FName
          
  #          try:
  #            FIn = Snap.TFIn(Snap.TStr(FName))
  #            NGraph = Snap.TNGraph()
  #            NGraph.Load(FIn)
  #            NGraph = LoadFromFile(FName)
  #
  #          except Exception, e:
  #            print "Unable to load graph file, '%s': %s" % (FName, str(e))

          results = {}
          
          if Graph:
            # Read in from file
            results['gen_time'] = 0
          
          else:
            
            # Generate graph
            start_time = time()
            print "Generating %s graph with %e NNodes, %e edges" % \
                        (g, NNodes, NEdges)

            if g in ['rnd', 'rmat']:
              
              if g == 'rnd':
                Graph = Snap.GenRndGnm_PNGraph(NNodes, NEdges)
              elif g == 'rmat':
                Graph = Snap.GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2)
              else:
                print "Invalid directed graph"
        
            results['type'] = 'directed'

            else:
                
              if g == 'sw':
                Graph = Snap.GenSmallWorld(NNodes, NNodes/NEdges, 0.1)
              elif g == 'pref':
                Graph = Snap.GenPrefAttach(NNodes, NNodes/NEdges)

            results['gen_time'] = time() - start_time
            results['type'] = 'undirected'
              
          results = benchmark(results, Graph)

          results['model'] = g
          results['hostname'] = HOSTNAME
  
          else:
            print "Invalid undirected graph"
            pass
          
          # TFIn is buggy, pass for now
  #        print "Saving %s graph to file...%s" % (g, FName)
  #        FOut = Snap.TFOut(Snap.TStr(FName))
  #        NGraph.Save(FOut)
  #        FOut.Flush()

  #          FOut = Snap.TFOut(Snap.TStr(FName))
  #            Graph.Save(FOut)
  #            FOut.Flush()

          print "Elapsed Time = %.4f" % results['run_time']
          print "-"*75

          all_results.append(results)
          
          # Output to JSON for posterity
          with open(DATA_FILE, 'w') as outfile:
            json.dump(all_results, outfile)
          
          write_stats(all_results)

  return all_results


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
  
  global results_dir, verbose, hostname, max_nodes_exponent

  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")
  parser.add_argument("-r", "--range", default=DEFAULT_RANGE,
                      help="range (4-5) (10^4 to 10^5")
  parser.add_argument("-n", "--num_iterations", type=int,
                      default=NUM_ITERATIONS, help="number of iterations")
#  parser.add_argument("-i", "--hostname", help="hostname")
#  parser.add_argument("-p", "--plot", action="store_true", help="plot stats")
#  parser.add_argument("-r", "--run", action="store_true", help="run stats")
#  
#  parser.add_argument("results_dir", help="directory to save/store data")
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


