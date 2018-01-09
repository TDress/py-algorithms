import lib.assertion

def mod_exp(base, exp, n):
    if(exp == 0):
        return 1
    
    intermediate = mod_exp(base, exp // 2, n)
    if(exp % 2 == 0):
        return intermediate ** 2 % n
    else:
        return (base * intermediate ** 2) % n



def main():
    lib.assertion.equals(1, mod_exp(2, 4, 3))
    lib.assertion.equals(3, mod_exp(3, 25, 7))
    lib.assertion.equals(1, mod_exp(8, 300, 13))


if __name__ == '__main__':
    main()


































# running time
# we can think about it in terms of bit complexity, where multiplications take quadratic time
# and the size of the exponent input in bits (n) is the greatest number of recursive calls
# possible
# But casually we would just say that this runs O(log n) .
