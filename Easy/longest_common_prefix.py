/* https://leetcode.com/problems/longest-common-prefix/ */

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minn = min(strs, key=len)
        strs.remove(minn)
        
        for i in range(len(minn)):
            for s in strs:
                if minn[i] != s[i]:
                    return minn[:i]
        return minn
