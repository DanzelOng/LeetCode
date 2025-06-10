class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = self.tail = None

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._remove(node)
        self._insert_at_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = ListNode(key, value)
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.key]
                self._remove(self.tail)
            
            self.cache[key] = newNode
            self._insert_at_head(newNode)
        else:
            node.val = value
            self._remove(node)
            self._insert_at_head(node)

    def _remove(self, node):
        if node.prev:
            node.prev.nxt = node.nxt
        else:
            self.head = node.nxt
        
        if node.nxt:
            node.nxt.prev = node.prev
        else:
            self.tail = node.prev
        
        node.nxt = node.prev = None

    def _insert_at_head(self, node):
        node.prev, node.nxt = None, self.head

        if self.head:
            self.head.prev = node

        self.head = node
        
        if self.tail is None:
            self.tail = node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)