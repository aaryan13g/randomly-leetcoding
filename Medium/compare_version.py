/* https://leetcode.com/problems/compare-version-numbers/ */

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(elem) for elem in version1.split('.')]
        v2 = [int(elem) for elem in version2.split('.')]
        n1, n2 = len(v1), len(v2)
        if n1 < n2:
            v1.append(0)
            v2 = v2[:n1] + [sum(v2[n1:])]
            n1 += 1
        elif n1 > n2:
            v2.append(0)
            v1 = v1[:n2] + [sum(v1[n2:])]
            n1 = n2 + 1
        for i in range(n1):
            if v1[i] < v2[i]:
                return -1
            elif v2[i] < v1[i]:
                return 1
        return 0
