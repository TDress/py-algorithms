from collections import MutableMapping

class MapBase(MutableMapping):
    """Base class for map ADT implementations."""

    class _Item:
        """Lightweight composite to store key-value pairs in the map"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            return self._key < other._key

