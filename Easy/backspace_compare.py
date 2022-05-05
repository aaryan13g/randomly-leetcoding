# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for c in s:
            if c == '#' and s1:
                s1.pop()
            elif c != '#':
                s1.append(c)
        s2 = []
        for c in t:
            if c == '#' and s2:
                s2.pop()
            elif c != '#':
                s2.append(c)
        if ''.join(s1) == ''.join(s2):
            return True
        else:
            return False
