/* https://leetcode.com/problems/zigzag-conversion/ */

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ''
        dct = collections.defaultdict(list)
        p = 1
        revFlag = False
        for i in range(len(s)):
            dct[p].append(s[i])
            if p == numRows:
                revFlag = True
            if p == 1:
                revFlag = False
            if revFlag:
                p -= 1
            else:
                p += 1
        for j in range(1, numRows + 1):
            ans += ''.join(dct[j])
        return ans
