# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_dict = collections.defaultdict(list)
        for i in range(len(mat)):
            row_dict[sum(mat[i])].append(i)
        ans = []
        for key in sorted(row_dict.keys()):
            if len(row_dict[key]) < k:
                ans += row_dict[key]
                k -= len(row_dict[key])
            else:
                ans += row_dict[key][:k]
                break
        return ans
