/* https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/ */

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
