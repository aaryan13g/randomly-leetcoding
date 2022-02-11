/* https://leetcode.com/problems/reverse-integer/ */

class Solution:
    def reverse(self, x: int) -> int:
        ch = str(x)
        ch = ch[::-1]
        if x < 0:
            ch = '-' + ch[:-1]
        intt = int(ch)
        if -2**31 <= intt <= 2**31 -1:
            return intt
        else:
            return 0
