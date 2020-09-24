"""PORTED FROM NETWORKX"""

__all__ = [
    "SnapXException",
    "SnapXError",
    "SnapXAlgorithmError",
    "SnapXUnfeasible",
    "SnapXNoPath",
    "NodeNotFound",
    "SnapXTypeError",
    "SnapXKeyError",
]


class SnapXException(Exception):
    """Base class for exceptions in SnapX."""


class SnapXError(SnapXException):
    """Exception for a serious error in SnapX"""


class SnapXAlgorithmError(SnapXException):
    """Exception for unexpected termination of algorithms."""


class SnapXUnfeasible(SnapXAlgorithmError):
    """Exception raised by algorithms trying to solve a problem
    instance that has no feasible solution."""


class SnapXNoPath(SnapXUnfeasible):
    """Exception for algorithms that should return a path when running
    on graphs where such a path does not exist."""


class NodeNotFound(SnapXException):
    """Exception raised if requested node is not present in the graph"""


class SnapXTypeError(TypeError):
    """Exception for SNAP specific type errors"""


class SnapXKeyError(KeyError):
    """Exception for SNAP specific key errors"""
