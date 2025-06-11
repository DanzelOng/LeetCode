# Node Class
class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

# Doubly Linked List Class
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # inserts node at the head of the new DLL 
    # -> moves node to MRU
    def _insert_at_head(self, node):
        # set pointers of node to prepare it to be new head
        node.prev, node.nxt = None, self.head
        
        # set old head to point to node if head exists
        if self.head:   
            self.head.prev = node

        # set head to node
        self.head = node

        # DLL is initially empty, set tail to node as well
        if not self.tail:
            self.tail = node
        
        return node
    
    # removes node and prepares for re-insertion at head of new DLL
    def _remove(self, node):
        # checks if node is at the front of the DLL
        # and updates head to be its next node
        if not node.prev:
            self.head = node.nxt

            # update pointers of new head if DLL is not empty
            if self.head:
                self.head.prev = None
        
        # node is not the head,
        # connect its previous node to its next node
        else:
            node.prev.nxt = node.nxt

        # checks if node is at the end of the DLL,
        # and updates tail to be its previous node
        if not node.nxt:
            self.tail = node.prev

            # update pointers of new tail if DLL is not empty
            if self.tail:
                self.tail.nxt = None
        
        # node is not the tail
        # connect its next node to point to its previous node
        else:
            node.nxt.prev = node.prev
        
        # reset all pointers of the node
        node.prev = node.nxt = None      

        return node

class LFUCache:
    def __init__(self, capacity: int):
        # LFU Cache maps frequencies to DLLs
        self.lfuCache = {}

        # Key Hash Table maps each node's key to its current freq and the node obj
        self.keyMap = {}
        self.capacity = capacity
        self.leastFreqCount = float('inf')

    # retrieves value of key, returns -1 if key does not exists
    def get(self, key: int) -> int:
        # checks for a result from getting a key
        res = self.keyMap.get(key)

        # no result -> key does not exists, return -1
        if not res:
            return -1

        # unpack current freq of node and node obj 
        freq, node = res

        # get the corresponding DLL of the node
        dll = self.lfuCache.get(freq)

        # remove the node from that DLL,
        # before re-insertion at new freq DLL
        dll._remove(node)

        # guard clause:
        # checks if node was the only node in the old DLL and freq was the least frequency,
        # and updates least freq counter and deletes the DLL entry from LFU cache
        if not dll.head and freq == self.leastFreqCount:
            del self.lfuCache[freq]
            self.leastFreqCount += 1

        # check if the new freq DLL already exists
        newFreqDll = self.lfuCache.get(freq + 1)

        # new freq DLL does not exist,
        # create and insert the DLL entry in the LFU cache
        if not newFreqDll:
            newFreqDll = DLL()
            self.lfuCache[freq + 1] = newFreqDll
        
        # insert the node at the new freq DLL
        # node becomes MRU
        newFreqDll._insert_at_head(node)
        
        # updates node entry in the Key Map
        self.keyMap[key] = freq + 1, node

        # return value of node obj
        return node.val

    # updates the value of a key if it exists, otherwise creates a new key-value pair
    def put(self, key: int, value: int) -> None:
        # checks for a result from getting a key
        res = self.keyMap.get(key)
        
        # result exists
        if res:
            # unpack current freq of node and node obj 
            freq, node = res

            # update value of node
            node.val = value

            # get the corresponding DLL of the node
            dll = self.lfuCache.get(freq)

            # remove the node from that DLL,
            # before re-insertion at new freq DLL
            dll._remove(node)

            # guard clause:
            # checks if node was the only node in the old DLL and freq was the least frequency,
            # and updates least freq counter and deletes the DLL entry from LFU cache
            if not dll.head and freq == self.leastFreqCount:
                del self.lfuCache[freq]
                self.leastFreqCount += 1
            
            # check if the new freq DLL already exists
            newFreqDll = self.lfuCache.get(freq + 1)

            # new freq DLL does not exist,
            # create and insert the DLL entry in the LFU cache
            if not newFreqDll:
                newFreqDll = DLL()
                self.lfuCache[freq + 1] = newFreqDll
            
            # insert the node at the new freq DLL
            # node becomes MRU
            newFreqDll._insert_at_head(node)

            # updates node entry in the Key Map
            self.keyMap[key] = freq + 1, node

        # no result, check if keys have exceeded capacity before inserting a new entry
        else:
            # key capacity is full, delete LFU node before inserting new node
            if len(self.keyMap) == self.capacity:
                # get the DLL which contains LFU node
                dll = self.lfuCache.get(self.leastFreqCount)

                # remove LRU node within the LFU DLL
                node = dll._remove(dll.tail)

                # guard clause:
                # checks if node was the only node in the freq DLL and deletes that DLL entry
                if not dll.head:
                    del self.lfuCache[self.leastFreqCount]

                # remove node entry from Key Map
                del self.keyMap[node.key]
            
            # create the node and check if the DLL at freq 1 exists
            newNode = Node(key, value)
            newFreqDll = self.lfuCache.get(1)

            # DLL at freq 1 does not exists, create the DLL and add to LFU cache
            if not newFreqDll:
                newFreqDll = DLL()
                self.lfuCache[1] = newFreqDll   

            # insert node at freq 1 DLL
            newFreqDll._insert_at_head(newNode)

            # insert node entry in Key Map and update least freq count to 1
            self.keyMap[key] = 1, newNode
            self.leastFreqCount = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)