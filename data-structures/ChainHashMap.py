from HashMapBase import HashMapBase
from UnsortedMapBase import UnsortedMapBase
from lib import assertion

class ChainHashMap(HashMapBase):
    """Hash map implemented with seperate chaining"""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedMapBase()
        bucket = self._table[j]
        old_len = len(bucket)
        bucket[k] = v
        if len(bucket) > old_len:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if not bucket is None:
                for key in bucket:
                    yield key



def main():
    map = ChainHashMap()
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
