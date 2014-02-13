%pythoncode %{

#
# define __getitem__ for [] addressing
#
def getitem_hashset(self, i):
    return self.GetSetKey(i)

#
# define iterator for THashSet
#

class IterHashSet:
    def __init__(self, hash):
        self.hash = hash
        self.iter = None
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if not self.iter:
            if self.count >= self.hash.GetMxKeyIds():
                raise StopIteration
            while not self.hash.IsKeyId(self.count):
                self.count += 1
                if self.count >= self.hash.GetMxKeyIds():
                    raise StopIteration
            self.iter = self.hash.GetKey(self.count)
            self.count += 1
            return self.iter

        if self.count >= self.hash.GetMxKeyIds():
            raise StopIteration
        while not self.hash.IsKeyId(self.count):
            self.count += 1
            if self.count >= self.hash.GetMxKeyIds():
                raise StopIteration

        self.iter = self.hash.GetKey(self.count)
        self.count += 1
     
        return self.iter

def iterhashset(self):
    return IterHashSet(self)


TIntSet.__iter__ = iterhashset

%}