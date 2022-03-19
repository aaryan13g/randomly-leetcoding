# https://leetcode.com/contest/biweekly-contest-74/problems/maximize-number-of-subsequences-in-a-string/

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first_occ, second_occ = [], []
        for i in range(len(text)):
            if text[i] == pattern[0]:
                first_occ.append(i)
            if text[i] == pattern[1]:
                second_occ.append(i)
        cnt = 0
        ptr = 0
        m, n = len(first_occ), len(second_occ)
        if pattern[0] == pattern[1]:
            return (m * (m + 1)) // 2
        for i in first_occ:
            while ptr < n and i > second_occ[ptr]:
                ptr += 1
            cnt = cnt + n - ptr
        return max(cnt + m, cnt + n)
