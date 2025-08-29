class MinStack:
    '''

    Time Complexity: 
    - push(): O(1)
    - pop(): O(1)
    - top(): O(1)
    - getMin(): O(1)

    Space Complexity: O(n)
    
    To solve this problem, each value in the stack would be associated with
    the current minimum value. 
    
    By storing each entry in the stack with a snapshot of current minimum at 
    the time of its insertion, retrieving the minimum value happens in constant
    time without needing to scan the stack each time.

    '''

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        currentMin = min(self.stack[-1][-1] if self.stack else val, val)
        self.stack.append([val, currentMin])

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()