# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        sm = -1
        for i in range(k, len(nums) - k):
            if sm == -1:
                sm = sum(nums[i-k:i+k+1])
            else:
                sm = sm - nums[i-k-1] + nums[i+k]
            ans[i] = sm // ((2*k) + 1)
        return ans
