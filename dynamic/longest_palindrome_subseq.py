from lib import assertion

# leet code 516 logest palindromic subsequence
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

#DP solution

#memoization alternative
def _lcs_pal_memo(s, l, r, memo={}):
    if l > r:
        return 0
    if l == r:
        return 1

    if (l, r) in memo:
        return memo[(l, r)]
    elif s[l] == s[r]:
        memo[(l, r)] = 2 + _lcs_pal_memo(s, l + 1, r - 1, memo)
    else:
        memo[(l, r)] = max(
            _lcs_pal_memo(s, l + 1, r, memo), 
            _lcs_pal_memo(s, l, r - 1, memo)
        )
    return memo[(l, r)]

def longestPalindromeSubseq(s):
    return _lcs_pal_memo(s, 0, len(s) - 1)

def main():
    s1 = "bbbab"
    s2 = "aa"
    s3 = "cbbd"

    assertion.equals(4, longestPalindromeSubseq(s1))
    assertion.equals(2, longestPalindromeSubseq(s2))
    assertion.equals(2, longestPalindromeSubseq(s3))

if __name__ == "__main__":
    main()

