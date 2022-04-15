# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            diff = y - x
            if diff > 0:
                bisect.insort(stones, diff)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
