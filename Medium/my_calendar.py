# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:
    cal_start = None
    cal_end = None
    n = None
    def __init__(self):
        self.cal_start = []
        self.cal_end = []
        self.n = 0

    def book(self, start: int, end: int) -> bool:
        pos = 0
        for i in range(self.n):
            if start <= self.cal_start[i]:
                break
            pos = i + 1
        if pos == 0:
            if self.cal_start and self.cal_start[0] < end:
                return False
            else:
                self.cal_start.insert(0, start)
                self.cal_end.insert(0, end)
                self.n += 1
                return True
        elif pos == self.n:
            if start < self.cal_end[pos - 1]:
                return False
            else:
                self.cal_start.append(start)
                self.cal_end.append(end)
                self.n += 1
                return True
        else:
            if start < self.cal_end[pos - 1] or end > self.cal_start[pos]:
                return False
            else:
                self.cal_start.insert(pos, start)
                self.cal_end.insert(pos, end)
                self.n += 1
                return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
