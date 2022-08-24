# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elems = []
        for row in matrix:
            elems += row
        elems.sort()
        return elems[k-1]
