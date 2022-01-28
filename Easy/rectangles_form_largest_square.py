/* https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/ */

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count_dict = {}
        for rect in rectangles:
            minn = min(rect)
            if minn not in count_dict:
                count_dict[minn] = 1
            else:
                count_dict[minn] += 1
        return count_dict[max(count_dict.keys())]
