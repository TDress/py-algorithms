from HashMapBase import HashMapBase
from lib import assertion

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing"""

    _AVAIL = object()

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If not found, success is false and index denotes first available slot.
        """
        walk = j
        first_avail = None
        while self._table[walk] is not None:
            if isinstance(self._table[walk], self._Item):
                if k == self._table[walk]._key:
                    return (True, walk)
            elif first_avail is None:
                first_avail = walk
            walk = (walk + 1) % len(self._table)

        return (False, first_avail or walk)

    def _bucket_getitem(self, j, k):
        is_found, index = self._find_slot(j, k)
        if not is_found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[index]._value

    def _bucket_setitem(self, j, k, v):
        is_found, index = self._find_slot(j, k)
        if is_found:
            self._table[index]._value = v
        else:
            self._table[index] = self._Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j, k):
        is_found, index = self._find_slot(j, k)
        if not is_found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[index] = self._AVAIL

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None and bucket is not self._AVAIL:
                yield bucket._key



def main():
    map = ProbeHashMap()
    map[3] = 'three'
    map[5] = 'five'
    assertion.equals('three', map[3])
    assertion.equals('five', map[5])

    for i in range(10, 100):
        map[i] = 'sweet', 'example'

    assertion.equals(92, len(map))

    map[(4,5)] = 100
    map[(1,2,3,4,5)] = 101
    assertion.equals(100, map[(4,5)])
    assertion.equals(101, map[(1,2,3,4,5)])

    del map[3]
    assertion.equals(93, len(map))

    test_key  = None
    for key in map:
        test_key = key
        break
    assertion.equals(False, test_key is None)


if __name__ == '__main__':
    main()

