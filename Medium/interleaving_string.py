# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        @cache
        def check(ptr1, ptr2, i):
            if (ptr1 == n1 and ptr2 == n2 and i == n3) or (ptr1 == n1 and ptr2 < n2 and s2[ptr2:] == s3[i:]) or (ptr2 == n2 and ptr1 < n1 and s1[ptr1:] == s3[i:]):
                return True
            elif (ptr1 == n1 and ptr2 < n2 and s2[ptr2:] != s3[i:]) or (ptr2 == n2 and ptr1 < n1 and s1[ptr1:] != s3[i:]):
                return False
            elif (ptr2 < n2 and s2[ptr2] != s3[i]) and (ptr1 < n1 and s1[ptr1] != s3[i]):
                return False
            else:
                if s1[ptr1] == s2[ptr2] == s3[i]:
                    return check(ptr1 + 1, ptr2, i + 1) or check(ptr1, ptr2 + 1, i + 1)
                elif s1[ptr1] == s3[i]:
                    return check(ptr1 + 1, ptr2, i + 1)
                elif s2[ptr2] == s3[i]:
                    return check(ptr1, ptr2 + 1, i + 1)
        
        return check(0, 0, 0)
