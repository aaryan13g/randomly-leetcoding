# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ['a'] * n
        k -= n
        i = n - 1
        while k:
            add = min(25, k)
            s[i] = chr(97 + add)
            i -= 1
            k -= add
        return ''.join(s)
