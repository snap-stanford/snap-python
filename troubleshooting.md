# bug: snap_wrap.cxx:178:11: fatal error: 'Python.h' file not found: include <Python.h>.
This bug occurs when the system has difficulty finding the Python.h file that Python uses. It can be fixed with the below solutions.

MacOS Solution:
The first thing one should do to resolve this bug is check if they have a Python.h file and to check where it is. This can be done with the following script 'find -L /usr -name "Python.h" -print' 

A lot of times this error can occur due to multiple versions of Python being installed on a given system and therefore multiple Python.h files. To resolve this, on MacOS, one option is to get rid of the excess versions of Python, leaving only the system version of Python. If you would like to keep all of your versions of Python, you can simply change the include directory (add '-I/usr/<insert where your Python.h file is>') in the Makefile (in the swig subdirectory) to the directory of the Python.h file found above. 

Linux Solution:
Check that python-dev is installed: if not use 'sudo apt-get install python-dev' If this does not solve the problem, try parts of the above solution.

Windows Solution:
Add the directory of your Python headers to the VC++ Directories in Visual Studio's settings. This can be found in Project -> Properties -> VC++ Directories

# Fatal Python error: PyThreadState_Get: no current thread
MacOS Solution:
This bug is caused by multiple versions of Python being installed. It can thus be solved by the latter part of the above solution.

# error: self assert when running tests
You need to install gnuplot and/or graphviz

# error installing graphviz on MacOS
Use macports: 'port install graphviz' *requires installing macports


