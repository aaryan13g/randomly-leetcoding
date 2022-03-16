# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par_dict = {}
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                par_dict[i] = s[i]
        rem = []
        stack = []
        for idx in par_dict:
            if par_dict[idx] == '(':
                stack.append(idx)
            else:
                if stack and par_dict[stack[-1]] == '(':
                    stack.pop()
                else:
                    rem.append(idx)
        rem = rem + stack
        ans = list(s)
        for i in reversed(rem):
            ans.pop(i)
        return ''.join(ans)
