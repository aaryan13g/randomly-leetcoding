/* https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ */

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                maxx = max(maxx, prices[r] - prices[l])
                r += 1
        return maxx
