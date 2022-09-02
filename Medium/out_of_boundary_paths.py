# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        @cache
        def check(i, j, moves):
            cnt = 0
            if moves == 1:
                if i == 0:
                    cnt += 1
                if i == m - 1:
                    cnt += 1
                if j == 0:
                    cnt += 1
                if j == n - 1:
                    cnt += 1
                return cnt
            dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for d in dirs:
                if 0 <= d[0] < m and 0 <= d[1] < n:
                    cnt += check(d[0], d[1], moves - 1)
            return cnt
        ans = 0
        while maxMove:
            ans += check(startRow, startColumn, maxMove)
            maxMove -= 1
        return ans % 1000000007
