/* https://leetcode.com/problems/valid-parentheses/ */

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_dict = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
                continue
            if ch in close_dict:
                if not stack or stack.pop() != close_dict[ch]:
                    return False
        if not stack:
            return True
        else:
            return False
