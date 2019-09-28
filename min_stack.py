class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]
        #self.minstack=[]
        

    def push(self, x: int) -> None:
        self.items.append(x)
        #self.items.sort()
        

    def pop(self) -> None:
        #sorted(self.items)
        
        print(self.items)
        self.items.pop()
        print(self.items)

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        #self.items.sort()
        #print(self.items)
        return min(self.items)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()