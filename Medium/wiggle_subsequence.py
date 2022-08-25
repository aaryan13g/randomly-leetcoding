# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cnt = 1
        flag = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and flag != True:
                cnt += 1
                flag = True
            elif nums[i] < nums[i - 1] and flag != False:
                cnt += 1
                flag = False
        return cnt
