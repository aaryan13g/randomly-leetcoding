/* https://leetcode.com/contest/weekly-contest-281/problems/count-integers-with-even-digit-sum/ */

class Solution:
    def countEven(self, num: int) -> int:
        ans = 5 * ((num // 10)) - 1
        lower = num - (num % 10)
        for numm in range(lower, num + 1):
            temp = sum(list(map(int, str(numm))))
            if temp % 2 == 0:
                ans += 1
        return ans
