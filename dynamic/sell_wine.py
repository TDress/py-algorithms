# see http://www.quora.com/Are-there-any-good-resources-or-tutorials-for-dynamic-programming-besides-the-TopCoder-tutorial/answer/Michal-Danil%C3%A1k?srid=3OBi&share=1
# Imagine you have a collection of N wines placed next to each other on a shelf. 
# For simplicity, let's number the wines from left to right as they are standing on the shelf with integers from 1 to N, respectively. 
# The price of the ith wine is pi. (prices of different wines can be different).

# Because the wines get better every year, supposing today is the year 1, on year y the price of the ith wine will be y*pi, i.e. y-times the value that current year.

# You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this year. One more constraint - on each year you are allowed to sell only either the leftmost or the rightmost wine on the shelf and you are not allowed to reorder the wines on the shelf (i.e. they must stay in the same order as they are in the beginning).

# You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order?

def sellWine(prices):
    if len(prices) == 0:
        return 0

    n = len(prices)
    dp = [0] * n

    for s in range(n - 1, -1, -1):
        for e in range(s, n):
            year = n - (e - s)
            if year == n:
                dp[e] = n * prices[s]
            else:
                dp[e] = max((prices[s] * year) + dp[e],
                           (prices[e] * year + dp[e - 1]))

    return dp[-1]



def main():
    prices = [2,3,5,1,4]
    assert(50 == sellWine(prices))

if __name__ == '__main__':
    main()
