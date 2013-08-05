#!/usr/bin/python
# benchmark.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Randomly generates a graph of specified size and type, and saves
#         or loads the graph if it has already been created.
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
#   Examples:
#   1. Use default arguments.
#   $ python menchmark.py
#   2. Generate deterministic RMAT graphs from 10^2-10^3 nodes, and
#       run 3 times, outputing to results.txt.
#   $ python benchmark.py -v -n 3 -g -d -r 2-3 -t rmat -o results/results.txt
#

import os.path
import sys
import argparse
from socket import gethostname
from time import clock
from datetime import datetime

sys.path.append("../swig-r")
import snap

PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Comma-separated, graph types:
# 'rmat' - R-MAT
# 'pref' - preferential attachment
# 'sw' - small world
# 'rand_ungraph' - random undirected
# 'rand_ngraph' - random directed
# 'rand_neanet' - random directed attribute
# 'syn_ngraph' - random directed
# 'syn_negraph' - synthetic multi-edge
# 'syn_neanet' - synthetic directed multi-edge attribute

DEFAULT_TYPES = "rand_neanet"

# Average is 1, non-average is 0.
DEFAULT_DEGREES = "1-2"  #  Default is 10x and 100x edges/node
DEFAULT_WRITE = False
SW_REWIRE_PROB = 0.1
SYNTHETIC_DELTA = 10

# Exponent range (e.g. 10^x to 10^y)
DEFAULT_VERBOSE=True
DEFAULT_RANGE = '3-4'
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
    num = snap.NodesGTEDegree_PNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg

  # Check for over-weighted nodes
  results['max_degree'] = snap.MxDegree_PNGraph(Graph)

  num = snap.NodesGTEDegree_PNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = snap.MxWccSz_PNGraph(Graph) \
    / results['num_nodes']
  results['max_scc_percent'] = snap.MxSccSz_PNGraph(Graph).GetNodes() \
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
    num = snap.NodesGTEDegree_PUNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = snap.MxDegree_PUNGraph(Graph)
  
  num = snap.NodesGTEDegree_PUNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  results['max_wcc_percent'] = snap.MxWccSz_PUNGraph(Graph) \
                                / results['num_nodes']
  results['max_scc_percent'] = snap.MxSccSz_PUNGraph(Graph).GetNodes() \
                                / results['num_nodes']

  # TODO: Calculate graph skew
  return results

def benchmark_neanet(Graph):
  '''
    Perform benchmark tests for Directed Attribute Graphs
    '''
  
  results = {}
  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0, 11):
    num = snap.NodesGTEDegree(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = snap.MxDegree(Graph)
  
  num = snap.NodesGTEDegree(Graph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = snap.MxWccSz(Graph) \
    / results['num_nodes']
  results['max_scc_percent'] = snap.MxSccSz(Graph).GetNodes() \
    / results['num_nodes']
  
  return results


def convert_graph(Graph, TypeSrc, TypeDst):
  '''
  Converts a GRAPH from type TYPESRC to a TYPEDST and returns the new graph
  '''
  pass


def generate_graph(NNodes, NEdges, Model, Type, Rnd):
    
  if Model == 'rand_ungraph':
    # GnRndGnm returns error, so manually generate
    Graph = snap.GenRndGnm_PUNGraph(NNodes, NEdges, 0)

  elif Model == 'rand_ngraph':
    Graph = snap.GenRndGnm_PNGraph(NNodes, NEdges, 1)
      
  elif Model == 'rand_neanet':
    Graph = snap.GenRndGnm(NNodes, NEdges, 1)

  elif Model == 'syn_neanet':
    Graph = snap.GenSyntheticGraph(NNodes, NEdges/NNodes,
                                             SYNTHETIC_DELTA)

  elif Model == 'syn_ngraph':
    Graph = snap.GenSyntheticGraph_PNGraph(NNodes, NEdges/NNodes,
                                             SYNTHETIC_DELTA)

  elif Model == 'rmat':
    Graph = snap.GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2, Rnd)

  elif Model == 'sw':
    Graph = snap.GenSmallWorld(NNodes, NNodes/NEdges, 0.1)
  
  elif Model == 'pref':
    Graph = snap.GenPrefAttach(NNodes, NNodes/NEdges)

  return Graph

def run_tests(num_iterations=3, min_nodes_exponent=3, max_nodes_exponent=4):
  '''
  Perform tests with specified exponent range
  '''

  if verbose:
    print "Running results from %e to %e" % (min_nodes_exponent,
                                           max_nodes_exponent)

  Rnd = snap.TRnd()

  for exp in range(min_nodes_exponent,max_nodes_exponent+1):
    
    for n in range(num_iterations):
        
      if verbose:
        print "Iteration: %d of %d" % (n+1, num_iterations)

      # Random number of nodes of degree i
      NNodes = 10**exp;
      
      for avg_deg in range(min_degree_edges, max_degree_edges+1):
          
        for g in graph_types:

          if deterministic:
            if verbose:
              print "Deterministic mode, putting seed"
          else:
            if verbose:
              print "Non-deterministic mode"
            Rnd.PutSeed(0)

          if verbose: print "Using average degree of 10^%d" % avg_deg
          NEdges = NNodes*(10**avg_deg)
        
          Graph = None
          if g in ['rmat', 'rand_ngraph', 'syn_ngraph','syn_negraph']:
            Type = "directed"
      
          elif g in ['sw', 'pref', 'rand_ungraph']:
            Type = "undirected"
        
          elif g in ['rand_neanet', 'syn_neanet']:
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
                  print "Loading '%s' from ...'%s'" % (g, FName),
                  sys.stdout.flush()

                FIn = snap.TFIn(snap.TStr(FName))
                if Type == "directed":
                  Graph = snap.PNGraph_New()
                elif Type == "undirected":
                  Graph = snap.PUNGraph_New()
                elif Type == "attribute":
                  Graph = snap.PNEANet_New()

                Graph = Graph.Load(FIn)
                if verbose: print "done"
              
                if verbose:
                  print "Re-loaded graph with %d Nodes and %d Edges" % \
                    (Graph.GetNodes(), Graph.GetEdges())
  
              except Exception, e:
                print "Unable to load graph file, '%s': %s" % (FName, str(e))

#            else:
#              print "File not found: %s" % FName
            
          if not Graph:
            
            try:
            
              # User wants to re-generate graph, or no graph data available.
              if verbose:
                print "Generating '%s %s' graph with %e nodes, %e edges..." % \
                        (Type, g, NNodes, NEdges),
                sys.stdout.flush()
              Graph = generate_graph(NNodes, NEdges, g, Type, Rnd)
              if verbose: print "done"
            
              if opt_write:
              
                # Save the graph
                if verbose:
                  print "Saving '%s' graph to file '%s'..." % (g, FName),
                  sys.stdout.flush()
                          
                if Graph:
                    FOut = snap.TFOut(snap.TStr(FName))
                    Graph.__ref__().Save(FOut)   # Save as TUNGraph or TNGraph
                    FOut.Flush()
                if verbose: print "done"
            
            except Exception, e:
              print "Unable to generate/save graph file, '%s': %s" % \
                    (FName, str(e))
              continue

          TimeGenerate = clock() - StartTime

          print "Running tests...",
          sys.stdout.flush()

          StartTime = clock()

          if Type == 'directed':
            results = benchmark_ngraph(Graph)
          elif Type == 'undirected':
            results = benchmark_ungraph(Graph)
          elif Type == 'attribute':
            results = benchmark_neanet(Graph)

          if verbose: print "done"

          TimeElapsed = clock() - StartTime
          
          print "Elapsed Time = %.4f sec" % TimeElapsed

          row_header = ["Hostname", "Model", "Type", "Nodes", "Edges",
                        "StartTime", "Generation Time", "Run Time"]

          print "Header: %s" % " ".join(row_header)

          import csv
          with open(results_file, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            if verbose:
              print "Writing to '%s'..." % results_file,
              sys.stdout.flush()

            row = [HOSTNAME, g, Type, NNodes, NEdges,
                   datetime.now().strftime("%d/%b/%Y:%H:%M:%S"),
                   TimeGenerate, TimeElapsed]
            if verbose: print "done"
            print "Time Data: %s" % repr(row)
            writer.writerow(row)
              
          print "-"*75

def main():
  
  global results_dir, verbose, deterministic, generate, graph_types, \
          hostname, num_iterations, results_file, \
          min_degree_edges, max_degree_edges, opt_write
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=DEFAULT_VERBOSE,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")

  parser.add_argument("-r", "--range", default=DEFAULT_RANGE,
                      help="range (4-6) (10^4 to 10^6 nodes)")

  parser.add_argument("-e", "--edges_deg", default=DEFAULT_DEGREES,
      help="range of degrees (e.g \"2-3\" => (10^1 to 10^3 edges per node)")

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

  parser.add_argument("-w", "--write_graph", default=DEFAULT_WRITE,
                      action="store_true", dest="write",
                      help="save graph")

  args = parser.parse_args()

  verbose = args.verbose
  generate = args.generate
  deterministic = args.deterministic
  results_file = args.output_file
  num_iterations = args.num_iterations
  graph_types = args.graph_types.split(",")
  min_degree_edges = int(args.edges_deg.split("-")[0])
  max_degree_edges = int(args.edges_deg.split("-")[-1])
  opt_write = args.write


  print "Edge degree = 10^%d to 10^%d edges/node" % \
        (min_degree_edges, max_degree_edges)

  if verbose:
    print "Hostname: %s" % HOSTNAME
  min = int(args.range.split("-")[0])
  max = int(args.range.split("-")[-1])
  print "Node range = 10^%d to 10^%d" % (min, max)
  
  if not os.path.exists(RESULTS_DIR):
    print "Creating results directory %s" % RESULTS_DIR
    os.makedirs(RESULTS_DIR)
                        
  run_tests(num_iterations, min, max)

if __name__ == "__main__":
  main()
                      
                      
