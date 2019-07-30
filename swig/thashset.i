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
        self.iter = None

    def __iter__(self):
        return self

    def next(self):
        if self.hash.Len() == 0:
            raise StopIteration
        if not self.iter:
            self.iter = self.hash.BegI()
            if not self.iter:
                raise StopIteration
            if self.iter:
                return self.iter.GetKey()
            return self.iter

        if self.iter.IsEnd():
            raise StopIteration

        self.iter.Next()

        if self.iter.IsEnd():
            raise StopIteration

        if self.iter:
            return self.iter.GetKey()
        return self.iter

def iterhashset(self):
    return IterHashSet(self)


TIntSet.__iter__ = iterhashset
TIntSet.__contains__ = contains_hashset

%}
