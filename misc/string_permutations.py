from lib import assertion

def permute(S, prefix, perms):
    """Recursive function for finding permutations.

    The for loop makes N recursive calls (where N is the size of S),
    and each recursive call decreases N by 1.  So at the 0 level of recursion
    we make N recursive calls and for each of those calls we make N - 1 calls
    at the first level of recursion and so on.  This is N * (N - 1) * (N - 2)... 
    So we have O(n!)
    """
    if len(S) == 0:
        perms.add(prefix)
    else:
        for i in range(len(S)):
            rem = S[:i] + S[i+1:]
            permute(rem, prefix + S[i], perms)

def permutations(S):
    """Return a set of all permutations of the string S."""

    perms = set()
    permute(S, '', perms)
    return perms


def main():
    expected = set(('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'))
    assertion.equals(expected, permutations('ABC'))

if __name__ == '__main__':
    main()
