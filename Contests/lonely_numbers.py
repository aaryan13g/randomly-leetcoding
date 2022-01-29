/* https://leetcode.com/contest/weekly-contest-277/problems/find-all-lonely-numbers-in-the-array/ */

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums
        lonely_nums = []
        if nums[0] != nums[1] and nums[1] != nums[0] + 1:
            lonely_nums.append(nums[0])
        if nums[n-1] != nums[n-2] and nums[n-2] != nums[n-1] - 1:
            lonely_nums.append(nums[n-1])
        for i in range(1, n - 1):
            if nums[i-1] + 1 < nums[i] < nums[i+1] - 1:
                lonely_nums.append(nums[i])                
        return lonely_nums
                
