# https://leetcode.com/problems/stamping-the-sequence/

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        def check(temp_str):
            for i in range(len(temp_str)):
                if temp_str[i] != '?' and temp_str[i] != stamp[i]:
                    return False
            return True
        
        n = len(target)
        m = len(stamp)
        target = list(target)
        ans = []
        while target.count('?') != n:
            changed = False
            for i in range(n - m + 1):
                temp = target[i:i+m]
                if set(list(temp)) == {'?'}:
                    continue
                else:
                    if check(temp):
                        target = target[:i] + ['?'] * m + target[i+m:]
                        ans.append(i)
                        changed = True
            if not changed:
                return []
        return ans[::-1]
