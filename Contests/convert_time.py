# https://leetcode.com/contest/weekly-contest-287/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(':')
        correct = correct.split(':')
        minute_diff = int(correct[1]) - int(current[1])
        ops = 0
        if minute_diff >= 0:
            ops += int(correct[0]) - int(current[0])
        else:
            ops += int(correct[0]) - int(current[0]) - 1
            minute_diff += 60
        ops += minute_diff // 15
        minute_diff = minute_diff % 15
        ops += minute_diff // 5
        minute_diff = minute_diff % 5
        ops += minute_diff
        return ops
