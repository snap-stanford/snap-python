# coding: utf-8
import hashlib
import math
import os
import re
import time
import unittest

import snap

PATH_TO_GNUTELLA = "data/p2p-Gnutella08.txt"

class SnapPythonTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.gnutella = snap.LoadEdgeList(snap.PNGraph, PATH_TO_GNUTELLA)
        super(SnapPythonTest, self).__init__(*args, **kwargs)

    def setUp(self):
        # Defaults for creating graphs
        self.num_nodes = 10

        # Full Graphs
        self.DirGraphFull = snap.GenFull(snap.PNGraph, self.num_nodes)
        self.UnDirGraphFull = snap.GenFull(snap.PUNGraph, self.num_nodes)
        self.NetFull = snap.GenFull(snap.PNEANet, self.num_nodes)

        # Star Graphs
        self.DirGraphStar = snap.GenStar(snap.PNGraph, self.num_nodes)
        self.UnDirGraphStar = snap.GenStar(snap.PUNGraph, self.num_nodes)
        self.NetStar = snap.GenStar(snap.PNEANet, self.num_nodes)

        # Graph With Self Edges
        self.DirGraphSelfEdge = snap.GenRndGnm(snap.PNGraph, 10, 20)
        self.DirGraphSelfEdge.AddEdge(0, 0)
        self.UnDirGraphSelfEdge = snap.GenRndGnm(snap.PUNGraph, 10, 20)
        self.UnDirGraphSelfEdge.AddEdge(0, 0)
        self.NetSelfEdge = snap.GenRndGnm(snap.PNEANet, 10, 20)
        self.NetSelfEdge.AddEdge(0, 0)

        # Graph With Multiple Zero-Degree Nodes
        self.DirGraphZeroDegree = snap.GenRndGnm(snap.PNGraph, 10, 1)
        self.UnDirGraphZeroDegree = snap.GenRndGnm(snap.PUNGraph, 10, 1)
        self.NetZeroDegree = snap.GenRndGnm(snap.PNEANet, 10, 1)

        # Trees
        self.DirTree = snap.GenTree(snap.PNGraph, 3, 3)
        self.UnDirTree = snap.GenTree(snap.PUNGraph, 3, 3)
        self.NetTree = snap.GenTree(snap.PNEANet, 3, 3)

        # Random
        self.DirRand = snap.GenRndGnm(snap.PNGraph, 10, 20)
        self.UnDirRand = snap.GenRndGnm(snap.PUNGraph, 10, 20)
        self.NetRand = snap.GenRndGnm(snap.PNEANet, 10, 20)






    #### Helper Functions for Tests ####

    def checkPlotHash(self, gen_file, exp_hash):
        self.assertTrue(os.path.isfile(gen_file))
        f = open(gen_file,'r')
        lines = f.readlines()
        f.close()
        # remove comments, since these include time
        newlines = []
        for line in lines:
            if len(line) > 0  and  line[0] == "#":
                continue
            newlines.append(line)
        # remove carriage return, which is included on Windows
        newcontent = str("".join(newlines).replace("\r","")).encode("utf-8")
        act_hash = hashlib.md5(newcontent).hexdigest()
        self.assertEqual(exp_hash, act_hash)

    def getFileHash(self, fname):
        f = open(fname, 'r')
        content = f.read()
        f.close()
        newcontent = str(content.replace("\r","")).encode("utf-8")
        test_hash = hashlib.md5(newcontent).hexdigest()
        return test_hash

    def checkPrintInfoOutput(self, filename, params):
        count = 0
        with open(filename) as f:
            for line in f:
                if count == 0:
                    firstLine = line.split(':')
                    self.assertEqual(params[count], firstLine[0])
                else:
                    result = re.findall('[0-9]+', line)
                    self.assertEqual(params[count], result[0])
                count += 1

    #### Tests ####

    # Avery Vector tests
    def test_vec_append(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)

        vector = snap.TIntV()
        vector.append(1)
        self.assertEqual(vector, new_vec)

    def test_vec_extend(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)
        new_vec.Add(2)
        new_vec.Add(3)

        # Vector to extend by
        extend_vec = snap.TIntV()
        extend_vec.Add(2)
        extend_vec.Add(3)

        # Extend operation
        vector = snap.TIntV()
        vector.Add(1)
        vector.extend(extend_vec)

        self.assertEqual(vector, new_vec)

    def test_vec_clear(self):
        # Vector to test against
        new_vec = snap.TIntV()

        # Adding to and clearing vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.clear()

        self.assertEqual(vector, new_vec)

    def test_vec_insert(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)
        new_vec.Add(2)
        new_vec.Add(3)

        # Attempting insert on self.vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(3)
        vector.insert(1, 2)

        self.assertEqual(vector, new_vec)
    #
    def test_vec_remove(self):
        # Vector to test against
        new_vec = snap.TIntV()
        new_vec.Add(1)

        # Attempting insert on vector
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        vector.remove(2)

        self.assertEqual(vector, new_vec)

    def test_vec_index(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        index = vector.index(2)

        self.assertEqual(index, 1)

    def test_vec_count(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(1)
        vector.Add(1)
        num_ones = vector.count(1)

        self.assertEqual(num_ones, 3)

    def test_vec_pop(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        popped = vector.pop(1)

        self.assertEqual(popped, 2)

    def test_vec_reverse(self):
        # Vector to compare
        new_vec = snap.TIntV()
        new_vec.Add(2)
        new_vec.Add(1)

        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        vector.reverse()

        self.assertEqual(vector, new_vec)

    def test_vec_sort(self):
        # Vector to compare
        new_vec = snap.TIntV()
        new_vec.Add(3)
        new_vec.Add(2)
        new_vec.Add(1)

        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(3)
        vector.Add(2)
        vector.sort(asc=False)
        self.assertEqual(vector, new_vec)

    def test_vec_copy(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(2)
        new_vec = vector.copy()

        self.assertEqual(vector, new_vec)

    def test_vec_max(self):
        vector = snap.TIntV()
        vector.Add(1)
        vector.Add(5)
        vector.Add(2)

        maximum = max(vector)

        self.assertEqual(maximum, 5)

    def test_vec_min(self):
        vector = snap.TIntV()
        vector.Add(2)
        vector.Add(1)
        vector.Add(5)

        minimum = min(vector)

        self.assertEqual(minimum, 1)

    # # Avery Hash Table Tests
    def test_hash_clear(self):
        new_ht = snap.TIntH()

        ht = snap.TIntH()
        ht[1] = 2
        ht.clear()

        self.assertEqual(ht, new_ht)

    def test_hash_copy(self):
        ht = snap.TIntH()
        ht[1] = 2
        new_ht = ht.copy()

        self.assertEqual(ht, new_ht)

    def test_hash_get(self):
        ht = snap.TIntH()
        ht[1] = 2
        value = ht.get(1)

        self.assertEqual(value, 2)

    def test_hash_items(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        items = [(1, 2), (3, 4)]
        ht_items = ht.items()

        self.assertEqual(items, ht_items)

    def test_hash_keys(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        keys = [1, 3]
        ht_keys = ht.keys()

        self.assertEqual(keys, ht_keys)

    def test_hash_pop(self):
        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        popped = 2
        ht_popped = ht.pop(1)

        self.assertEqual(popped, ht_popped)

    def test_hash_setdefault(self):
        new_ht = snap.TIntH()
        new_ht[1] = 2
        new_ht[3] = 4

        ht = snap.TIntH()
        ht[1] = 2
        default_val = ht.setdefault(3, 4)

        self.assertEqual(ht, new_ht)
        self.assertEqual(default_val, 4)

    def test_hash_update(self):
        new_ht = snap.TIntH()
        new_ht[1] = 2
        new_ht[3] = 5

        ht = snap.TIntH()
        ht[3] = 4
        ht.update(new_ht)

        final_ht = snap.TIntH()
        final_ht[1] = 2
        final_ht[3] = 5

        self.assertEqual(ht, final_ht)

    def test_hash_values(self):
        expected_values = [2, 4]

        ht = snap.TIntH()
        ht[1] = 2
        ht[3] = 4
        values = ht.values()

        self.assertEqual(expected_values, values)


if __name__ == '__main__':
  unittest.main()

