/* https://leetcode.com/problems/find-greatest-common-divisor-of-array/ */

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        def GCD(a, b):
            if b == 0:
                return a
            else:
                return GCD(b, a % b)
        return GCD(small, large)
