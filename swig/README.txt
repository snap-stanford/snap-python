========================================================================
  Snap.py - SNAP for Python
  http://snap.stanford.edu
========================================================================

About Snap.py

Snap.py is a Python interface for SNAP (Stanford Network Analysis Platform).
SNAP is a general purpose, high performance system for analysis and
manipulation of large networks. SNAP is written in C++ and optimized
for maximum performance and compact graph representation. It easily scales
to massive networks with hundreds of millions of nodes, and billions of edges.
Snap.py provides performance benefits of SNAP, combined with flexibility
of Python. Most of the SNAP functionality is available via Snap.py in Python.

========================================================================

Prerequisites

Packages for Mac OS X, Linux (as CentOS) and Windows 64-bit are available
at http://snap.stanford.edu. Download the package for your operating system.

Snap.py requires that 64-bit Python 2.7.x is installed on your machine.
Supported versions of Python are: system version, Anaconda and Homebrew
on Mac OS X, system version on Linux, and packages from python.org on
Windows 64-bit. Make sure that you are using 64-bit Python 2.7.x packages.

On Windows, Snap.py requires a 64-bit operating system version. Visual
C++ Redistributable for Visual Studio 2012 must be installed on the system.

To install Snap.py, download and unpack the package for your platform
and run setup.py.

Snap.py is largely self-contained and requires external packages only for
drawing and visualization. The following packages need to be installed
on the system to support drawing and visualization in Snap.py:
  - Gnuplot for plotting structural properties of networks, and
  - Graphviz for drawing and visualizing small graphs.

Set the system PATH variable, so that Gnuplot and Graphviz are available,
or put the executables in the working directory.

========================================================================

Installation

Installation of Snap.py on Mac OS X

On Mac OS X (supported releases are 10.7.5 or later), use the following
commands:
  tar zxvf snap-*-macosx10.7.5-x64-py2.7.tar.gz
  cd snap-*-macosx10.7.5-x64-py2.7
  sudo python setup.py install
If you use Anaconda and Homebrew Python, then 'sudo' in the last command
line is not required.

Installation of Snap.py on Linux

On Linux, use the following commands:
  tar zxvf snap-*-centos6.2-x64-py2.6.tar.gz
  cd snap-*-centos6.2-x64-py2.6
  sudo python setup.py install

Installation of Snap.py on Windows 64-bit

On Windows, verify that your operating system is 64-bit and that Visual
C++ Redistributable for Visual Studio 2012 is installed, then unzip the
Snap.py package and install it with the following command in the
Command Prompt:
  cd snap-1.0-2.2-Win-x64-py2.7
  python setup.py install

Local Install of Snap.py

If you want to use Snap.py in a local directory without installing it
system-wide, then download the corresponding Snap.py package for your
system, unpack, and copy files snap.py and _snap.so (or _snap.pyd) to
your working directory.

========================================================================

Documentation and Support

Additional information is available at http://snap.stanford.edu.

