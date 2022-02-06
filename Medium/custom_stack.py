/* https://leetcode.com/problems/design-a-stack-with-increment-operation/ */

class CustomStack:
    stack = []
    maxSize = 0
    
    def __init__(self, maxSize: int):
        if len(self.stack) < maxSize:
            self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        i = 0
        while k > 0 and i < len(self.stack):
            self.stack[i] += val
            i += 1
            k -= 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
