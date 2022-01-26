/* https://leetcode.com/problems/remove-outermost-parentheses/ */

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        decomposed = []
        temp_str = ''
        temp = 0
        for i in range(len(s)):
            temp_str += s[i]
            if s[i] == '(':
                temp += 1
            else:
                temp -= 1
            if temp == 0:
                decomposed.append(temp_str[1:-1])
                temp_str = ''
        return ''.join(decomposed)
