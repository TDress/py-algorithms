from lib import assertion

def LCS(X, Y):
    """Find the longest common subsequence lengths of the two input strings.

    A subsequence is a sequence that appears in the larger sequence but
    need not be continuous (although the characters in the subsequence must
    appear in-order in the larger sequence.)
    Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]
    In other words, the returned list is 2 dimensional and each value L[j,k]
    is the LCS for the two strings X[0:j] and Y[0:k]
    """
    len_X, len_Y = len(X), len(Y)
    L=[[0] * (len_Y + 1) for i in range(len_X + 1)]

    for j in range(len_X):
        for k in range (len_Y):
            if X[j] == Y[k]:
                L[j + 1][k + 1] = 1 + L[j][k]
            else:
                L[j + 1][k + 1] = max(L[j + 1][k], L[j][k + 1])

    return L

def LCS_extract(X, Y, L):
    """Extract the LCS of X and Y using subsequence length table L.

    Reverse engineer the table of lengths to construct the 
    longest subsequence and return it as a string.
    """

    answer = []
    walk_X, walk_Y = len(X), len(Y)
    while L[walk_X][walk_Y] != 0:
        if X[walk_X - 1] == Y[walk_Y - 1]:
            answer.append(X[walk_X - 1])
            walk_X -= 1
            walk_Y -= 1
        elif L[walk_X - 1][walk_Y] > L[walk_X][walk_Y - 1]:
            walk_X -= 1
        else:
            walk_Y -= 1

    return ''.join(reversed(answer))


def main():
    X = 'GTCAATAACACAGTTCACTGTACGACTG'
    Y = 'ACGTCAGTATCGATGCATGCATGCTAGC'

    table = LCS(X, Y)
    # Note that the table indices correspond to subsequence lengths and 
    # NOT the actual indices of the characters in the sequences.  So
    # for example the LCS length of the first character of each string
    # is in spot L[1, 1], not L[0, 0]
    assertion.equals(1, table[20][1])
    assertion.equals(0, table[20][0])
    assertion.equals(2, table[20][2])
    assertion.equals(3, table[20][3])
    assertion.equals(3, table[5][5])
    assertion.equals(5, table[8][8])

    assertion.equals('GTCATACACATCATGTAGC', LCS_extract(X, Y, table))


if __name__ == '__main__':
    main()


