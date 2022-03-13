# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        p = 0
        n = len(intervals)
        intervals.sort()
        while p < n - 1 and n > 1:
            if intervals[p][1] >= intervals[p+1][0]:
                intervals[p][1] = max(intervals[p+1][1], intervals[p][1])
                intervals[p][0] = min(intervals[p+1][0], intervals[p][0])
                intervals.pop(p+1)
                n = len(intervals)
            else:
                p += 1
        return intervals
