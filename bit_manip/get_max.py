from lib import assertion

# get the max if two ints without using any comparison operators or if/else
# NOTE THAT THIS DOES NOT ACCOUNT FOR OVERFLOW!
def getMax(a, b):
    """Get maximum of 2 integers

    :param int a: 32 bit integer
    :param int b: 32 bit integer
    :return int: maximum of integers a and b
    """
    msb = 1 << 31
    # i is 1 if a is bigger or equal, 0 otherwise
    i = 1 & ~((a-b) & msb)
    bmask = i - 1
    amask = ~(i - 1)
    return (bmask & b) | (amask & a)


def main():
    assert 12345 == getMax(12345, 12344)
    assert 1 == getMax(1, -1)
    assert 9 == getMax(9, 3)
    assert 14 == getMax(14, 13)

if __name__ == '__main__':
    main()
