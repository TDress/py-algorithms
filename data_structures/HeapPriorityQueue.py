from .PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """A min oriented priority queue implemented with a heap"""

    def _parent(self, index): 
        """returns an index only; does not check for out of bounds error"""
        return (index - 1) // 2

    def _left_child(self, index): 
        """returns an index only; does not check for out of bounds error"""
        return index * 2 + 1

    def _right_child(self, index): 
        """returns an index only; does not check for out of bounds error"""
        return index * 2 + 2 

    def _has_left(self, j):
        return self._left_child(j) < len(self._data)

    def _has_right(self, j):
        return self._right_child(j) < len(self._data)

    def _swap(self, i, j): 
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap_bubble(self, index):
        j = index
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap_bubble(parent)

    def _downheap_bubble(self, index):
        if self._has_left(index):
            left = self._left_child(index)
            min_child = left
            if self._has_right(index):
                right = self._right_child(index)
                if self._data[right] < self._data[left]:
                    min_child = right

            if self._data[index] > self._data[min_child]:
                self._swap(index, min_child)
                self._downheap_bubble(min_child)

    def __init__(self, data = ()):
        """Create a new priority queue

        By default, queue will be empty.  If data is given, it should be as an iterable 
        sequence of (key, value) tuples specifying the initial contents.
        """
        self._data = [self._Item(key, value) for key, value in data]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        """Organize list into a heap.
        
        down bubble from every position (starting from bottom)
        """
        start = self._parent(len(self._data) - 1)
        for i in range(start, -1, -1):
            self._downheap_bubble(i)

    def __len__(self):
        return len(self._data)

    def add_item(self, key, value): 
        self._data.append(self._Item(key, value))
        self._upheap_bubble(len(self._data) - 1)

    def min(self):
        if self.is_empty(): 
            raise self.Empty('priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self): 
        if self.is_empty(): 
            raise self.Empty('priority queue is empty')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap_bubble(0)
        return item._key, item._value
