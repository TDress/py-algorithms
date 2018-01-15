from lib import assertion 

class ArrayStack:
    def __init__(self): 
        self._data = []

    def __len__(self): 
        return len(self._data)

    def is_empty(self): 
        return len(self._data) == 0

    def top(self): 
        if self.is_empty(): 
            raise ValueError('The stack has zero entries.')

        return self._data[-1]

    def pop(self): 
        if self.is_empty(): 
            raise ValueError('The stack has zero entries.')

        return self._data.pop()

    def push(self, item): 
        self._data.append(item)






#  in cases where we could have a maximum size up front for the stack
# we could avoid the amortization by passing a maximum to the constructor and
# initializing the data member like self._data = [0] * max.  
# Then you would need a member to keep track of how long the list is.
# This would avoid the overhead of all of the function calls to append(),
# and the amortization of resizing.  both approaches run in linear time 
