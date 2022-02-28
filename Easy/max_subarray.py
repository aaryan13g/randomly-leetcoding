/* https://leetcode.com/problems/maximum-subarray/ */

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums.copy()
        for i in range(1, len(nums)):
            if res[i-1] > 0:
                res[i] += res[i-1]
        return max(res)
