## SnapX: An experimental SNAP API with NetworkX-like interface
This subdirectory contains an experimental interface to SNAP, whose goal is to offer an alternative, more Pythonic way to interact with C++ SNAP's graph data structures and algorithms. The new API provided here is aimed to be fully compatible with NetworkX, with the ultimate goal of behaving as its drop-in replacement. 

## Getting started
To install the interface, simply run `setup.py` in your environment. By design, you can manipulate SnapX graphs as if you are working with NetworkX, as the following code snippet demonstrates:
```python3
import snapx as sx

g = sx.Graph() 
g.add_nodes_from([0, 1, (2, {'weight': 0.4}), (3, {'name': 'foo'})]) 
g.add_edges_from([(0, 1, {'bar': 'baz'}), (1, 3)]) 

g.nodes(data=True) # Show nodes with their attributes
g.edges[(0, 1)] # Show attributes associated with edge (0, 1)
```

## Currently supported features

### Data structures
- `Graph`: An undirected graph data structure emulated by SNAP's `TNEANet`, a multigraph with support for node and edge attributes. Please see the docstring for `Graph` class, available under `classes/graph.py` for notes on its design.

### Views
The following view classes are currently available for use:
- `AtlasView`
- `AdjacencyView`
- `NodeView`
- `EdgeView`


## Testing
The entire test suite can be invoked by calling `pytest`. 

## License
This project depends heavily on NetworkX's various components such as code, docstrings and, most importantly, the API design. The original licence of NetworkX can be found in `LICENSE_NETWORKX`.
