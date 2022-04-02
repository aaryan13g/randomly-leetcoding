# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxx = 0
        temp = 1
        nums = list(set(nums))
        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                temp += 1
            else:
                maxx = max(maxx, temp)
                temp = 1
        return max(maxx, temp)
