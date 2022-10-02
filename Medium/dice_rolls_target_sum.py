# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/submissions/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        @cache
        def roll(i, sm):
            if i == n and sm == target:
                return 1
            if i == n and sm != target:
                return 0
            ans = 0
            for j in range(1, min(target - sm, k) + 1):
                ans = (ans % mod + roll(i + 1, sm + j) % mod) % mod
            return ans
        return roll(0, 0) % mod
