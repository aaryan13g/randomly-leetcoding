/* https://leetcode.com/problems/matrix-diagonal-sum/ */

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sm = 0
        n = len(mat)
        for i in range(n):
            sm += mat[i][i]
            sm += mat[i][n - i - 1]
        if n % 2 != 0:
            sm -= mat[n // 2][n // 2]
        return sm
