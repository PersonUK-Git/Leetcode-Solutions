from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit
sol = Solution() 
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0