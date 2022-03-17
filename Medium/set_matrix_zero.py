# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False
        for i in range(m):
            for j in range(n):
                if i == 0 and matrix[i][j] == 0:
                    first_row_zero = True
                if j == 0 and matrix[i][j] == 0:
                    first_col_zero = True
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
