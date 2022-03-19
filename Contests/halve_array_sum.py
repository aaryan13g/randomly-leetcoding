# https://leetcode.com/contest/biweekly-contest-74/problems/minimum-operations-to-halve-array-sum/

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sm = sum(nums)
        half_sum = sm / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)
        ops = 0
        while sm > half_sum:
            maxx = heapq.heappop(heap) / 2
            sm = sm + maxx
            heapq.heappush(heap, maxx)
            ops += 1
        return ops
