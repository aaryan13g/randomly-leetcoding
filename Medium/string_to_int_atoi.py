/* https://leetcode.com/problems/string-to-integer-atoi/submissions/ */

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = "0"
        for ch in s:
            if 0 <= ord(ch) - 48 <= 9:
                res += ch
            else:
                break
        intt = int(res) * sign
        if -2**31 <= intt <= 2**31 - 1:
            return intt
        elif intt < 0:
            return -2**31
        elif intt > 0:
            return 2**31 - 1
