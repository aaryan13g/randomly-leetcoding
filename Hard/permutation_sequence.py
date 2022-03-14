# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        perms = [''.join(perm) for perm in itertools.permutations(arr)]
        return perms[k-1]
