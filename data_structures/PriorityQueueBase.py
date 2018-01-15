
class PriorityQueueBase:
    """Abstract base class for a priority queue"""

    class Empty(Exception): 
        """Items cannot be removed because the priority queue is empty"""
        pass

    class _Item:
        """lightweight composite class for priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


