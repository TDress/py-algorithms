from lib import assertion

class LinkedQueue:
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
        self._tail = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def front(self): 
        if self._is_empty(): 
            raise self.Empty('The queue is empty.')
        return self._head._element

    def dequeue(self): 
        if self._is_empty(): 
            raise self.Empty('The queue is empty.')
        answer = self._head._element
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head._next
        self._size -= 1
        return answer

    def enqueue(self, element):
        node = self._Node(None, element)
        if self._is_empty(): 
            self._head = node
        else:
            self._tail._next = node
        self._tail = node

        self._size += 1



class LinkedNode:
    def __init__(self, element, next=None):
        self._elem = element
        self._next = next


class LinkedListTail:
    def __init__(self):
        self._ref = None

def enqueue(tail, elem):
    new = LinkedNode(elem)
    if tail._ref is None:
        new._next = new
        tail._ref = new
    else:
        new._next = tail._ref._next
        tail._ref._next = new
        tail._ref = new

def dequeue(tail):
    if tail._ref is None:
        raise ValueError('The Linked List is empty')
    answer = tail._ref._next._elem
    if tail._ref._next is tail._ref:
        tail._ref = None
    else:
        tail._ref._next = tail._ref._next._next
     
    return answer







def main():
    tail = LinkedListTail()
    enqueue(tail, 5)
    enqueue(tail, 4)
    enqueue(tail, 3)

    assertion.equals(5, tail._ref._next._elem)
    assertion.equals(4, tail._ref._next._next._elem)
    assertion.equals(3, tail._ref._elem)

    assertion.equals(dequeue(tail), 5)
    assertion.equals(4, tail._ref._next._elem)

    #q = LinkedQueue()
    #q.enqueue(1)
    #assertion.equals(1, q.front())
    #assertion.equals(False, q._is_empty())
    ## [1, None, None, None, None]
    #for i in range(2, 6):
    #    q.enqueue(i)
    #assertion.equals(1, q.front())
    #assertion.equals(5, q._size)
    ## [1, 2, 3, 4, 5]
    #for i in range(3):
    #    q.dequeue()
    #assertion.equals(2, q._size)
    #assertion.equals(4, q.dequeue())
    #assertion.equals(1, q._size)
    #assertion.equals(5, q.dequeue())
    #assertion.equals(0, q._size)
    ## [None, None, None, None, None]
    

if __name__ == '__main__':
    main()
