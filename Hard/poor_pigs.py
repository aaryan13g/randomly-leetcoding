# https://leetcode.com/problems/poor-pigs/

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie
        pigs = 0
        while pow(T + 1, pigs) < buckets:
            pigs += 1
        return pigs
