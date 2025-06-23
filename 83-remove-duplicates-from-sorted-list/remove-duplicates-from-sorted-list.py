# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            # duplicate identified, update current node to point to node after next node
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            
            # move cur to point to next node
            else:
                cur = cur.next
        
        return head