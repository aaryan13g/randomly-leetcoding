/* https://leetcode.com/contest/weekly-contest-277/problems/rearrange-array-elements-by-sign/ */

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        ans = []
        for i in range(len(nums) // 2):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
