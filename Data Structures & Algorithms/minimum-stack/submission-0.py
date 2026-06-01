
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        # if not self.minimum or val < self.minimum[-1]:
        #     self.minimum.append(val)
        # else: self.minimum[0]
        self.stack.append(val)
        val  = min(val,self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
