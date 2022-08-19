# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in dct:
                return sorted([i+1, dct[temp] + 1])
            else:
                dct[numbers[i]] = i
