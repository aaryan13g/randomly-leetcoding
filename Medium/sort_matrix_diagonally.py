/* https://leetcode.com/problems/sort-the-matrix-diagonally/ /*
  
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dct = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i - j not in dct:
                    dct[i - j] = []
                dct[i - j].append(mat[i][j])
        for diag in dct:
            dct[diag].sort(reverse=True)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = dct[i - j].pop()
        return mat
