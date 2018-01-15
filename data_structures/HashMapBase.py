from MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):
    """Abstract base class for map using hash table with MAD compression"""

    def __init__(self, cap = 11, prime = 109345121):
        self._n = 0
        self._prime = prime
        self._table = [None] * cap
        self._scale = randrange(1, prime - 1)
        self._shift = randrange(prime)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) //2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, cap):
        old_items = list(self.items())
        self._table = [None] * cap
        self._n = 0
        for (k, v) in old_items:
            self[k] = v

