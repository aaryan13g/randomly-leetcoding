/* https://leetcode.com/problems/find-the-highest-altitude/ */

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        alt = 0
        for g in gain:
            alt += g
            if alt > maxx:
                maxx = alt
        return maxx
      

/* Another Solution */

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sm = []
        for i in range(len(gain)):
            sm.append(sum(gain[:i+1]))
        return max(max(sm), 0)
