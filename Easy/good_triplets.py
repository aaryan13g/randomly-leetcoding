/* https://leetcode.com/problems/count-good-triplets */

from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        combs = list(combinations(arr, 3))
        for comb in combs:
            if abs(comb[0] - comb[1]) <= a and abs(comb[1] - comb[2]) <= b and abs(comb[0] - comb[2]) <= c:
                ans += 1
        return ans
