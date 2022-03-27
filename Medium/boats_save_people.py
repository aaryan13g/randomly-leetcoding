# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        h, l = len(people) - 1, 0
        while h >= l:
            if people[h] + people[l] <= limit:
                l += 1
            h -= 1
            boats += 1
        return boats
