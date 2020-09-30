## SnapX: A new SNAP API with NetworkX-like interface
This directory contains an alternative interface to SNAP, whose goal is to offer a more Pythonic way to interact with C++ SNAP's graph data structures and algorithms. The new API provided here is aimed to be fully compatible with NetworkX, with the ultimate goal of behaving as its drop-in replacement. 

## Getting started
To install the interface for development, simply run `python3 setup.py develop` in your environment. By design, you can manipulate SnapX graphs as if you are working with NetworkX, as the following code snippet demonstrates:
```python3
import snapx as sx

g = sx.Graph() 
g.add_nodes_from([0, 1, (2, {'weight': 0.4}), (3, {'name': 'foo'})]) 
g.add_edges_from([(0, 1, {'bar': 'baz'}), (1, 3)]) 

g.nodes(data=True) # Show all nodes with their attributes
g.edges[(0, 1)] # Show attributes associated with edge (0, 1)

g.adj[0][1]['data'] = 12 # Assign a new attribute to edge (0, 1)

for n in g.nodes:
    print(n, g.nodes[n]) # Iterate over nodes

for e in g.edges:
    print(e, g.edges[e]) # Iterate over edges
```

## Implementation overview

### Data structures
- `Graph`: An undirected graph data structure emulated by SNAP's `TNEANet`, a multigraph with support for node and edge attributes. Please see the docstring for `Graph` class, available under `classes/graph.py` for more information on its design. 

### Views
The following view classes are currently available for use:
- `AtlasView`
- `AdjacencyView`
- `NodeView`
- `EdgeView`

### Generators
Two simple graph generators from NetworkX are made available at the moment: `empty_graph` and `path_graph`. Support for more graph generators can be added with relative ease insofar as the generators interact only with the available APIs of the graph data structures. Adding generators defined in SNAP is another possibility for future implementations.

### Algorithms (NOT working)
The subdirectory `algorithms` is where you can find SNAP's graph algorithms. Currently, only a tiny subset of algorithms are exposed from snap.py; they are NOT not working at the moment due to the use of TNEANet. This subdirectory is left here nonetheless in order to help illustrate the future direction should we choose to support graph algorithms. 

## Testing
The entire test suite can be invoked by calling `pytest`. Remaining faithful to NetworkX's original interface is an importal goal of this project, and thus we put our code through the same set of test cases as NetworkX to the extent possible.

## License
This project depends heavily on NetworkX's various components such as code, docstrings and, most importantly, the API design. The original licence of NetworkX can be found in `LICENSE_NETWORKX`.
