/* https://leetcode.com/contest/weekly-contest-277/problems/count-elements-with-strictly-smaller-and-greater-elements/ */

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[0] < nums[i] < nums[n - 1]:
                cnt += 1
        return cnt
