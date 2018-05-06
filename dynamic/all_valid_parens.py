# get all valid combinations of N pairs of parentheses.
def getValidParens(n):
    if n < 1:
        raise ValueError('n must be a positive integer')
    if n == 1:
        return set(["()"])

    combos = getValidParens(n - 1)
    for combo in combos.copy():
        combos.add("{0}{c}".format("()", c=combo))
        combos.add("{0}{c}{1}".format("(", ")", c=combo))
        combos.add("{c}{0}".format("()", c=combo))
        
        combos.remove(combo)

    return combos

def main():
    print(getValidParens(2))
    print(getValidParens(3))
    print(getValidParens(4))

if __name__ == '__main__':
    main()
