/* https://leetcode.com/problems/summary-ranges/ */

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        flag = True
        n = len(nums)
        for i in range(n):
            if flag:
                start = nums[i]
                end = nums[i]
            if i < n - 1 and nums[i + 1] == nums[i] + 1:
                flag = False
                end += 1
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + '->' + str(end))
                flag = True
        return ans
