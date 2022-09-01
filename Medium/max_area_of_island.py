# https://leetcode.com/problems/max-area-of-island/

class Solution:
    visited = []
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = []
        islands = [0]
        m, n = len(grid), len(grid[0])
        
        def area(p, q, visit):
            dirs = [(p - 1, q), (p + 1, q), (p, q - 1), (p, q + 1)]
            for d in dirs:
                if 0 <= d[0] < m and 0 <= d[1] < n and d not in visit and grid[d[0]][d[1]]:
                    visit.append(d)
                    area(d[0], d[1], visit)
            self.visited += visit
            return len(visit)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    islands.append(area(i, j, [(i, j)]))
        return max(islands)
