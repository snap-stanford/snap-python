namespace TSnap {

typedef TVec<TInt, int> TIntV;
typedef TVec<TIntV, int> TIntIntVV;

int StdDist(double Mean, double Dev) {
  int i;
  double x;

  x = -6.0;
  for (i = 0; i < 12; i++) {
    x += drand48();
  }

  x *= Dev;
  x += Mean;

  return int(x + 0.5);
}

#if 0
void GetDegrees(TIntV* Nodes, double Mean, double Dev) {
  int i;
  int d;
  int Len;
  printf("GetDegrees\n");
  printf("Nodes Len %d\n",Nodes->Len());

  Len = Nodes->Len();
  for (i = 0; i < Len; i++) {
    d = StdDist(Mean, Dev);
    printf("degree1 %d %d\n", i, d);
    (*Nodes)[i] = d;
  }

  for (i = 0; i < Len; i++) {
    printf("degree2 %d %d\n", i, Nodes->GetVal(i).Val);
  }
}
#endif

void GetDegrees(TIntV& Nodes, double Mean, double Dev) {
  int i;
  int d;
  int Len;
  printf("GetDegrees\n");
  printf("Nodes Len %d\n",Nodes.Len());

  // assign degree to each node
  Len = Nodes.Len();
  for (i = 0; i < Len; i++) {
    d = StdDist(Mean, Dev);
    printf("degree1 %d %d\n", i, d);
    Nodes[i] = d;
  }

  for (i = 0; i < Len; i++) {
    printf("degree2 %d %d\n", i, Nodes[i].Val);
  }
}

void AssignRndTask(const TIntV& Nodes, TIntIntVV& Tasks) {
  int i;
  int j;
  int n;
  int t;
  int NumNodes;
  int NumTasks;
  printf("AssignRndTask\n");
  printf("Nodes Len %d\n",Nodes.Len());
  printf("Tasks Len %d\n",Tasks.Len());

  NumNodes = Nodes.Len();
  NumTasks = Tasks.Len();

  // distribute stubs randomly to tasks
  for (i = 0; i < NumNodes; i++) {
    n = Nodes[i].Val;
    printf("degree3 %d %d\n", i, n);
    for (j = 0; j < n; j++) {
      t = (long) (drand48() * NumTasks);
      Tasks[t].Add(i);
    }
  }
}

}; // namespace TSnap

