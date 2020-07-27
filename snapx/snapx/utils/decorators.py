from .decorator import decorator

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

