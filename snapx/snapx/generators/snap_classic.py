"""Generators of common graphs derived from C++ snap."""

from snap import GenFull, GenCircle, PNEANet

from snapx import Graph

__all__ = [
    'complete_graph',
    'cycle_graph'
]

def complete_graph(n, create_using=None):
    """ Return the complete graph `K_n` with n nodes."""
    # TODO: Come back to support a semantics identical
    # to that of NetworkX!

    gen = Graph if create_using is None else create_using

    return gen(GenFull(PNEANet, n))


def cycle_graph(n, create_using=None):
    """Returns the cycle graph $C_n$ of cyclically connected nodes.
    """
    # TODO: Come back to support different graphs.
    gen = Graph if create_using is None else create_using

    return gen(GenCircle(PNEANet, n, 1))
