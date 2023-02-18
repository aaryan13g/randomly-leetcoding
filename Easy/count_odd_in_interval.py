# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        ans = diff // 2
        if high % 2 == 1 or low % 2 == 1:
            return ans + 1
        else:
            return ans
