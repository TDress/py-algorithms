from lib import assertion

# A sequence of numbers is called a zig-zag sequence if the 
# differences between successive numbers strictly alternate between 
# positive and negative. The first difference (if one exists) may be 
# either positive or negative. A sequence with fewer than 
# two elements is trivially a zig-zag sequence.

# For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences are positive and the second because its last difference is zero.

# Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

def zigzag(S):
    dp = [[None, 1] for _ in range(len(S))]
    if len(S) < 2:
        return 1

    for i in range(1, len(S)):
        for j in range(i):
            last_rel, last_ans = dp[j]
            relation = None
            if S[i] > S[j]:
                relation = 1
            elif S[i] < S[j]:
                relation = 0

            if (relation is not None and last_rel != relation
                    and last_ans + 1 > dp[i][1]):
                dp[i][0] = relation
                dp[i][1] = last_ans + 1

    return dp[-1][1]

                
            

def main():
    S1 = [1,7,4,9,2,5]
    S2 = [1,17,5,10,13,15,10,5,16,8]
    S3 = [44]
    S4 = [1,2,3,4,5,6,7,8,9]
    S5 = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]

    assertion.equals(6, zigzag(S1))
    assertion.equals(7, zigzag(S2))
    assertion.equals(1, zigzag(S3))
    assertion.equals(2, zigzag(S4))
    assertion.equals(8, zigzag(S5))

if __name__ == '__main__':
    main()


