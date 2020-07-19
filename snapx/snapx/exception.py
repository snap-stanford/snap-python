"""PORTED FROM NETWORKX"""

__all__ = [
    "SnapXException",
    "SnapXError",
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


class SnapXTypeError(TypeError):
    """Exception for SNAP specific type errors"""


class SnapXKeyError(KeyError):
    """Exception for SNAP specific key errors"""
