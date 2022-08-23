# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        target = n // 2
        counter = Counter(arr).most_common()
        k = 0
        for i in range(len(counter)):
            n -= counter[i][1]
            k += 1
            if n <= target:
                break
        return k
