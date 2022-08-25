# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def foo(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            return foo(i - 1) + foo(i - 2)
        return foo(n)
