# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '+':
                    stack.append(n2 + n1)
                elif t == '-':
                    stack.append(n1 - n2)
                elif t == '*':
                    stack.append(n2 * n1)
                elif t == '/':
                    if (n1 >= 0 and n2 > 0) or (n1 <= 0 and n2 < 0) or (n1 // n2 == n1 / n2):
                        stack.append(n1 // n2)
                    else:
                        stack.append((n1 // n2) + 1)
            else:
                stack.append(int(t))
        return stack[0]
