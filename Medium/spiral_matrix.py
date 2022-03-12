# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        rows, cols = [], [[] for k in range(n)]
        for i in range(m):
            rows.append(matrix[i])
            for j in range(n):
                cols[j].append(matrix[i][j])
        m1, n1 = m, n
        ans = []
        while m - m1 < m1 and n - n1 < n1:
            for elem in rows[m-m1][n-n1:n1]:
                ans.append(elem)
            for elem in cols[n1-1][m-m1+1:m1]:
                ans.append(elem)
            if m - m1 + 1 > m1 - 1 or n - n1 + 1 > n1 - 1:
                break
            for elem in reversed(rows[m1-1][n-n1:n1-1]):
                ans.append(elem)
            for elem in reversed(cols[n-n1][m-m1+1:m1-1]):
                ans.append(elem)
            if m - m1 + 1 > m1 - 1 or n - n1 + 1 > n1 - 1:
                break
            m1 -= 1
            n1 -= 1
        return ans
