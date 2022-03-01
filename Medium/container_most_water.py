/* https://leetcode.com/problems/container-with-most-water/ */

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxx = 0
        i = 0
        j = n - 1
        while i < j:
            cur_max = min(height[i], height[j])
            maxx = max(maxx, cur_max * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxx
