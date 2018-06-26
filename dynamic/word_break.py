# Leetcode 139
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. 

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dp, words = [False] * len(s), set(wordDict)
    for i in range(len(s) - 1, -1, -1):
        if s[i:] in words:
            dp[i] = True
            continue
        for j in range(len(s) - 2, i - 1, -1):
            if s[i:j + 1] in words and dp[j + 1]:
                dp[i] = True
                break

    return dp[0]

def main():
    s = "ab"
    wordDict = ["a", "b"]
    assert(True == wordBreak(s, wordDict))

if __name__ == '__main__':
    main()
