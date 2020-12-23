import importlib
import os
import sys

import snap

snappath = os.path.dirname(snap.__file__)

# get the 'snap' module location as the first place to load from
sys.path.insert(0,snappath)

# reload 'snap' to keep 'snap' object paths, not 'snap.snap'
importlib.reload(snap)
sys.path.pop(0)

# set path for 'import snapx', add 'snap' path to the end
sys.path.append(snappath)

