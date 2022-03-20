# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        wordlen = len(word)
        
        def rec(i, j, wc_ptr, visited):
            if board[i][j] == word[wc_ptr]:
                wc_ptr += 1
                visited = visited + ((i, j),)
                if wc_ptr == wordlen:
                    return True
                else:
                    new_dirs = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
                    for d in new_dirs:
                        if d not in visited and 0 <= d[0] < m and 0 <= d[1] < n:
                            visited_temp = visited[:]
                            if rec(d[0], d[1], wc_ptr, visited_temp):
                                return True
                    return False
            else:
                return False
        
        # Condition to eliminate TLE in cases such as where whole board consists of 'A' but searchword is like 'AAAAAAAAAAAAAB'
        if not set(list(word)).issubset(set(sum(board, []))):
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    word_found = rec(i, j, 0, ())
                    if word_found:
                        return True
        return False
