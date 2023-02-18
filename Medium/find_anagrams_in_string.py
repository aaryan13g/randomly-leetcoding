# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        m = len(p)
        ans = []
        for i in range(len(s) - m + 1):
            temp = s[i:i+m]
            if p_c == Counter(temp):
                ans.append(i)
        return ans
