from lib import assertion

class CircularLinkedQueue:
    class Empty(Exception): 
        """Items cannot be removed because the Deque is empty"""
        pass
    class _Node:
        __slots__ = '_next', '_element'
        def __init__(self, next, element):
            self._next = next
            self._element = element

    def __init__(self):
        self._tail = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _print_inner(self): 
        answer = ''
        if self._size > 2:
            current = self._tail._next._next
            for i in range(self._size - 2): 
                answer += '<{}>-->'.format(current._element)
                current = current._next

        return answer

    def __str__(self): 
        if self._is_empty(): 
            raise self.Empty('The queue is empty.')

        front = self.front()
        if self._size == 1:
            return '<{}>'.format(front)
        else:
            return '<{}>-->{}<{}>'.format(
                front, self._print_inner(), self._tail._element)

    def front(self): 
        if self._is_empty(): 
            raise self.Empty('The queue is empty.')

        head = self._tail._next
        return head._element

    def dequeue(self): 
        if self._is_empty(): 
            raise self.Empty('The queue is empty.')
        head = self._tail._next
        answer = head._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next

        self._size -= 1
        return answer

    def enqueue(self, element):
        node = self._Node(None, element)
        if self._is_empty(): 
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node

        self._tail = node
        self._size += 1

    def rotate(self):
        if self._size < 2:
            raise Empty('The queue must at least have two elements to rotate')
        self._tail = self._tail._next



def main():
    q = CircularLinkedQueue()
    q.enqueue(1)
    assertion.equals(1, q.front())
    assertion.equals(False, q._is_empty())
    # [1, None, None, None, None]
    q.enqueue(2)
    q.enqueue(3)
    assertion.equals(3, q._tail._element)
    assertion.equals(1, q._tail._next._element)
    for i in range(4, 6):
        q.enqueue(i)
    assertion.equals(1, q.front())
    assertion.equals(5, q._size)
    # [1, 2, 3, 4, 5]
    q.rotate()
    print(q)
    assertion.equals(2, q.front())
    q.rotate()
    assertion.equals(3, q.front())
    # [3, 4, 5, 1, 2]

    for i in range(3):
        q.dequeue()
    assertion.equals(2, q._size)
    q.rotate()
    assertion.equals(2, q.dequeue())
    assertion.equals(1, q._size)
    assertion.equals(1, q.dequeue())
    assertion.equals(0, q._size)
    # [None, None, None, None, None]
    

if __name__ == '__main__':
    main()

