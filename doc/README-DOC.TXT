Undocumented Functions
Provided in C++, but not documented for Python
Mar 11, 2014

TUNGraph
- AddNode (const int &NId, const TIntV &NbrNIdV)
- AddNode (const int &NId, const TVecPool< TInt > &Pool, const int &NIdVId)
- GetNIdV (TIntV &NIdV)
- IsOk (const bool &ThrowExcept=true)
- operator =

TNGraph
- AddNode (const int &NId, const TIntV &InNIdV, const TIntV &OutNIdV)
- AddNode (const int &NId, const TVecPool< TInt > &Pool, const int &SrcVId, const int &DstVId)
- GetNIdV (TIntV &NIdV)
- IsOk (const bool &ThrowExcept=true)
- operator =

TNEANet
- GetNIdV (TIntV &NIdV)
- IsOk (const bool &ThrowExcept=true)

- AttrNameNI(const TInt& NId, TStrV& Names)
- AttrNameNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Names)
- AttrValueNI(const TInt& NId, TStrV& Values)
- AttrValueNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Values)
- IntAttrNameNI(const TInt& NId, TStrV& Names) 
- IntAttrNameNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Names)
- IntAttrValueNI(const TInt& NId, TIntV& Values)
- IntAttrValueNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TIntV& Values)
- StrAttrNameNI(const TInt& NId, TStrV& Names)
- StrAttrNameNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Names)
- StrAttrValueNI(const TInt& NId, TStrV& Values)
- StrAttrValueNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Values)
- FltAttrNameNI(const TInt& NId, TStrV& Names)
- FltAttrNameNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TStrV& Names)
- FltAttrValueNI(const TInt& NId, TFltV& Values)
- FltAttrValueNI(const TInt& NId, TStrIntPrH::TIter NodeHI, TFltV& Values)

- AttrNameEI(const TInt& EId, TStrV& Names)
- AttrNameEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Names)
- AttrValueEI(const TInt& EId, TStrV& Values)
- AttrValueEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Values)
- IntAttrNameEI(const TInt& EId, TStrV& Names)
- IntAttrNameEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Names)
- IntAttrValueEI(const TInt& EId, TIntV& Values)
- IntAttrValueEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TIntV& Values)
- StrAttrNameEI(const TInt& EId, TStrV& Names)
- StrAttrNameEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Names)
- StrAttrValueEI(const TInt& EId, TStrV& Values)
- StrAttrValueEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Values)
- FltAttrNameEI(const TInt& EId, TStrV& Names)
- FltAttrNameEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TStrV& Names)
- FltAttrValueEI(const TInt& EId, TFltV& Values)
- FltAttrValueEI(const TInt& EId, TStrIntPrH::TIter EdgeHI, TFltV& Values)

- NodeAttrIsDeleted(const int& NId, const TStrIntPrH::TIter& NodeHI)
- NodeAttrIsIntDeleted(const int& NId, const TStrIntPrH::TIter& NodeHI)
- NodeAttrIsStrDeleted(const int& NId, const TStrIntPrH::TIter& NodeHI)
- NodeAttrIsFltDeleted(const int& NId, const TStrIntPrH::TIter& NodeHI)

- EdgeAttrIsDeleted(const int& EId, const TStrIntPrH::TIter& EdgeHI)
- EdgeAttrIsIntDeleted(const int& EId, const TStrIntPrH::TIter& EdgeHI)
- EdgeAttrIsStrDeleted(const int& EId, const TStrIntPrH::TIter& EdgeHI)
- EdgeAttrIsFltDeleted(const int& EId, const TStrIntPrH::TIter& EdgeHI)
- GetNodeAttrValue(const int& NId, const TStrIntPrH::TIter& NodeHI)
- GetEdgeAttrValue(const int& EId, const TStrIntPrH::TIter& EdgeHI)

