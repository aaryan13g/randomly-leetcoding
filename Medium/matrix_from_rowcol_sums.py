/* https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/submissions/ */

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        mat = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]
        return mat
