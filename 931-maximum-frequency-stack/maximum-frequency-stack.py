import heapq
from datetime import datetime

class FreqStack:
    def __init__(self):
        self.heap = []
        self.hashMap = {}

    def push(self, val: int) -> None:
        # get current frequency of value and increment it by 1
        freq = self.hashMap.get(val, 0) + 1

        # update frequency into hash table
        self.hashMap[val] = freq

        # compute time of insertion
        timeOfInsertion = -datetime.now().timestamp()

        # create entry for heap insertion
        item = (-freq, timeOfInsertion, val)

        # insert item to heap 
        heapq.heappush(self.heap, item)   

    def pop(self) -> int:
        # pop the most frequent value
        value = heapq.heappop(self.heap)[-1]

        # decrement frequency of the value by 1
        self.hashMap[value] = self.hashMap.get(value, 0) - 1
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()