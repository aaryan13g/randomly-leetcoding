/* https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/ */

class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapp = {}
        for i in range(1, 10):
            mapp[str(i)] = chr(96 + i)
        for i in range(10, 27):
            mapp[str(i) + '#'] = chr(96 + i)
        i = 0
        ans = ""
        while i < len(s):
            if '#' in s[i + 1:]:
                if s[i:i+3] in mapp:
                    ans += mapp[s[i:i+3]]
                    i += 3
                else:
                    ans += mapp[s[i]]
                    i += 1
            else:
                ans += mapp[s[i]]
                i += 1
        return ans
            
