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






