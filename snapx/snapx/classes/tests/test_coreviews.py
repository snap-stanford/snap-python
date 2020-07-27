import pytest
import pickle

import snapx as sx


class TestAtlasView:
    def setup(self):
        g = sx.Graph()
        g.add_nodes_from([0, 1, 2])
        # This is what we expect the AtlasView for node 0 to look like
        self.atlas = {0: {'color': 'blue', 'weight': 1.2}, 1: {}, 2: {'color': 'green'}}
        for key in self.atlas.keys():
            g.add_edge(0, key)
            g.edges[(0, key)].update(self.atlas[key])
        self.g = g
        self.av = sx.classes.coreviews.AtlasView(g, 0)

    # NOTE: Not supported
    #def test_pickle(self):
    #    view = self.av
    #    pview = pickle.loads(pickle.dumps(view, -1))
    #    assert view == pview
    #    assert view.__slots__ == pview.__slots__
    #    pview = pickle.loads(pickle.dumps(view))
    #    assert view == pview
    #    assert view.__slots__ == pview.__slots__

    def test_len(self):
        assert len(self.av) == len(self.atlas)

    def test_iter(self):
        assert list(self.av) == list(self.atlas)

    def test_getitem(self):
        for n in self.atlas:
            for key in self.atlas[n]:
                assert self.av[n][key] == self.atlas[n][key]
        with pytest.raises(KeyError):
            self.av[3]

    # NOTE: Not supported
    #def test_copy(self):
    #    avcopy = self.av.copy()
    #    assert avcopy[0] == self.av[0]
    #    assert avcopy == self.av
    #    assert avcopy[0] is not self.av[0]
    #    assert avcopy is not self.av
    #    avcopy[5] = {}
    #    assert avcopy != self.av

    #    avcopy[0]['ht'] = 4
    #    assert avcopy[0] != self.av[0]
    #    self.av[0]['ht'] = 4
    #    assert avcopy[0] == self.av[0]
    #    del self.av[0]['ht']

    #    assert not hasattr(self.av, '__setitem__')

    def test_items(self):
        assert sorted(self.av.items()) == sorted(self.atlas.items())

    def test_str(self):
        out = str(self.atlas)
        assert str(self.av) == out

    def test_repr(self):
        out = "AtlasView(" + str(self.atlas) + ")"
        assert repr(self.av) == out

class TestAdjacencyView:
    # node->nbr->data
    def setup(self):
        g = sx.Graph()
        g.add_nodes_from([0, 1, 2, 3])
        dd03 = {'color': 'blue', 'weight': 1.2}
        dd23 = {'color': 'green'}
        # This is what we expect the AdjacencyView to look like:
        self.adj = {0: {3: dd03}, 1: {}, 2: {3: dd23}, 3: {0: dd03, 2: dd23}}
        for src in self.adj.keys():
            for dst in self.adj[src]:
                g.add_edge(src, dst)
                g.edges[(src, dst)].update(self.adj[src][dst])
        self.g = g
        self.adjview = sx.classes.coreviews.AdjacencyView(g)

    # NOTE: Not supported
    #def test_pickle(self):
    #    view = self.adjview
    #    pview = pickle.loads(pickle.dumps(view, -1))
    #    assert view == pview
    #    assert view.__slots__ == pview.__slots__

    def test_len(self):
        assert len(self.adjview) == len(self.adj)

    def test_iter(self):
        assert sorted(list(self.adjview)) == sorted(list(self.adj))

    def test_getitem(self):
        for src in self.adj:
            for dst in self.adj[src]:
                for key in self.adj[src][dst]:
                    assert self.adjview[src][dst][key] == self.adj[src][dst][key]

        with pytest.raises(KeyError):
            self.adjview[4]

    # NOTE: Not supported
    #def test_copy(self):
    #    avcopy = self.adjview.copy()
    #    assert avcopy[0] == self.adjview[0]
    #    assert avcopy[0] is not self.adjview[0]

    #    avcopy[2][3]['ht'] = 4
    #    assert avcopy[2] != self.adjview[2]
    #    self.adjview[2][3]['ht'] = 4
    #    assert avcopy[2] == self.adjview[2]
    #    del self.adjview[2][3]['ht']

    #    assert not hasattr(self.adjview, '__setitem__')

    def test_items(self):
        view_items = sorted((n, dict(d)) for n, d in self.adjview.items())
        assert view_items == sorted(self.adj.items())

    def test_str(self):
        out = str(dict(self.adj))
        assert str(self.adjview) == out

    def test_repr(self):
        out = self.adjview.__class__.__name__ + "(" + str(self.adj) + ")"
        assert repr(self.adjview) == out
