/* https://leetcode.com/problems/count-the-number-of-consistent-strings/ */

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            if set(word).issubset(allowed):
                ans += 1
        return ans
