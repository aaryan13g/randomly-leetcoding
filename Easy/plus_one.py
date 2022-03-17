# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            num = ''
            for d in digits:
                num += str(d)
            num = str(int(num) + 1)
            ans = []
            for dg in num:
                ans.append(int(dg))
            return ans
