/* https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ */

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[mid] < target:
                l = mid + 1
                continue
            if nums[mid] > target:
                r = mid
                continue
            if nums[mid] == target and r - l < 3:
                if nums[l] == target:
                    ans[0] = l
                else:
                    ans[0] = mid
                break
            else:
                r = mid + 1
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[mid] < target:
                l = mid + 1
                continue
            if nums[mid] > target:
                r = mid
                continue
            if nums[mid] == target and r - l < 3:
                if nums[r - 1] == target:
                    ans[1] = r - 1
                else:
                    ans[1] = mid
                break
            else:
                l = mid
        return ans
                
