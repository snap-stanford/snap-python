PlotSngVec
''''''''''

.. function:: PlotSngVec(Graph, FNmPref, DescStr)

Ranks the values of the leading left singular vector of the graph adjacency matrix plots the first SngVals on a log-log chart

Parameters:

- *Graph*: PNGraph
    A Snap.py directed graph

- *FNmPref*: TStr
    Filename string to to be added to output files
    PlotSngVec generates three output files

	* sngVecL.[FNmPref].tab: adjacency matrix entry rank data
	* sngVecL.[FNmPref].plt: gnuplot commands that generate the plot. Sets the *terminal* value to 'postscript eps'. Change the *terminal* entry to aqua and you will be able to directly generate in gnuplot: gnuplot sngVecL.*FNmPref*.plt
	* sngVecL.[FNmPref].eps: encapsulated postscript output (you can load this into drawing programs or MS Word, for instance)

- *DescStr*: TStr
    Will appear as a title on the plotted graphs, along the number of nodes and edges in the graph

Return value:

- None

For more info see: 
	
* `Adjacency matrix - Wikipedia <http://en.wikipedia.org/wiki/Adjacency_matrix>`_
* `Singular Value Descomposition - Wikipedia <http://en.wikipedia.org/wiki/Singular_value_decomposition>`_
* `SNAP C++ library reference <http://snap.stanford.edu/snap/doc/snapdev-ref/d3/d73/namespaceTSnap.html#afe884c79b5b1344ac628a9b5e2ba6e2b>`_


Calling the fiunciotn is straightfoward, all you need is a graph to operate on::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    PlotSngVec(Graph,"my_filename","my_chart_title")

This generates
* sngVecL.my_filename.tab
* sngVecL.my_filename.plt
* sngVecL.my_filename.eps

In this example the fisrt few lines of the .tab file contain something like::

	#
	# my_chart_title. G(100, 1000). Right signular vector (Sun Sep 29 10:06:15 2013)
	#
	# Rank	Component of right singular vector
	1	0.206801
	2	0.171068
	3	0.169928
	4	0.167472
	5	0.161439
	6	0.140474
	7	0.137822
	8	0.135348
	9	0.132904
	10	0.131604

The plt file looks like::

	#
	# my_chart_title. G(100, 1000). Right signular vector (Sun Sep 29 10:06:15 2013)
	#
	
	set title "my_chart_title. G(100, 1000). Right signular vector"
	set key bottom right
	set logscale xy 10
	set format x "10^{%L}"
	set mxtics 10
	set format y "10^{%L}"
	set mytics 10
	set grid
	set xlabel "Rank"
	set ylabel "Component of right singular vector"	
	set tics scale 2
	set terminal postscript eps 10 enhanced color
	set output 'sngVecL.my_filename.eps'
	plot 	"sngVecL.my_filename.tab" using 1:2 title "" with linespoints pt 6

For instance, to plot on aqua,  change the set terminal entry to::

	set terminal aqua

Refer to the gnuplot documentation for more info on tailoring output http://www.gnuplot.info/docs/tutorial.pdf

Here is an example output chart

.. image:: https://dl.dropboxusercontent.com/u/3706134/sngVecL.my_filename.png

Observations: 

* Apparent error: The chart title shows "right" singular vector as oppsed to "left"
* The C++ code seems to be set up to output both right and left vectors, but only generates the left
* Function documentation specifies that only the first SngVals values will be plotted. Its not clear (to me) that this is the case, nor where this value is set, if at all it is
* Its not clear (to me, encore...) how one sets the default output values (e.g., generate a png file or show directly in aqua vs eps) 