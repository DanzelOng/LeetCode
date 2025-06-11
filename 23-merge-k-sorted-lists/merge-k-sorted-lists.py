# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        idx, heap = 0, []
        
        # O(klogk)
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, idx, head))
                idx += 1
        
        cur = dummy = ListNode()

        # O(nlogk)
        while heap:
            node = heapq.heappop(heap)[-1]
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
                idx += 1
            cur.next = node
            cur = cur.next     
        
        return dummy.next