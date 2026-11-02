"""Single Python entry point for all five exercises.

Import from the repository root, for example:
    from java6.search import findAll, resetCounters, getCounters

Each algorithm lives in its exercise folder, with one shared counter owner.
"""

from java6.detyra1.main import (
    bruteForce, shiftTable, horspool, horspool2, resetCounters, getCounters,
)
from java6.detyra2.main import findAll
from java6.detyra3.main import highlight
from java6.detyra4.main import goodSuffixTable
from java6.detyra5.main import boyerMoore

# Python's equivalent of the assignment's module.exports interface.
__all__ = [
    "bruteForce", "shiftTable", "horspool", "horspool2",
    "findAll", "highlight", "goodSuffixTable", "boyerMoore",
    "resetCounters", "getCounters",
]
