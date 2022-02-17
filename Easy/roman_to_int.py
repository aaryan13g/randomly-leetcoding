/* https://leetcode.com/problems/roman-to-integer/ */

class Solution:
    def romanToInt(self, s: str) -> int:
        unit = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
        tens = {'X': 1, 'XX': 2, 'XXX': 3, 'XL': 4, 'L': 5, 'LX': 6, 'LXX': 7, 'LXXX': 8, 'XC': 9}
        hundreds = {'C': 1, 'CC': 2, 'CCC': 3, 'CD': 4, 'D': 5, 'DC': 6, 'DCC': 7, 'DCCC': 8, 'CM': 9}
        thousands = {'M': 1, 'MM': 2, 'MMM': 3}
        roman_dict = {1: thousands, 2:hundreds, 3:tens, 4:unit}
        
        i = 1
        num = ''
        while i < 5:
            j = 5
            while j > 0:
                if s[:j] in roman_dict[i]:
                    num += str(roman_dict[i][s[:j]])
                    s = s[j:]
                    break
                j -= 1
            if j == 0:
                num += '0'
            i += 1
        return int(num)
