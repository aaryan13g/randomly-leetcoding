/* https://leetcode.com/problems/search-in-rotated-sorted-array/ */

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if l == r and nums[l] != target:
                break
            if nums[mid] > nums[r] and (target > nums[mid] or target <= nums[r]):
                l = mid + 1
            elif nums[mid] < nums[r] and nums[mid] < target <= nums[r]:
                l = mid + 1
            elif nums[mid] > nums[l] and target > nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[l] and nums[mid] < target < nums[l]:
                l = mid + 1
            else:
                r = mid
        return -1
