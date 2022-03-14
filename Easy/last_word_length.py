# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Solution 1
        # s = s.strip(' ')
        # return len(s.split(' ')[-1])
        
        # Solution 2
        for word in reversed(s.split(' ')):
            if word:
                return len(word)
