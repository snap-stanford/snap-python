"""Undirected graphs.
"""

import snapx as sx

from snap import TNEANet, TNEANetNodeI, Nodes, Edges, TSIn

from snapx.classes.reportviews import NodeView, EdgeView
from snapx.classes.coreviews import AdjacencyView
import snapx.convert as convert
from snapx.exception import SnapXTypeError, SnapXError
from ._nodeiter import _GraphNodeIterator, _GraphEdgeIterator, _TNEANetEdgeIter


class Graph:
    """
    Base class for undirected graphs, much like the "Graph" class in NetworkX.

    DESIGN NOTES:
    1) Use of TNEANet and its consequences:
    This class is built on top of TNEANet, a multigraph implemented in C++ SNAP.
    For that reason, some of the behaviors expected out of an undirected graph
    are emulated in this layer. More specifically, we did the following:
    - When an edge (u, v) is added, both (u, v) and (v, u) get registered
      to the underlying TNEANet.
    - We keep a counter 'self._num_edges' to track how many edges exist in
      the graph.

    We currently rely on TNEANet due to its rich support for node and edge
    attributes. A future implementation may obviate the need for this emulation
    by expanding the C++ SNAP's undirected graph to provide support for such
    attributes.

    2) How graph/node/edge attributes are stored
    - Graph attributes: Stored in self.graph, a built-in dict.
    - Node and edge attributes:
        - An int typed attribute gets stored in the TNEANet's feature storage.
        - All other types will go to the extra attribute builtin dicts
          (self._node_extra_attr and self._edge_extra_attr).
        AttributeDict handles manipulation of edge/node features.

    Docstrings are mostly copied over from NetworkX for reference, and thus may not
    accurately reflect the exact features supported in SnapX.
    """

    def to_directed_class(self):
        """PORTED FROM NETWORKX
        Returns the class to use for empty directed copies.

        If you subclass the base classes, use this to designate
        what directed class to use for `to_directed()` copies.
        """
        return sx.DiGraph

    def to_undirected_class(self):
        """PORTED FROM NETWORKX
        Returns the class to use for empty undirected copies.

        If you subclass the base classes, use this to designate
        what directed class to use for `to_directed()` copies.
        """
        return Graph

    def __init__(self, incoming_graph_data=None, **attr):
        """PORTED FROM NETWORKX
        Initialize a graph with edges, name, or graph attributes.
        Parameters
        ----------
        incoming_graph_data : input graph (optional, default: None)
            Data to initialize graph. If None (default) an empty
            graph is created.  The data can be an edge list, or any
            NetworkX graph object.  If the corresponding optional Python
            packages are installed the data can also be a NumPy matrix
            or 2d ndarray, a SciPy sparse matrix, or a PyGraphviz graph.
        attr : keyword arguments, optional (default= no attributes)
            Attributes to add to graph as key=value pairs.
        See Also
        --------
        convert
        Examples
        --------
        >>> G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G = nx.Graph(name='my graph')
        >>> e = [(1, 2), (2, 3), (3, 4)]  # list of edges
        >>> G = nx.Graph(e)
        Arbitrary graph attribute pairs (key=value) may be assigned
        >>> G = nx.Graph(e, day="Friday")
        >>> G.graph
        {'day': 'Friday'}
        """
        self._graph = TNEANet.New()

        # Because we are emulating an undirected graph using multigraph,
        # we need a counter to keep track of edges
        self._num_edges = 0
        # Supplementary dicts to keep data not supported by snap graph
        self._node_extra_attr = {}
        self._edge_extra_attr = {}
        if incoming_graph_data is not None:
            if type(incoming_graph_data) == type(TNEANet.New()):
                self._graph = incoming_graph_data
                self._num_edges = self._graph.GetEdges()
            else:
                convert.to_snapx_graph(incoming_graph_data, create_using=self)

        # Graph attributes
        self.graph = {}
        self.graph.update(attr)

    @property
    def adj(self):
        """PORTED FROM NETWORKX
        Graph adjacency object holding the neighbors of each node.
        This object is a read-only dict-like structure with node keys
        and neighbor-dict values.  The neighbor-dict is keyed by neighbor
        to the edge-data-dict.  So `G.adj[3][2]['color'] = 'blue'` sets
        the color of the edge `(3, 2)` to `"blue"`.
        Iterating over G.adj behaves like a dict. Useful idioms include
        `for nbr, datadict in G.adj[n].items():`.
        The neighbor information is also provided by subscripting the graph.
        So `for nbr, foovalue in G[node].data('foo', default=1):` works.
        For directed graphs, `G.adj` holds outgoing (successor) info.
        """
        return AdjacencyView(self)

    @property
    def name(self):
        """PORTED FROM NETWORKX
        String identifier of the graph.
        This graph attribute appears in the attribute dict G.graph
        keyed by the string `"name"`. as well as an attribute (technically
        a property) `G.name`. This is entirely user controlled.
        """
        return self.graph.get("name", "")

    @name.setter
    def name(self, s):
        self.graph["name"] = s

    def __str__(self):
        """PORTED FROM NETWORKX
        Returns the graph name.
        Returns
        -------
        name : string
            The name of the graph.
        Examples
        --------
        >>> G = nx.Graph(name='foo')
        >>> str(G)
        'foo'
        """
        return self.name

    def __iter__(self):
        """PORTED FROM NETWORKX
        Iterate over the nodes. Use: 'for n in G'.
        Returns
        -------
        niter : iterator
            An iterator over all nodes in the graph.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> [n for n in G]
        [0, 1, 2, 3]
        >>> list(G)
        [0, 1, 2, 3]
        """
        return _GraphNodeIterator(self._graph.Nodes())

    def __contains__(self, n):
        """PORTED FROM NETWORKX
        Returns True if n is a node, False otherwise. Use: 'n in G'.

        Examples
        --------
        >>> G = sx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> 1 in G
        True
        """
        try:
            return self._graph.IsNode(n)
        except TypeError:
            return False

    def __len__(self):
        """PORTED FROM NETWORKX
        Returns the number of nodes in the graph. Use: 'len(G)'.

        Returns
        -------
        nnodes : int
            The number of nodes in the graph.

        See Also
        --------
        number_of_nodes, order  which are identical

        Examples
        --------
        >>> G = sx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> len(G)
        4

        """
        return self._graph.GetNodes()

    def __getitem__(self, n):
        """PORTED FROM NETWORKX
        Returns a dict of neighbors of node n.  Use: 'G[n]'.
        Parameters
        ----------
        n : node
           A node in the graph.
        Returns
        -------
        adj_dict : dictionary
           The adjacency dictionary for nodes connected to n.
        Notes
        -----
        G[n] is the same as G.adj[n] and similar to G.neighbors(n)
        (which is an iterator over G.adj[n])
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G[0]
        AtlasView({1: {}})
        """
        return self.adj[n]

    def add_node(self, node_for_adding, **attr):
        """PORTED FROM NETWORKX
        Add a single node `node_for_adding` and update node attributes.
        Parameters
        ----------
        node_for_adding : node
            A node can be any hashable Python object except None.
        attr : keyword arguments, optional
            Set or change node attributes using key=value.
        See Also
        --------
        add_nodes_from
        Examples
        --------
        >>> G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_node(1)
        >>> G.add_node('Hello')
        >>> K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
        >>> G.add_node(K3)
        >>> G.number_of_nodes()
        3
        Use keywords set/change node attributes:
        >>> G.add_node(1, size=10)
        >>> G.add_node(3, weight=0.4, UTM=('13S', 382871, 3972649))
        Notes
        -----
        A hashable object is one that can be used as a key in a Python
        dictionary. This includes strings, numbers, tuples of strings
        and numbers, etc.
        On many platforms hashable items also include mutables such as
        NetworkX Graphs, though one should be careful that the hash
        doesn't change on mutables.
        """
        try:
            if node_for_adding not in self:
                self._graph.AddNode(node_for_adding)
            self.nodes[node_for_adding].update(attr)
        except TypeError:
            raise SnapXTypeError("The node ID must be int.")

    def add_nodes_from(self, nodes_for_adding, **attr):
        """PORTED FROM NETWORKX
        Add multiple nodes.
        Parameters
        ----------
        nodes_for_adding : iterable container
            A container of nodes (list, dict, set, etc.).
            OR
            A container of (node, attribute dict) tuples.
            Node attributes are updated using the attribute dict.
        attr : keyword arguments, optional (default= no attributes)
            Update attributes for all nodes in nodes.
            Node attributes specified in nodes as a tuple take
            precedence over attributes specified via keyword arguments.
        See Also
        --------
        add_node
        Examples
        --------
        >>> G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_nodes_from('Hello')
        >>> K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
        >>> G.add_nodes_from(K3)
        >>> sorted(G.nodes(), key=str)
        [0, 1, 2, 'H', 'e', 'l', 'o']
        Use keywords to update specific node attributes for every node.
        >>> G.add_nodes_from([1, 2], size=10)
        >>> G.add_nodes_from([3, 4], weight=0.4)
        Use (node, attrdict) tuples to update attributes for specific nodes.
        >>> G.add_nodes_from([(1, dict(size=11)), (2, {'color':'blue'})])
        >>> G.nodes[1]['size']
        11
        >>> H = nx.Graph()
        >>> H.add_nodes_from(G.nodes(data=True))
        >>> H.nodes[1]['size']
        11
        """
        for n in nodes_for_adding:
            try:
                self.add_node(n)
                self.nodes[n].update(attr)
            except SnapXTypeError:
                nn, ndict = n
                if nn not in self.nodes:
                    self.add_node(nn)
                self.nodes[nn].update(attr)
                self.nodes[nn].update(ndict)

    def remove_node(self, n):
        """PORTED FROM NETWORKX
        Remove node n.

        Removes the node n and all adjacent edges.
        Attempting to remove a non-existent node will raise an exception.

        Parameters
        ----------
        n : node
           A node in the graph

        Raises
        -------
        NetworkXError
           If n is not in the graph.

        See Also
        --------
        remove_nodes_from

        Examples
        --------
        >>> G = nx.path_graph(3)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> list(G.edges)
        [(0, 1), (1, 2)]
        >>> G.remove_node(1)
        >>> list(G.edges)
        []
        """
        try:
            if n in self:
                self._graph.DelNode(n)
        except TypeError:
            raise SnapXTypeError("The node ID must be int.")

    def remove_nodes_from(self, nodes):
        """PORTED FROM NETWORKX        
        Remove multiple nodes.

        Parameters
        ----------
        nodes : iterable container
            A container of nodes (list, dict, set, etc.).  If a node
            in the container is not in the graph it is silently
            ignored.

        See Also
        --------
        remove_node

        Examples
        --------
        >>> G = nx.path_graph(3)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> e = list(G.nodes)
        >>> e
        [0, 1, 2]
        >>> G.remove_nodes_from(e)
        >>> list(G.nodes)
        []
        """
        for n in nodes:
            try:
                self.remove_node(n)
            except SnapXTypeError:
                pass

    @property
    def nodes(self):
        """PORTED FROM NETWORKX
        A NodeView of the Graph as G.nodes or G.nodes().
        Can be used as `G.nodes` for data lookup and for set-like operations.
        Can also be used as `G.nodes(data='color', default=None)` to return a
        NodeDataView which reports specific node data but no set operations.
        It presents a dict-like interface as well with `G.nodes.items()`
        iterating over `(node, nodedata)` 2-tuples and `G.nodes[3]['foo']`
        providing the value of the `foo` attribute for node `3`. In addition,
        a view `G.nodes.data('foo')` provides a dict-like interface to the
        `foo` attribute of each node. `G.nodes.data('foo', default=1)`
        provides a default for nodes that do not have attribute `foo`.
        Parameters
        ----------
        data : string or bool, optional (default=False)
            The node attribute returned in 2-tuple (n, ddict[data]).
            If True, return entire node attribute dict as (n, ddict).
            If False, return just the nodes n.
        default : value, optional (default=None)
            Value used for nodes that don't have the requested attribute.
            Only relevant if data is not True or False.
        Returns
        -------
        NodeView
            Allows set-like operations over the nodes as well as node
            attribute dict lookup and calling to get a NodeDataView.
            A NodeDataView iterates over `(n, data)` and has no set operations.
            A NodeView iterates over `n` and includes set operations.
            When called, if data is False, an iterator over nodes.
            Otherwise an iterator of 2-tuples (node, attribute value)
            where the attribute is specified in `data`.
            If data is True then the attribute becomes the
            entire data dictionary.
        Notes
        -----
        If your node data is not needed, it is simpler and equivalent
        to use the expression ``for n in G``, or ``list(G)``.
        Examples
        --------
        There are two simple ways of getting a list of all nodes in the graph:
        >>> G = nx.path_graph(3)
        >>> list(G.nodes)
        [0, 1, 2]
        >>> list(G)
        [0, 1, 2]
        To get the node data along with the nodes:
        >>> G.add_node(1, time='5pm')
        >>> G.nodes[0]['foo'] = 'bar'
        >>> list(G.nodes(data=True))
        [(0, {'foo': 'bar'}), (1, {'time': '5pm'}), (2, {})]
        >>> list(G.nodes.data())
        [(0, {'foo': 'bar'}), (1, {'time': '5pm'}), (2, {})]
        >>> list(G.nodes(data='foo'))
        [(0, 'bar'), (1, None), (2, None)]
        >>> list(G.nodes.data('foo'))
        [(0, 'bar'), (1, None), (2, None)]
        >>> list(G.nodes(data='time'))
        [(0, None), (1, '5pm'), (2, None)]
        >>> list(G.nodes.data('time'))
        [(0, None), (1, '5pm'), (2, None)]
        >>> list(G.nodes(data='time', default='Not Available'))
        [(0, 'Not Available'), (1, '5pm'), (2, 'Not Available')]
        >>> list(G.nodes.data('time', default='Not Available'))
        [(0, 'Not Available'), (1, '5pm'), (2, 'Not Available')]
        If some of your nodes have an attribute and the rest are assumed
        to have a default attribute value you can create a dictionary
        from node/attribute pairs using the `default` keyword argument
        to guarantee the value is never None::
            >>> G = nx.Graph()
            >>> G.add_node(0)
            >>> G.add_node(1, weight=2)
            >>> G.add_node(2, weight=3)
            >>> dict(G.nodes(data='weight', default=1))
            {0: 1, 1: 2, 2: 3}
        """
        nodes = NodeView(self)
        # Lazy View creation: overload the (class) property on the instance
        # Then future G.nodes use the existing View
        # setattr doesn't work because attribute already exists
        self.__dict__["nodes"] = nodes
        return nodes

    def number_of_nodes(self):
        """PORTED FROM NETWORKX
        Returns the number of nodes in the graph.
        Returns
        -------
        nnodes : int
            The number of nodes in the graph.
        See Also
        --------
        order, __len__  which are identical
        Examples
        --------
        >>> G = nx.path_graph(3)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.number_of_nodes()
        3
        """
        return self._graph.GetNodes()

    def order(self):
        """PORTED FROM NETWORKX
        Returns the number of nodes in the graph.
        Returns
        -------
        nnodes : int
            The number of nodes in the graph.
        See Also
        --------
        number_of_nodes, __len__  which are identical
        Examples
        --------
        >>> G = nx.path_graph(3)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.order()
        3
        """
        return self._graph.GetNodes()

    def has_node(self, n):
        """PORTED FROM NETWORKX
        Returns True if the graph contains the node n.
        Identical to `n in G`
        Parameters
        ----------
        n : node
        Examples
        --------
        >>> G = nx.path_graph(3)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.has_node(0)
        True
        It is more readable and simpler to use
        >>> 0 in G
        True
        """
        try:
            return n in self
        except TypeError:
            return False

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        """PORTED FROM NETWORKX:
        Add an edge between u and v.
        The nodes u and v will be automatically added if they are
        not already in the graph.
        Edge attributes can be specified with keywords or by directly
        accessing the edge's attribute dictionary. See examples below.
        Parameters
        ----------
        u, v : nodes
            Nodes can be, for example, strings or numbers.
            Nodes must be hashable (and not None) Python objects.
        attr : keyword arguments, optional
            Edge data (or labels or objects) can be assigned using
            keyword arguments.
        See Also
        --------
        add_edges_from : add a collection of edges
        Notes
        -----
        Adding an edge that already exists updates the edge data.
        Many NetworkX algorithms designed for weighted graphs use
        an edge attribute (by default `weight`) to hold a numerical value.
        Examples
        --------
        The following all add the edge e=(1, 2) to graph G:
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> e = (1, 2)
        >>> G.add_edge(1, 2)           # explicit two-node form
        >>> G.add_edge(*e)             # single edge as tuple of two nodes
        >>> G.add_edges_from([(1, 2)])  # add edges from iterable container
        Associate data to edges using keywords:
        >>> G.add_edge(1, 2, weight=3)
        >>> G.add_edge(1, 3, weight=7, capacity=15, length=342.7)
        For non-string attribute keys, use subscript notation.
        >>> G.add_edge(1, 2)
        >>> G[1][2].update({0: 5})
        >>> G.edges[1, 2].update({0: 5})
        """
        u = u_of_edge
        v = v_of_edge

        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)

        # Emulate (non-multi) graph by checking if the edge
        # already exists.
        if self.has_edge(u, v):
            return
        try:
            self._graph.AddEdge(u, v)
            if u != v:
                self._graph.AddEdge(v, u)
            self._num_edges += 1

            # Finally update attrs
            self.adj[u][v].update(attr)

        except TypeError:
            raise SnapXTypeError("SNAP only supports int as edge keys.")

    def add_edges_from(self, ebunch_to_add, **attr):
        """PORTED FROM NETWORKX
        Add all the edges in ebunch_to_add.
        Parameters
        ----------
        ebunch_to_add : container of edges
            Each edge given in the container will be added to the
            graph. The edges must be given as as 2-tuples (u, v) or
            3-tuples (u, v, d) where d is a dictionary containing edge data.
        attr : keyword arguments, optional
            Edge data (or labels or objects) can be assigned using
            keyword arguments.
        See Also
        --------
        add_edge : add a single edge
        add_weighted_edges_from : convenient way to add weighted edges
        Notes
        -----
        Adding the same edge twice has no effect but any edge data
        will be updated when each duplicate edge is added.
        Edge attributes specified in an ebunch take precedence over
        attributes specified via keyword arguments.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_edges_from([(0, 1), (1, 2)]) # using a list of edge tuples
        >>> e = zip(range(0, 3), range(1, 4))
        >>> G.add_edges_from(e) # Add the path graph 0-1-2-3
        Associate data to edges
        >>> G.add_edges_from([(1, 2), (2, 3)], weight=3)
        >>> G.add_edges_from([(3, 4), (1, 4)], label='WN2898')
        """
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise SnapXError("The edge must be a 2-tuple or 3-tuple.")
            try:
                self.add_edge(u, v)
                # FIXME: Faster way than simply walking over the dict?
                self.edges[(u, v)].update(attr)
                self.edges[(u, v)].update(dd)

            except (TypeError, RuntimeError) as e:
                pass

    def add_weighted_edges_from(self, ebunch_to_add, weight="weight", **attr):
        """PORTED FROM NETWORKX
        Add weighted edges in `ebunch_to_add` with specified weight attr
        Parameters
        ----------
        ebunch_to_add : container of edges
            Each edge given in the list or container will be added
            to the graph. The edges must be given as 3-tuples (u, v, w)
            where w is a number.
        weight : string, optional (default= 'weight')
            The attribute name for the edge weights to be added.
        attr : keyword arguments, optional (default= no attributes)
            Edge attributes to add/update for all edges.
        See Also
        --------
        add_edge : add a single edge
        add_edges_from : add multiple edges
        Notes
        -----
        Adding the same edge twice for Graph/DiGraph simply updates
        the edge data. For MultiGraph/MultiDiGraph, duplicate edges
        are stored.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])
        """
        self.add_edges_from(((u, v, {weight: d}) for u, v, d in ebunch_to_add), **attr)

    def remove_edge(self, u, v):
        """PORTED FROM NETWORKX
        Remove the edge between u and v.

        Parameters
        ----------
        u, v : nodes
            Remove the edge between nodes u and v.

        Raises
        ------
        NetworkXError
            If there is not an edge between u and v.

        See Also
        --------
        remove_edges_from : remove a collection of edges

        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, etc
        >>> G.remove_edge(0, 1)
        >>> e = (1, 2)
        >>> G.remove_edge(*e)  # unpacks e from an edge tuple
        >>> e = (2, 3, {"weight": 7})  # an edge with attribute data
        >>> G.remove_edge(*e[:2])  # select first part of edge tuple
        """
        if not self.has_edge(u, v):
            return
        
        try:
            self._graph.DelEdge(u, v)
            if u != v:
                self._graph.DelEdge(v, u)
            self._num_edges -= 1
        except TypeError:
            raise SnapXTypeError("SNAP only supports int as edge keys.")

    def remove_edges_from(self, ebunch):
        """PORTED FROM NETWORKX
        Remove all edges specified in ebunch.

        Parameters
        ----------
        ebunch: list or container of edge tuples
            Each edge given in the list or container will be removed
            from the graph. The edges can be:

                - 2-tuples (u, v) edge between u and v.
                - 3-tuples (u, v, k) where k is ignored.

        See Also
        --------
        remove_edge : remove a single edge

        Notes
        -----
        Will fail silently if an edge in ebunch is not in the graph.

        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> ebunch = [(1, 2), (2, 3)]
        >>> G.remove_edges_from(ebunch)
        """
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, _ = e
            elif ne == 2:
                u, v = e
            else:
                raise SnapXError("The edge must be a 2-tuple or 3-tuple.")

            try:
                self.remove_edge(u, v)
            except (TypeError, RuntimeError) as e:
                pass

    def update(self, edges=None, nodes=None):
        """PORTED FROM NETWORKX
        Update the graph using nodes/edges/graphs as input.
        Like dict.update, this method takes a graph as input, adding the
        graph's nodes and edges to this graph. It can also take two inputs:
        edges and nodes. Finally it can take either edges or nodes.
        To specify only nodes the keyword `nodes` must be used.
        The collections of edges and nodes are treated similarly to
        the add_edges_from/add_nodes_from methods. When iterated, they
        should yield 2-tuples (u, v) or 3-tuples (u, v, datadict).
        Parameters
        ----------
        edges : Graph object, collection of edges, or None
            The first parameter can be a graph or some edges. If it has
            attributes `nodes` and `edges`, then it is taken to be a
            Graph-like object and those attributes are used as collections
            of nodes and edges to be added to the graph.
            If the first parameter does not have those attributes, it is
            treated as a collection of edges and added to the graph.
            If the first argument is None, no edges are added.
        nodes : collection of nodes, or None
            The second parameter is treated as a collection of nodes
            to be added to the graph unless it is None.
            If `edges is None` and `nodes is None` an exception is raised.
            If the first parameter is a Graph, then `nodes` is ignored.
        Examples
        --------
        >>> G = nx.path_graph(5)
        >>> G.update(nx.complete_graph(range(4,10)))
        >>> from itertools import combinations
        >>> edges = ((u, v, {'power': u * v})
        ...          for u, v in combinations(range(10, 20), 2)
        ...          if u * v < 225)
        >>> nodes = [1000]  # for singleton, use a container
        >>> G.update(edges, nodes)
        Notes
        -----
        It you want to update the graph using an adjacency structure
        it is straightforward to obtain the edges/nodes from adjacency.
        The following examples provide common cases, your adjacency may
        be slightly different and require tweaks of these examples.
        >>> # dict-of-set/list/tuple
        >>> adj = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
        >>> e = [(u, v) for u, nbrs in adj.items() for v in  nbrs]
        >>> G.update(edges=e, nodes=adj)
        >>> DG = nx.DiGraph()
        >>> # dict-of-dict-of-attribute
        >>> adj = {1: {2: 1.3, 3: 0.7}, 2: {1: 1.4}, 3: {1: 0.7}}
        >>> e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
        ...      for v, d in nbrs.items()]
        >>> DG.update(edges=e, nodes=adj)
        >>> # dict-of-dict-of-dict
        >>> adj = {1: {2: {'weight': 1.3}, 3: {'color': 0.7, 'weight':1.2}}}
        >>> e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
        ...      for v, d in nbrs.items()]
        >>> DG.update(edges=e, nodes=adj)
        >>> # predecessor adjacency (dict-of-set)
        >>> pred = {1: {2, 3}, 2: {3}, 3: {3}}
        >>> e = [(v, u) for u, nbrs in pred.items() for v in nbrs]
        >>> # MultiGraph dict-of-dict-of-dict-of-attribute
        >>> MDG = nx.MultiDiGraph()
        >>> adj = {1: {2: {0: {'weight': 1.3}, 1: {'weight': 1.2}}},
        ...        3: {2: {0: {'weight': 0.7}}}}
        >>> e = [(u, v, ekey, d) for u, nbrs in adj.items()
        ...      for v, keydict in nbrs.items()
        ...      for ekey, d in keydict.items()]
        >>> MDG.update(edges=e)
        See Also
        --------
        add_edges_from: add multiple edges to a graph
        add_nodes_from: add multiple nodes to a graph
        """
        if edges is not None:
            if nodes is not None:
                self.add_nodes_from(nodes)
                self.add_edges_from(edges)
            else:
                # check if edges is a Graph object
                try:
                    graph_nodes = edges.nodes
                    graph_edges = edges.edges
                except AttributeError:
                    # edge not Graph-like
                    self.add_edges_from(edges)
                else:  # edges is Graph-like
                    self.add_nodes_from(graph_nodes.data())
                    self.add_edges_from(graph_edges.data())
                    self.graph.update(edges.graph)
        elif nodes is not None:
            self.add_nodes_from(nodes)
        else:
            raise sx.SnapXError("update needs nodes or edges input")

    def has_edge(self, u, v):
        """PORTED FROM NETWORKX
        Returns True if the edge (u, v) is in the graph.
        This is the same as `v in G[u]` without KeyError exceptions.
        Parameters
        ----------
        u, v : nodes
            Nodes can be, for example, strings or numbers.
            Nodes must be hashable (and not None) Python objects.
        Returns
        -------
        edge_ind : bool
            True if edge is in the graph, False otherwise.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.has_edge(0, 1)  # using two nodes
        True
        >>> e = (0, 1)
        >>> G.has_edge(*e)  #  e is a 2-tuple (u, v)
        True
        >>> e = (0, 1, {'weight':7})
        >>> G.has_edge(*e[:2])  # e is a 3-tuple (u, v, data_dictionary)
        True
        The following syntax are equivalent:
        >>> G.has_edge(0, 1)
        True
        >>> 1 in G[0]  # though this gives KeyError if 0 not in G
        True
        """
        u, v = Graph._order_edge(u, v)

        # Avoid snap runtime error by first checking
        # if the nodes exist
        if u not in self or v not in self:
            return False
        try:
            return self._graph.IsEdge(u, v)
        except TypeError:
            return False

    def neighbors(self, n):
        """PORTED FROM NETWORKX
        Returns an iterator over all neighbors of node n.
        This is identical to `iter(G[n])`
        Parameters
        ----------
        n : node
           A node in the graph
        Returns
        -------
        neighbors : iterator
            An iterator over all neighbors of node n
        Raises
        ------
        NetworkXError
            If the node n is not in the graph.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> [n for n in G.neighbors(0)]
        [1]
        Notes
        -----
        Alternate ways to access the neighbors are ``G.adj[n]`` or ``G[n]``:
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_edge('a', 'b', weight=7)
        >>> G['a']
        AtlasView({'b': {'weight': 7}})
        >>> G = nx.path_graph(4)
        >>> [n for n in G[0]]
        [1]
        """
        try:
            return iter(self.adj[n])
        except KeyError:
            raise SnapXError("The node {} is not in the graph.".format(n))

    @property
    def edges(self):
        """PORTED FROM NETWORKX
        An EdgeView of the Graph as G.edges or G.edges().
        edges(self, nbunch=None, data=False, default=None)
        The EdgeView provides set-like operations on the edge-tuples
        as well as edge attribute lookup. When called, it also provides
        an EdgeDataView object which allows control of access to edge
        attributes (but does not provide set-like operations).
        Hence, `G.edges[u, v]['color']` provides the value of the color
        attribute for edge `(u, v)` while
        `for (u, v, c) in G.edges.data('color', default='red'):`
        iterates through all the edges yielding the color attribute
        with default `'red'` if no color attribute exists.
        Parameters
        ----------
        nbunch : single node, container, or all nodes (default= all nodes)
            The view will only report edges incident to these nodes.
        data : string or bool, optional (default=False)
            The edge attribute returned in 3-tuple (u, v, ddict[data]).
            If True, return edge attribute dict in 3-tuple (u, v, ddict).
            If False, return 2-tuple (u, v).
        default : value, optional (default=None)
            Value used for edges that don't have the requested attribute.
            Only relevant if data is not True or False.
        Returns
        -------
        edges : EdgeView
            A view of edge attributes, usually it iterates over (u, v)
            or (u, v, d) tuples of edges, but can also be used for
            attribute lookup as `edges[u, v]['foo']`.
        Notes
        -----
        Nodes in nbunch that are not in the graph will be (quietly) ignored.
        For directed graphs this returns the out-edges.
        Examples
        --------
        >>> G = nx.path_graph(3)   # or MultiGraph, etc
        >>> G.add_edge(2, 3, weight=5)
        >>> [e for e in G.edges]
        [(0, 1), (1, 2), (2, 3)]
        >>> G.edges.data()  # default data is {} (empty dict)
        EdgeDataView([(0, 1, {}), (1, 2, {}), (2, 3, {'weight': 5})])
        >>> G.edges.data('weight', default=1)
        EdgeDataView([(0, 1, 1), (1, 2, 1), (2, 3, 5)])
        >>> G.edges([0, 3])  # only edges incident to these nodes
        EdgeDataView([(0, 1), (3, 2)])
        >>> G.edges(0)  # only edges incident to a single node (use G.adj[0]?)
        EdgeDataView([(0, 1)])
        """
        return EdgeView(self)

    def get_edge_data(self, u, v, default=None):
        """PORTED FROM NETWORKX
        Returns the attribute dictionary associated with edge (u, v).
        This is identical to `G[u][v]` except the default is returned
        instead of an exception if the edge doesn't exist.
        Parameters
        ----------
        u, v : nodes
        default:  any Python object (default=None)
            Value to return if the edge (u, v) is not found.
        Returns
        -------
        edge_dict : dictionary
            The edge attribute dictionary.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G[0][1]
        {}
        Warning: Assigning to `G[u][v]` is not permitted.
        But it is safe to assign attributes `G[u][v]['foo']`
        >>> G[0][1]['weight'] = 7
        >>> G[0][1]['weight']
        7
        >>> G[1][0]['weight']
        7
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.get_edge_data(0, 1)  # default edge data is {}
        {}
        >>> e = (0, 1)
        >>> G.get_edge_data(*e)  # tuple form
        {}
        >>> G.get_edge_data('a', 'b', default=0)  # edge not in graph, return 0
        0
        """
        try:
            return self.adj[u][v]
        except KeyError:
            return default

    def adjacency(self):
        """PORTED FROM NETWORKX
        Returns an iterator over (node, adjacency dict) tuples for all nodes.
        For directed graphs, only outgoing neighbors/adjacencies are included.
        Returns
        -------
        adj_iter : iterator
           An iterator over (node, adjacency dictionary) for all nodes in
           the graph.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> [(n, nbrdict) for n, nbrdict in G.adjacency()]
        [(0, {1: {}}), (1, {0: {}, 2: {}}), (2, {1: {}, 3: {}}), (3, {2: {}})]
        """
        return iter(self.adj.items())

    @property
    def degree(self):
        raise NotImplementedError("TODO")

    def clear(self):
        """PORTED_FROM_NETWORKX
        Remove all nodes and edges from the graph.
        This also removes the name, and all graph, node, and edge attributes.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.clear()
        >>> list(G.nodes)
        []
        >>> list(G.edges)
        []
        """
        self._graph.Clr()
        self._num_edges = 0
        self._node_extra_attr.clear()
        self._edge_extra_attr.clear()
        self.graph.clear()

    def is_multigraph(self):
        return False

    def is_directed(self):
        return False

    def copy(self, as_view=False):
        """PORTED FROM NETWORKX
        Returns a copy of the graph.
        The copy method by default returns an independent shallow copy
        of the graph and attributes. That is, if an attribute is a
        container, that container is shared by the original an the copy.
        Use Python's `copy.deepcopy` for new containers.
        If `as_view` is True then a view is returned instead of a copy.
        Notes
        -----
        All copies reproduce the graph structure, but data attributes
        may be handled in different ways. There are four types of copies
        of a graph that people might want.
        Deepcopy -- A "deepcopy" copies the graph structure as well as
        all data attributes and any objects they might contain.
        The entire graph object is new so that changes in the copy
        do not affect the original object. (see Python's copy.deepcopy)
        Data Reference (Shallow) -- For a shallow copy the graph structure
        is copied but the edge, node and graph attribute dicts are
        references to those in the original graph. This saves
        time and memory but could cause confusion if you change an attribute
        in one graph and it changes the attribute in the other.
        NetworkX does not provide this level of shallow copy.
        Independent Shallow -- This copy creates new independent attribute
        dicts and then does a shallow copy of the attributes. That is, any
        attributes that are containers are shared between the new graph
        and the original. This is exactly what `dict.copy()` provides.
        You can obtain this style copy using:
            >>> G = nx.path_graph(5)
            >>> H = G.copy()
            >>> H = G.copy(as_view=False)
            >>> H = nx.Graph(G)
            >>> H = G.__class__(G)
        Fresh Data -- For fresh data, the graph structure is copied while
        new empty data attribute dicts are created. The resulting graph
        is independent of the original and it has no edge, node or graph
        attributes. Fresh copies are not enabled. Instead use:
            >>> H = G.__class__()
            >>> H.add_nodes_from(G)
            >>> H.add_edges_from(G.edges)
        View -- Inspired by dict-views, graph-views act like read-only
        versions of the original graph, providing a copy of the original
        structure without requiring any memory for copying the information.
        See the Python copy module for more information on shallow
        and deep copies, https://docs.python.org/2/library/copy.html.
        Parameters
        ----------
        as_view : bool, optional (default=False)
            If True, the returned graph-view provides a read-only view
            of the original graph without actually copying any data.
        Returns
        -------
        G : Graph
            A copy of the graph.
        See Also
        --------
        to_directed: return a directed copy of the graph.
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> H = G.copy()
        """
        if as_view is True:
            raise NotImplementedError("TODO")
            # return nx.graphviews.generic_graph_view(self)
        G = self.__class__()
        G.graph.update(self.graph)
        # Copy snap graph
        G.add_nodes_from((n, d) for n, d in self.nodes(data=True))
        G.add_edges_from(
            (u, v, datadict)
            for u, nbrs in self.adj.items()
            for v, datadict in nbrs.items()
        )
        return G

    def to_directed(self, as_view=False):
        raise NotImplementedError("TODO")

    def to_undirected(self, as_view=False):
        raise NotImplementedError("TODO")

    def subgraph(self, nodes):
        """PORTED FROM NETWORKX
        Returns a SubGraph view of the subgraph induced on `nodes`.
        The induced subgraph of the graph contains the nodes in `nodes`
        and the edges between those nodes.
        Parameters
        ----------
        nodes : list, iterable
            A container of nodes which will be iterated through once.
        Returns
        -------
        G : SubGraph View
            A subgraph view of the graph. The graph structure cannot be
            changed but node/edge attributes can and are shared with the
            original graph.
        Notes
        -----
        The graph, edge and node attributes are shared with the original graph.
        Changes to the graph structure is ruled out by the view, but changes
        to attributes are reflected in the original graph.
        To create a subgraph with its own copy of the edge/node attributes use:
        G.subgraph(nodes).copy()
        For an inplace reduction of a graph to a subgraph you can remove nodes:
        G.remove_nodes_from([n for n in G if n not in set(nodes)])
        Subgraph views are sometimes NOT what you want. In most cases where
        you want to do more than simply look at the induced edges, it makes
        more sense to just create the subgraph as its own graph with code like:
        ::
            # Create a subgraph SG based on a (possibly multigraph) G
            SG = G.__class__()
            SG.add_nodes_from((n, G.nodes[n]) for n in largest_wcc)
            if SG.is_multigraph():
                SG.add_edges_from((n, nbr, key, d)
                    for n, nbrs in G.adj.items() if n in largest_wcc
                    for nbr, keydict in nbrs.items() if nbr in largest_wcc
                    for key, d in keydict.items())
            else:
                SG.add_edges_from((n, nbr, d)
                    for n, nbrs in G.adj.items() if n in largest_wcc
                    for nbr, d in nbrs.items() if nbr in largest_wcc)
            SG.graph.update(G.graph)
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> H = G.subgraph([0, 1, 2])
        >>> list(H.edges)
        [(0, 1), (1, 2)]
        """
        induced_nodes = sx.filters.show_nodes(self.nbunch_iter(nodes))
        # if already a subgraph, don't make a chain
        subgraph = sx.graphviews.subgraph_view
        if hasattr(self, "_NODE_OK"):
            return subgraph(self._graph, induced_nodes, self._EDGE_OK)
        return subgraph(self, induced_nodes)

    # def edge_subgraph(self, edges):
    #     """Returns the subgraph induced by the specified edges.
    #     The induced subgraph contains each edge in `edges` and each
    #     node incident to any one of those edges.
    #     Parameters
    #     ----------
    #     edges : iterable
    #         An iterable of edges in this graph.
    #     Returns
    #     -------
    #     G : Graph
    #         An edge-induced subgraph of this graph with the same edge
    #         attributes.
    #     Notes
    #     -----
    #     The graph, edge, and node attributes in the returned subgraph
    #     view are references to the corresponding attributes in the original
    #     graph. The view is read-only.
    #     To create a full graph version of the subgraph with its own copy
    #     of the edge or node attributes, use::
    #         >>> G.edge_subgraph(edges).copy()  # doctest: +SKIP
    #     Examples
    #     --------
    #     >>> G = nx.path_graph(5)
    #     >>> H = G.edge_subgraph([(0, 1), (3, 4)])
    #     >>> list(H.nodes)
    #     [0, 1, 3, 4]
    #     >>> list(H.edges)
    #     [(0, 1), (3, 4)]
    #     """
    #     return nx.edge_subgraph(self, edges)

    def size(self, weight=None):
        """PORTED FROM NETWORKX
        Returns the number of edges or total of all edge weights.
        Parameters
        ----------
        weight : string or None, optional (default=None)
            The edge attribute that holds the numerical value used
            as a weight. If None, then each edge has weight 1.
        Returns
        -------
        size : numeric
            The number of edges or
            (if weight keyword is provided) the total weight sum.
            If weight is None, returns an int. Otherwise a float
            (or more general numeric if the weights are more general).
        See Also
        --------
        number_of_edges
        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.size()
        3
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_edge('a', 'b', weight=2)
        >>> G.add_edge('b', 'c', weight=4)
        >>> G.size()
        2
        >>> G.size(weight='weight')
        6.0
        """
        if weight is not None:
            raise NotImplementedError("TODO")
        return self._num_edges

    def number_of_edges(self, u=None, v=None):
        """PORTED FROM NETWORKX
        Returns the number of edges between two nodes.
        Parameters
        ----------
        u, v : nodes, optional (default=all edges)
            If u and v are specified, return the number of edges between
            u and v. Otherwise return the total number of all edges.
        Returns
        -------
        nedges : int
            The number of edges in the graph.  If nodes `u` and `v` are
            specified return the number of edges between those nodes. If
            the graph is directed, this only returns the number of edges
            from `u` to `v`.
        See Also
        --------
        size
        Examples
        --------
        For undirected graphs, this method counts the total number of
        edges in the graph:
        >>> G = nx.path_graph(4)
        >>> G.number_of_edges()
        3
        If you specify two nodes, this counts the total number of edges
        joining the two nodes:
        >>> G.number_of_edges(0, 1)
        1
        For directed graphs, this method can count the total number of
        directed edges from `u` to `v`:
        >>> G = nx.DiGraph()
        >>> G.add_edge(0, 1)
        >>> G.add_edge(1, 0)
        >>> G.number_of_edges(0, 1)
        1
        """
        if u is None:
            return self.size()
        if self.has_edge(u, v):
            return 1
        return 0

    def nbunch_iter(self, nbunch=None):
        """PORTED FROM NETWORKX
        Returns an iterator over nodes contained in nbunch that are
        also in the graph.
        The nodes in nbunch are checked for membership in the graph
        and if not are silently ignored.
        Parameters
        ----------
        nbunch : single node, container, or all nodes (default= all nodes)
            The view will only report edges incident to these nodes.
        Returns
        -------
        niter : iterator
            An iterator over nodes in nbunch that are also in the graph.
            If nbunch is None, iterate over all nodes in the graph.
        Raises
        ------
        NetworkXError
            If nbunch is not a node or or sequence of nodes.
            If a node in nbunch is not hashable.
        See Also
        --------
        Graph.__iter__
        Notes
        -----
        When nbunch is an iterator, the returned iterator yields values
        directly from nbunch, becoming exhausted when nbunch is exhausted.
        To test whether nbunch is a single node, one can use
        "if nbunch in self:", even after processing with this routine.
        If nbunch is not a node or a (possibly empty) sequence/iterator
        or None, a :exc:`NetworkXError` is raised.  Also, if any object in
        nbunch is not hashable, a :exc:`NetworkXError` is raised.
        """
        if nbunch is None:
            bunch = iter(self)
        elif nbunch in self:
            bunch = iter([nbunch])
        else:

            def bunch_iter(nlist, adj):
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                except TypeError as e:
                    message = e.args[0]
                    # capture error for non-sequence/iterator nbunch.
                    if "iter" in message:
                        msg = "nbunch is not a node or a sequence of nodes."
                        raise SnapXError(msg)
                    else:
                        raise

            bunch = bunch_iter(nbunch, self.adj)
        return bunch

    def _edge_iter(self):
        """Returns a SNAP edge iterator."""
        return _TNEANetEdgeIter(self._graph.Edges(), directed=False)

    @property
    def snap_graph(self):
        """Returns the underlying SNAP graph."""
        return self._graph

    @staticmethod
    def _order_edge(u, v):
        return (u, v) if u <= v else (v, u)
