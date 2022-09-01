# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def check(i, j, p_flag, visited):
            visited.append((i, j))
            if p_flag:
                if i == 0 or j == 0:
                    return True
            else:
                if i == m - 1 or j == n - 1:
                    return True
            dirs = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            flag = False
            for d in dirs:
                if 0 <= d[0] < m and 0 <= d[1] < n and heights[i][j] >= heights[d[0]][d[1]] and d not in visited and check(d[0], d[1], p_flag, visited):
                    flag = True
                    break
            if not flag:
                return False
            else:
                return True
            
        ans = []
        for r in range(m):
            for c in range(n):
                if check(r, c, True, []) and check(r, c, False, []):
                    ans.append([r, c])
        return ans
