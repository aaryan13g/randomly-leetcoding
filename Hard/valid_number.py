# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if s == 'e' or 'inf' in s or 'Inf' in s:
                raise
            float(s)
            return True
        except:
            return False
