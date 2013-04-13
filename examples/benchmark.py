#!/usr/bin/python
# benchmark.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Randomly generates a graph of specified size and type and saving,
#         or loading the graph if has already been created.
#     - Benchmarks a number of "is this a good graph?" tests on the graph,
#       calculating the amount of time required and appends to a file.
#           
#  usage: benchmark.py [-h] [-v] [-r RANGE] [-d] [-t GRAPH_TYPES]
#    [-n NUM_ITERATIONS] [-o OUTPUT_FILE] [-g]
#
#  optional arguments:
#    -h, --help            show this help message and exit
#    -v, --verbose         increase output verbosity
#    -r RANGE, --range RANGE
#      range (4-6) (10^4 to 10^6 nodes)
#    -d, --deterministic   deterministic benchmark
#    -t GRAPH_TYPES, --graph_types GRAPH_TYPES
#      Graph types, comma separated. Available: rand_ungraph,
#      rand_ngraph, rmat, pref, sw
#    -n NUM_ITERATIONS, --num_iterations NUM_ITERATIONS
#      number of iterations
#    -o OUTPUT_FILE, --output_file OUTPUT_FILE
#      file to output results
#    -g, --generate        generate new graphs
#
#   Example:
#   $ python benchmark.py -v -n 3 -g -d -r 2-3 -t rmat -o results/results.txt
#

import os.path
import sys
import argparse
from socket import gethostname
from time import clock
from datetime import datetime

sys.path.append("../swig-r")
import snap as Snap

PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Comma-separated, graph types:
# 'rand_ungraph' - random undirected
# 'rand_ngraph' - random directed
# 'rand_neagraph' - random directed attribute
# 'rmat' - R-MAT
# 'pref' - preferential attachment
# 'sw' - small world
DEFAULT_TYPES = "rmat,rand_ungraph"

# Average is 1, non-average is 0.
DEGREES = [10, 100]  #  List of degrees to loop [10, 100] tries N*10, N*100 edges
SW_REWIRE_PROB = 0.1

# Exponent range (e.g. 10^x to 10^y)
DEFAULT_RANGE = '5-7'
DEFAULT_ITERATIONS = 1

# Hostname for results
HOSTNAME = gethostname()

RESULTS_DIR = 'results'
DEFAULT_RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%M%S'))

def benchmark_ngraph(Graph):
  '''
  Perform benchmark tests for Directed Graphs
  '''
  
  results = {}
  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0, 11):
    num = Snap.NodesGTEDegree_PNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg

  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PNGraph(Graph)

  num = Snap.NodesGTEDegree_PNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = Snap.MxWccSz_PNGraph(Graph) \
    / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PNGraph(Graph).GetNodes() \
    / results['num_nodes']

  return results

def benchmark_ungraph(Graph):
  '''
  Perform benchmark tests for Undirected Graphs
  '''

  results = {}
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
  results['max_scc_percent'] = Snap.MxSccSz_PUNGraph(Graph).GetNodes() \
                                / results['num_nodes']

  # TODO: Calculate graph skew
  return results

def benchmark_neagraph(Graph):
  '''
    Perform benchmark tests for Directed Attribute Graphs
    '''
  
  results = {}
  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0, 11):
    num = Snap.NodesGTEDegree_PNEAGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PNEAGraph(Graph)
  
  num = Snap.NodesGTEDegree_PNEAGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = Snap.MxWccSz_PNEAGraph(Graph) \
    / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PNEAGraph(Graph).GetNodes() \
    / results['num_nodes']
  
  return results


def generate_graph(NNodes, NEdges, Model, Type, Rnd):
    
  if Model == 'rand_ungraph':
    # GnRndGnm returns error, so manually generate
    Graph = Snap.GenRndGnm_PUNGraph(NNodes, NEdges, 0)

  elif Model == 'rand_ngraph':
    Graph = Snap.GenRndGnm_PNGraph(NNodes, NEdges, 1)

  elif Model == 'rmat':
    Graph = Snap.GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2, Rnd)

  elif Model == 'sw':
    Graph = Snap.GenSmallWorld(NNodes, NNodes/NEdges, 0.1)
  
  elif Model == 'pref':
    Graph = Snap.GenPrefAttach(NNodes, NNodes/NEdges)

  elif Model == "rand_neagraph":
    Graph = Snap.GenRndGnm_PNEAGraph(NNodes, NEdges, 1)

  return Graph

def run_tests(num_iterations=3, min_nodes_exponent=3, max_nodes_exponent=4):
  '''
  Perform tests with specified exponent range
  '''

  if verbose:
    print "Running results from %e to %e" % (min_nodes_exponent,
                                           max_nodes_exponent)

  Rnd = Snap.TRnd()

  for exp in range(min_nodes_exponent,max_nodes_exponent+1):
    
    for n in range(num_iterations):
        
      if verbose:
        print "Iteration: %d of %d" % (n+1, num_iterations)

      # Random number of nodes of degree i
      NNodes = 10**exp;
      
      for avg_deg in DEGREES:
          
        for g in graph_types:

          if deterministic:
            if verbose:
              print "Deterministic mode, putting seed"
          else:
            if verbose:
              print "Non-deterministic mode"
            Rnd.PutSeed(0)

          if verbose:
            print "Using average degree of %d" % avg_deg
          NEdges = NNodes*avg_deg
        
          Graph = None
          if g in ['rmat', 'rand_ngraph']:
            Type = "directed"
      
          elif g in ['sw', 'pref', 'rand_ungraph']:
            Type = "undirected"
        
          elif g in ['rand_neagraph']:
            Type = "attribute"
              
          else:
            print "Unknown graph type: %s" % g
            sys.exit(1)
          
          StartTime = clock()
          FName = os.path.join(RESULTS_DIR, "%s_10e%d_deg%d_%d.graph" %
                              (g, exp, NEdges/NNodes, n))
        
          if not generate:
            
            if os.path.exists(FName):
              try:
              
                if verbose:
                  print "Loading '%s' from ...'%s'" % (g, FName)
                
                FIn = Snap.TFIn(Snap.TStr(FName))
                if Type == "directed":
                  Graph = Snap.PNGraph_New()
                elif Type == "undirected":
                  Graph = Snap.PUNGraph_New()
                elif Type == "attribute":
                  Graph = Snap.PNEAGraph_New()

                Graph = Graph.Load(FIn)
              
                if verbose:
                  print "Re-loaded graph with %d Nodes and %d Edges" % \
                    (Graph.GetNodes(), Graph.GetEdges())
  
              except Exception, e:
                print "Unable to load graph file, '%s': %s" % (FName, str(e))

            else:
              print "File not found: %s" % FName

            
          if not Graph:
            
            try:
            
              # User wants to re-generate graph, or no graph data available.
              if verbose:
                print "Generating %s '%s' graph with %e nodes, %e edges" % \
                        (Type, g, NNodes, NEdges)
            
              Graph = generate_graph(NNodes, NEdges, g, Type, Rnd)
            
              # Save the graph
              print "Saving '%s' graph to file ... '%s'" % (g, FName)
              if Graph:

                  FOut = Snap.TFOut(Snap.TStr(FName))
                  Graph.__ref__().Save(FOut)   # Save as TUNGraph or TNGraph
                  FOut.Flush()
            
            except Exception, e:
              print "Unable to generate/save graph file, '%s': %s" % \
                    (FName, str(e))
              continue

          TimeGenerate = clock() - StartTime

          print "Running tests..."
          StartTime = clock()

          if Type == 'directed':
            results = benchmark_ngraph(Graph)
          elif Type == 'undirected':
            results = benchmark_ungraph(Graph)
          elif Type == 'attribute':
            results = benchmark_neagraph(Graph)


          TimeElapsed = clock() - StartTime
          
          print "Elapsed Time = %.4f sec" % TimeElapsed

          row_header = ["Hostname", "Model", "Type", "Nodes", "Edges",
                        "StartTime", "Generation Time", "Run Time"]

          print "Header: %s" % " ".join(row_header)

          import csv
          with open(results_file, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            print "Writing to '%s'..." % results_file
            row = [HOSTNAME, g, Type, NNodes, NEdges,
                   datetime.now().strftime("%d/%b/%Y:%H:%M:%S"),
                   TimeGenerate, TimeElapsed]
            print "Time Data: %s" % repr(row)
            writer.writerow(row)
              
          print "-"*75

def main():
  
  global results_dir, verbose, deterministic, generate, graph_types, \
          hostname, num_iterations, results_file
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")

  parser.add_argument("-r", "--range", default=DEFAULT_RANGE,
                      help="range (4-6) (10^4 to 10^6 nodes)")

  parser.add_argument("-d", "--deterministic", default=False,
                        action="store_true", dest="deterministic",
                        help="deterministic benchmark")

  parser.add_argument("-t", "--graph_types", default=DEFAULT_TYPES,
                      help='''
          Graph types, comma separated.
          Available: rand_ungraph, rand_ngraph, rmat, pref, sw''')

  parser.add_argument("-n", "--num_iterations", type=int,
                      default=DEFAULT_ITERATIONS, help="number of iterations")

  parser.add_argument("-o", "--output_file",
                      default=DEFAULT_RESULTS_FILE,
                      help="file to output results")


  parser.add_argument("-g", "--generate", default=False,
                      action="store_true", dest="generate",
                      help="generate new graphs")
  
  args = parser.parse_args()
  
  verbose = args.verbose
  generate = args.generate
  deterministic = args.deterministic
  results_file = args.output_file
  num_iterations = args.num_iterations
  graph_types = args.graph_types.split(",")
  
  if verbose:
    print "Hostname: %s" % HOSTNAME
  min = int(args.range.split("-")[0])
  max = int(args.range.split("-")[-1])
  print "Range = 10^%d to 10^%d" % (min, max)
  
  if not os.path.exists(RESULTS_DIR):
    print "Creating results directory %s" % RESULTS_DIR
    os.makedirs(RESULTS_DIR)
                        
  run_tests(num_iterations, min, max)

if __name__ == "__main__":
  main()
                      
                      
