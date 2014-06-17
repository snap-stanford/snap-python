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
        self.iter = None
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if not self.iter or not self.vec:
            self.vec = TIntV()
            self.hash.GetKeyV(self.vec)
            self.count = 0

        if self.count >= self.vec.Len():
            raise StopIteration

        self.iter = self.vec.GetVal(self.count)
        self.count += 1
     
        return self.iter

def iterhashset(self):
    return IterHashSet(self)


TIntSet.__iter__ = iterhashset
TIntSet.__contains__ = contains_hashset

%}
