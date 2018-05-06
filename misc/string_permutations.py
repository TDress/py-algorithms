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


# Alternative method
def permute2(S, start, end, res):
    if start == end:
        res.add(''.join(S))
    else:
        for i in range(start, end + 1):
            S[i], S[start] = S[start], S[i]
            permute2(S, start + 1, end, res)
            S[i], S[start] = S[start], S[i]



def permutations2(str):
    S, res = list(str), set()
    permute2(S, 0, len(S) - 1, res)
    return res


def dynamicPermute(S):
    if len(S) == 0:
        return set()
    perms = set(S[0])

    for i in range(1, len(S)):
        for ss in perms.copy():
            for pos in range(len(ss) + 1):
                perms.add(ss[:pos] + S[i] + ss[pos:])
            perms.remove(ss)

    return perms

def recursiveDynamicPermute(S):
    if len(S) == 0:
        return set()
    elif len(S) == 1:
        return set(S[0])

    perms = set()
    for ss in recursiveDynamicPermute(S[:-1]):
        for j in range(len(ss) + 1):
            perms.add(ss[:j] + S[-1] + ss[j:])

    return perms



def main():
    expected = set(('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'))
    assertion.equals(expected, permutations('ABC'))

    assertion.equals(expected, permutations2('ABC'))

    assertion.equals(expected, dynamicPermute('ABC'))

    assertion.equals(expected, recursiveDynamicPermute('ABC'))

if __name__ == '__main__':
    main()
