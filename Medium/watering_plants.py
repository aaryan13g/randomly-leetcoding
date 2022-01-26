/* https://leetcode.com/problems/watering-plants/ */

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curr = capacity
        for i in range(len(plants)):
            if curr >= plants[i]:
                curr -= plants[i]
                steps += 1
            else:
                steps += (2 * (i + 1)) - 1
                curr = capacity - plants[i]
        return steps
