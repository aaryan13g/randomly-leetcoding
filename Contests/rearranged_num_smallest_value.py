/* https://leetcode.com/problems/smallest-value-of-the-rearranged-number/ */

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            digits = list(str(abs(num)))
            digits.sort(reverse=True)
            return int(''.join(digits)) * -1
        else:
            digits = list(str(num))
            digits.sort()
            i = 0
            while digits[i] == '0':
                i += 1
            temp = digits[0]
            digits[0] = digits[i]
            digits[i] = temp
            return int(''.join(digits))
