# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_counter = collections.defaultdict(int)
        bottom_counter = collections.defaultdict(int)
        same_counter = collections.defaultdict(int)
        n = len(tops)
        for i in range(n):
            top_counter[tops[i]] += 1
            bottom_counter[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same_counter[tops[i]] += 1
        minn = 20000
        for key in top_counter:
            if top_counter[key] + bottom_counter[key] - same_counter[key] == n:
                minn = min(minn, n - max(top_counter[key], bottom_counter[key]))
        if minn == 20000:
            return -1
        else:
            return minn
