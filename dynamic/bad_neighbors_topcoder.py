from lib import assertion

#The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to heart. Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the town's well than his neighbors, so the town has been arranged in a big circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. You have been hired to collect donations for the Save Our Well fund.

#Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor has also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last entries in donations are also for next-door neighbors. You must calculate and return the maximum amount of donations that can be collected.

def max_donations(dons):
    dp = [None] * len(dons)
    dp[0], dp[1] = (dons[0], 0), (dons[0], dons[1])

    for i in range(2, len(dons)):
        if i == len(dons) - 1:
            best_taken = dp[i - 1][0]
        else:
            best_taken = max(dp[i - 1][0], dp[i - 2][0] + dons[i])

        best_not_taken = max(dp[i - 1][1], dp[i - 2][1] + dons[i])
        dp[i] = (best_taken, best_not_taken)

    return max(dp[-1])

def main():
    l1 = [10, 3, 2, 5, 7, 8]
    l2 = [11, 15]
    l3 = [7,7,7,7,7,7,7]
    l4 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    l5 = [
        94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
        6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
        52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72
    ]

    assertion.equals(19, max_donations(l1))
    assertion.equals(15, max_donations(l2))
    assertion.equals(21, max_donations(l3))
    assertion.equals(16, max_donations(l4))
    assertion.equals(2926, max_donations(l5))

if __name__ == '__main__':
    main()
    
