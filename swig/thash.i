%pythoncode %{

#
# define __getitem__ for [] addressing
#
def getitem_hash(self, i):
    return self.GetDat(i)

def setitem_hash(self, key, value):
    self.AddDat(key, value)

def delitem_hash(self, key):
    self.DelKey(key)

def len_hash(self):
    return self.Len()

#
# define iterator for THash
#

class IterHash:
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

def iterhash(self):
    return IterHash(self)

TIntH.__getitem__ = getitem_hash
TIntH.__setitem__ = setitem_hash
TIntH.__delitem__ = delitem_hash
TIntH.__len__ = len_hash
TIntH.__iter__ = iterhash
TIntIntH.__getitem__ = getitem_hash
TIntIntH.__setitem__ = setitem_hash
TIntIntH.__delitem__ = delitem_hash
TIntIntH.__len__ = len_hash
TIntIntH.__iter__ = iterhash
TIntFltH.__getitem__ = getitem_hash
TIntFltH.__setitem__ = setitem_hash
TIntFltH.__delitem__ = delitem_hash
TIntFltH.__len__ = len_hash
TIntFltH.__iter__ = iterhash
TIntStrH.__getitem__ = getitem_hash
TIntStrH.__setitem__ = setitem_hash
TIntStrH.__delitem__ = delitem_hash
TIntStrH.__len__ = len_hash
TIntStrH.__iter__ = iterhash
TIntPrFltH.__getitem__ = getitem_hash
TIntPrFltH.__setitem__ = setitem_hash
TIntPrFltH.__delitem__ = delitem_hash
TIntPrFltH.__len__ = len_hash
TIntPrFltH.__iter__ = iterhash
%}


#if SNAP_ALL
%pythoncode %{
TUInt64H.__getitem__ = getitem_hash
TUInt64H.__setitem__ = setitem_hash
TUInt64H.__iter__ = iterhash
TUInt64H.__delitem__ = delitem_hash
TUInt64H.__len__ = len_hash
TIntBoolH.__getitem__ = getitem_hash
TIntBoolH.__setitem__ = setitem_hash
TIntBoolH.__iter__ = iterhash
TIntBoolH.__delitem__ = delitem_hash
TIntBoolH.__len__ = len_hash
TIntUInt64H.__getitem__ = getitem_hash
TIntUInt64H.__setitem__ = setitem_hash
TIntUInt64H.__iter__ = iterhash
TIntUInt64H.__delitem__ = delitem_hash
TIntUInt64H.__len__ = len_hash
TIntIntVH.__getitem__ = getitem_hash
TIntIntVH.__setitem__ = setitem_hash
TIntIntVH.__iter__ = iterhash
TIntIntVH.__delitem__ = delitem_hash
TIntIntVH.__len__ = len_hash
TIntIntHH.__getitem__ = getitem_hash
TIntIntHH.__setitem__ = setitem_hash
TIntIntHH.__iter__ = iterhash
TIntIntHH.__delitem__ = delitem_hash
TIntIntHH.__len__ = len_hash
TIntFltPrH.__getitem__ = getitem_hash
TIntFltPrH.__setitem__ = setitem_hash
TIntFltPrH.__iter__ = iterhash
TIntFltPrH.__delitem__ = delitem_hash
TIntFltPrH.__len__ = len_hash
TIntFltTrH.__getitem__ = getitem_hash
TIntFltTrH.__setitem__ = setitem_hash
TIntFltTrH.__iter__ = iterhash
TIntFltTrH.__delitem__ = delitem_hash
TIntFltTrH.__len__ = len_hash
TIntFltVH.__getitem__ = getitem_hash
TIntFltVH.__setitem__ = setitem_hash
TIntFltVH.__iter__ = iterhash
TIntFltVH.__delitem__ = delitem_hash
TIntFltVH.__len__ = len_hash
TIntStrVH.__getitem__ = getitem_hash
TIntStrVH.__setitem__ = setitem_hash
TIntStrVH.__iter__ = iterhash
TIntStrVH.__delitem__ = delitem_hash
TIntStrVH.__len__ = len_hash
TIntIntPrH.__getitem__ = getitem_hash
TIntIntPrH.__setitem__ = setitem_hash
TIntIntPrH.__iter__ = iterhash
TIntIntPrH.__delitem__ = delitem_hash
TIntIntPrH.__len__ = len_hash
TIntIntPrVH.__getitem__ = getitem_hash
TIntIntPrVH.__setitem__ = setitem_hash
TIntIntPrVH.__iter__ = iterhash
TIntIntPrVH.__delitem__ = delitem_hash
TIntIntPrVH.__len__ = len_hash
TUInt64StrVH.__getitem__ = getitem_hash
TUInt64StrVH.__setitem__ = setitem_hash
TUInt64StrVH.__iter__ = iterhash
TUInt64StrVH.__delitem__ = delitem_hash
TUInt64StrVH.__len__ = len_hash
TIntPrIntH.__getitem__ = getitem_hash
TIntPrIntH.__setitem__ = setitem_hash
TIntPrIntH.__iter__ = iterhash
TIntPrIntH.__delitem__ = delitem_hash
TIntPrIntH.__len__ = len_hash
TIntPrIntVH.__getitem__ = getitem_hash
TIntPrIntVH.__setitem__ = setitem_hash
TIntPrIntVH.__iter__ = iterhash
TIntPrIntVH.__delitem__ = delitem_hash
TIntPrIntVH.__len__ = len_hash
TIntPrIntPrVH.__getitem__ = getitem_hash
TIntPrIntPrVH.__setitem__ = setitem_hash
TIntPrIntPrVH.__iter__ = iterhash
TIntPrIntPrVH.__delitem__ = delitem_hash
TIntPrIntPrVH.__len__ = len_hash
TIntTrIntH.__getitem__ = getitem_hash
TIntTrIntH.__setitem__ = setitem_hash
TIntTrIntH.__iter__ = iterhash
TIntTrIntH.__delitem__ = delitem_hash
TIntTrIntH.__len__ = len_hash
TIntVIntH.__getitem__ = getitem_hash
TIntVIntH.__setitem__ = setitem_hash
TIntVIntH.__iter__ = iterhash
TIntVIntH.__delitem__ = delitem_hash
TIntVIntH.__len__ = len_hash
TUIntH.__getitem__ = getitem_hash
TUIntH.__setitem__ = setitem_hash
TUIntH.__iter__ = iterhash
TUIntH.__delitem__ = delitem_hash
TUIntH.__len__ = len_hash
TIntPrIntH.__getitem__ = getitem_hash
TIntPrIntH.__setitem__ = setitem_hash
TIntPrIntH.__iter__ = iterhash
TIntPrIntH.__delitem__ = delitem_hash
TIntPrIntH.__len__ = len_hash
TIntPrIntVH.__getitem__ = getitem_hash
TIntPrIntVH.__setitem__ = setitem_hash
TIntPrIntVH.__iter__ = iterhash
TIntPrIntVH.__delitem__ = delitem_hash
TIntPrIntVH.__len__ = len_hash
TIntTrFltH.__getitem__ = getitem_hash
TIntTrFltH.__setitem__ = setitem_hash
TIntTrFltH.__iter__ = iterhash
TIntTrFltH.__delitem__ = delitem_hash
TIntTrFltH.__len__ = len_hash
TIntPrStrH.__getitem__ = getitem_hash
TIntPrStrH.__setitem__ = setitem_hash
TIntPrStrH.__iter__ = iterhash
TIntPrStrH.__delitem__ = delitem_hash
TIntPrStrH.__len__ = len_hash
TIntPrStrVH.__getitem__ = getitem_hash
TIntPrStrVH.__setitem__ = setitem_hash
TIntPrStrVH.__iter__ = iterhash
TIntPrStrVH.__delitem__ = delitem_hash
TIntPrStrVH.__len__ = len_hash
TIntStrPrIntH.__getitem__ = getitem_hash
TIntStrPrIntH.__setitem__ = setitem_hash
TIntStrPrIntH.__iter__ = iterhash
TIntStrPrIntH.__delitem__ = delitem_hash
TIntStrPrIntH.__len__ = len_hash
TFltFltH.__getitem__ = getitem_hash
TFltFltH.__setitem__ = setitem_hash
TFltFltH.__iter__ = iterhash
TFltFltH.__delitem__ = delitem_hash
TFltFltH.__len__ = len_hash
TStrH.__getitem__ = getitem_hash
TStrH.__setitem__ = setitem_hash
TStrH.__iter__ = iterhash
TStrH.__delitem__ = delitem_hash
TStrH.__len__ = len_hash
TStrBoolH.__getitem__ = getitem_hash
TStrBoolH.__setitem__ = setitem_hash
TStrBoolH.__iter__ = iterhash
TStrBoolH.__delitem__ = delitem_hash
TStrBoolH.__len__ = len_hash
TStrIntH.__getitem__ = getitem_hash
TStrIntH.__setitem__ = setitem_hash
TStrIntH.__iter__ = iterhash
TStrIntH.__delitem__ = delitem_hash
TStrIntH.__len__ = len_hash
TStrIntPrH.__getitem__ = getitem_hash
TStrIntPrH.__setitem__ = setitem_hash
TStrIntPrH.__iter__ = iterhash
TStrIntPrH.__delitem__ = delitem_hash
TStrIntPrH.__len__ = len_hash
TStrIntVH.__getitem__ = getitem_hash
TStrIntVH.__setitem__ = setitem_hash
TStrIntVH.__iter__ = iterhash
TStrIntVH.__delitem__ = delitem_hash
TStrIntVH.__len__ = len_hash
TStrUInt64H.__getitem__ = getitem_hash
TStrUInt64H.__setitem__ = setitem_hash
TStrUInt64H.__iter__ = iterhash
TStrUInt64H.__delitem__ = delitem_hash
TStrUInt64H.__len__ = len_hash
TStrUInt64VH.__getitem__ = getitem_hash
TStrUInt64VH.__setitem__ = setitem_hash
TStrUInt64VH.__iter__ = iterhash
TStrUInt64VH.__delitem__ = delitem_hash
TStrUInt64VH.__len__ = len_hash
TStrIntPrVH.__getitem__ = getitem_hash
TStrIntPrVH.__setitem__ = setitem_hash
TStrIntPrVH.__iter__ = iterhash
TStrIntPrVH.__delitem__ = delitem_hash
TStrIntPrVH.__len__ = len_hash
TStrFltH.__getitem__ = getitem_hash
TStrFltH.__setitem__ = setitem_hash
TStrFltH.__iter__ = iterhash
TStrFltH.__delitem__ = delitem_hash
TStrFltH.__len__ = len_hash
TStrFltVH.__getitem__ = getitem_hash
TStrFltVH.__setitem__ = setitem_hash
TStrFltVH.__iter__ = iterhash
TStrFltVH.__delitem__ = delitem_hash
TStrFltVH.__len__ = len_hash
TStrStrH.__getitem__ = getitem_hash
TStrStrH.__setitem__ = setitem_hash
TStrStrH.__iter__ = iterhash
TStrStrH.__delitem__ = delitem_hash
TStrStrH.__len__ = len_hash
TStrStrPrH.__getitem__ = getitem_hash
TStrStrPrH.__setitem__ = setitem_hash
TStrStrPrH.__iter__ = iterhash
TStrStrPrH.__delitem__ = delitem_hash
TStrStrPrH.__len__ = len_hash
TStrStrVH.__getitem__ = getitem_hash
TStrStrVH.__setitem__ = setitem_hash
TStrStrVH.__iter__ = iterhash
TStrStrVH.__delitem__ = delitem_hash
TStrStrVH.__len__ = len_hash
TStrStrPrVH.__getitem__ = getitem_hash
TStrStrPrVH.__setitem__ = setitem_hash
TStrStrPrVH.__iter__ = iterhash
TStrStrPrVH.__delitem__ = delitem_hash
TStrStrPrVH.__len__ = len_hash
TStrStrKdVH.__getitem__ = getitem_hash
TStrStrKdVH.__setitem__ = setitem_hash
TStrStrKdVH.__iter__ = iterhash
TStrStrKdVH.__delitem__ = delitem_hash
TStrStrKdVH.__len__ = len_hash
TStrIntFltPrH.__getitem__ = getitem_hash
TStrIntFltPrH.__setitem__ = setitem_hash
TStrIntFltPrH.__iter__ = iterhash
TStrIntFltPrH.__delitem__ = delitem_hash
TStrIntFltPrH.__len__ = len_hash
TStrStrIntPrVH.__getitem__ = getitem_hash
TStrStrIntPrVH.__setitem__ = setitem_hash
TStrStrIntPrVH.__iter__ = iterhash
TStrStrIntPrVH.__delitem__ = delitem_hash
TStrStrIntPrVH.__len__ = len_hash
TStrStrIntKdVH.__getitem__ = getitem_hash
TStrStrIntKdVH.__setitem__ = setitem_hash
TStrStrIntKdVH.__iter__ = iterhash
TStrStrIntKdVH.__delitem__ = delitem_hash
TStrStrIntKdVH.__len__ = len_hash
TStrPrBoolH.__getitem__ = getitem_hash
TStrPrBoolH.__setitem__ = setitem_hash
TStrPrBoolH.__iter__ = iterhash
TStrPrBoolH.__delitem__ = delitem_hash
TStrPrBoolH.__len__ = len_hash
TStrPrIntH.__getitem__ = getitem_hash
TStrPrIntH.__setitem__ = setitem_hash
TStrPrIntH.__iter__ = iterhash
TStrPrIntH.__delitem__ = delitem_hash
TStrPrIntH.__len__ = len_hash
TStrPrFltH.__getitem__ = getitem_hash
TStrPrFltH.__setitem__ = setitem_hash
TStrPrFltH.__iter__ = iterhash
TStrPrFltH.__delitem__ = delitem_hash
TStrPrFltH.__len__ = len_hash
TStrPrStrH.__getitem__ = getitem_hash
TStrPrStrH.__setitem__ = setitem_hash
TStrPrStrH.__iter__ = iterhash
TStrPrStrH.__delitem__ = delitem_hash
TStrPrStrH.__len__ = len_hash
TStrPrStrVH.__getitem__ = getitem_hash
TStrPrStrVH.__setitem__ = setitem_hash
TStrPrStrVH.__iter__ = iterhash
TStrPrStrVH.__delitem__ = delitem_hash
TStrPrStrVH.__len__ = len_hash
TStrTrIntH.__getitem__ = getitem_hash
TStrTrIntH.__setitem__ = setitem_hash
TStrTrIntH.__iter__ = iterhash
TStrTrIntH.__delitem__ = delitem_hash
TStrTrIntH.__len__ = len_hash
TStrIntPrIntH.__getitem__ = getitem_hash
TStrIntPrIntH.__setitem__ = setitem_hash
TStrIntPrIntH.__iter__ = iterhash
TStrIntPrIntH.__delitem__ = delitem_hash
TStrIntPrIntH.__len__ = len_hash
TStrVH.__getitem__ = getitem_hash
TStrVH.__setitem__ = setitem_hash
TStrVH.__iter__ = iterhash
TStrVH.__delitem__ = delitem_hash
TStrVH.__len__ = len_hash
TStrVIntVH.__getitem__ = getitem_hash
TStrVIntVH.__setitem__ = setitem_hash
TStrVIntVH.__iter__ = iterhash
TStrVIntVH.__delitem__ = delitem_hash
TStrVIntVH.__len__ = len_hash
TStrVStrH.__getitem__ = getitem_hash
TStrVStrH.__setitem__ = setitem_hash
TStrVStrH.__iter__ = iterhash
TStrVStrH.__delitem__ = delitem_hash
TStrVStrH.__len__ = len_hash
TStrVStrVH.__getitem__ = getitem_hash
TStrVStrVH.__setitem__ = setitem_hash
TStrVStrVH.__iter__ = iterhash
TStrVStrVH.__delitem__ = delitem_hash
TStrVStrVH.__len__ = len_hash
%}
#endif

