/* https://leetcode.com/problems/valid-anagram/ */

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_t = collections.Counter(t)
        if collections.Counter(s) & counter_t == counter_t:
            return True
        return False
