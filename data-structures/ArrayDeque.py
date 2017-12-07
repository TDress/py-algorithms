from lib import assertion

class ArrayDeque:
    class Empty(Exception): 
        """Items cannot be removed because the Deque is empty"""
        pass

    def __init__(self, capacity): 
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def __len__(self): 
        return self._size

    def _is_empty(self): 
        return self._size == 0

    def front(self): 
        if self._is_empty(): 
            raise Empty('The deque is empty.')
        return self._data[self._front]

    def insert_front(self, element): 
        if self._size == len(self._data): 
            self._resize(len(self._data) * 2)
        if self._size != 0:
            self._front = (self._front - 1) % len(self._data)

        self._data[self._front] = element
        self._size += 1

    def insert_back(self, element): 
        if self._size == len(self._data): 
            self._resize(len(self._data) * 2)

        self._data[(self._front + self._size) % len(self._data)] = element
        self._size += 1

    def pop_front(self): 
        if self._is_empty(): 
            raise Empty('The deque is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None

        self._front = self._front + 1 % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def pop_back(self): 
        if self._is_empty(): 
            raise Empty('The deque is empty.')
        back_index = (self._size + self._front - 1) % len(self._data)
        answer = self._data[back_index]
        self._data[back_index] = None

        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def _resize(self, new_capacity): 
        old_data = self._data
        self._data = [None] * new_capacity
        for i in range(self._size): 
            self._data[i] = old_data[(i + self._front) % len(old_data)]

        self._front = 0


def main():
    d = ArrayDeque(5)
    d.insert_front(1)
    assertion.equals(1, d.front())
    # [1, None, None, None, None]
    for i in range(2, 6):
        d.insert_back(i)
    assertion.equals(0, d._front)
    assertion.equals(5, d._size)
    # [1, 2, 3, 4, 5]
    for i in range(3):
        d.pop_front()
    assertion.equals(2, d._size)
    assertion.equals(3, d._front)
    assertion.equals(4, d.front())
    # [None, None, None, 4, 5]
    for i in range(6):
        d.insert_front(i)
    assertion.equals(10, len(d._data))
    assertion.equals(8, d._size)
    assertion.equals(5, d.front())
    assertion.equals(5, d.pop_back())

    d.insert_front(7)
    assertion.equals(6, d._front)
    assertion.equals(4, d.pop_back())
    assertion.equals(7, d._size)


if __name__ == '__main__':
    main()
