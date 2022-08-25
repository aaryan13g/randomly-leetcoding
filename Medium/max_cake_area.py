# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0, h]
        horizontalCuts.sort()
        verticalCuts += [0, w]
        verticalCuts.sort()
        maxh = 1
        for i in range(len(horizontalCuts) - 1):
            maxh = max(maxh, horizontalCuts[i+1] - horizontalCuts[i])
        maxv = 1
        for i in range(len(verticalCuts) - 1):
            maxv = max(maxv, verticalCuts[i+1] - verticalCuts[i])
        return (maxh * maxv) % (10**9 + 7)
