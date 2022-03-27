# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costA = 0
        diff = []
        for i in range(len(costs)):
            costA += costs[i][0]
            diff.append(costs[i][0] - costs[i][1])
        diff.sort()
        costB = sum(diff[len(diff)//2:len(diff)])
        return costA - costB
