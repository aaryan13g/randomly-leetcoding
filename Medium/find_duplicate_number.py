# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set(nums)
        for num in nums:
            try:
                sett.remove(num)
            except:
                return num
