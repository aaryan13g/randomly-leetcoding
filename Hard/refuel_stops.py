# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# TLE - Need to upgrade from DFS to DP or Heap

class Solution:
    global_min = math.inf
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        @cache
        def check_stop(pos, num_stops, fuel_left, i, stop):
            if num_stops >= self.global_min:
                return math.inf
            if pos >= target or (target - pos) <= fuel_left:
                self.global_min = min(self.global_min, num_stops)
                return num_stops
            if i >= n and (target - pos) > fuel_left:
                return math.inf
            fuel_left = fuel_left - (stations[i][0] - pos)
            pos = stations[i][0]
            if fuel_left < 0 or i >= n:
                return math.inf
            if stop:
                fuel_left += stations[i][1]
                num_stops += 1
            i += 1
            return min(check_stop(pos, num_stops, fuel_left, i, stop=False), check_stop(pos, num_stops, fuel_left, i, stop=True))
        ans = min(check_stop(0, 0, startFuel, 0, stop=False), check_stop(0, 0, startFuel, 0, stop=True))
        if ans == math.inf:
            return -1
        else:
            return ans
