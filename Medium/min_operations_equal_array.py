/* https://leetcode.com/problems/minimum-operations-to-make-array-equal/ */
  
class Solution:
    def minOperations(self, n: int) -> int:
        return int((pow(n, 2) // 2) - ((pow(n / 2, 2)) // 1))
