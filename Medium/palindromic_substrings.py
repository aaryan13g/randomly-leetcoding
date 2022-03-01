/* https://leetcode.com/problems/palindromic-substrings/ */

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        window = 2
        while window <= len(s):
            for i in range(len(s) - window + 1):
                if s[i:i+window] == s[i:i+window][::-1]:
                    ans += 1
            window += 1
        return ans
