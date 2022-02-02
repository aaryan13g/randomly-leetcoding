/* https://leetcode.com/problems/arithmetic-subarrays/ */

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            temp = sorted(nums[l[i]:r[i] + 1])
            flag = True
            if len(temp) < 2:
                flag = False
                ans.append(False)
            for j in range(1, len(temp)):
                if temp[j] - temp[j - 1] != temp[1] - temp[0]:
                    ans.append(False)
                    flag = False
                    break
            if flag:
                ans.append(True)
        return ans
