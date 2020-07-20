__all__ = ["set_node_attributes", "set_edge_attributes", "freeze"]


def set_node_attributes(G, values, name=None):
    """PORTED FROM NETWORKX
    Sets node attributes from a given value or dictionary of values.
    .. Warning:: The call order of arguments `values` and `name`
        switched between v1.x & v2.x.
    Parameters
    ----------
    G : NetworkX Graph
    values : scalar value, dict-like
        What the node attribute should be set to.  If `values` is
        not a dictionary, then it is treated as a single attribute value
        that is then applied to every node in `G`.  This means that if
        you provide a mutable object, like a list, updates to that object
        will be reflected in the node attribute for every node.
        The attribute name will be `name`.
        If `values` is a dict or a dict of dict, it should be keyed
        by node to either an attribute value or a dict of attribute key/value
        pairs used to update the node's attributes.
    name : string (optional, default=None)
        Name of the node attribute to set if values is a scalar.
    Examples
    --------
    After computing some property of the nodes of a graph, you may want
    to assign a node attribute to store the value of that property for
    each node::
        >>> G = nx.path_graph(3)
        >>> bb = nx.betweenness_centrality(G)
        >>> isinstance(bb, dict)
        True
        >>> nx.set_node_attributes(G, bb, 'betweenness')
        >>> G.nodes[1]['betweenness']
        1.0
    If you provide a list as the second argument, updates to the list
    will be reflected in the node attribute for each node::
        >>> G = nx.path_graph(3)
        >>> labels = []
        >>> nx.set_node_attributes(G, labels, 'labels')
        >>> labels.append('foo')
        >>> G.nodes[0]['labels']
        ['foo']
        >>> G.nodes[1]['labels']
        ['foo']
        >>> G.nodes[2]['labels']
        ['foo']
    If you provide a dictionary of dictionaries as the second argument,
    the outer dictionary is assumed to be keyed by node to an inner
    dictionary of node attributes for that node::
        >>> G = nx.path_graph(3)
        >>> attrs = {0: {'attr1': 20, 'attr2': 'nothing'}, 1: {'attr2': 3}}
        >>> nx.set_node_attributes(G, attrs)
        >>> G.nodes[0]['attr1']
        20
        >>> G.nodes[0]['attr2']
        'nothing'
        >>> G.nodes[1]['attr2']
        3
        >>> G.nodes[2]
        {}
    """
    # Set node attributes based on type of `values`
    if name is not None:  # `values` must not be a dict of dict
        try:  # `values` is a dict
            for n, v in values.items():
                try:
                    G.nodes[n][name] = values[n]
                except KeyError:
                    pass
        except AttributeError:  # `values` is a constant
            for n in G:
                G.nodes[n][name] = values
    else:  # `values` must be dict of dict
        for n, d in values.items():
            try:
                G.nodes[n].update(d)
            except KeyError:
                pass


def set_edge_attributes(G, values, name=None):
    """PORTED FROM NETWORKX
    Sets edge attributes from a given value or dictionary of values.
    .. Warning:: The call order of arguments `values` and `name`
        switched between v1.x & v2.x.
    Parameters
    ----------
    G : NetworkX Graph
    values : scalar value, dict-like
        What the edge attribute should be set to.  If `values` is
        not a dictionary, then it is treated as a single attribute value
        that is then applied to every edge in `G`.  This means that if
        you provide a mutable object, like a list, updates to that object
        will be reflected in the edge attribute for each edge.  The attribute
        name will be `name`.
        If `values` is a dict or a dict of dict, it should be keyed
        by edge tuple to either an attribute value or a dict of attribute
        key/value pairs used to update the edge's attributes.
        For multigraphs, the edge tuples must be of the form ``(u, v, key)``,
        where `u` and `v` are nodes and `key` is the edge key.
        For non-multigraphs, the keys must be tuples of the form ``(u, v)``.
    name : string (optional, default=None)
        Name of the edge attribute to set if values is a scalar.
    Examples
    --------
    After computing some property of the edges of a graph, you may want
    to assign a edge attribute to store the value of that property for
    each edge::
        >>> G = nx.path_graph(3)
        >>> bb = nx.edge_betweenness_centrality(G, normalized=False)
        >>> nx.set_edge_attributes(G, bb, 'betweenness')
        >>> G.edges[1, 2]['betweenness']
        2.0
    If you provide a list as the second argument, updates to the list
    will be reflected in the edge attribute for each edge::
        >>> labels = []
        >>> nx.set_edge_attributes(G, labels, 'labels')
        >>> labels.append('foo')
        >>> G.edges[0, 1]['labels']
        ['foo']
        >>> G.edges[1, 2]['labels']
        ['foo']
    If you provide a dictionary of dictionaries as the second argument,
    the entire dictionary will be used to update edge attributes::
        >>> G = nx.path_graph(3)
        >>> attrs = {(0, 1): {'attr1': 20, 'attr2': 'nothing'},
        ...          (1, 2): {'attr2': 3}}
        >>> nx.set_edge_attributes(G, attrs)
        >>> G[0][1]['attr1']
        20
        >>> G[0][1]['attr2']
        'nothing'
        >>> G[1][2]['attr2']
        3
    """
    if name is not None:
        # `values` does not contain attribute names
        try:
            # if `values` is a dict using `.items()` => {edge: value}
            if G.is_multigraph():
                for (u, v, key), value in values.items():
                    try:
                        G[u][v][key][name] = value
                    except KeyError:
                        pass
            else:
                for (u, v), value in values.items():
                    try:
                        G[u][v][name] = value
                    except KeyError:
                        pass
        except AttributeError:
            # treat `values` as a constant
            for u, v, data in G.edges(data=True):
                data[name] = values
    else:
        # `values` consists of doct-of-dict {edge: {attr: value}} shape
        if G.is_multigraph():
            for (u, v, key), d in values.items():
                try:
                    G[u][v][key].update(d)
                except KeyError:
                    pass
        else:
            for (u, v), d in values.items():
                try:
                    G[u][v].update(d)
                except KeyError:
                    pass


# def edge_subgraph(G, edges):
#     """PORTED FROM NETWORKX
#     Returns a view of the subgraph induced by the specified edges.
#     The induced subgraph contains each edge in `edges` and each
#     node incident to any of those edges.
#     Parameters
#     ----------
#     G : NetworkX Graph
#     edges : iterable
#         An iterable of edges. Edges not present in `G` are ignored.
#     Returns
#     -------
#     subgraph : SubGraph View
#         A read-only edge-induced subgraph of `G`.
#         Changes to `G` are reflected in the view.
#     Notes
#     -----
#     To create a mutable subgraph with its own copies of nodes
#     edges and attributes use `subgraph.copy()` or `Graph(subgraph)`
#     If you create a subgraph of a subgraph recursively you can end up
#     with a chain of subgraphs that becomes very slow with about 15
#     nested subgraph views. Luckily the edge_subgraph filter nests
#     nicely so you can use the original graph as G in this function
#     to avoid chains. We do not rule out chains programmatically so
#     that odd cases like an `edge_subgraph` of a `restricted_view`
#     can be created.
#     Examples
#     --------
#     >>> import networkx as nx
#     >>> G = nx.path_graph(5)
#     >>> H = G.edge_subgraph([(0, 1), (3, 4)])
#     >>> list(H.nodes)
#     [0, 1, 3, 4]
#     >>> list(H.edges)
#     [(0, 1), (3, 4)]
#     """
#     sxf = sx.filters
#     edges = set(edges)
#     nodes = set()
#     for e in edges:
#         nodes.update(e[:2])
#     induced_nodes = sxf.show_nodes(nodes)
#     if G.is_multigraph():
#         if G.is_directed():
#             induced_edges = sxf.show_multidiedges(edges)
#         else:
#             induced_edges = sxf.show_multiedges(edges)
#     else:
#         if G.is_directed():
#             induced_edges = sxf.show_diedges(edges)
#         else:
#             induced_edges = sxf.show_edges(edges)
#     return sx.graphviews.subgraph_view(G, induced_nodes, induced_edges)


def frozen(*args, **kwargs):
    """Dummy method for raising errors when trying to modify frozen graphs"""
    raise sx.SnapXError("Frozen graph can't be modified")


def freeze(G):
    """Modify graph to prevent further change by adding or removing
    nodes or edges.
    Node and edge data can still be modified.
    Parameters
    ----------
    G : graph
      A NetworkX graph
    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> G = nx.freeze(G)
    >>> try:
    ...    G.add_edge(4, 5)
    ... except nx.NetworkXError as e:
    ...    print(str(e))
    Frozen graph can't be modified
    Notes
    -----
    To "unfreeze" a graph you must make a copy by creating a new graph object:
    >>> graph = nx.path_graph(4)
    >>> frozen_graph = nx.freeze(graph)
    >>> unfrozen_graph = nx.Graph(frozen_graph)
    >>> nx.is_frozen(unfrozen_graph)
    False
    See Also
    --------
    is_frozen
    """
    G.add_node = frozen
    G.add_nodes_from = frozen
    G.remove_node = frozen
    G.remove_nodes_from = frozen
    G.add_edge = frozen
    G.add_edges_from = frozen
    G.add_weighted_edges_from = frozen
    G.remove_edge = frozen
    G.remove_edges_from = frozen
    G.clear = frozen
    G.frozen = True
    return G
