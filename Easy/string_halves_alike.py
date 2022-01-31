/* https://leetcode.com/problems/determine-if-string-halves-are-alike/ */

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt1 = len([ch for ch in s[:len(s) // 2] if ch in vowels])
        cnt2 = len([ch for ch in s[len(s) // 2:] if ch in vowels])
        return cnt1 == cnt2
