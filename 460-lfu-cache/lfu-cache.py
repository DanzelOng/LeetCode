class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

class LFUCache:
    def __init__(self, capacity: int):
        # maps frequency to DLLs
        self.lfuCache = {}

        # maps key of node to freq count and node obj
        self.keyMap = {}
        self.capacity = capacity
        self.leastFreqCount = float('inf')

    def _insert_at_head(self, node, dll):
        # freq dll does not exists -> new insertion
        if dll is None:
            dll = DLL()
        
        node.prev, node.nxt = None, dll.head

        if dll.head:
            dll.head.prev = node

        dll.head = node

        if not dll.tail:
            dll.tail = node
        
        return node, dll

    def _remove(self, node, dll):
        # check if node is the head
        if not node.prev:
            dll.head = node.nxt
            if dll.head:
                dll.head.prev = None
        
        # node is not the head
        else:
            node.prev.nxt = node.nxt

        # check if node is the tail
        if not node.nxt:
            dll.tail = node.prev
            if dll.tail:
                dll.tail.nxt = None
        
        # node is not the tail
        else:
            node.nxt.prev = node.prev
        
        # clear all node links
        node.prev = node.nxt = None      

        return node

    def get(self, key: int) -> int:
        print(f"[GET] Accessing key: {key}")
        # check if key exists
        res = self.keyMap.get(key)

        # key does not exist
        if not res:
            print('Key', key, 'does not exist')
            print()
            return -1

        # unpack freq and node obj
        freq, node = res

        # get freq dll which contains the node
        dll = self.lfuCache.get(freq)

        # remove the node from the current freq dll
        self._remove(node, dll)

        if not dll.head and freq == self.leastFreqCount:
            # prevent errors during cache size checking
            del self.lfuCache[freq]
            self.leastFreqCount += 1
        
        # insert the node in the next freq dll
        node, updatedDll = self._insert_at_head(node, self.lfuCache.get(freq + 1))

        # increment frequency of node
        self.keyMap[key] = freq + 1, node

        self.lfuCache[freq + 1] = updatedDll

        self._debug_state(f"After GET({key})")
        return node.val

    def _debug_state(self, tag):
        pass
        # print(f"\n--- {tag} ---")
        # print(f"Least Freq Count: {self.leastFreqCount}")
        # print("Cache Contents (freq → list of keys in LRU order):")
        # for freq, dll in self.lfuCache.items():
        #     cur = dll.head
        #     keys = []
        #     while cur:
        #         keys.append(cur.key)
        #         cur = cur.nxt
        #     print(f"  Freq {freq}: {keys}")
        # print("KeyMap:", {k: (v[0], v[1].val) for k, v in self.keyMap.items()})
        # print(f"Total keys in cache: {len(self.keyMap)} / {self.capacity}")
        # print("--- End Debug ---\n")

    def put(self, key: int, value: int) -> None:
        print(f"[PUT] Inserting key: {key}, value: {value}")

        # check if key exists
        res = self.keyMap.get(key)

        # node exists
        if res:
            freq, node = res
            node.val = value

            # get the dll which the node belongs in
            dll = self.lfuCache.get(freq)

            # remove the node from the dll
            self._remove(node, dll)

            if not dll.head and freq == self.leastFreqCount:
                # prevent errors during cache size checking
                del self.lfuCache[freq]
                self.leastFreqCount += 1
            
            # insert the node in the next freq dll
            node, updatedDll = self._insert_at_head(node, self.lfuCache.get(freq + 1))

            # increment frequency of node
            self.keyMap[key] = freq + 1, node
            self.lfuCache[freq + 1] = updatedDll
            self._debug_state(f"After updating existing key: {key}")
        
        # node does not exist
        else:
            # check if lfu cache is full
            if len(self.keyMap) == self.capacity:
                print(f"[EVICT] Cache full. Evicting from freq {self.leastFreqCount}")
                # get least frequent dll   
                dll = self.lfuCache.get(self.leastFreqCount)

                # remove lru element
                node = self._remove(dll.tail, dll)

                # check if dll still exists after node removal
                if not dll.head:
                    del self.lfuCache[self.leastFreqCount]

                # remove node from key map
                del self.keyMap[node.key]
            
            newNode = Node(key, value)

            newNode, updatedDll = self._insert_at_head(newNode, self.lfuCache.get(1))
            self.lfuCache[1] = updatedDll
            self.keyMap[key] = 1, newNode
            self.leastFreqCount = 1
            self._debug_state(f"After inserting new key: {key}")


     

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)