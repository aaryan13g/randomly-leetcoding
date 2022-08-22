# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4 and n != 1:
            return False
        logg = log2(n) / 2
        if logg / 1 == logg // 1:
            return True
        else:
            return False
