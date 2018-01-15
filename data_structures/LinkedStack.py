from lib import assertion

class LinkedStack:
    class Empty(Exception): 
        """Items cannot be removed because the Deque is empty"""
        pass
    class _Node:
        __slots__ = '_next', '_element'
        def __init__(self, next, element):
            self._next = next
            self._element = element

    def __init__(self):
        self._head = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def top(self):
        if self._is_empty():
            raise self.Empty('The stack is empty')
        return self._head._element

    def pop(self):
        if self._is_empty():
            raise self.Empty('The stack is empty')
        answer = self._head._element
        self._head = self._head._next

        self._size -= 1
        return answer

    def push(self, element):
        node = self._Node(self._head, element)    
        self._head = node
        self._size += 1


def main():
    s = LinkedStack()
    s.push(5)
    s.push(4)
    assertion.equals(4, s.top())
    assertion.equals(4, s.pop())
    assertion.equals(1, s._size)

    for i in range(4, 0, -1):
        s.push(i)
    assertion.equals(1, s.top())
    assertion.equals(1, s.pop())
    assertion.equals(2, s.pop())

if __name__ == '__main__':
    main()
