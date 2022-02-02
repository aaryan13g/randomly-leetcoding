/* https://leetcode.com/problems/increasing-decreasing-string/ */

class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        ans = ""
        while s:
            for ch in sorted(set(s)):
                ans += ch
                s.remove(ch)
            for ch in sorted(set(s), reverse=True):
                ans += ch
                s.remove(ch)
        return ans
