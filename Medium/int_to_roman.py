/* https://leetcode.com/problems/integer-to-roman/ */

class Solution:
    def intToRoman(self, num: int) -> str:
        unit = {1: 'I', 4: 'IV', 5:'V', 9: 'IX'}
        tens = {1: 'X', 4: 'XL', 5:'L', 9: 'XC'}
        hundreds = {1: 'C', 4: 'CD', 5:'D', 9: 'CM'}
        thousands = {1: 'M'}
        roman_dct = {1:unit, 2:tens, 3:hundreds, 4:thousands}
        
        i = 1
        roman = ''
        while num > 0:
            digit = num % 10
            num = num // 10
            if digit in roman_dct[i]:
                roman = roman_dct[i][digit] + roman
            elif 0 < digit < 4:
                roman = (roman_dct[i][1] * digit) + roman
            elif digit > 5:
                roman = roman_dct[i][5] + (roman_dct[i][1] * (digit - 5)) + roman
            i += 1
        return roman
