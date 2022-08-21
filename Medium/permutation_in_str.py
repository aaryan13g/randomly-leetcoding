/* https://leetcode.com/problems/permutation-in-string/ */

# from collections import Counter

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         k = len(s1)
#         c_s1 = Counter(s1)
#         for i in range(len(s2) - k + 1):
#             if c_s1 == Counter(s2[i:i+k]):
#                 return True
#         return False

# Optimized solution
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        countt = dict(Counter(list(s1)))
        s2 = list(s2)
        count_match = dict(Counter(s2[:m]))
        for i in range(n - m):
            # temp = s2[i:i+m]
            if count_match == countt:
                return True
            if count_match[s2[i]] == 1:
                del(count_match[s2[i]])
            else:
                count_match[s2[i]] -= 1
            if s2[i+m] not in count_match:
                count_match[s2[i+m]] = 1
            else:
                count_match[s2[i+m]] += 1
        if count_match == countt:
            return True
        return False
