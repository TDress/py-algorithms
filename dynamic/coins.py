# Given a value N, if we want to make change for N cents, and we have infinite supply of each of 
# S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4

from lib import assertion

def _getWays(n, c, used, visited):
    if n == 0:
        return 1
    print(used)
    ways = 0
    for cn in c:
        if cn <= n:
            nused = used[:cn] + str(int(used[cn]) + 1) + used[cn + 1:]
            if (nused) not in visited:
                ways += _getWays(n - cn, c, nused, visited)
                visited.add(nused)
    return ways

# recursive, naive solution.  memoizes to avoid to dups
# but pretty inefficient.
def getWays(n, c):
    visited, used = set(), "0" * 51
    return _getWays(n, c, used, visited)

# DP solution.  THIS IS THE CORRECT ANSWER.  
def getWaysDP(n, c):
    dp = [[1] * (len(c)) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(len(c)):
            res = 0 if j == 0 else dp[i][j - 1]
            res += 0 if c[j] > i else dp[i - c[j]][j]
            dp[i][j] = res

    return dp[n][len(c) - 1]

def main():
    c1, n1 = [1,2,3], 4
    c2, n2 = [2,5,3,6], 10
    assertion.equals(4, getWaysDP(n1, c1))
    assertion.equals(5, getWaysDP(n2, c2))

if __name__ == '__main__':
    main()
