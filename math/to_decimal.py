from lib import assertion

"""
write a function that takes a number and the base of that number (between 2 and 10),
and returns the decimal value of the number.
Then write a function that takes as input a decimal number and a base and 
converts that decimal number to a number in the given base (up to base 10).

future: try modifying the second function so that you can convert from decimal
to any base up to 16

"""

def to_decimal(n, base):
    result = 0
    multiplier = 1

    while n > 0:
        result += (n % 10) * multiplier
        multiplier *= base
        n //= 10

    return result


def from_decimal(n, base):
    """given a decimal number, return the same number 
    represented in a different base
    """
    result = 0
    multiplier = 1

    while n > 0:
        result += (n % base) * multiplier
        multiplier *= 10
        n //= base

    return result



def main():
    print('testing to_decimal function...')
    assertion.equals(73, to_decimal(111, 8))
    assertion.equals(7, to_decimal(111, 2))
    assertion.equals(13, to_decimal(111, 3))

    print('testing from_decimal function...')
    assertion.equals(1011, from_decimal(11, 2))
    assertion.equals(111, from_decimal(73, 8))
    assertion.equals(111, from_decimal(13, 3))


if __name__ == '__main__':
    main()
        
