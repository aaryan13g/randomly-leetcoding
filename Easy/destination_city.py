/* https://leetcode.com/problems/destination-city/ */

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_dict = {}
        for path in paths:
            if path[0] not in path_dict:
                path_dict[path[0]] = []
            if path[1] not in path_dict:
                path_dict[path[1]] = []
            path_dict[path[0]].append(path[1])
        for city in path_dict:
            if path_dict[city] == []:
                return city
