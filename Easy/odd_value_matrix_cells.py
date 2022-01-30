/* https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/ */

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0] * n for i in range(m)]
        for ind in indices:
            mat[ind[0]] = [x + 1 for x in mat[ind[0]]]
            for i in range(m):
                mat[i][ind[1]] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 != 0:
                    ans += 1
        return ans
