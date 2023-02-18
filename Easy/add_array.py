# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(i) for i in num]
        num = int("".join(num))
        ans = str(num + k)
        return [int(i) for i in ans]
