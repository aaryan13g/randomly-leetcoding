/* https://leetcode.com/problems/permutation-in-string/ */

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        c_s1 = Counter(s1)
        for i in range(len(s2) - k + 1):
            if c_s1 == Counter(s2[i:i+k]):
                return True
        return False
