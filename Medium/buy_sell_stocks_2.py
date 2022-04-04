# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        total = 0
        hills, valleys = [], []
        if prices[0] < prices[1]:
            valleys.append(0)
        for i in range(1, len(prices) - 1):
            if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
                hills.append(i)
            elif prices[i-1] >= prices[i] and prices[i] < prices[i+1]:
                valleys.append(i)
        if prices[-1] > prices[-2]:
            hills.append(len(prices) - 1)
        for j in range(len(hills)):
            total += prices[hills[j]] - prices[valleys[j]]
        return total
