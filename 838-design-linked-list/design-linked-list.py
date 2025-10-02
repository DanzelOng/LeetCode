class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyLinkedList:
    '''
    
    Time Complexities:

    -> get()          : O(index) ≈ O(n)
    -> addAtHead()    : O(1)
    -> addAtTail()    : O(1)
    -> addAtIndex()   : O(index) ≈ O(n)
    -> deleteAtIndex(): O(index) ≈ O(n)

    Space Complexity: O(n)

    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        for _ in range(index):
            cur = cur.next

        return cur.val
           
    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = Node(val=val)
        else:
            node = Node(val=val, nxt=self.head)
            self.head.prev = node
            self.head = node
        
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = Node(val=val)
        else:
            node = Node(val=val, prev=self.tail)
            self.tail.next = node
            self.tail = node

        self.size += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:     # invalid index
            return

        if index <= 0:            # insert at head 
            self.addAtHead(val)

        elif index == self.size:  # insert at tail
            self.addAtTail(val)

        else:                     # insert at index
            cur = self.head

            for _ in range(index - 1):
                cur = cur.next

            node = Node(val, nxt=cur.next, prev=cur)
            cur.next.prev = node
            cur.next = node
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # invalid index
            return

        if index == self.size - 1:           # delete at tail
            if self.size == 1:
                self.head = self.tail = None
            else:
                tail = self.tail
                self.tail.prev.next = None
                self.tail = self.tail.prev
                tail.next = tail.prev = None

        else:                                # delete at index
            cur = self.head

            for _ in range(index):
                cur = cur.next
            
            if self.head == cur:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

            cur.next = cur.prev = None
   
        self.size -= 1