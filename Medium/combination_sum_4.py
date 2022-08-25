# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def check(curr_sum, adder):
            new_sum = curr_sum + adder
            if new_sum == target:
                return 1
            if new_sum > target:
                return 0
            cnt = 0
            for num in nums:
                cnt += check(new_sum, num)
            return cnt
        return check(0, 0)
