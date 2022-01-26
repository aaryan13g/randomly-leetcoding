/* https://leetcode.com/problems/replace-all-digits-with-characters/ /*
  
class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(1, len(s), 2):
            ans += s[i - 1] + chr(ord(s[i - 1]) + int(s[i]))
        if len(s) % 2 == 0:
            return ans
        else:
            return ans + s[-1]
