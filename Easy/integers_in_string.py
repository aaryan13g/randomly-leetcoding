# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        temp = ''
        for c in word:
            if '0' <= c <= '9':
                temp += c
            else:
                if temp != '':
                    nums.add(int(temp))
                    temp = ''
        if temp != '':
            nums.add(int(temp))
        return len(nums)
