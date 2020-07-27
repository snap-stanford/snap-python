To generating class function extensions for graphs in Python, the following script was run: 
python genPyClassFn.py classFn.txt > out.txt

The input file classFn.txt contains the names of the class functions.
The output "out.txt" was appended to pylayer.i as a %pythoncode% code block. 

Custom edits were made for the following class functions: 

    def ConvertGraph_classFn(self, *args, **kwargs):
        return ConvertGraph(args[0], self, *(args[1:]), **kwargs)
    PUNGraph.ConvertGraph = ConvertGraph_classFn
    PNGraph.ConvertGraph = ConvertGraph_classFn
    PNEANet.ConvertGraph = ConvertGraph_classFn

    def ConvertSubGraph_classFn(self, *args, **kwargs):
        return ConvertSubGraph(args[0], self, *args[1:], **kwargs)
    PUNGraph.ConvertSubGraph = ConvertSubGraph_classFn
    PNGraph.ConvertSubGraph = ConvertSubGraph_classFn
    PNEANet.ConvertSubGraph = ConvertSubGraph_classFn

    def ConvertESubGraph_classFn(self, *args, **kwargs):
        return ConvertESubGraph(args[0], self, *args[1:], **kwargs)
    PUNGraph.ConvertESubGraph = ConvertESubGraph_classFn
    PNGraph.ConvertESubGraph = ConvertESubGraph_classFn
    PNEANet.ConvertESubGraph = ConvertESubGraph_classFn