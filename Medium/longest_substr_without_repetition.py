/* https://leetcode.com/problems/longest-substring-without-repeating-characters/ */

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = len(set(s))
        while max_len:
            for j in range(len(s) - max_len + 1):
                temp = s[j:j+max_len]
                if len(temp) == len(set(temp)):
                    return max_len
            max_len -= 1
        return 0
