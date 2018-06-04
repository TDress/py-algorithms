# Leet code 309. Best Time to Buy and Sell Stock with Cooldown
from lib import assertion

def maxProfit(prices):

    if len(prices) == 0:
        return 0
    dp = [[0] * 4 for _ in range(len(prices) + 1)]
    dp[1] = [-prices[0], 0, -prices[0], 0]
    for dpi in range(2, len(dp)):
        # buy profit is previous dp cool - current price
        dp[dpi][0] = dp[dpi - 1][3] - prices[dpi - 1] 
        # sell profit is max of selling the held value and selling the bought value
        dp[dpi][1] = max(
            prices[dpi - 1] + dp[dpi - 1][2], prices[dpi - 1] + dp[dpi - 1][0]
        )
        # hold value is the max of the previous hold value 
        # and the previous cool value minus the current price
        dp[dpi][2] = max(
            dp[dpi - 1][2], dp[dpi - 1][3] - prices[dpi - 1]
        )
        # cool value is the value of selling on the previous turn
        dp[dpi][3] = max(dp[dpi - 1][1], dp[dpi - 1][3])
        print(dp)

    largest = max(dp[-1])
    return 0 if largest < 0 else largest

def main():
    assertion.equals(3, maxProfit([1,2,3,0,2]))
    assertion.equals(1, maxProfit([2,1,2,0,1]))

if __name__ == '__main__':
    main()

