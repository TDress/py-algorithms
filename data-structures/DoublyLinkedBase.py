class _DoublyLinkedBase:
    """This non-public class provides a superclass for concrete

    classes that depend on a doubly linked list.  
    """
    class _Node:
        """A class for respresenting nodes in a doubly linked list."""
        def __init__(self, prev, next, element):
            self._prev = prev
            self._next = next
            self._element = element
    class Empty(Exception): 
        """Empty data structure"""
        pass
            
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(self._header, None, None)
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def _insert_between(self, node_prev, node_next, element):
        node = self._Node(node_prev, node_next, element)
        node_prev._next  = node
        node_next._prev = node
        self._size += 1
        
        return node

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        answer = node._element

        node._next = node._prev = node._element = None
        self._size -= 1
        return answer





