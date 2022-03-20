# https://leetcode.com/contest/weekly-contest-285/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] == nums[i]:
                nums.pop(i)
        cnt = 0
        for i in range(1, len(nums) - 1):
            if (nums[i] < nums[i-1] and nums[i] < nums[i+1]) or (nums[i] > nums[i-1] and nums[i] > nums[i+1]):
                cnt += 1
        return cnt
