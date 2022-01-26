/* https://leetcode.com/problems/finding-the-users-active-minutes/ */

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        activity_dict = {}
        for log in logs:
            id, time = log[0], log[1]
            if id not in activity_dict:
                activity_dict[id] = set([time])
            else:
                activity_dict[id].add(time)
        ans = [0] * k
        for user in activity_dict:
            ans[len(activity_dict[user]) - 1] += 1
        return ans
