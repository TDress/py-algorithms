import lib.assertion 

def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -1 * exponent) 
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base

    return base * power(base, exponent - 1)

def powers_improved(base, exponent): 
    if exponent < 0:
        return 1 / powers_improved(base, (-1)*exponent)
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base

    half_power = powers_improved(base, exponent // 2)

    if exponent % 2 == 0:
        return half_power * half_power
    else:
        return base * half_power * half_power


def main(): 
    lib.assertion.equals(2**8, powers_improved(2, 8))
    print 'base: 2, exponent: 8.  Expected: %d, Actual: %d' % (2**8, powers_improved(2, 8))
    print 'base: 2, exponent: 0.  Expected: %d, Actual: %d' % (2**0, powers_improved(2, 0))
    print 'base: 2, exponent: -8.  Expected: %d, Actual: %d' % (2**-8, powers_improved(2, -8))
    print 'base: -4, exponent: 5.  Expected: %d, Actual: %d' % (-4**5, powers_improved(-4, 5))
    print 'base: 0, exponent: 8.  Expected: %d, Actual: %d' % (0**8, powers_improved(0, 8))



if __name__ == '__main__': 
    main()
