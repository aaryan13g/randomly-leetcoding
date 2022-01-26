/* https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/ */
  
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sums = []
        n = len(nums)
        for i in range(n // 2):
            pair_sums.append(nums[i] + nums[n - 1 - i])
        return max(pair_sums)
