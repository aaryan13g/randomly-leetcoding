/* https://leetcode.com/problems/group-anagrams/ */

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
            for s in strs:
                key = ''.join(sorted(s))
                anagrams[key].append(s)
            return list(anagrams.values())
          

/* Another solution but with TLE */

        # anagrams = []
        # while strs:
        #     anagram = [strs[0]]
        #     pivot_len = len(strs[0])
        #     counter_pivot = collections.Counter(strs.pop(0))
        #     for i in range(len(strs) - 1, -1, -1):
        #         if len(strs[i]) == pivot_len and collections.Counter(strs[i]) == counter_pivot:
        #             anagram.append(strs.pop(i))
        #     anagrams.append(anagram)
        # return anagrams
