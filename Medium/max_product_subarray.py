/* https://leetcode.com/problems/maximum-product-subarray/ */

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = nums[::-1]
        orig = nums.copy()
        for i in range(1, len(nums)):
            if nums[i-1] == 0:
                nums[i] *= 1
            else:
                nums[i] *= nums[i-1]
            if temp[i-1] == 0:
                temp[i] *= 1
            else:
                temp[i] *= temp[i-1]
        maxx = max(nums + temp)
        return maxx
