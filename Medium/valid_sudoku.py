/* https://leetcode.com/problems/valid-sudoku/ */

class Solution:
    def check(self, lst):
        lst = [elem for elem in lst if elem != '.']
        return len(lst) == len(set(lst))
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check(row):
                return False
        cols = []
        for i in range(9):
            col = [row[i] for row in board]
            cols.append(col)
        for col in cols:
            if not self.check(col):
                return False
        windows = []
        p, q = 0, 0
        for i in range(9):
            window = []
            for j in range(p, p+3):
                for k in range(q, q+3):
                    window.append(board[j][k])
            windows.append(window)
            q += 3
            if q == 9:
                p += 3
                q = 0
        for window in windows:
            if not self.check(window):
                return False
        return True
