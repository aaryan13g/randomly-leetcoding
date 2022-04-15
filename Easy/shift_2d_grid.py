# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        lenn = m * n
        k = k % lenn
        flat_grid = []
        for row in grid:
            flat_grid += row
        flat_grid = flat_grid[lenn - k:lenn] + flat_grid[0:lenn - k]
        rotated_grid = []
        j = 0
        for i in range(m):
            rotated_grid.append(flat_grid[j:j+n])
            j += n
        return rotated_grid
