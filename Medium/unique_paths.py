# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def path(i, j, cnt):
            if not (i < m - 1 and j < n - 1):
                cnt += 1
                return cnt
            else:
                return path(i+1, j, cnt) + path(i, j+1, cnt)
        return path(0, 0, 0)
