# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def path(i, j):
            if i >= m or j >= n:
                return math.inf
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            else:
                return grid[i][j] + min(path(i+1, j), path(i, j+1))
        return path(0, 0)
