%pythoncode %{

#
# define __getitem__ for [] addressing
#
def getitem_hashset(self, i):
    return self.GetSetKey(i)

def delitem_hashset(self, i):
    self.DelKey(i)

def contains_hashset(self, key):
    return self.IsKey(key)

#
# define iterator for THashSet
#

class IterHashSet:
    def __init__(self, hash):
        self.hash = hash
        self.vec = None
        self.count = -1

    def __iter__(self):
        return self

    def next(self):
        if not self.vec:
            self.vec = TIntV()
            self.hash.GetKeyV(self.vec)
        if self.count + 1 < self.vec.Len():
            self.count += 1
            return self.vec[self.count]
        raise StopIteration

def iterhashset(self):
    return IterHashSet(self)


TIntSet.__iter__ = iterhashset
TIntSet.__contains__ = contains_hashset

%}
