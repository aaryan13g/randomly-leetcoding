# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = collections.Counter(nums).most_common()
        i = 0
        ans = []
        while k:
            ans.append(common[i][0])
            i += 1
            k -= 1
        return ans
