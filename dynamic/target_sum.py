# Leet code 494 target sum
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

#Find out how many ways to assign symbols to make sum of integers equal to target S.
from lib import assertion

class Solution:
    def test_sum_totals(self, nums, i, total, goal, memo):
        #translate total into the grid position
        grid_total = 1001 + total if total < 0 else 1001 + total

        if i == len(nums):
            if total == goal:
                return 1
            return 0
        if memo[i][grid_total] is not None:
            return memo[i][grid_total]
        
        memo[i][grid_total] = (
            self.test_sum_totals(nums, i + 1, total - nums[i], goal, memo) + 
            self.test_sum_totals(nums, i + 1, total + nums[i], goal, memo) 
        )
        return memo[i][grid_total]

    def num_ways(self, nums, s):
        # memo grid will use (col * 2) for the positive sums
        # and (col) for the negative sums
        memo = [[None] * 2002 for _ in range(len(nums))]
        return self.test_sum_totals(nums, 0, 0, s, memo)

def main():
    nums1 = ([1,1,1,1, 1], 3)
    sol1 = Solution()
    assertion.equals(5, sol1.num_ways(*nums1))

if __name__ == '__main__':
    main()
