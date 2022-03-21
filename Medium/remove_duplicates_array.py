# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-1] == nums[i] and nums[i-2] == nums[i]:
                nums.pop(i)
        return len(nums)
