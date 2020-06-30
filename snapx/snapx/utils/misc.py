"""PORTED FROM NETWORKX

Miscellaneous Helpers for NetworkX.
These are not imported into the base networkx namespace but
can be accessed, for example, as
>>> import networkx
>>> networkx.utils.is_list_of_ints([1, 2, 3])
True
>>> networkx.utils.is_list_of_ints([1, 2, "spam"])
False
"""

from itertools import tee

# Recipe from the itertools documentation.
def pairwise(iterable, cyclic=False):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    first = next(b, None)
    if cyclic is True:
        return zip(a, chain(b, (first,)))
    return zip(a, b)
