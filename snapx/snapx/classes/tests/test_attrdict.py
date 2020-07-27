import pytest

import snapx as sx

class TestAttributeDict:
    def setup(self):
        """By design, is impossible to decouple the graph from the AttributeDict,
        so I am setting up a graph first in this series of tests. I certainly don't
        enjoy passing around states, but I also don't have a better idea at the moment.
        Maybe someone can refine the design and reduce the amount of inter-
        dependence between Views, Graphs, and AttributeDict. """
        g = sx.Graph()
        g.add_nodes_from([0, 1, 2])
        g.add_edges_from([(0, 1), (0, 2), (1, 2)])
        self.g = g
        self.ndicts = {0: {"int": 1, "float": 1.234, "str": "This is a test string."},
                       1: {"float": 0.4, "foo": ["bar", "baz"]},
                       2: {"str": "string", "list": [1, 2], "dict": {"hello": "world"}}}
        self.edicts = {(0, 1): {"int": 2, "dict": {"aa": "bbb"}},
                       (0, 2): {"float": 0.23, "tuple": (1, 2, 4), "str": "abc", "int": 3},
                       (1, 2): {"str": "bar", "list": [3, "aaa"]}}
        # Implicitly calling __setitem__
        for n in self.ndicts.keys():
            self.g.nodes[n].update(self.ndicts[n])
        for e in self.edicts.keys():
            self.g.edges[e].update(self.edicts[e])

    def test_init_fail(self):
        """Checks if initialization successfully fails
        for invalid inputs"""
        g = sx.Graph()
        # Invalid node ID (not integer)
        with pytest.raises(sx.SnapXTypeError):
            sx.AttributeDict(g, "hoge")
        # Invalid format
        with pytest.raises(sx.SnapXTypeError):
            sx.AttributeDict(g, (1, 2, 3))
        # Invalid edge (not integer)
        with pytest.raises(sx.SnapXTypeError):
            sx.AttributeDict(g, (0, "hoge"))
        with pytest.raises(sx.SnapXTypeError):
            sx.AttributeDict(g, ("foo", 2))

        g.add_nodes_from([0, 1])
        # Nonexistent edge
        with pytest.raises(sx.SnapXKeyError):
            sx.AttributeDict(g, (0, 1))

    def test_contains(self):
        # Implicitly tests __iter__
        for n in self.ndicts.keys():
            for gt in self.ndicts[n]:
                assert gt in self.g.nodes[n]

        for e in self.edicts.keys():
            for gt in self.edicts[e]:
                assert gt in self.g.edges[e]

    def test_len(self):
        for n in self.ndicts.keys():
            assert len(self.g.nodes[n]) == len(self.ndicts[n])
        for e in self.edicts.keys():
            assert len(self.g.edges[e]) == len(self.edicts[e])

    def test_setitem_overwrite(self):
        self.g.nodes[0]["int"] = 34
        self.g.nodes[2]["str"] = "new string"

        assert self.g.nodes[0]["int"] == 34
        assert self.g.nodes[2]["str"] == "new string"

    def test_setitem_fail(self):
        # Only str is allowed as attr name
        with pytest.raises(sx.SnapXTypeError):
            self.g.nodes[0][123] = 456

    def test_items(self):
        # This implicitly tests __getitem__
        for n in self.ndicts.keys():
            assert sorted(self.ndicts[n].items()) == sorted(self.g.nodes[n].items())
        for e in self.edicts.keys():
            assert sorted(self.edicts[e].items()) == sorted(self.g.edges[e].items())

    def test_delitem(self):
        # attribute type supported by snap
        del self.g.nodes[0]["int"]
        del self.ndicts[0]["int"]
        for key in self.ndicts[0]:
            assert self.g.nodes[0][key] == self.ndicts[0][key]
        assert not "int" in self.g.nodes[0]

        # Not supported by snap
        del self.g.edges[(0, 2)]["float"]
        del self.edicts[(0, 2)]["float"]
        for key in self.edicts[(0, 2)]:
            assert self.g.edges[(0, 2)][key] == self.edicts[(0, 2)][key]
        assert not "float" in self.g.edges[(0, 2)]

