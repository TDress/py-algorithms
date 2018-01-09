import random
import lib.assertion

def is_prime(a):
    for i in range(0, 100): 
        random_num = random.randrange(1, a)
        if random_num**(a-1) % a != 1:
            return False

    return True


def main(): 
    lib.assertion.equals(True, is_prime(1223))
    lib.assertion.equals(True, is_prime(13)
    lib.assertion.equals(True, is_prime(1109))
    lib.assertion.equals(False, is_prime(789872))


if __name__ == '__main__':
    main()
































# running time.  
# the key insight is that on each recursive call one of the arguments will become
# at the largest cut in half, but usually cut down much more than that.  to see this
# think about what will happen if b < a/2 and if b > a/2.  in the first case a%b has to
# be less then b (think about it).  in the second case a%b is equal to a-b, which
# is of course less then a/2 because b > a/2!
# O(n)=2logn == log n

