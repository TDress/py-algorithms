from lib import assertion 
import ctypes

class DArray:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._A = self._makearray()

    def __len__(self):
        return self._length

    def __getitem__(self, key):
        if type(key) != slice:
            true_key = key
            if key >= self._length:
                raise ValueError('Index out of range')
            if key < 0:
                abs_key = abs(key)
                if abs_key > self._length:
                    raise ValueError('Index out of range')
                true_key = self._length - abs_key
            return self._A[true_key]
        else:
            start, stop, step = 0, self._length, 1
            if key.start:
                if key.start < 0:
                    abs_start = abs(key.start)
                    if abs > self._length:
                        start = 0
                    else:
                        start = self._length - abs_start
                else:
                    if start >= self._length:
                        return DArray()

            if key.stop != None and key.stop != self._length:
                if key.stop < 0:
                    abs_stop = abs(keys.stop)
                    if abs_stop >= self._length:
                        return DArray()
                    else:
                        stop = self._length - abs_stop
                elif key.stop == 0:
                    return DArray()
                else:
                    if key.stop > self._length:

            if key.step == 0:
                raise ValueError('step argument of slice must be non-negative')
            elif key.step != None and key.step != step:
                step = key.step

            if start >= stop:
                return DArray()

            result = DArray()
            for i in range(start, stop)


    def _resize(self): 
        self._capacity *= 2
        new_A = self._makearray()
        for i in range(self._length): 
            new_A[i] = self._A[i]
        self._A = new_A

    def append(self, item): 
        if self._length + 1 > self._capacity:
            self._resize()

        self._A[self._length] = item
        self._length += 1

    def _makearray(self):
        return (self._capacity * ctypes.py_object)()


def main(): 
    a = DArray();
    a.append(5)

    assertion.equals(5, a[0])
    assertion.equals(1, a._capacity)
    assertion.equals(1, a._length)

    a.append(3)
    print(str(a._A))
    assertion.equals(2, a._capacity)
    assertion.equals(2, a._length)

    a.append(3)
    print(str(a._A))
    assertion.equals(4, a._capacity)
    assertion.equals(3, a._length)
    assertion.equals(True, a[1] == a[2])


if __name__ == '__main__': 
    main()
