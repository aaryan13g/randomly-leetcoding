# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    k = 0
    nums = []
    n = 0
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.n = len(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        self.n += 1
        return self.nums[self.n - self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
