# https://leetcode.com/problems/majority-element/submissions/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        for num in cnt:
            if cnt[num] > n // 2:
                return num
