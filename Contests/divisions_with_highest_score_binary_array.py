/* https://leetcode.com/contest/weekly-contest-278/problems/all-divisions-with-the-highest-score-of-a-binary-array/ */

from collections import defaultdict

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score_dict = defaultdict(lambda: [])
        n = len(nums)
        score = sum(nums)
        score_dict[score].append(0)
        for i in range(n):
            if nums[i] == 0:
                score += 1
            else:
                score -= 1
            score_dict[score].append(i + 1)
        return score_dict[max(score_dict.keys())]
