# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                while stack and s[i] < stack[-1] and last[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])
        return ''.join(stack)
