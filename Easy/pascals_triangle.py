# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(len(pascal[i - 1]) - 1):
                row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            row.append(1)
            pascal.append(row)
        return pascal[:numRows]
