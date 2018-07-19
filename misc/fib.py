import lib.assertion

def fib2(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp[0], dp[1] = dp[1], sum(dp)

    return dp[1]

def fib(seq_length):
    if not isinstance(seq_length, int) or seq_length < 1:
        raise RuntimeError('The argument must be a positive integer')
    elif seq_length == 1 or seq_length == 2:
        return 1

    sequence = [1,1]
    previous = sequence[:]
    i = 2

    while i < seq_length:
        sequence.append(reduce(lambda x,y: x + y, previous))
        previous = sequence[-2:]
        i += 1

    return sequence[-1]

def fib_recursive(n):
    '''return the nth fibonnaci number

    '''
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib_recursive(n - 1)
        return (a + b, a)


def main():
    #lib.assertion.equals(1, fib(1))
    #lib.assertion.equals(1, fib(2))
    #lib.assertion.equals(2, fib(3))
    #lib.assertion.equals(13, fib(7))
    #lib.assertion.equals(21, fib(8))

    lib.assertion.equals(99194853094755497, fib2(83))


if __name__ == '__main__':
    main()

