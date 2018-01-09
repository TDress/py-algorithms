from lib import assertion

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def add_fractions(x, y):
    """add the two fractions represented by the 2-tuples x and y
    (where index zero is the numerator and index 1 is the denominator)
    """
    lcm = (x[1] * y[1]) // gcd(x[1], y[1])
    multiplier_x = lcm / x[1]
    multiplier_y = lcm / y[1]

    return ((multiplier_x * x[0]) + (multiplier_y * y[0]), lcm)


def main():
    assertion.equals((17, 12), add_fractions((2, 3), (3, 4)))
    assertion.equals((71, 24), add_fractions((5, 8), (7, 3)))
    assertion.equals((50, 82), add_fractions((1, 2), (9, 82)))

if __name__ == '__main__':
    main()
