/* https://leetcode.com/problems/valid-palindrome/ */

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                if s[i].isupper():
                    s[i] = s[i].lower()
            else:
                s.pop(i)
        temp = s[::-1]
        return s == temp
