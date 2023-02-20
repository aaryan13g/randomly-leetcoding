# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = '#' + order
        order_dict = {}
        for i in range(27):
            order_dict[order[i]] = i
        for i in range(len(words) - 1):
            l1 = len(words[i])
            l2 = len(words[i + 1])
            if l1 > l2:
                itr = l2 + 1
                words[i + 1] += '#'
            else:
                itr = l1 
            for j in range(itr):
                if order_dict[words[i][j]] < order_dict[words[i + 1][j]]:
                    break
                elif order_dict[words[i][j]] > order_dict[words[i + 1][j]]:
                    return False
                else:
                    continue
        return True
