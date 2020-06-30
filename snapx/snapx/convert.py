import warnings
import snapx as sx

def to_snapx_graph(data, create_using=None, multigraph_input=False):
    """PORTED FROM NETWORKX
    Make a SnapX graph from a known data structure.
    The preferred way to call this is automatically
    from the class constructor
    >>> d = {0: {1: {'weight':1}}} # dict-of-dicts single edge (0,1)
    >>> G = nx.Graph(d)
    instead of the equivalent
    >>> G = nx.from_dict_of_dicts(d)
    Parameters
    ----------
    data : object to be converted
        Current known types are:
         any NetworkX graph
         dict-of-dicts
         dict-of-lists
         container (ie set, list, tuple, iterator) of edges
         Pandas DataFrame (row per edge)
         numpy matrix
         numpy ndarray
         scipy sparse matrix
         pygraphviz agraph
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
        Graph type to create. If graph instance, then cleared before populated.
    multigraph_input : bool (default False)
        If True and  data is a dict_of_dicts,
        try to create a multigraph assuming dict_of_dict_of_lists.
        If data and create_using are both multigraphs then create
        a multigraph from a multigraph.
    """
    # SX graph
    if hasattr(data, "adj"):
        try:
            result = from_dict_of_dicts(
                data.adj,
                create_using=create_using,
                multigraph_input=data.is_multigraph(),
            )
            if hasattr(data, "graph"):  # data.graph should be dict-like
                result.graph.update(data.graph)
            if hasattr(data, "nodes"):  # data.nodes should be dict-like
                # result.add_node_from(data.nodes.items()) possible but
                # for custom node_attr_dict_factory which may be hashable
                # will be unexpected behavior
                for n, dd in data.nodes.items():
                    result._node[n].update(dd)
            return result
        except:
            raise sx.SnapXError("Input is not a correct SnapX graph.")

    # pygraphviz  agraph
    if hasattr(data, "is_strict"):
        raise NotImplementedError("TODO")
        #try:
        #    return nx.nx_agraph.from_agraph(data, create_using=create_using)
        #except:
        #    raise nx.NetworkXError("Input is not a correct pygraphviz graph.")

    # dict of dicts/lists
    if isinstance(data, dict):
        raise NotImplementedError("TODO")
        #try:
        #    return from_dict_of_dicts(
        #        data, create_using=create_using, multigraph_input=multigraph_input
        #    )
        #except:
        #    try:
        #        return from_dict_of_lists(data, create_using=create_using)
        #    except:
        #        raise TypeError("Input is not known type.")

    # list or generator of edges

    if isinstance(data, (list, tuple, set)) or any(
        hasattr(data, attr) for attr in ["_adjdict", "next", "__next__"]
    ):
        raise NotImplementedError("TODO")
        #try:
        #    return from_edgelist(data, create_using=create_using)
        #except:
        #    raise nx.NetworkXError("Input is not a valid edge list")

    # Pandas DataFrame
    try:
        import pandas as pd

        if isinstance(data, pd.DataFrame):
            raise NotImplementedError("TODO")
            #if data.shape[0] == data.shape[1]:
            #    try:
            #        return nx.from_pandas_adjacency(data, create_using=create_using)
            #    except:
            #        msg = "Input is not a correct Pandas DataFrame adjacency matrix."
            #        raise nx.NetworkXError(msg)
            #else:
            #    try:
            #        return nx.from_pandas_edgelist(
            #            data, edge_attr=True, create_using=create_using
            #        )
            #    except:
            #        msg = "Input is not a correct Pandas DataFrame edge-list."
            #        raise nx.NetworkXError(msg)
    except ImportError:
        msg = "pandas not found, skipping conversion test."
        warnings.warn(msg, ImportWarning)

    # numpy matrix or ndarray
    try:
        import numpy

        if isinstance(data, (numpy.matrix, numpy.ndarray)):
            raise NotImplementedError("TODO")
            #try:
            #    return nx.from_numpy_matrix(data, create_using=create_using)
            #except:
            #    raise nx.NetworkXError("Input is not a correct numpy matrix or array.")
    except ImportError:
        warnings.warn("numpy not found, skipping conversion test.", ImportWarning)

    # scipy sparse matrix - any format
    try:
        import scipy

        if hasattr(data, "format"):
            raise NotImplementedError("TODO")
            #try:
            #    return nx.from_scipy_sparse_matrix(data, create_using=create_using)
            #except:
            #    raise nx.NetworkXError(
            #        "Input is not a correct scipy sparse matrix type."
            #    )
    except ImportError:
        warnings.warn("scipy not found, skipping conversion test.", ImportWarning)

    raise sx.SnapXError("Input is not a known data type for conversion.")

def from_dict_of_dicts(d, create_using=None, multigraph_input=False):
    """PORTED FROM NETWORKX
    Returns a graph from a dictionary of dictionaries.
    Parameters
    ----------
    d : dictionary of dictionaries
      A dictionary of dictionaries adjacency representation.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
        Graph type to create. If graph instance, then cleared before populated.
    multigraph_input : bool (default False)
       When True, the values of the inner dict are assumed
       to be containers of edge data for multiple edges.
       Otherwise this routine assumes the edge data are singletons.
    Examples
    --------
    >>> dod = {0: {1: {'weight': 1}}} # single edge (0,1)
    >>> G = nx.from_dict_of_dicts(dod)
    or
    >>> G = nx.Graph(dod) # use Graph constructor
    """
    G = sx.empty_graph(0, create_using)
    G.add_nodes_from(d)
    # is dict a MultiGraph or MultiDiGraph?
    if multigraph_input:
        # make a copy of the list of edge data (but not the edge data)
        if G.is_directed():
            if G.is_multigraph():
                G.add_edges_from(
                    (u, v, key, data)
                    for u, nbrs in d.items()
                    for v, datadict in nbrs.items()
                    for key, data in datadict.items()
                )
            else:
                G.add_edges_from(
                    (u, v, data)
                    for u, nbrs in d.items()
                    for v, datadict in nbrs.items()
                    for key, data in datadict.items()
                )
        else:  # Undirected
            if G.is_multigraph():
                seen = set()  # don't add both directions of undirected graph
                for u, nbrs in d.items():
                    for v, datadict in nbrs.items():
                        if (u, v) not in seen:
                            G.add_edges_from(
                                (u, v, key, data) for key, data in datadict.items()
                            )
                            seen.add((v, u))
            else:
                seen = set()  # don't add both directions of undirected graph
                for u, nbrs in d.items():
                    for v, datadict in nbrs.items():
                        if (u, v) not in seen:
                            G.add_edges_from(
                                (u, v, data) for key, data in datadict.items()
                            )
                            seen.add((v, u))

    else:  # not a multigraph to multigraph transfer
        if G.is_multigraph() and not G.is_directed():
            # d can have both representations u-v, v-u in dict.  Only add one.
            # We don't need this check for digraphs since we add both directions,
            # or for Graph() since it is done implicitly (parallel edges not allowed)
            seen = set()
            for u, nbrs in d.items():
                for v, data in nbrs.items():
                    if (u, v) not in seen:
                        G.add_edge(u, v, key=0)
                        G[u][v][0].update(data)
                    seen.add((v, u))
        else:
            G.add_edges_from(
                ((u, v, data) for u, nbrs in d.items() for v, data in nbrs.items())
            )
    return G
