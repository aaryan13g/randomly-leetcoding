# https://leetcode.com/problems/reordered-power-of-2/

from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        digits = []
        while n:
            digits.append(str(n % 10))
            n = n // 10
        perms = permutations(digits, len(digits))
        for perm in perms:
            if int(perm[0]) != 0 and int(perm[-1]) % 2 != 1:
                numm = int(''.join(perm))
                logg = log2(numm)
                if logg == logg // 1:
                    return True
        return False
