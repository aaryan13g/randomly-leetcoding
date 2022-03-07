/* https://leetcode.com/problems/arithmetic-slices/ */

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        p = 1
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i-1] == nums[i + 1] - nums[i]:
                ans += p
                p += 1
            else:
                p = 1
        return ans
