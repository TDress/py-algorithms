from lib import assertion
import math

# given a positive integer, get the next largest and next smallest integers
# that have the same number of bits set in their binary representations.

def getNextVal(num, val, start=0, end=31):
    pos = 2 ** start
    for _ in range(start, end):
        if ((val == 1 and pos & num)
                    or (val == 0 and not pos & num)):
            return pos
        pos <<= 1

    return None

def getLastVal(num, val, start=31, end=0):
    pos = 2 ** start
    for _ in range(start, end, -1):
        if ((val == 1 and pos & num) 
                    or (val == 0 and not pos & num)):
            return pos
        pos >>= 1

    return None


def getNextSmallest(num):
    LSB = getNextVal(num, 1)
    if LSB is None:
        return False

    nontrailing_set = LSB
    if nontrailing_set == 1:
        while nontrailing_set and (num & ((nontrailing_set >> 1) or 1)):
            nontrailing_set = getNextVal(num, 1, int(math.log2(nontrailing_set)) + 1)
    if nontrailing_set is None:
        return False

    answer = (num ^ nontrailing_set) | (nontrailing_set >> 1)
    if LSB != nontrailing_set:
        next_unset = getLastVal(num, 0, int(math.log2(nontrailing_set >> 1)) - 1, int(math.log2(LSB)))
        if next_unset:
            answer ^= LSB
            answer |= (next_unset)

    return answer



def getNextBiggest(num):
    LSB = getNextVal(num, 1)
    if LSB is None:
        return False

    nontrailing_unset = getNextVal(num, 0, int(math.log2(LSB)) + 1)
    if nontrailing_unset is None:
        return False

    return (num | nontrailing_unset) ^ (nontrailing_unset >> 1)

def getNext(num):
    if num <= 0:
        raise ValueError('Argument must be a positive integer')
    return (getNextBiggest(num), getNextSmallest(num))

def main():
    n1 = 128
    n2 = 129
    n3 = 3
    n4 = 9

    assertion.equals((256, 64), getNext(n1))
    assertion.equals((130, 96), getNext(n2))
    assertion.equals((5, False), getNext(n3))
    assertion.equals((10, 6), getNext(n4))

if __name__ == '__main__':
    main()
