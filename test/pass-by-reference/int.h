class TInt{
public:
  int Val;
public:
  TInt(): Val(0){}
  TInt(const int& _Val): Val(_Val){}
  operator int() const {return Val;}
  TInt& operator=(const TInt& Int){Val=Int.Val; return *this;}
  TInt& operator=(const int& Int){Val=Int; return *this;}
  bool operator==(const TInt& Int) const {return Val==Int.Val;}
  bool operator==(const int& Int) const {return Val==Int;}
  bool operator!=(const int& Int) const {return Val!=Int;}
  bool operator<(const TInt& Int) const {return Val<Int.Val;}
  bool operator<(const int& Int) const {return Val<Int;}
  int operator()() const {return Val;}
  TInt& operator+=(const int& Int){Val+=Int; return *this;}
  TInt& operator-=(const int& Int){Val-=Int; return *this;}
  TInt operator++(int){Val++; return *this;}
  TInt operator--(int){Val--; return *this;}
  static int increment_value(TInt& ValX) {
    ValX += 1;
    return 0;
  }
};