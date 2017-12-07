from lib import assertion

class ArrayQueue:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self.size == 0

    def front(self):
        if self._size == 0:
            raise ValueError('The Queue is empty')
        return self._data[self._front]

    def enqueue(self, item):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        insert_index = (self._size + self._front) % len(self._data)
        self._data[insert_index] = item
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise ValueError('The Queue is empty')

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if(0 < self._size < len(self._data) // 4):
            self._resize(len(self._data) // 2)

        return answer

    def _resize(self, new_capacity): 
        old_data = self._data
        self._data = [None] * new_capacity
        for i in range(self._size): 
            self._data[i] = old_data[(i + self._front) % len(old_data)]

        self._front = 0




def main():
    q = ArrayQueue(5)
    q.enqueue(1)
    assertion.equals(1, q.front())
    assertion.equals(False, q.is_empty)
    # [1, None, None, None, None]
    for i in range(2, 6):
        q.enqueue(i)
    assertion.equals(0, q._front)
    assertion.equals(5, q._size)
    # [1, 2, 3, 4, 5]
    for i in range(5):
        q.dequeue()
    assertion.equals(0, q._size)
    assertion.equals(0, q._front)
    # [None, None, None, None, None]
    for i in range(6):
        q.enqueue(i)
    assertion.equals(10, len(q._data))
    assertion.equals(6, q._size)

    for i in range(2):
        q.dequeue()
    assertion.equals(2, q._front)
    assertion.equals(4, q._size)

    for i in range(3):
        q.dequeue()
    assertion.equals(5, len(q._data))
    assertion.equals(0, q._front)
    assertion.equals(1, q._size)

    assertion.equals(5, q.dequeue())


if __name__ == '__main__':
    main()
