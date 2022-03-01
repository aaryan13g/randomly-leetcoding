/* https://leetcode.com/problems/valid-palindrome/ */

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t1 = []
        for i in range(len(s)):
            if s[i].isalnum():
                t1.append(s[i])
        t1 = ''.join(t1).lower()
        t2 = t1[::-1]
        return t1 == t2
