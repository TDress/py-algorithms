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

if __name__ == '__main__':
    main()


