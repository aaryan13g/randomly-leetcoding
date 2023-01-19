# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        start = s.find('1')
        end = s.rfind('0')
        if start == -1 or end == -1 or start > end:
            return 0
        ans = 0
        ones = 0
        for i in range(start, end + 1):
            if s[i] == '1':
                ones += 1
            elif ones:
                ones -= 1
                ans += 1
        return ans
