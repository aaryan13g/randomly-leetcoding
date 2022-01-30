*/ https://leetcode.com/problems/sum-of-all-subset-xor-totals/ */

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        for i in range(1, len(nums) + 1):
            combs = list(itertools.combinations(nums, i))
            for comb in combs:
                xor = 0
                for num in comb:
                    xor ^= num
                ans += xor
        return ans
