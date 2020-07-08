"""Defines private classes for vairous iterators
"""
from snap import TIntV, TFltV, TStrV
from collections.abc import Generator

class _BaseIterator:
    def __init__(self, it):
        if not isinstance(it, Generator):
            raise TypeError('Expected Generator, but got {}'.format(type(it).__name__))
        self._iter = it
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            cur = next(self._iter).GetId()
            return cur
        except:
            # TODO: We need to find a better way to handle the stopiter?
            raise StopIteration


class _GraphNodeIterator(_BaseIterator):
    '''Iterates over graph nodes'''

class _GraphEdgeIterator(_BaseIterator):
    '''Iterates over edges'''

class _TNEANetEdgeIter:
    def __init__(self, it, directed=False):
        if not isinstance(it, Generator):
            raise TypeError('Expected Generator, but got {}'.format(type(it).__name__))
        self._iter = it
        self._directed = directed
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            # HACK: Use the fact that we need only return (lo, hi) pair for
            # undirected graph. (Need to check if the snap C++ layer indeed
            # throws an exception when reaching the end of chain though, otherwise
            # we risk infinite loop...) 
            while True:
                cur = next(self._iter)
                src = cur.GetSrcNId(); dst = cur.GetDstNId()
                if self._directed or src <= dst:
                    return (src, dst)

        except:
            # TODO: We need to find a better way to handle the stopiter?
            raise StopIteration

class _GraphNodeDataIterator:
    def __init__(self, g):
        self._graph = g
        self._attr_fns = ((self._graph.snap_graph.IntAttrNameNI, self._graph.snap_graph.GetIntAttrDatN),
                          (self._graph.snap_graph.FltAttrNameNI, self._graph.snap_graph.GetFltAttrDatN),
                          (self._graph.snap_graph.StrAttrNameNI, self._graph.snap_graph.GetStrAttrDatN))

    def __iter__(self):
        for n in self._graph:
            res = {} # TODO: Maybe there's a way to do this in-memory?
            for (key_fn, val_fn) in self._attr_fns:
                _attr_names = TStrV()
                key_fn(n, _attr_names)
                for _attr in _attr_names:
                    res[_attr] = val_fn(n, _attr)

            yield (n, res)

class _GraphEdgeDataIterator:
    pass