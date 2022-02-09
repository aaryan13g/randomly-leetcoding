/* https://leetcode.com/problems/two-sum/ */

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in temp:
                return [temp[t], i]
            else:
                temp[nums[i]] = i
