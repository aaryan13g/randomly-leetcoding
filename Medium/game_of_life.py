# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for d in dirs:
                    new_i, new_j = i + d[0], j + d[1]
                    if 0 <= new_i < m and 0 <= new_j < n and abs(board[new_i][new_j]) == 1:
                        cnt += 1
                if cnt < 2 or cnt > 3:
                    board[i][j] -= 2
                elif cnt == 3 and board[i][j] == 0:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] < 0:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        
