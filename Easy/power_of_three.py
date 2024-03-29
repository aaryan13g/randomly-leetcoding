# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            n = n / 3
            if n != n // 1:
                return False
        return True
