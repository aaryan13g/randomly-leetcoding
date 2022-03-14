# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        idx_to_check = 0
        if newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
        elif newInterval[0] >= intervals[-1][0]:
            intervals.append(newInterval)
            idx_to_check = len(intervals) - 2
        else:
            l, r = 0, len(intervals) - 1
            while l < r:
                mid = (l + r) // 2
                if intervals[mid][0] <= newInterval[0] <= intervals[mid+1][0]:
                    intervals.insert(mid + 1, newInterval)
                    idx_to_check = mid
                    break
                elif newInterval[0] <= intervals[mid][0]:
                    r = mid
                elif newInterval[0] >= intervals[mid][0]:
                    l = mid + 1
        while len(intervals) > idx_to_check + 1:
            if intervals[idx_to_check+1][0] > intervals[idx_to_check][1]:
                idx_to_check += 1
            else:
                intervals[idx_to_check][0] = min(intervals[idx_to_check][0], intervals[idx_to_check+1][0])
                intervals[idx_to_check][1] = max(intervals[idx_to_check][1], intervals[idx_to_check+1][1])
                intervals.pop(idx_to_check+1)
        return intervals
