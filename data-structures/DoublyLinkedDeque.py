from lib import assertion
from DoublyLinkedBase import _DoublyLinkedBase

class DoublyLinkedDeque(_DoublyLinkedBase):
    def front(self):
        if self._is_empty():
            raise Empty('The deque is empty')
        return self._header._next._element
    
    def back(self):
        if self._is_empty():
            raise Empty('The deque is empty')
        return self._trailer._prev._element

    def insert_front(self, element):
        self._insert_between(self._header, self._header._next, element)

    def insert_back(self, element):
        self._insert_between(self._trailer._prev, self._trailer, element)

    def pop_front(self):
        if self._is_empty():
            raise Empty('The deque is empty')
        return self._delete_node(self._header._next)

    def pop_back(self):
        if self._is_empty():
            raise Empty('The deque is empty')
        return self._delete_node(self._trailer._prev)

def main(): 
    d = DoublyLinkedDeque()
    d.insert_front(1)
    d.insert_back(2)
    assertion.equals(1, d.pop_front())
    assertion.equals(2, d.front())
    assertion.equals(2, d.pop_back())
    d.insert_back(1)

    for i in range(2, 6):
        d.insert_back(i)
    assertion.equals(5, d._size)

    for i in range(3):
        d.pop_front()
    assertion.equals(2, d._size)
    assertion.equals(4, d.front())
    assertion.equals(5, d.back())

    for i in range(6):
        d.insert_front(i)
    assertion.equals(8, len(d))
    assertion.equals(5, d.front())
    assertion.equals(5, d.pop_back())

    d.insert_front(7)
    assertion.equals(4, d.pop_back())


if __name__ == '__main__':
    main()
