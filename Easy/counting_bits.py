/* https://leetcode.com/problems/counting-bits/ */

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ones = 0
            temp = i
            while temp > 0:
                ones += temp % 2
                temp = temp // 2
            ans.append(ones)
        return ans
