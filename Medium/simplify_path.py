# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        simple_path = []
        for elem in path.split('/'):
            if elem and elem != '.':
                if elem == '..':
                    if simple_path:
                        simple_path.pop()
                else:
                    simple_path.append(elem)
        return '/' + '/'.join(simple_path)
