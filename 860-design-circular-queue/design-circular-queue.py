class MyCircularQueue:
    '''
    
    Time Complexities:
    -> __init__()    : O(1)
    -> enQueue()     : O(1)
    -> deQueue()     : O(1)
    -> Front()       : O(1)
    -> Rear()        : O(1)
    -> isEmpty()     : O(1)
    -> isFull()      : O(1)

    Space Complexity: O(k)

    To achieve circular queue traversal, we use a fixed-length array of size `k` 
    and two pointers, `front` and `rear`. By advancing the pointers using modular 
    arithmetic (pointer + 1) % k, each pointer automatically wraps back to the 
    start of the array after reaching the end. This enables true circular structure 
    and allows the efficient reuse of freed positions whenever elements are dequeued.

    The `front` pointer marks the current front element, while `rear` identifies 
    the most recently inserted element. During enqueue operations, `rear` advances 
    with (rear + 1) % k, and during dequeue operations, `front` advances with 
    (front + 1) % k. 
    
    A separate size variable is maintained to keep track of how many elements are 
    in the queue, which indicates whether the queue is full or empty at a given time.

    This design ensures that all operations run in constant time, while making full 
    use of the fixed array without the need to resize.

    '''

    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = self.front = 0
        self.rear = -1
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.limit:
            return False
    
        self.rear = (self.rear + 1) % self.limit
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.limit
        self.size -= 1
        return True
        
    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1
     
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()