# https://leetcode.com/contest/weekly-contest-285/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        collisions = 0
        i = 0
        while i < len(directions) - 1:
            temp = directions[i:i+2]
            if temp == ['R', 'L']:
                collisions += 2
                directions[i] = directions[i+1] = 'S'
                i += 1
            elif temp == ['R', 'S'] or temp == ['S', 'L']:
                collisions += 1
                directions[i] = directions[i+1] = 'S'
                i += 1
            else:
                i += 1
        try:
            first_s_idx = directions.index('S')
            tempp = list(reversed(directions))
            last_s_idx = len(directions) - tempp.index('S') - 1
            for i in range(len(directions)):
                if directions[i] == 'R' and i < last_s_idx:
                    collisions += 1
                elif directions[i] == 'L' and i > first_s_idx:
                    collisions += 1
        except:
            pass
        return collisions
