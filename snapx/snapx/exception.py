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

class SnapXTypeError(TypeError):
    """Exception for SNAP specific type errors"""

class SnapXKeyError(KeyError):
    """Exception for SNAP specific key errors"""
