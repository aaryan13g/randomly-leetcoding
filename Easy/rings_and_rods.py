/* https://leetcode.com/problems/rings-and-rods/ */

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        ans = 0
        for i in range(0, len(rings), 2):
            numb = rings[i + 1]
            if numb not in rods:
                rods[numb] = set(rings[i])
            else:
                rods[numb].add(rings[i])
        for rod in rods:    
            if len(rods[rod]) == 3:
                    ans += 1
        return ans
