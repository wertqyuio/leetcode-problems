class MinStack:
    # the biggest problem was naming the self.data self.top, don't do that!
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        if not self.data:
            self.data.append((x,x))
        else:
            self.data.append((x,min(x,self.data[-1][1])))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()