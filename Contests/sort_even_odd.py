/* https://leetcode.com/problems/sort-even-and-odd-indices-independently/ */

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        odd = []
        even = []
        for i in range(n):
            if i % 2 == 1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ans = []
        for i in range(len(even)):
            ans.append(even[i])
            if i < len(odd):
                ans.append(odd[i])
        return ans
