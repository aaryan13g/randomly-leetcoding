# https://leetcode.com/problems/maximum-units-on-a-truck/

from collections import defaultdict

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        dct = defaultdict(int)
        for typ in boxTypes:
            dct[typ[1]] += typ[0]
        keys = sorted(dct.keys(), reverse=True)
        units = 0
        for key in keys:
            boxes = min(dct[key], truckSize)
            units += boxes * key
            truckSize -= boxes
            if truckSize == 0:
                break
        return units
