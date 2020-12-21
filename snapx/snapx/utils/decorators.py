from .decorator import decorator
import snapx as sx

def nodes_or_number(which_args):
    """PORTED FROM NETWORKX
    Decorator to allow number of nodes or container of nodes.
    Parameters
    ----------
    which_args : int or sequence of ints
        Location of the node arguments in args. Even if the argument is a
        named positional argument (with a default value), you must specify its
        index as a positional argument.
        If more than one node argument is allowed, can be a list of locations.
    Returns
    -------
    _nodes_or_numbers : function
        Function which replaces int args with ranges.
    Examples
    --------
    Decorate functions like this::
       @nodes_or_number(0)
       def empty_graph(nodes):
           pass
       @nodes_or_number([0,1])
       def grid_2d_graph(m1, m2, periodic=False):
           pass
       @nodes_or_number(1)
       def full_rary_tree(r, n)
           # r is a number. n can be a number of a list of nodes
           pass
    """
    @decorator
    def _nodes_or_number(func_to_be_decorated, *args, **kw):
        # form tuple of arg positions to be converted.
        try:
            iter_wa = iter(which_args)
        except TypeError:
            iter_wa = (which_args,)
        # change each argument in turn
        new_args = list(args)
        for i in iter_wa:
            n = args[i]
            try:
                nodes = list(range(n))
            except TypeError:
                nodes = tuple(n)
            else:
                if n < 0:
                    msg = "Negative number of nodes not valid: {}".format(n)
                    raise sx.SnapXError(msg)
            new_args[i] = (n, nodes)
        return func_to_be_decorated(*new_args, **kw)
    return _nodes_or_number

def not_implemented_for(*graph_types):
    """PORTED FROM NETWORKX
    Decorator to mark algorithms as not implemented

    Parameters
    ----------
    graph_types : container of strings
        Entries must be one of 'directed','undirected', 'multigraph', 'graph'.

    Returns
    -------
    _require : function
        The decorated function.

    Raises
    ------
    NetworkXNotImplemented
    If any of the packages cannot be imported

    Notes
    -----
    Multiple types are joined logically with "and".
    For "or" use multiple @not_implemented_for() lines.

    Examples
    --------
    Decorate functions like this::

       @not_implemnted_for('directed')
       def sp_function(G):
           pass

       @not_implemnted_for('directed','multigraph')
       def sp_np_function(G):
           pass
    """

    @decorator
    def _not_implemented_for(not_implement_for_func, *args, **kwargs):
        graph = args[0]
        terms = {
            "directed": graph.is_directed(),
            "undirected": not graph.is_directed(),
            "multigraph": graph.is_multigraph(),
            "graph": not graph.is_multigraph(),
        }
        match = True
        try:
            for t in graph_types:
                match = match and terms[t]
        except KeyError as e:
            raise KeyError(
                "use one or more of " "directed, undirected, multigraph, graph"
            ) from e
        if match:
            msg = "not implemented for {} type".format(' '.join(graph_types))
            raise sx.SnapXNotImplemented(msg)
        else:
            return not_implement_for_func(*args, **kwargs)

    return _not_implemented_for
