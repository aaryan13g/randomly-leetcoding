# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    row_sum, col_sum = None, None
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.row_sum, self.col_sum = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    self.row_sum[i][j] = matrix[i][j]
                else:
                    self.row_sum[i][j] = matrix[i][j] + self.row_sum[i][j-1]
                if i == 0:
                    self.col_sum[i][j] = matrix[i][j]
                else:
                    self.col_sum[i][j] = matrix[i][j] + self.col_sum[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sm = 0
        adder = 0
        if row2 - row1 >= col1 - col2:
            for c in range(col1, col2 + 1):
                if row1 > 0:
                    adder = self.col_sum[row1 - 1][c]
                sm += self.col_sum[row2][c] - adder
        else:
            for r in range(row1, row2 + 1):
                if col1 > 0:
                    adder = self.col_sum[r][col1 - 1]
                sm += self.row_sum[r][col2] - adder
        return sm


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
