# get all valid combinations of N pairs of parentheses.
# NOTE: THIS IS INEFFICIENT: SEE SOLUTION BELOW!
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
    #test inefficient solution
    print(getValidParens(2))
    print(getValidParens(3))
    print(getValidParens(4))

    # test better solution
    print(betterValidParens(2))
    print(betterValidParens(3))
    print(betterValidParens(4))



# this is the more efficient solution, that avoids finding duplicates.
# We use the rules of parens to build up each valid combo. 
def betterGetValidRec(combos, left_rem, right_rem, progress, count):
    if count == (len(progress)):
        combos.append("".join(progress))
    else:
        if left_rem > 0:
            progress[count] = "("
            betterGetValidRec(combos, left_rem - 1, right_rem, progress, count + 1)
        if right_rem > left_rem:
            progress[count] = ")"
            betterGetValidRec(combos, left_rem, right_rem - 1, progress, count + 1)

def betterValidParens(n):
    combos, progress, count, right_rem, left_rem = [], [None] * (2 * n), 0, n, n
    betterGetValidRec(combos, left_rem, right_rem, progress, count)
    return combos

if __name__ == '__main__':
    main()
