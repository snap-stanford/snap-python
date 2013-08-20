%pythoncode %{

#
# define iterator for THash
#

class Iter:
    def __init__(self, hash):
        self.hash = hash
        self.iter = None

    def __iter__(self):
        return self

    def next(self):
        if not self.iter:
            self.iter = self.hash.BegI()
            if not self.iter:
                raise StopIteration
            return self.iter

        if self.iter.IsEnd():
            raise StopIteration

        self.iter.Next()

        if self.iter.IsEnd():
            raise StopIteration
     
        return self.iter

def iter(self):
    return Iter(self)

TIntH.__iter__ = iter

%}

