/* https://leetcode.com/problems/subarray-sum-equals-k/ */

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0: 1}
        ans = 0
        temp = 0
        for num in nums:
            temp += num
            if temp - k in dct:
                ans += dct[temp - k]
            if temp in dct:
                dct[temp] += 1
            else:
                dct[temp] = 1
        return ans
