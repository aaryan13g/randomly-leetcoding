/* https://leetcode.com/problems/maximum-69-number/ */

class Solution:
    def maximum69Number (self, num: int) -> int:
        if '6' not in str(num):
            return num
        num = str(num)
        idx = num.find('6')
        num = list(num)
        num[idx] = '9'
        return int(''.join(num))
