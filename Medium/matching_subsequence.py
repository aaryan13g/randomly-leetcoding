# https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lenn = len(s)
        def sub(to_check, m, n):
            if m == 0:
                return True
            if n == 0 or n < m:
                return False
            if to_check[m - 1] == s[n - 1]:
                return sub(to_check, m - 1, n - 1)
            else:
                return sub(to_check, m, n - 1)
        ans = 0
        sett = set(list(s))
        for word in words:
            temp_set = set(list(word))
            if temp_set.issubset(sett) and sub(word, len(word), lenn):
                ans += 1
        return ans
