/* https://leetcode.com/problems/to-lower-case/ */

class Solution:
    def toLowerCase(self, s: str) -> str:
        for ch in s:
            if 65 <= ord(ch) <= 90:
                s = s.replace(ch, chr(ord(ch) + 32))
        return s
