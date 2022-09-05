# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    ans = []
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = []
        def consec(digit, curr, nn, flag):
            if nn == 0:
                self.ans.append(int(curr))
                return
            if flag:
                new = digit + k
            else:
                new = digit - k
            if new < 0 or new > 9:
                return
            else:
                consec(new, curr + str(new), nn - 1, True)
                consec(new, curr + str(new), nn - 1, False)
        dig = [i for i in range(1, 10)]
        for d in dig:
            consec(d, str(d), n - 1, True)
            consec(d, str(d), n - 1, False)
        return list(set(self.ans))
