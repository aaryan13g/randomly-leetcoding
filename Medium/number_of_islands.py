# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])

        def numm(p, q, visit):
            dirs = [(p - 1, q), (p + 1, q), (p, q - 1), (p, q + 1)]
            for d in dirs:
                if 0 <= d[0] < m and 0 <= d[1] < n and d not in visit and grid[d[0]][d[1]] == "1":
                    visit.append(d)
                    numm(d[0], d[1], visit)
            for v in visit:
                grid[v[0]][v[1]] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    numm(i, j, [(i, j)])
                    islands += 1
        return islands
