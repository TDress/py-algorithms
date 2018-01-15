from MapBase import MapBase

class UnsortedMapBase(MapBase):
    """Map implementation using an unordered list"""

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return

        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k, or raise a KeyError if not found."""
        for i in range(len(self)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key
