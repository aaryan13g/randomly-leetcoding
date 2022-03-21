# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = []
        while s:
            print(s)
            if len(s) == 1:
                parts.append(1)
                break
            for i in range(1, len(s)):
                if not set(s[:i]).intersection(set(s[i:])):
                    s = s[i:]
                    parts.append(i)
                    break
                if i == len(s) - 1:
                    parts.append(i + 1)
                    s = ''
                    break
        return parts
