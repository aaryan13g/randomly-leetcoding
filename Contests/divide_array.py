# https://leetcode.com/contest/biweekly-contest-74/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for c in counter:
            if counter[c] % 2 != 0:
                return False
        return True
