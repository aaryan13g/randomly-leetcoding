# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 0
        temp = [1]
        while i != rowIndex:
            temp1 = [1]
            for j in range(len(temp) - 1):
                temp1.append(temp[j] + temp[j + 1])
            temp1.append(1)
            temp = temp1
            i += 1
        return temp
