# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def check(rem):
            if rem == "":
                return 0
            if rem[0] == '0':
                return -1
            ans = 0
            temp = int(rem[:2])
            if temp in (10, 20):
                ans = check(rem[2:])
            elif 10 < temp < 27:
                ans = 1 + check(rem[2:]) + check(rem[1:])
            else:
                ans = check(rem[1:])
            return ans
        return check(s) + 1
