import math
import lib.assertion

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)


def main(): 
    lib.assertion.equals(math.gcd(24, 9), gcd(24, 9))
    lib.assertion.equals(math.gcd(3, 3), gcd(3, 3))
    lib.assertion.equals(math.gcd(456355, 2345), gcd(456355, 2345))


if __name__ == '__main__':
    main()
































# running time.  
# the key insight is that on each recursive call one of the arguments will become
# at the largest cut in half, but usually cut down much more than that.  to see this
# think about what will happen if b < a/2 and if b > a/2.  in the first case a%b has to
# be less then b (think about it).  in the second case a%b is equal to a-b, which
# is of course less then a/2 because b > a/2!
# O(n)=2logn == log n
