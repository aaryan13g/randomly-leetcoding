# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def path(i, j, cnt):
            if obstacleGrid[i][j] == 1:
                return cnt
            if i == m - 1 and j == n - 1:
                return cnt + 1
            else:
                cnt1, cnt2 = 0, 0
                if i < m - 1:
                    cnt1 = path(i+1, j, cnt)
                if j < n - 1:
                    cnt2 = path(i, j+1, cnt)
                return cnt1 + cnt2
        return path(0,0,0)
